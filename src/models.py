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
    b"tCPz8_Pd@2JfKe*?1Cp+i+0=yS1cPPt!4P-P`T?QKaAERdoV{@hF#g%=wv{+Bx3fY2_QPkz1Id(kTZmgfOA<HYFm"
    b"KX`V(i5n1U_>t>MGz4kKJ;PG3O}@jh`v$?^Fq(qdJw3LWl$99Up$EP`hPQdxtm^{MANFd)1LA;1w^@xSvJ#*dsXH"
    b"4?SzAb@n&G@k606H;(cNPD`E!S0#1D7Z$i)$@V1--jv!92HOqX$_g6-hQ~=!kA~fBfwaPd8(pp2NsT0GT}T<;vWG"
    b"wIURWA+1>D<NP|~>P$f19$WOQE!Ksa?rt%hP;QE2H1swKRn|Hhv9nk;mR8Kbh+nYefmoLK7uGI3C>c`-vF58@F`~"
    b"IBh+_*_}Z_viNJK}~-bc{p5L92$`_~<g+YeT6w3>iH7dLp?NO~lK8pC^-436Hj6;a<!}6t#^QcA&`5Yb!Ei&lqc*"
    b"BF$iY^Muq}Jmo&1Ho&^<Vs)CYc;P{-U%~Xd`swidOC9PIS`dLi8bWXEo*@5@FzQ1L{WQ|GSRy8C>yWs-QYgdhsB&"
    b"(Q?9Gsd7v`$B5+d5v+$;Ua9(awtQRGu~H}S1N_T8}~nM9c$ejYQbd3QSM{`Q%NM>aBRO5RtJL0asfGx2ZQOzl*EG"
    b"iEe7&D1GF@*^za8nKiCf2^v->A~Gn^j{UM@J3~|sCi=b(8v96=o%IPNAvK_y9!tI3={zeNN$X(_~M4+?n_s|(Fgd"
    b"s?gc!H?8Nu^hMuG-g(t|lKBDC|P-U}$$hoQ4zB#0ev$tI1rGV9jOvVc_5m0kb4HBO_Df*jihUlm4&wT2C%IL4;3O"
    b"KSx2%_X(f~K(cfH&yq+prg&#b$?(hy#^S5f8X*GJ^Kjyuqfb2T<C^F*gUmd36QGy-{L^p~goFum*Yfesk8=hDxx$"
    b"o41(f`o#VK7*nZ}YnD3R*KTC9FNlHg?;x*SQucZV&6oSX%ae>E+TmvL!T<`HybEAzC+~NPz8>AQ!Pty04WxqW3BM"
    b"O@bQg#bZ9AyS;mHAnZf|ZIyyZ(vZD~iLV}ez~!MV~qk8rIl|KS>Q9`IUT-Tt6<_&58AN=9!#?+I0JX`^A!KJ1&>>"
    b"%y|5r^dVZ_&guCySIlAK97GY)9L+#5%ETz+sXO1vCc%!;E1Cf7B{JR{F?`tY<5Z#a|$`GJbZ;ugCg0RL18kdta7$"
    b"@$MPLJNdVupGsPh06l*w`ZL>7QtyxAoODwu9TNY^Q^r)_~7Q;_xR9D`B((>i`$cj^Y{%$CfHel3k$#o!%kb("
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
