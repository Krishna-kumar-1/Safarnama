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
    b")60d_ORXhtP*t3m@p}Qiw9KyId!C$=C13i>)ctst+N9pPmSD^1jSlN#aK<5;n22<Vf_+aTV0Mio@lV(99Id;0Ngv"
    b"YMw(@gUmx853?ZM~my`kQbpru1+Z+uo$=WT%?mMJo#_%a}z2#wzPdnbL?k5^WTXvvieiF$pyr`i+f`CRbhRAule)"
    b"cPE|JBDrXDu{)itVrL-`e;kn;lFDFGZY47IHD39N^uK=FQI$lEr^xQiOLlmWb)alon?STD!H<hgg`+_S8uhsmS*a"
    b"=T4TN-9$j<Kr?21Y=0G9is1Za&Chx8(d1Y1I;`-4$6il|>8L^>$4#!14S*C(?jIFyy38GbTaZy<59kdijBhwXNLm"
    b"cMKd?>3JU&8wGW9br5?xiVV=XbHSu9sU%`s}&$zGqeG+YnD)Bhxm!=Q@#wRuc8A5vUcY(SxTtn?Roy$+by&!Uwxr"
    b"hV08h0~2r(#&rO{KVo2*fICsQjx0U}W22jLvDZLb>R-HHVzu(5l*y9F<!e$&oyBaEpKkbLCEy#nHvQuXx|{l8#V6"
    b"x($${6`+U&#YkyEI|e+o?fQ-;$5r3@|ms%6|Jp7<Aey_%%-o3Q#;rk$WL4{jLb%bBE-eOF7*kkl3GqP&b{Xq|U`H"
    b"!-|Wi7?_pJil3g6Sp&I<{?KlNmv^1maI5f&lf*Y5?@@=okU3pj-6UTQBP{<C3K(l3lhm_$p+vB;@96^>1-|}2&;u"
    b"5yx$xSNU}d3tcP{`8;`CU0WeqV%{Uw+c<VZC*$c*4)&0rhwyV(i-!~>2yOovnH|oEv?MUKT1c%qEu^AzpFVh2oS!"
    b"yY|*+=Noe3kr-MNA1{$ACLHxl6+F_#;XxKa)9ExYSzP;KWu0K`#Dkq)Up2PE;I)k(LD&GEW~`5lTQ8VcoN3yWSb6"
    b"#5HCw_HJu6S~VMv(*n_W#S}@fswQRPvBjiPyxRIadDS22*!r8Q20}H|YAa~ddO==~;7k%_0kBybW?<#)aJFpHof*"
    b"q^^lqr~;lcu6{R`1l?!LI{P-ST@aWr^S7mXHw8l_e{)=H^~%cfZ}(H0Y{8=i0h!oW>fgr7BvvvH%I&~X|A4@7w64"
    b"7`azH0_H=W2Q@$S_61K|H8xBVZT%w_YfT_fHRE_E}!ehmjus;e*=4k!630|eQ{wvppINZJ8B@Jaa!zAnmKxBxvu;"
    b"2D%x${aB5!p$EGMY*E>zxqE0&?0y0~!7rVMBOpJPC43vD_gb>z+RXKugx2|{cAL^3(A1#hY&!JK$Qz8;i_7*JP?c"
    b"gcp)1n{L>*8vvedCq8A4PZ%Q?Er#w-f%Upm<ASaM_J^M7}Fz|M@CybnUs}iEbKz42eJ|dj;F)JCh=}QeQfO9GLB&"
    b"cdfi@<f0B2KYrwWDtak+(4h~<4jZ3;?`RWZO)X*xKX3M;cF+9bth&la6jG~MfYxbunm2K`wWp;?tVAO<2(&eVTFx"
    b"}@ufPe227;~MS%8+@Q9BPt!fXe7T0za(IzR0%BJz)y9NAB)*u#aFo74VDj`2G!)Ht8$i+LX!3L_0_<|xI#pdWWpz"
    b"?|m0=^CuCZZeS&RAXhldLEMnz=L7jSb`@OS~-mNP@m|hD`xP}T)lY20xL(u3XA8xIR!Eq5NW#Cj0=Y&4fOJ}2xRj"
    b"FamsnnM66DR4raf2gm*y))8U-u>=h-KdQ`HqMr9p)?J4E)4VUtPMg3RhGrLEmG<+ZSr>micwo&BhPx#z)J&tHl6s"
    b"IC1H*vKxa%ut+j+#@2d8i3xlW{hRfR?ahD5ob`&DdJy-MDIf#^Y*}z6&4tT_-5Z&1Syk?ULzw$j^(#hFdQF+6mcA"
    b"3hfpO4fKur`ze5!i*jzVTp`qU48XUw)DY)iS8>cr+Ft}mP8H@HP|%(gjW<0dvPAG78VtLXO4JG-6eMY2AcJh;lN+"
    b"DOCtCboa%e)cCESc_F{yF|fv)2geIXY+wUB#BH%T|onXprcjRL==-#-otiVoRe^p@4-Gh<9?Ojks|V&~08aSnN`D"
    b"h{qm$e1)hOui3k-k>x8vSmuimAxcK{Ew>YzT58OM#;4EN7GKhuspD9eB_b+1G0$B<3N6t)I6tA{On+c%#YB7P_Yv"
    b"!thVDZaKZX$O9m&{{~vI}as5%TrbeDQCsVmbk3rpVn3#+UGM7M(S@X$m$I7efO?Cp`+<lF|M%E_vo9(USQWI$eN>"
    b"YzCZ?^}+1qJUy;3=eS58&?NOx)gj_*6VfRwI||e@^VXauKcuVq*>VfwOY}SzxwY;9H2bC?VxTq)W(cr=aMFR0M*4"
    b"d33ZhX<3I(SaYxa2f$J!V|gt9=Naslzbz8!#iP5G35kGL1h|E;w~7jr&AyK)<(0YrhJwTQvekUZau__B>dR9uZ#F"
    b")U?F`E!Emsq_%cINPff!hDUtWI+3$8>>XA8}|OL*szTv#No?lX`%%mZ7Rm~McSz#(Fvqi@U8pAA=II$a>ts-mVh>"
    b"|ET8!5Y*&d*$icKYJqn!@PUL!cG}c1nPIe1J?ndoQROfN(X+M>N|r<mb9fQcH3k-o}y@TBwHCYK5Hu(aG$-&V9FG"
    b"Er@w0I(!o{qPqb^{qiwZ?k5TiZaFB{M(-dVpZ$UvCc2KF;5`aX1<sP#rhnym49q@l=4hWZGP{Jf9yM>teq++40!|"
    b"7RwN(}F1_GyB`7S4`(myvyv1u8lStG)w61xjV+EO$eUm>L$2m)6GlX@7AH*?#pemZMX67$DR7i=I(K6v~BNF}XxF"
    b"KQ=&XE||(W{?{9q|A+y8=S<rqd>^KN2rGjlHFxH=5J?w}HYFZvzw=|$;*C234LQHzQ|uZK^lZ$!0I}~(S|3O$Y?Q"
    b"=6oCV~bcXr@k62aGNyjZdWKsEcYdllIs_W?omp9Qy$HT{s}w8Ir@Gf%3i=FK*p<MnW|Q=mzxP0+UwG;a?mXY6@Q#"
    b"^GX;nD@z6c57^#&~O#ExfG%^us8{v53NNUmdkYnmq9lG$$1f~fWj+5PBN@k8x%^pmU|fpKISn_@e4=7S&q^cgU{y"
    b"d0Z&R35#Ws*Eg1WymQaC<!fa|+!Xf~<wj~X=eWsxk<!9I|@om6-DCjA*%&IdKg$U6S_VZ;%J=_;1$b;|AL*aB!ln"
    b"joUVmIO{=__5YE*~zlocEtuC(Be9RY|_jNAd!l0>YeoHLDm2KGv_;M^3E=PY<O+YckC32XW78iNwClqd0gtE4ewd"
    b"mDtt|oj2^XBN<*<%_A07(<7eVwGUW4+p4z#lU;G0Ipl)8JxlX(&@eWZI&Z!%E)&kQ*V=}^#+SZv5Hk0~geP~`+EZ"
    b"|OD&MAmM**_b9)_d<WB{!R3hAD_nsZ+fWG;8%8~w~MBgcE~yZPs8I|ZnVqpi>gWgbb)!T6CkOGRmW%b!Ca^BIw~F"
    b"DXo8uk$rjHrDg7t~JW{^gc?`v`aFBgTjXa`{USeY<MQT17R1(ysA@zL(o-1R}Lu8y|=SIuBHI+_h(bmdayW-9f<0"
    b"yjz%jebJHkclcd$*hWp6g9m`_IELEExOZl32Dt50@^XVjLbK)Zb1!40aP?b|yZ8OYHoMWm-TF3}F8xH#-u*-B@-3"
    b"{TI4(VCq4>o(Q#<*ywb5RaA8#kr&UyM*tJ`(;8N<gL3aE^y)Gw^>-$(mesJjx_L3@A}drltaBDKjfBjdw75K*nD@"
    b"r8rOy<GwVLY-Yx@ztJ&e^0pW5sGeOo-W>ae0MZ4bX_J#v@8h(R0XA{Wd>P%@+z=LpzAf^1dTSrr_(Wr&pwyql0w9"
    b"!IgNdhKuMM|%|BSa?H1n>LjK&NpbkRL_q~EH^vNuuaVew|s)9Em#J4Chy`7A}LqcclWE8EE|hC;R9KVpjM`FUQu^"
    b"EXH|%g@4*C?so^ZNKj8&f2Sk7ZX|6jaJx9rnT8TtJ5+?&V<s?Mu(r=o+VZGh5kT%Sf+!5epgfx)UTrkF#9ZF|Jr?"
    b"NLwrblH$Fu`PE-v7%FcNgb$X!S7QbJ4)vo>KM=xPl?zFVvR7}&YAYyDw!dK;X9(wg88}Dd^(nWw6uB$trd?dpeOQ"
    b"!q+T%5+c&R*z0V|1Z#V}4i{?t&W%x~5YW6!)jZ6IXZMKvEAN3wC*KtQ|e<@j6L>)4lA~R27<%QO#unz<HvYfyjv@"
    b"sLLoDTe#nbk`t)V6{R?`{o=p~pLY_=e6yPJ-?o{DU>;(~gD*n50o*cdJ}(fkDR8Atu9N^R2m}p7Z(P|^7cGYA;GR"
    b"30)QhjB@yznYLeUG~!!6%~`BQ}<o7ifi*^%uBY(dlxQ$wzWd=5!cX4rDm`!rW6;m~DH9CwaA1H=eg9dc1;aK<S3w"
    b"p?JAo;LS1X=6H=0nMyouN`g950cHg#~(Rh?#NFJ(-(fHz+|SIKJPMrecvSI#@66vLZog~WS?V>S78Lh<_`eSaAzB"
    b"0>kCi{M#nU@_JO!86BqN;WLmAIXU=ifns%%<eS%yzNpD5k;p$3OKK-PvOk&z2Oi0@Uw~feJAVb{_IUpV`lcWn!!l"
    b"*d|3Vd6yN8;Bmf}PC`BqYO1c!I##yb&O2P|_8Obh8?at~dyOhQ!hV>4Z=4B+E0$KdZt#JaZ9jzSCZ00l;vs2l3vP"
    b"lgITJ*US^VMWvLT0tiCXkd6)G@(nAc2vD2dTd8pdr9JHhxG6A*w#U-xX0TuoHRTwoHI(^MyG==%$nwW-NRBLO`Dk"
    b"=r2k?xF)K~vZXe$ze>()>F!jhvd?NPGmNt3e>>hZT7fKMydsH>;xotSHZtQju#$3FwWnpat@HwoeVD}UTq7tkd-="
    b"X=4!8DB8G`m|i+(Zx>Q_cJ99`7<w_NdNt$DTiy_Gjb{5=m;|Z3dmP9Q*))J2*xx?h=qi_KYIgztGE3$b*n^kCLdD"
    b"3zQRb=2BNh&L<WkUnpEzs{I|NY_7%kU4pp_h9ub<|VHf)fJiUZ4(j^<F<RDB74QK*hJhcTCwn|`;zh=MZh}~5M+k"
    b"{@aAurOw3f+2es)u>RiC=uTh+ZTX?c7c3J$IG3E{_!B?`p_ypo^&fR-;ud7hp=`w^-*Kl>ON#;jc%4l9r+Mbs#O`"
    b"(`&r+-{A@%BF=iw8%;z1xdhRYU_yQV&3HJSV{nkVdgr_Q23x>Ab=WLP+pN)X#j5FZVxCUUtSh2)`R)t~y(gC*yf0"
    b"YAddo53D4ti|Ay`SyUO1ddQ^%urhcHALcG}&xB7TWU($B%(x;bR6Xu={PtjDP~n3%W%R_bxS8sJtQCuu)w!Q}1m="
    b"_}Y`J`^V0TM87tS<p~|QM8lt-)d|kyA((^ZAmZA!BQ1Q*?s+To|M>{2k)E`w_OZIbhID;J~1ws%*#%-i6>IOr(I?"
    b"%O}mAl3#@?wi)^?dUqr^NC*=0ajN$<w!mG)*lRnqb4Tl(fTXD=wm-TWI?G4cnkhjCGj6E%~$&$wCjJKf2sIc~d9U"
    b"8&#XVWk9*zW2C%o6ureh|5HQLw+HL+cJ`_(tSy?K-IRk^KVqLukItj-d}n1|__zAY(@f<&>oz?+xBf4=46ixjr|R"
    b"AubYItj7`*k^PC!9EzQ8{2s1x&^ijzTLAHcH41_#TEpr(60l*an{B=d_K?It!~#p887VsWKHhHY%|ZW_H#u#K93h"
    b"aVH@&8JF;%$uLBB&?7Vr0rz`oNUjGc_AnBJbZIx&5CrG2r@Jc9;u(Ejm?y(vy1yyM)$NEeCuAtTmAzphX>kC8#x0"
    b"?hJ6fU%5J-q1J9kvN_ivlEFZSkMsnbC{;X=zRydPoBWGdU80f+%YUkQ#$K7Ev6UIgC5GPk#B*fcAmW%z3=EP<&Ws"
    b"ReNr5NRG&=f52x#zY>~`I2c2oNWa$FDFVlaj8@qRG)sG6HQeN%{TCv&vU4q~^SwG1=)>r4+trL*n<)Fm"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
