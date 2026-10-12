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
    b">tEJugUZOr;k+Q9Fh4b{^9lMUJTe}3Nh&z$+BieY(OpkL68vqZWH(5`wX3p_4+~zYulOkFKl5uFpoIS%6zirv1U|"
    b"<A+UUl5VO5T&NkqVU2F*`m;VlQoie_cU-<jd{CvpNh9Y($%?U`)KwpJp)w)Sf*87pbvydx;(bN;2aZgbL2PoXT#@"
    b"flmXompBg<OCC_OLquP45w>YmUm-8BKho<6u++-x7$phXkwPTdsEDjnMbL{_i2<AYda0S;jDWNG8%9)+5#iW%f4J"
    b">6aTyU#vB1E&$D*qh#cKyjVXG~@W8>Tn<;N+zj;R*9cxi4mUM{oHH&xq(w10e_MNi*9d%s;Qw?h*hc%0Lvh!&#!K"
    b"91TyPWIGXWFWmoTvn|4#&9PfLFTz8>pJD4_(Al|5URo$oPH{KJ;qG-Z^KUD6+9?*$ly|%SRgVs6#-PY*9PX+=dS2"
    b"hre<*B~L~~tU8;P2x65rY0m2@%;i2|kC+HY4*VkKyiyUi9GGs6>qef$I8)>v82%*L<EHuC7mFj|&;=z=+9W)8%hQ"
    b"<q2{i~X#N```|4oU5)x4T~FMoOw`wg@!r<R<^Ev1E{(~h@RueJe4OVSS2I!2TV1O@>|B-*6Z;5jb?Gk5tRQ0;iK3"
    b"ena0bs^K&Ib>Z<;gT;w5?Y9VR|R}N96XxLI+CM%`9f**-*<zgNYZnz$UTC^*&cK)Uv@9&2p#Kc&|;eWb2y$C-?26"
    b"mxeZhkV_ITTvsRs^FnW`SyE16S{DQmArJi&<Ge&<L51?#ZRxpDWYwo{<I>77nEJAFmje{?wQR1^UR8^GYD*gTi1Q"
    b"(L<H)wJdMApbl2DNKU=1>xSLBd+Nh|Nat3WICbP&A-fa*1Fbvw^Jss89@i_l(*NvROcf0%W+Be8>#Pk_Jb6Jl35?"
    b"izRRK2+AQ-;-j&!AzM>x;`<*hk25+YG{B}ldttLwLw3ns(&`ibF^t4U=x}(cZqTXiI_}R}kuPmykx(5#*s2g>oF|"
    b"@Sg}7pm&M4ykY2%Hl{xmZ;cl6R$8B*)F_9M||BMeQ%4tn@Cuwg_K7X"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
