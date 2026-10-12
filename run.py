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
    b"Dsh=VCyh<uJ$H;3ge8K97NXEHDtl+Ig8Wa(+N*&gKo1@T5`A8H?F!(+Mw`maxOvKc%C#-NH;d<x5%jwJJX$92nXj"
    b"xTaJuJ{9BX~rf$YJ1cooXdQ?qzh3V@j{W!^$lF5<ujtyi^!o6*e22RWm_1KLGxuY|(ek<1M}uveqoQ@I5U=DGh)Q"
    b"|N}6kNEBa$O9(E1kAX&9Eq)%7NHX=y=<RDdJuLiFgL?IbC$B4-Vs^x^yklpfs_3L;8?PqwGjd-m?RasQgi6k!~2`"
    b"pWAA6xoW$_JT>>ze0#?pzN1lHl{{ymL6~^>~P(j1Bax3VyvhYZz*n)6`&t57Ht9Il)U*Mva9xR_0_}+A`JK2tGGl"
    b"kVy(XPRd+`=&_TFf*x!vOzgc-Kv*?|hZ`6<a;k$>QYhKsQwL*n;mPNpgcE@exn|B_}6+4w~K$Z8(&8n>I>aIg*vm"
    b"rJ6E(XV1uPf7B<FC$v4>KB=%D@EX|4%!K@+%3{YncDJVq8q*zL&ah<Oph^v9kPSCLr~*O3>U@^B9wAa)LTTM?VFs"
    b"`Q-KplYRAN2(VN7=W)CzUEu#G}O3Z!qzRBJ=nSQwEx@oR68p$xjfRzI-{Z%`LcR4RZTXuH9H{|CtLSt|LRG#j#k)"
    b"N$+iS4J;f$cHaF=$%M$sHv?E#?#C-aeYC=6;bmoO54yYicQ`W+U}ZJU>M?;iHnztChVpY=e%5XgX3HIfM=-!II`}"
    b"Q4VcK|*RzMw3i^rA+?TT<Hvy*8=eDU4Dm!v+<C3vm{53r(-PaA*87=P^LjzSWReVf@;sZt3!hnM{5{U3G!Y9IOI}"
    b"bmImaQiMsLlugrBH@@StmG*G}WMuH=@e%WuJ#_s>9`dsKpiD+BG(YU9bN|EgF~^=&6w5@`x>QR0IWHaV*CAJ@+*h"
    b"MB_g@y>F$}^>qrVfJf_qm)MJgoA9lxz-zfzsQxBNk<3b{HszWMbr*>Ty2Fonc}gNt*8alrzL7Z4i^5COwN1pq;Hu"
    b"O^4l35mpqs={&{z7P2^b05&UG4IDsZQl4Fg6+%RhAQ|E?@RKce0hm+Bx7T*n2!6}ysMCcj$u-R95{BUNh{x4k8?%"
    b"Z<2@Atf+WuK1;l+@ae=RsFDYC~Pp7sO$p60moN##w4b)7Gns~If&*6M@WB<xitGzQrP0^){+G~-knZWdBR0WgjKq"
    b"AS}QC>RSOV;w8=l5ah-z-^Rp7e&J7$p$0w7Ricxqwd>HTq280UE?P+v2cSUj?&#C)78GSn0R2CNbHW3&Gu*T3?fj"
    b"3+6NS%y?=uUAEKfm=OrPVAZy$yg9hzey7VM4)nCQt+?I)d*=6k^<jjk%ej7!9MXt^E8I{%27dx(xZIjAyq48MER0"
    b"E~-icbu~Dj9KTIKr^>o&V|D$h4DG^h0Q^m%IDg+`(=s)2aO(dN%Y+|RdzNYsgV9(^_nbdTk5+A)@j0!VpLJcj-Y7"
    b"-1c0_G=Icq01FNX}800"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
