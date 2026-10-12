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
    b"s-{+oKsdFN)TfPi8h%ariOtA>!9N+-C&_7I3Z3yjb1a4#a4H7Au~(0_ZyvM3_74Eq1bqQzTlqlhF^<cCPr8Sn283"
    b"$nH-M9dj1Apvvj~E$i{wb_4^9?6TJH}!eQ+4v#YABuXeOCdw-9X?&r*caoqs~1{Xr6?jqPMPXfK4AY%Omm0y*KJe"
    b"9@5o=bdPHY3&RpC77AjJT95(G(svFz$=GsL7(W}ZB9*bk!HBgV9KSueJxV|<~LY~@M<g{<7O7;-$EU}CrW4yG5Ti"
    b"0j`GA*XnPQ$|0+yX>g^Pa?|a#`rJ$D1QJ`)*#(in$Hu9LGa(c5eB$czD35Pid^y3d#aE-8c9@U^<{qeaiFaB<x?}"
    b"PeIt3eq)1+U}4K6YQrJEz|i%F?@1;-tLWq}Xlx8(Ik487fMRB_T^C+;_@2<;vWaBt(jBF#{+wB`!BM!ZONP?9XIW"
    b"<%+u=$6c))*&1|V!snD^kjl+iXK-h1Yo0UyKPF~6Cqpop9@^9Ark-oKMVlvCVmcm+Uc3HrS!{A@08r23cvW>@DPc"
    b"R~JXOy_eq<Wg21%!O{z22xOLZ~S>I3+1yoY@zFKZw{{`TUkLhee8v6eIsw_A(DDy0y>G=t7%f)M8G(Ir|rg$<v@z"
    b"*y9&j3xD|BH5IG#hm;ELrBCMj2N9D9`^UD7ixCzgo>iCrL(~T#oufnrrr}i3AetS{X=FCY7dB#g@X0>xv`&0rnMO"
    b"6B8VM2M^u@UB1}>GE30y5x$w;&(b|q8SmrnQ$pS^nl96-qm`{?8duR3an293X&U6RTIAiF~n`g3PEm1NS5qPJ_AR"
    b"Xy7COWo>pU3Gj1bfCRtGLJUEDDkP@(Fykhi-It9@FvCV$_nW5jf@6O5SH=B5bwlc+f%G`)HP9S50MxcJOpcjm%Nn"
    b"(D+W-3J8R;FT314%o7->7{4X=5<W$!`rmiOYy1J_p~H}MFuZW)WNeEuqWO9Fm&^woA!inIbw$1+z(P^n1A8(2o@o"
    b"OD$WXW2qu?pI6DPO(gFP&kITORpNedZDR8|O%!5XHVJ6fMYdgw()?f"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
