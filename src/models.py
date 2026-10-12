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
    b"cP5=-{@`0Tx@2x@PQTq9sXvAuqWbC{eHUKx;cfEk(0-;JmhZMNhf&xr>LC$G{;=C6BA>Q=MRFD@zW!J!72V<C3zT"
    b"#=b2mk5B?`Qxk1QekOHnOe9*vhofQo2|<_Ae1?;*rm3lZ<-9u+Ygc2LTOS=#>@Z4kGDp3$JJbP|aZ5U782FROk-h"
    b"?+M{0yQqp0Z<)|<0R&Txv!&GZrth21$VdF)W3jF-A4OzMq6cxf{q=wX4~kNjOlY%c9P&v*g;O9ZZfQ$e`&7hz}6!"
    b"zd`}79i4SJ8xkr9BKNAK5<&Z`pz=e!Hq%+4Ey13Lf9-De@BT~%VvmskZ!J)o0`qVUvUJK}_16+77$c}=)>j`adE3"
    b"h)_O>_{uz`FL()*<(Vbtpn6L+aNoA}XI<fW$2glt4^E<WD7X*seo2zQA92V5^jvOy)k|Hh@<SL(aL#JNcY&UQ}|^"
    b"jk~ah&O=4EJxM=CG=1xwI6Jp8b7I9A=O`re<QQz1-m_v{dsp=g(`HSD6R3?S5~Cp+I08eih*Yp>T3n%Xy%O`*g|X"
    b"i`?ctH&6{mYgNbvVn$E<mNrqO+M|BZ(c;$J0rR|ZAr&}g&MGp4x=TfXT0yQt`pcL<zlyQ+TKZg3o`j<Vh_O+i)VF"
    b"{fq87ak18`J|}xq8Nm^QB|&CJTFxW)d*qW`C>=B74hg#@{Xr<EzIZl_rYcgN<Mx&BPP)S<*ohS`Ob%d?1~03i%H!"
    b"$^@g~)bfqUj*wZ+S5J^x0A4w6~89|wNbulA-ob-N~=H)Hi)vkL{-2&2jemcWCu+c6SC^niJgeCTz6*fl#;b$}Ql9"
    b"A$W)=zl47fdKVVK9885{xy|c-{pys!GpR#NA1A0yJO&ErqXPC_1XV4ES~lcsT?hzm&80dyHy_yM_Hu2G+)&*!L`2"
    b"4w)b?TPyO+QFnu0)()_E^{2kEYSs|vzs@Ol<FaGT;-O2)=2ZRX+f8Saz&+dP=Ee2rJaGFwM!T*24=K=!m`)0#=%`"
    b"B}eKVqHz_TK3!-S)vtG%BjY?lRy{GASJ%y=ceTzW&6jzp~5{iI6+L?U<F#(gB<fD#L^6#HxAI%nOd2uzjxH_(9~R"
    b"!TSlg%4@&y=rd2>xI!ouiI8(yx&cItg^Rr+GY4qvyYWNx=N0n4Y(~!ggzHvVoMHoCg{QDo%8YgY6kPx?CH1-jyvp"
    b"a5=87onXY-C!htz0`(22#&~&8@tW`(MNoi}`0bEUI?<X>(j;22k3M%>}M__HisbQZ_cS-_Yi|AIz>%hXA#WV"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
