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
    b"OiX96eP)D8!(^}TS%^c&U+eTU2<lCLSG>hq0ke(K|CvAt41F-JmdxXmlYY@Z1YNoKuPty8;8JVk%_*T@Ep3We$bR"
    b"_!wf5h|&eZ{(V$z@Zd4v^LToGixAd5O6LBc6sL|0^7*6?1Q&t@?0^+Zce%db)X%?{G0A%~IIxgVlTremYJjRPcWU"
    b"2ItJcyOGT_Pkd>v3c_y=eLp)x=M4wt5ab<lI`VK?y;gZZ{i9BWI=^r>&B|g_fmfeN9<u_{b4P3CKFpj&7YFVno^a"
    b"kkUy`(?829R#f>-Dked=`-Mspe(gy>04Y!jPxZEVa?JwNn)!bvnm4W?o#{G_G%2$Qli<i-X(>@ZlvDSDZ5YPRgHw"
    b"L%BhNqX6bQqUtl(DZHB>G_qMK`3-jASe~fr`J3Pce-z#&BmI32gR6X)imWHssT!dbvLG#~mto|24}!;@U!wEtg`}"
    b"hHMs>6s%m#otf`U7v?^8IR83&|GRLsB20owoaFgwu9+D%0=>nt8Z;bNF2p-v9QvP4za>BF{>d4NrJJUGn`KMLp<)"
    b"D&b}drR(ryFutwRvLM8q!J7oQ~mDQ+fU$9d~Snkcd}C#S)z<RMxNGz#SpyGc`PvzfeDMQ#Ho0nUVfQ3iNF#W#rU5"
    b"huXqKgT9egl@}FJLFKcL0W>TOUqObfUaWMcT&(UUEQGhY!>F^uDK*qZu>R$e)EeK=YP`jO`KR(g%aV0v>vM1_3Fa"
    b"hJV8bJXu38rmGL^z#ds(lRwwt8`E1!YAQ@|j*jr+yx&"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
