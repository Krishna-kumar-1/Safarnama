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
    b"M2P)51e7U|4`<hXz^m)=v`J;7E<+GEj_UJ6BVCzB4N6{h|8sJO*J+N#uv-;g8*a^(eXO&|4v#iw0^9+ky9O*VEIg"
    b"Zv<(L3R#)S1xBZCzBeBCu>Kf%n{vq}L;D4PP~BM{UTm$*ZL-I0@7Brc@b#K*gu7Kl@sf}}3yH;b{IwyqMba~Eg=I"
    b"e-2UEgwU3%)3!82-*xb)xUMT+h|jo&~~#_Aa4jc#&;a9P=U2{X&~PwP2)Z=k~_YcXAHnwP}UWQEpF;%xSU{JVU#v"
    b"rS0|8N@Um1s6v$}2&l8T@I@FUeC1gZpV}>gg^H#*&RW@$o3+&m@%j(M;NP;L#9`W<s>N35`L_;T=S~cM(KcVRa-*"
    b"<7=D12G75r=V^XO<u)*<W#B{uh!t%x{t)GDgF~aOO40Q;(;tU*6^Aymgd?WIwpezrdgLtnqV)X#i{R_el2NfY=SH"
    b"=-=`STA{pMr8C))(RAWY9lo#k*9Ts`^@xqs*$Q;y@hh!Iub3*rJ7W8?${~g8GUl4Kth!byCTc1**XPQ453rrxY}}"
    b"*~$4Z#7q9S5vLSK0ka~JE*iHXy68B9!4)Avyt?bCkPWF?q9OXD(0^jHLoYlr~XI6UN_5$)Mzvcia8WH=434!lHzB"
    b"C#}Q^ieQ0|C*^y(V5x9d%@0?K@Z0B)ap)UfPai(AhcMfD5i6v-lhf7tR{XHu)Tk7>n-M^+NNk`8H5e%_9yO;o2Bu"
    b"6I*CrOZnqXA8PYOGTg$=U(&m|Va@;<>z|{KVLHPvO`2FI+vE{i{V0))Lj>eUrXl6K*IApWUG{D@WF_Z5{1v)&Kq6"
    b"^Nhg_Ts7FA@quARBoe?CDRyPOc~fl}Tr0ao6w#X0d_)QG*To7xZ@aaKRH+m$~K(j_F5l(UU5P^X+>n$S_yDPS1vo"
    b"!+$k>NPMz%U>o&yYM^5YHNPejpD0p8%y|vf(adfw+zkpCOZ%qz&v^I!JcG#U+Fd0n@$)<;Cza`@n5ythGLg=IWxd"
    b"1Zd+4!$%JfXxa==#=4Pb6kLWjoS)4FfFKt_hOwlQGfrA@j<x#GElH2ojv>)LzNEWZPn^(UdAT6)6IrjlHFB9ppZA"
    b"$BksgHDCvsz7=qu#<<!9LwlWWi9Y0mG%zQ8z`xAFywI{HFyWAj+t=#o<t7i>Ks7K)eP{cbJY^wYjZgX6RFL>CcYN"
    b"{UUO5dxf!(leSg=uyj(+i-o5_R^lr*YF=tE)DMoiw%L!%=Ux<4s9)U;g@EL&HIz9~Dtkb0huI-L+lzP37qz)(14M"
    b"hiQaqARdrHiqEQnBGQe>S=xJ5ASxs~uwJW-m9Pzf6@)Y3fYRlYZ95_^ze^t;4+G*OPRdT#)3OzEqwLfK>~L;B`6I"
    b"<8O*{h$~F6h9H|pQ3~bwKw|pQI|MwLSpd9KYiAt1R4zZS)%_5#KF-LBk!|9dA-es_17z6Y18CVH$Zz$x(lnh)^Ey"
    b"$Z%%l5lzpL=043rCk#{"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
