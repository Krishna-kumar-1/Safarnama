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
    b"2thyC2j74j8gK0WS(l78{i4bh=NYCOlnjyF&5(4N=F~F`5NW*+5rYnlZr=sc3G-#3ieHZ-&FPKr30h#Wk)+%@%Do"
    b"8qPe4AR#7zFHz#FOB787p6AHi@qENDaM7>g=eNRtV{QKyrovIpdQ_->!2?%giw;I*`|H8{{oMN%|wq@=UE_o;=Lc"
    b"lB4o+9jg78B4rea>?J9`<$y<ql198rxy%g6($f*6IAY`Vo+Xe(Nm&S2A#|Y;~_qmyCn}s{~{f4yqUTn$1;`oIGd}"
    b"D?@-iNuM)fXnX*0)$x<O};jnM3RnYEl@K(Qrwf1;d$X&bE*aJn9!7@A`Iy7KO$e5Mc@f~nx$<q~s6Q52%??4v)^j"
    b"4cTTFjo^ZC#vfn6)~BqfwLsDAw>nfzANm)O_HVVhU@d62GR5b){%#Yj8`X%t~^<U?@SrW!My2phl?Sp=u5#A-r22"
    b"U!fhF7{C#68u9{D`iBzZHPLP&+R2Z<4|AjrxDz<H64=L60RGjqKze<wBuzY0zO$)oVAkZ8J$XIsxwwxt!Z1k8orY"
    b";H@#Y`cuMf{=pzT~%@zPPq8ps0Ft-a^6J2-u2m}jCgy$xX3?yy}xmc!dI)H*Pa@F|$y8BzM~*oTjEP2%<5LSSw7?"
    b"8cOIGU;-tF`%qtHv2B36{*Abw}yf-f^Bl#4cu|rcXXe}&R^ihQA+<VtxF+)QqXc<{x;#}QP34<0yz|Y*}wKl_(+y"
    b"C8B=2Ig`rrcK|*^%IXO1`RA>j2<HC4MI*4q#dXij&)c"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
