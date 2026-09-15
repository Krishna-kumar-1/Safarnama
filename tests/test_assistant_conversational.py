# -*- coding: utf-8 -*-
"""
Unit tests for Safarnama AI Conversational Assistant:
- Multi-turn conversational slot filling
- Missing month and destination clarification ("25 taarikh ke liye lucknow se train")
- Hindi, Hinglish, and English language matching
- Month name resolution (English, Hindi, and relative)
- Ultra-low latency verification
"""

import time
import unittest
from datetime import datetime
from src.assistant_engine import (
    SafarnamaAssistant,
    detect_language,
    extract_day,
    extract_month
)


class TestAssistantConversational(unittest.TestCase):
    def setUp(self):
        self.assistant = SafarnamaAssistant()

    def test_language_detection(self):
        # Hindi Devanagari
        self.assertEqual(detect_language("25 तारीख के लिए लखनऊ से ट्रेन"), "hindi")
        self.assertEqual(detect_language("धनबाद से ट्रेन बताओ"), "hindi")
        self.assertEqual(detect_language("नमस्ते"), "hindi")

        # Hinglish
        self.assertEqual(detect_language("25 taarikh ke liye lucknow se train"), "hinglish")
        self.assertEqual(detect_language("dhanbad se train chahiye"), "hinglish")
        self.assertEqual(detect_language("kahan jana hai"), "hinglish")
        self.assertEqual(detect_language("kal subah 10 bje"), "hinglish")

        # English
        self.assertEqual(detect_language("Train from Lucknow on 25th"), "english")
        self.assertEqual(detect_language("from dhanbad to where"), "english")
        self.assertEqual(detect_language("Book a ticket to Delhi"), "english")

    def test_extract_day(self):
        self.assertEqual(extract_day("25 taarikh ke liye lucknow se train"), 25)
        self.assertEqual(extract_day("25 तारीख को ट्रेन"), 25)
        self.assertEqual(extract_day("train on 25th"), 25)
        self.assertEqual(extract_day("tareekh 15"), 15)
        self.assertEqual(extract_day("25"), 25)
        self.assertIsNone(extract_day("lucknow se kanpur"))

    def test_extract_month(self):
        # English
        num, name = extract_month("in October")
        self.assertEqual(num, 10)
        num, name = extract_month("15 sept")
        self.assertEqual(num, 9)

        # Hindi
        num, name = extract_month("अक्टूबर महीने में")
        self.assertEqual(num, 10)
        num, name = extract_month("15 सितंबर")
        self.assertEqual(num, 9)

        # Relative
        num, name = extract_month("agle mahine")
        expected_next_month = datetime.now().month + 1 if datetime.now().month < 12 else 1
        self.assertEqual(num, expected_next_month)

    def test_missing_destination_and_month_hinglish(self):
        # User asks: "25 taarikh ke liye lucknow se train"
        res = self.assistant.process_message("25 taarikh ke liye lucknow se train")
        self.assertIsNone(res["action"])
        self.assertEqual(res["extracted"]["source"], "LKO")
        self.assertIsNone(res["extracted"]["destination"])
        self.assertEqual(res["extracted"]["day"], 25)
        self.assertIsNone(res["extracted"]["month"])
        # Should ask destination and which month in Hinglish
        self.assertIn("kahan", res["reply"].lower())
        self.assertIn("mahine", res["reply"].lower())
        self.assertIn("25", res["reply"])

    def test_multi_turn_completion_hinglish(self):
        # Turn 1: "25 taarikh ke liye lucknow se train"
        turn1 = self.assistant.process_message("25 taarikh ke liye lucknow se train")
        
        # Turn 2: User provides destination and month: "Kanpur, October"
        history = [
            {"role": "user", "content": "25 taarikh ke liye lucknow se train", "extracted": turn1["extracted"]},
            {"role": "assistant", "content": turn1["reply"], "extracted": turn1["extracted"]}
        ]
        turn2 = self.assistant.process_message("Kanpur, October", history=history)

        self.assertIsNotNone(turn2["action"])
        self.assertEqual(turn2["action"]["type"], "fill_and_search")
        self.assertEqual(turn2["action"]["source"], "LKO")
        self.assertEqual(turn2["action"]["destination"], "CNB")
        self.assertTrue(turn2["action"]["date"].endswith("-10-25"))

    def test_hindi_language_matching_and_devanagari(self):
        # Turn 1: Devanagari Hindi
        turn1 = self.assistant.process_message("25 तारीख के लिए लखनऊ से ट्रेन")
        self.assertEqual(turn1["extracted"]["language"], "hindi")
        self.assertIsNone(turn1["action"])
        # Must respond in Hindi script asking where and which month
        self.assertIn("कहाँ", turn1["reply"])
        self.assertIn("महीने", turn1["reply"])

        # Turn 2: Devanagari reply
        history = [
            {"role": "user", "content": "25 तारीख के लिए लखनऊ से ट्रेन", "extracted": turn1["extracted"]},
            {"role": "assistant", "content": turn1["reply"], "extracted": turn1["extracted"]}
        ]
        turn2 = self.assistant.process_message("कानपुर, अक्टूबर", history=history)
        self.assertIsNotNone(turn2["action"])
        self.assertEqual(turn2["action"]["source"], "LKO")
        self.assertEqual(turn2["action"]["destination"], "CNB")
        self.assertTrue(turn2["action"]["date"].endswith("-10-25"))
        # Confirms in Hindi
        self.assertIn("खोज", turn2["reply"])

    def test_english_language_matching(self):
        # Turn 1: English
        turn1 = self.assistant.process_message("Train from Lucknow on 25th")
        self.assertEqual(turn1["extracted"]["language"], "english")
        self.assertIsNone(turn1["action"])
        self.assertIn("Where would you like to travel", turn1["reply"])
        self.assertIn("which month", turn1["reply"].lower())

        # Turn 2: English follow up
        history = [
            {"role": "user", "content": "Train from Lucknow on 25th", "extracted": turn1["extracted"]},
            {"role": "assistant", "content": turn1["reply"], "extracted": turn1["extracted"]}
        ]
        turn2 = self.assistant.process_message("To Kanpur in October", history=history)
        self.assertIsNotNone(turn2["action"])
        self.assertEqual(turn2["action"]["source"], "LKO")
        self.assertEqual(turn2["action"]["destination"], "CNB")
        self.assertTrue(turn2["action"]["date"].endswith("-10-25"))
        self.assertIn("found train routes", turn2["reply"].lower())

    def test_from_dhanbad_to_where(self):
        # User asks: "from dhanbad to where(kahan)"
        res = self.assistant.process_message("from dhanbad to where(kahan)")
        self.assertEqual(res["extracted"]["source"], "DHN")
        self.assertIsNone(res["extracted"]["destination"])
        self.assertIsNone(res["action"])
        self.assertIn("Dhanbad", res["reply"])

    def test_response_latency_is_under_50ms(self):
        # Ensure fast-path local resolution is ultra fast (< 50ms)
        t0 = time.time()
        res = self.assistant.process_message("25 taarikh ke liye lucknow se train")
        elapsed_ms = (time.time() - t0) * 1000
        self.assertLess(elapsed_ms, 50.0, f"Response too slow: {elapsed_ms}ms")


if __name__ == "__main__":
    unittest.main()
