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
    b"pmP#o+w_{dthf;+`r5|QBJZ8GBA@iyTEH)Ys|H5oOSALFGkR#IU|E_)v;%%BRA}CQm7j5-f}8aL_KlN1gG#g==5="
    b"UmAv6r5Cc`byhC2@*nx-U}*2b^p)b3hqp5JaFkxbXu9pRxSRnM7kGy~>g7&yZ1_QcI4zOZN(HC};HJ*^)DtHhj|%"
    b"N-%#-jLPmq{z-5MP7Vjqc}hx(oGon-y1{J8`lqW1Yv!^k=WUY_t!%j2-zrQ;Hg2yc>}$QO@R*0Qp(!16B77b=qKL"
    b"Y0fK(7%~x|D)vD(Id5CX3J{<PY`LEGX8j}MM=-!KdD~*e$^!Vc3iPOgqJ{(@Q1EU&^hiR?G_aVz*Yam$Fvn)DaJ0"
    b"PW6kca4vv!{u9zI(OB_mp?jxh9->LyNCF<l~6f#D77pCV=?)0^)kGzO0%+VI2y+_*;B>>73v$)=Awe?FphHWgJ9i"
    b"6CB}K6d^!%ubf|5sxU((lLrZP1hd>)dsbU^e%U5^B39DGumL8Kdl`bNAaib08^Wo4pJ>da<xSm)dTG)`e+CN^yoq"
    b"%CaW#=Bi+gJ_vQ?T%kXtvMxzpmv)XikBC1e5i-@nt=M6^^c+fh<48;SK88vhPncAH<i=5g|xw$eTNSO^xCeu|wUQ"
    b"7x0+ZC6Z+4gW?RNGAi5$@|%5N$RdKJM%M!fff-<%TnG4yKE#qsFRHRAzz-{uP$8>zkZeG&!T+AK#H!#SCFd(cE9T"
    b"i8r^s@w#vS{eQgw3;#P(Oamji?7bXA$Bz9Cnb<B4dW`%@)Dq!$Uo1}l#gnI)qhn(&Rk(LR5gK*E<>oKC*eA^H(ZH"
    b"b$1YiF4E9}9yt;!IJd4J7lqW8;4}4lIWCZmFo$q;~im$qIFi8*2un%q23dLCQcGC@37{ql~Smk#U*z)^2o*od>n_"
    b"tzA0+DWu`=Y1GMfcj7P24_C~*&wUKyEPzpVkE>*LQ|$~rB$bGr)S-i*e%|#7b29p%uq~B7+ee_6Hi{3T(Qjp{$8U"
    b">T0JV~#;WSoH8wg8<Pb%%l?!rSxEHzi&Z6L!7Y3SPOCja6IscGi3dby`?uJm+oh?t`?8SH#5Mlj5bU_fp0VX4kp_"
    b">ZA66jgj4e2<)GL{WFfU>_PN9Te#a>Om=R)CyQDbj!avXEA(}9pl1GX0D3j9$}acv6Uuh5_GrqOcv@vC%`id6VPq"
    b"rI8LvjZvqF}*hrJ*`0ud%l&}2NIQwH=)&HQfi%QoKPjUs>5e~FXfRSrVlD4C%Np;#_i+$>m^G5@iRT=hp-sC)>dw"
    b"rytpyLtqH(s4(iKAnjr>Wk-{wRZcZw&__)G4xn5tz5Z@a5y&e9=sO-b8kY2Nx(DUqOWTYv&qt&$&WTkaP7syq&8U"
    b"O=g6gsbLUiF}E=AelwO><RRVk6GfJ7F%lLE6-`>1`#FG~e-;ljcrv-G-Fx<zxj@KLDQsQRU}eY%w2*r#tzA2-^|P"
    b"wbGe#t|j87iSKe%B+pKVj7ntCvslIp8I5Tz-5cIC;(k|FZ8)r*}DPcU%+S@X)_s%L~%1Cz-5L;p88b*pX7E|4$lp"
    b"0A4rg!S-11T;2G1ew(xb}hI;5tv0k)Z42rYte!`d{Op8%eLA!$<6Cwnc2q++iH&A!R@OBj=6;l?g(N#gn1msy}nw"
    b"3F_wTAXrob{vc7H^q+ZKFJZ33y3%Te{*=v%V)mJiSWj*G=sL*^|$aAsJdkd(m;kUo5Vy&Ro&)n1kB}y%qX}@`Lqe"
    b"md`N3%h)S&i;JU#t8n;GC?P^h6m4eRk))2Y{qjKe`;hMs6UvDY}=YDZ+;}9~5Kwcv1mj8zZdIONHE8?BHofaGhjN"
    b"=s-@Rz$x!Nch+lP2jixdmOhyq7_s${&dkY+9tU|MF1zHCH8h%fs2LA02QWn=6sW(|{e{^4IP3AQj1L3!`yZF)p6}"
    b"XeNpU;nRSehi_c#O{0a)?|Y!T*RrX5VNc#^_n>xy2ngl-srSD;F54wR9Rijfx9LpmtYD$DLk64Z(rqrm{59M2J}s"
    b"Oi4-22^b=+9EwFGPER}6pqU``mg~TN$jj@ip!yga}~D(88YJQ+83xkR}p=)i12c?i=Wfrcbc9XdU+fx15KLENI1e"
    b"}1Z`(1a(YgT<AnUSFE4kI^)X(_2(BR9NzBiT^eQtxit<Z9!57V9V*H%9+Et>%9W9zAX1>L-s#|^^l>#s`a2}m3U1"
    b"K_aGg2M3iU_+UgJovs5r74z1NDwRhl;VkM)?zMr2(@tlufi&2X~U97hyqVdT2SH&R8wsqdlV|=3QMkA~pD`@Yi;0"
    b"t@MuGUAezh&;d{VCUjWlc18*m@ce;c+bKNzDtpHKIrkq!c6TC3*<@DHvA-Z<WT`y<?>yuJpG)B_F%DT>F5c4hPTz"
    b"SEW>riNfzRsHxX0CRWO8l`DERA3WrJ+?qNq#1dILlW#EK}7%X~+UMOX;yA4Z_;SDQL7vj^W>@oT|N9NOx!yRF$C@"
    b"+27bNGg;j&u&h0T8f+6-up!hZriMwcFWg8rY~_;*z&!8p#rLjY_4t1VWe4yM{qFWDNY-5qGdE3tYXQ!N)BZM8u_D"
    b"#m|@|jZDxT>9Wc>%<shZc7O7KZ#!H_0$EFg>*LaFfDCLvo*?+y=`-c;bS5c5RuWsId(Q$~-Imwt0z)jQVJe9`I_<"
    b"{w;yUi&G3#34uKDhxRXf^u>q;_-NI$zHt{Qap+O6^hL+sJg^IZ-d|w!+m{W2iC&3qKZuGyO#honLh4YdroF6f}ww"
    b"P9cWDjZRH#<r)u!c><7P_wF_59^$EY7J;pZj*5d*g-kT*0<e2;2eKB1`C1zE=F=otS~BkV7$6b&*tP6-_mS@;T{a"
    b"~%z}v56+>Casjj*t?&e)z;S#e{oLe>d<6N9olv7;o5RANo`@)SO)UbSU`1{HW>^nEGGJ62a_G|R;DxI#0TQ$G2b5"
    b"+_F5P_cKQyyG2nHCVoUVg&Lmz>aWAzit`SEB@P+mm?}BxUYK^&+SkJ;z9*)FeZ^5C5;7vs!)9!DFNK-s=+AkVYFN"
    b"MMV|f*WM847u@=eK4-X1tvp4YNRMM^zju1@N4a##!eI7fS==9tN0MmYR;(gVmtFUPd8<-sTYV#EQyG}>K^wOq4HN"
    b"W9SBJncs#)AdMVZWf{D~m%<5H<Civ>(;ROS82I_p`hgTkp*%KvZ8`{1!06^q+n?l{V{5fWcdu9-ipc!|h|0Tf@!&"
    b"19C>o>B|0uxO}gC(U1wV_!NTrSnFWDQAw9H$BEybx~E@JNo_x;hqZYbLN?BxpejgruAZqtw^Cd!UDcj=cWf7g1&A"
    b"m0TFSzdyYvF?HP`Q`l`5wzN8chDpHC#>-CHnkl%-7m7nIcKkY@`c`eyl1zg9_h&9#|+CyFx0aDTMq#)9og@U@&cW"
    b"hl(JuYeJ{qtW^fqN!7;E&76u=G_x#qOflJ2V~q!jBmeMX-K%cP3)!(Lh|Y*3QUs|pgE9h#))nSc9+_23vo70{5!m"
    b"^bm#d)p22m=4Ai2X<6qUGi_OctEHjDoE~R>;qU?5K^}{4zMcA9K|A_|-??L-u2_IaeDmBBG_nka+yE&rPJ_%ufN+"
    b"7;2oS7-A"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
