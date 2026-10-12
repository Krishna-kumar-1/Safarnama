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
    b"AXJRb4*p5$z_7D!tD6mqC=RRwP`PkJJaT3Q+@U?^0{XmLgAtWeME^Ar4?XntU7)x=<-=bGEb>;OVucaLdM{3%40r"
    b"1~Im@kDWe+=NA9-%Pn2!>Ypn^o~4Oep{%+G3a&~tJ>I+MzR8;z=(lK|BBFW|na6k{!(3;hf~;fmtNQDL1}(5#oF^"
    b"}E{z|3to&1kc$U?L#a-_6eMTRavR`t!iJtBE?w2q79sEnc4j{hPpYvQ-RCq7i@x-Oo<7K6xAe5ucaM*Hqky}*aIH"
    b"(jz&JqMf{C=!}ebUP8yhGL17M{@VbtfXi229K%^W`&%SqDo0%D<836IQADInc9tlPOIo>=j!oR3>^`Nb$<l1VW+B"
    b"$IePS{EV8~&~^_mWYk9OoVhybmYhJOW8LMbZzMTO~3gyjGmI0xIn)7h`~06}gj+dl-U8dTPru(dmh#NIg-l@q9&z"
    b"2qF-d#Z`K+`G)42gqE)A6`%_E6?siq&Dxy4+(%+i<pQMVcJYGl%~_lPzO|!Td<*!kx`bc8L++!8$@d)eqV7GZcq?"
    b"Pvwb#F?j!3Z4sQ#^-$<HHCy!jSKxBc)Mk#7JYC*%R@+Pwr9WA2c#ylmRNI1WF0WG;Pcc)p-^C1GRGzMgf@U{!cs>"
    b"9KfNi_jE18Mh&;I6d`5gdMkg^azw;j_Gj2mY!XST}Xq1=X55E)4lQ;v9A-k9$B*2pZT#2k!m5&d^r^)Vq0lYA>6r"
    b";VU3MdlTr0^&_CE}O8%nPR4>8O<`Kmy_e<hZu4p2uHbeGf{ELelqbY#k-yoojD?z#Sul08<oDa$CN|vpB&o_Lvl6"
    b"_b2e!kN(uP<<*klB6o1IO)!Tvv<mfP>S6Liq5jt8xHO6`s*x!t1MpuhaRYt(_S<%9gT0m9LUN%22P(zEuEkG5T0N"
    b"DfsSI`GA->xD>24+1DPLR*Dw$U9Kt2QYyZFh*;g-M*16fcQ|=L^FW_&$UZ5@)XR4ZP5J2OQ>W@s_{$Qk8@@bK#q>"
    b"$~PugsL(XC&gQbr*rgcuvEJ0Szl%`Yp(>{GK%`0ph;dlG)ZuULna1b%;2{pEo@TF#M<I{zX>h_<<IP|ZzJf!N+=-"
    b"CQ3aO#-Rt1Y?DrYn{91Pk@C2C|4LvHrB#3ntENl(z?_`#YM#^<(4F1je@-ZVznV&lG>2_*GQbOCIKHmlmjK)l2h}"
    b"Iym&UBJb92IP%2?z8*5dBZtzFcwu_6{tI1VsnhzDOQMavr?j+0PFEjPYXw{}J>}4RHU8!8+owkkN1_(*aZ^jmJeg"
    b"tO!t9Box5*w+KLGQ?+6--yrXeKN%TE_%yxNyzv`X>JeXX{!O4bK8~1Mc4#vlW<hqMIs(ZOx8*m@@lJdJ1{wQ=#}s"
    b"D;j7_mTA1L#Y{q+$C!gP@Ojal{S6BLSLwW`PAI0~BzPi~?6@a}%}w1|{Ze{|&8Lo%PDeBqODqe+`|aG_AWoiwQ`Z"
    b"(z*UYu(^0UVV*9{%H$5TOc@qg<Gi5Alc4syUA3(-=;^(f+W@FhN|=g|_*>SO=k#nwnbT#>?lX#>tLD{>IRueB%}c"
    b"IY6d$N8Av$?W+gA9;?LNdg7}_qE5@v&R{G4{kT0*U5V~k|U?Unw4YvFm>*(Ts_&O9@w0^oUH0vG)IVUl&C&fv*TZ"
    b"hS6y6Cfu0;d^?=r*@8K8MYCPzfZC`G}-V1UOO=rNZYFtpJexl{!*Zo%4uJ3uk#C92TlUu+^S{Cz}{lKz2sKz9rZ4"
    b"fSv<`+QnoOevGGTsq1_z{FS_=?j8QMi#R0|GhW#a^#hncVW)6!(@ioX{OmOwYRI<BqC7D#d96r=&!O%J;fvYGcOz"
    b"VAUVTc-E2l-W@I$k1R2RYE$dH;wk>mtoo>!0Xv*6SbqRDD}K|<<qlXGFGEwR8-z#IGaQmF0=Rwp1N6H8`9Y3G$*{"
    b"+S9D<g{X0(8==3<$})R|yhwX$S4;=f(~|NRVjaEneI(G5tbtk=URu*}gnHRl3W@5|V}2nnd?Yzy!am-;JujN5;G^"
    b"n(DAX0IgaUBSK;y$u}MH#hjum1W>upRR;XYXAoqS%WtyOFCBb=FR}Zp{T2u3N%iQ3`r61yN|6hnacowWFs$fL-%~"
    b"sm@q@a#!B2o$Xxf#qHZ%fbjP&BeJ+i1E=>`$v=3vt?_3#_k7>L>vq14U$?P{BH7l()zsO|F&HnSto`y$dtXZeJ6_"
    b"=bl2{>7;mO-ZHp8kLExtZ(7N%Ygmp=E>q&0+TDT-qd0oPiM-UA&e52H{#5r%0DYK|_&AOETD%!H!3Jxc{q=9;@K_"
    b"93g)gO$7P|bI?05SX^f_H0f-N*Lb1c?|xSpR}NxxS!TsqW<N?-2pJgV@0CdN=Yw1Risf*#06Fdz#(M^(O}FH8kGR"
    b"sXJfx>8Q>LqNjhC_LO~0UIV4JdEt;m_eAvaCdJF`ykN<a!FSXAWedew9wWq{WE&?Htijme_y=d1+tn3`+)trFn2)"
    b"okL6+&O`_p-LoOC#Tk!FeiD<qKm+(W!j^%gwR($|AgD07&9@J-(7PCA7wKbTE;@xtF61LH9FJs5SupGx`~;mPbxJ"
    b"07G_Vwko_;U%uoau$%g!0@TclYe^e8}s3MpiH14sAX$=1CS1n9;xKw(L*R$M&pD`ga!&Xd@acadv^z%`|Jn!$e=="
    b"DA+1?_bpelC*j!`gRWXz!KEDRF+Ke%C17f8-A=tOWYf!L_>NPVI^4C$A6h?errhZ{&hjej5)RnzpLHe0?>#)X}yz"
    b"D+zzo#xW`LFGyMbVc~frXy-~is=~-s8<M*&ndLB4dPeAHaxMQ%hb`6`G=`#hVmle*5CUiOrKN;t-LmNn_)#CJEOw"
    b")zo9Vg#TCD64!ScSBJd5$hN66hP+CEc)2(ZTBA)hZ57gH;2DWf@`(XU<{v<!%`2RD?6PYN{3!D%b=2y$9mP-`zhb"
    b"^ju|i4|nF6=^Q?!v^afnR6|{X~U(40`=1=32k+^kD4IZs5)TG39bw@{ta!`c3KMLC!UT);h6T*2foA)=#mq~c9^A"
    b"&Ja#6|E4+4Rje`f|$39t54?)KIUj$M%p)S*!kU&YqQ21F8w%X{va*_ng92t;G+shK29+f;t>N6{0&}wdlkk)=z1z"
    b"kN6mer1kP4e>n(nRQb51e?}SAl0>H~"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
