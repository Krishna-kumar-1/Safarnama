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
    b"nHSI%?Kz>$ay#jtTmSv!zJ><cf=*C41(^wt#%cmVS3b~;j8urpPCALG;NF8aR&DmSn91@aeW#^)5c<dsJm}RQ=QQ"
    b"VN!aKcD)8J3jU!I(}g=F{QtiOG|^fbK0c8Ww~d;_m>Wxnhcgyn*o6`y%A!==!KwturvNtt^tF6oF|NyleI-Rcl;0"
    b"!z~#rU~!otwfTAqdl^=N>(W?5u0=CMxFY5#&jo2!1$@^j{2a7WI$87TS#(1S2ZU5PiY{OFRBEyk&c0Hroy&xSu>z"
    b"j^V4a9Gz{WOjZwU=9H-n|6Ky8<A^B5ou<QzH(k#|Lwe{;srDJcp@+P4VZamf?VmXNiJ3Z_*HSb)DXIic?5si{+Oa"
    b"ZNY@^%UIC&a^*Ov4;bWMg-5f<i3Hww;yv7g;Y(YV5v4Nct*{3J51Hm>44v<zTyt#Sb={lp-ZVMTlyTp_nn<!;W)$"
    b"H>T)W46zI(z)obcz?+3q@Mt(}IClP)TQ5)htB_Z}L{H<=oCyS6-=ks<8mUM7L0I<{NU%jW0?W%7xV`MLB$<LaW4|"
    b"~~b|lHSKeDg5U<FV8*V9Cond+Yb7}HP>g}<56PK*B&9jzi^qE`y*M-&F&0=T>oEJuCDC~l_D);C6`(-nQ;rAqCs_"
    b"!OSRU!)v8beR_7lC~s$9A<;a)9#+&tN|%u)pTzfD`h99=Q9x59f!W69TYC$Sayv~+)2SP-YUvjG&I%U-ob!Jw{Nf"
    b"1&I*2OMvzQuWnAS#S%^n~6b!l71kt`KR|T-d_AYsWOQOgeTbUFg>V@Ld7c-sh^xMX$Zx^fNnK;GjY%ukZ^U)l64!"
    b"7p+Vwl<@=^3zewP_^?cw?J@(O@rc|9U}p(&-igW0zPx8l$9Ziq>GK-7*d(bAXd*#qE_lwm`{T6yyInL5?~_0iO{&"
    b"qife8B7|gYo_nmL4C*13{<xIu;E<J8)Za%L<4*;yLi3YpE{hrUY7cE{*O%T=QEx|9?0mPOD=zv>UvoQ?^EG65>;d"
    b"5lE{H0e(54K#Q;ol<aLO$zb0~keFP#+43-uZ0LJm50q>CdhH*-@3{uQt`vLp"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
