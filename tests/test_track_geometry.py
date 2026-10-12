#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 🛡️ SAFARNAMA_SHIELD_ARMORED_V2
# ==============================================================================
# PROPRIETARY & CONFIDENTIAL — SAFARNAMA RAILWAY INTELLIGENCE ENGINE
# This file is cryptographically armored to prevent unauthorized source theft,
# cloning, or reverse engineering on public repositories.
# Repository owner can unlock via: python protect_data.py unlock
# ==============================================================================
import base64 as _b, hashlib as _h, zlib as _z
_P = (
    b"gw)>z(nY6%Q`l}hoE@E?*6AOvBdqO%lSy))Bw;`N&rG+149A<v?pU%_+nNyY2X?MMjib&@giXW$i(>*=;g>Yd3y-"
    b"Ex?%Pdf2Y<%<v2byPKidj3Q$2Y^3J2^sQ3xq`Wlu3Ir*w@IcOr9R381konaJY9{lN1A87cK+EvS*E;C2ftB}~ul1"
    b"I}|uZB%tSP^w7#N0YcDh}8|H+)|isx$M~78{DdO{1btXecNI6*t!;oy-}LcjR3^nS$N)wp)%%olxfgBA<xXIP3g|"
    b"oNi9S5_P1;MIQ{4+Q&N0kq%A2tjF^a(RK@B3g8V5acN^H;Rw!9-?*5Nd>gh3FCXD>FU{ZH5u75q5{#8I&sP78qHf"
    b"I>(VS?^8h{(#0t?44ahwb4g>_RvSbOyNvC)kJ-fGasp_hz)Y#Jy!%a`ZU&iZd=L2!cNqA(~#-z|pakaiksyXiou-"
    b"r<27_x@ogI#Wrr#$30a(i+0y<i3HbPSD#Vc0qpk%G@g))4OO)-pRH{^-W*Ei?zJ{iX;oQTU%dfS>B&zW@Uc(Im{e"
    b"NejsY$MLmElWPLEOm-lK4I@@&4%(cStZtO1w>-yoRLkqq2T_OE6r*pN(25)puf&(01-m-26y?aG!lBDSj!tE8+(&"
    b"~5##v%5||wYu-}Zk@Y4+@q~(*gfbRIJM{ezdpPB7&7K~F7M%sFF=|#`iFSZl>q|$CSn>$P9YY9y9pmM1elkUp!Jb"
    b"Jk!D{-_{P_+DasvfQ5+x(iG8MxNkfl?r@#JoYBzYgLup)d9mr;cM?}3MNXNi^ESg7K78W}+9Fi2H0_0vzapF&~#$"
    b"YLnMTzyb^0hR^_-WjJO?b`G_^vW+f%at{7CJgF`y~L1b6TMB=08felWo#=#d6_qN}47IGc-#^B4*^>LHln=J|2dC"
    b"Ktz0x8`Yo7;1qS1gIj3F+OL-PCX3?}f};RZB(g<3*b`n?i1hD?!bm?2-K|!Slz4guf;`o#c`zhrl9r21wi3m!;i<"
    b"`<RQRE8Jn=jc8r=5U6GN^#?H8r6Zf0by(;FgiZ-;wnCWoXuQ4mu#`slo0r#>`w5mYlQ+T5Ti7~?#%r4jQ;;;u7a5"
    b"3s|;d@}(yYV6zN=ks?=lGO&$>E@k^*@Q^q;sCWCkCPt68iy2_i!US{rMbFMzYwqVscHw<mlGY3EDg)&FH*@AV3`2"
    b"H1!g(})~Tf*CrEULq+m^<%!YY>(dvHOqoNNZYy(uZ2i`+orFx7giArC*dU<XgbwCy=3|OEX0R^x?8DTpPMHK(jQI"
    b"9f?@a_#zxG!?crC`9MQZ))<#@D92!vVy%C>#kl72}S~_brhsq$t7HNEPJ>ZQ;Zn;5mL4RzWZ3nY{hgC4p=)Ob^?O"
    b"fe~Kre(d!w%~glDq0ddklU!5E+*hPeNKj3iRv|}_yp!RH$ISbR&ujQrPV=c#MmNukgSy1Ldlf;U!s&**<LwBU4}P"
    b"2&7sb#0UbfkcIS@67%u5288Mx^vwzAWK9#@WB#J%n"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
