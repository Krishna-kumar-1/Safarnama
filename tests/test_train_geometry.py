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
    b"D`lva9sknL!$HzVtlgg8e_WU2BedYd?+(HvRi0LIed$1PsDBP&AAx+S0%Ou&-x36Y2sO(qsKH2?Ae768erv98!?)"
    b"GR?L8mX=_bcHadNJ3A<M@r@o_|-F40xuVk1FxuOcK@AoW!nZxfZ=06UcG&IpU(6pn7Scy3s-_TWZPdHdBP4fxyU&"
    b"XPz3;zYmEdKXhBgU*d;mGqX?bEyLmj@yrU_(HW?pNyJn#W9IzR843&P;<P3wSYjd&p!$2+h+R$h~?)FWw2m+cwpH"
    b"1Z*yJBY+=*4#HZ5k!&&{R6-EUuE36nUX;BxXqvtxyL*<*b7kG=e-!lyhhP)bCs&lI>!MPAs`c^yxh&p7Cjm+!~`N"
    b"}9|FodSxYeaKjaQ?T_B2dr)c@`<dor&kWBw8RJhh$;`i@ylIFy5i?F7}X`U5X)CroECXvx$MTdJ!ZontEpUf|XHj"
    b"KR##H!iH-zx0f}A7>d~6)k7#GdE_WW=&V8f1P$3V>*KsLLlZ1msE49ted|7viO~4Lrm~XrjY+(Jqqlv&<|Qwi$(C"
    b"<K-*A@O;!FM}q25OKhY023;&X>}&9m>psP^VYcZYn)j#DaTlZtD+rhxL6sSm)J&$&b??x#eA4u!Lk^OEbF6i5iDM"
    b"68kXck%@6GOVmv|C-C08S*W;^@@o<Q*UF~_=^olq8k2z+zz*&*fb~NwYkKvGnjwv@u^>WqrsU<cJ)qt_n-SF1o;P"
    b"=ycygii-V0*qa+FP_lAWzoWiMwNITUbG1A<@g2dvs_yOVFH#^WQ$5j!U+^ZrXpzV_;<A^JPuu79$rlaJK%*|n{_0"
    b"dbp`-H0$XgQBQ<ga{ko=mijI#n2T^Z8bNHSgEkI^}A2CNyv}|0s#@s*>xiab~?KaQv!CO~%3ic{2&RAUhn=G3eqT"
    b"@n@>}9C`k%f1eyb9tYb(UEy78#eS4ih&e2&Qt2C)#8UqDuWIuDM8)em#dQnMt$lL|k-g-MmG8j!@?5_b#>ECLx*`"
    b"MmPwflR|Ne3RrM5?V9ga^jlH``eJA8q8u*a2$g}%Uzne6=@@NhbAsuu!0)v{6xLhHqL#8gD!-B_3H`We4m^+>T7Y"
    b"fbE4A#gc*of8u<)rdlTz#a?XPvXe_s9whYXO1A;rdz3#KeOCyogKg82%~{=J*cMn<zVGYj20q!F;!p3_57_X_>HL"
    b"<&774Q*j2e5u6fA#KTdp0F}q%kc@84qd^sIUlH&Tz)%!}SF=JT0f=n?B1~_NP%Jn(FH(4&{l@k8{`E##0-QBB*ey"
    b"&~mZ7c*fr1tlZ=yl+bQM*#+uTkv_@XJS68kZ{|_&3oP!!!@(h>_Gng*v`m8U?tMIw4NHOO*iPyYQr@_rXh6`LZjJ"
    b"Ty{D7Iw*j_IQr$g%IRFgIjvQir4A`k<`u<if^83wo!=UMQfwKgdc``b{>OPCSD2#Y@^o`wDYt^IT(&+|(9^C~&z&"
    b"^PINt^%yeu-`$56|)xkINB*4M=0v7wQ%=#SadW$xT_tJU+f@uRFKoJ~O~?wi~$$eXwxv0vMV3FVdh*7QCpJ2H#bk"
    b"Yx=|HW&T3v-1xeSyGyJ2>"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
