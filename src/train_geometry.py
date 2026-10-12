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
    b"^qzr8!NB&ngUz5{9ot;ExlEM$roe%R(3_nF9O<+N06v|~#!$2*AyUa7*FU5TT;nOIT@Dq;i#VdEfzb)ahpOOOh?1"
    b"j+F!te~V!Jz!^uSUSp@5;SzU{$IG_Sp&?ya9}YbPEZXlhPZBSi-97HR=|s{zr_@Xp>*5m2Y4B1TZc3fgLl=$iSF_"
    b"uWt=i1)r~<U6<;UX3rKdF}|Bqag8k!m#?ZbHSR+S{p?%?l8lWMn(}~dw@4mk4T`Y5>ko|iX<;R{C_j#o_XveU|+>"
    b"KUi~&(Ig;9ZcY0|4`Z;G18FPbCGr}TNjZ<HS_uiO-joKk|1_AVe?O`&awRm%l8v20TnQHgK2}<k_mQB{QH~x67`c"
    b"HBb=k7of|IiIG4vx?;Lc~Cjzw_~E7xZz||E3}m*jj7xSTjui7jCHu+2Y*)Pc`G=mcfx;nf<im$c&zhuaPz|;KjvF"
    b"Q0ix$h3Lxl7|>ZW^ss`PqvvQDYPfOk?P>%56h~ULlc4mJ9=MJBDxmeuNC?$?WpVXkRI6bv;zkz=0_5#4hPw}7zUs"
    b")*9D1Qgwb9y1j&a8(7E0|x^O=%FCWZ1H)>~A@%-~CwPKua3F>Ma?_nr5DCTKE{7<-V|wIG4DW@%1hV*UvSQO01la"
    b"$=%mg^S5cC}<)o6=4FyAk&x!=l?6kRC8pHM~<jOK3vv>vl<Tj*+{;e`4V}I@wyJb7<VK5R&OV}^5=3Zkhn{fhVU;"
    b"Suap#z$}|=Ks>zAkLyFOeyCiBHhL$?l8|)7sg)&IOA)U^T{yNVICvB)9w{5}KmG(omTtC(y6ZF-h-7f!W;q_|=hT"
    b"}SbR-EDZKS50{K8}9pG|}?uBCWlbp%?)FBLwuRUv9$+@}FdIq247_^iaUL&~=!-)K%5M&6mTt`$^nSj`VxPk>Ovz"
    b"A%uk2Q>gsPRYWnT$N7Rx)jW;!OQEtsJn(jiSxB$OU;M(@j7a-l<qtom*-x(ty>JsW<Aq1HR^{<%WT@!=E7fTJju%"
    b"rx&Y$7T%{g0t4lsCcOaTSYn<xscQ1zYK5A+_|qHj@Fx#8Ad8mJiC%$T#k9S`oytQt-IiqKHC2ERzybZ5xl%>_ae("
    b"7;P2Q)tvsI`bnbdtDWd!ljVcr^^%tiXKA@BYzDhECz&8O{4hELo>>+uJ6eHnblO6K((^Z4CWyOubu-xFUlrAPi2;"
    b"c`a%~uvcn!f+DoJIcHwMkp$X89eygZD+}fB@<&jhX{`f*M+Rk-BzS$ZqYAjK;<6Q^Mo<EmX*m8R!27Db;xx8aK7%"
    b"&^Ba<_(4x;=m}{M&UYZpy`7u3LaFXs*^qScb|I_@~d5XtFyk`6pAPNwZ7kc%s5E=ur&fJTaL1_n@CWahPkrr>~v9"
    b"b5!Gk)#9ZD^S_5*Y-350pooA9*e;hN6sg^KZD!l$JQ^70LrGtSoR&K+=)?XH5`nff$50PAs~oM42dC^DAPvyyHIN"
    b"y(ek}VAwM}P$f*>=7OMTjiI-A-Cw~=ugl&-~tOBxG9J7xn<ME^&T27bv9gM03r1Z8+_Y-hqb$JyTi(mv3o3RGLlR"
    b"0h?~CY9lMM{c?KfzUueaOK+oYE)-A8|70Zd1*y38s(?Oyn2-O+)?JsWQg-DfZrnpk4(nejzZKEX-`<-Nf}6I=c_L"
    b"%wA^WK>n7hihsao<l3>upC5OEJH0FvR)fuyYmPf3_cBNzb38Ex=1;mDcK~8;K3T@Oz@J-j-9W37-p5IojL(Du^$n"
    b";kc2Efjv1v-RE)pl`eAME!gum3_EPBP&U=CP}9x98JJaW`(C#@Y=aXo=5>6U1T%4+?MMv}DSDM<F$7qMn*Wf^Loa"
    b"!tneR;Adgdl}6!M(zIwZRO_Z`^?dYF@Q!}uJ559L&XVQQ=R9PO3r!Oh*nlgvrGEKSXuYjSeI4`b1@BNKU$c?|{_*"
    b"gKLFlOnj@DG4z{(u`CVt#s{Hh$(IvN&#`=;NwiT{yKZA8b~vW9-s$8}VbRjXrh5)#?@w(Qn!d3)(eqVpJUkI5?4*"
    b"N_C;q(^o%!B_;6jv^MDY3AaaNh)aR#cpz|>~8rx2z%4HuwmlwM_A{N>`z-@)R-__f<8NyvQnw)>^W5m1|7V~myVR"
    b"N8Sb_GQ9{vwKqHA4UKgo?Wdi#YwflLesP3Dv{Su#3L6LAkSAH@25YXd=lG?6vP9KV+ZpN)CGc78j`T~a&MYjT2)u"
    b"viP6oyDV%l{@H@!$O-k;(g=aVb#<aNd%1)f;4qarVY;nP&Pv>WuFr(c_0%dOjQnVB`I0R~$%KuU0|)IG)HbEPuEa"
    b"OY)u;`MfTiuzF3m1d|VZ7lYRMx}h;njZCZbvTsMvDm7vq;@3G!{?X-8UBzj9g1zgVP{qmIs8Bc4AQg?I{r~7n)Np"
    b"9%)1X$>9l95f2V~_+f%KBV;1(J!L-^gcLm{GQrc0o!e-lTR(9s_maGoX)9GsQ-4;@gR!K+}0S)Sj?gHv?lXriE2T"
    b"PoHxYnV{tK)&2Huzy1v+HRe0^SFX1OEQ$H8dilvdcUkv&JilKP!nKxR~uI#xnGfhZKv=Kkxrb?`#M_7_>NY_2)<@"
    b"b3^f(8wZsNxIB4)>(|di<u})qNf5?@ziM&8)-I&&_A|T+|DJp;ZGQu<n&g-iv+78ABw8W^hVOgMVq6Z}&EQdTTp<"
    b"<SjPL`A!^i}BF#dG76`Rhjt`r?-Am1>$TSC%Cdi(F*b85KPghn-U1)2vS;Tnirk0AO!qXV?%Gnb5Q2(Flt?+zzv2"
    b"94n1mk-;~TfC8V83)D}@cAvR(_=6!Z#_8MCRTrXw%MEAN`uwx108kwMTd6cBnIoOfN*?EYsOO4&k7^4Ncvm0$5|x"
    b"SrcPhRJX>XP_I4r%C;K_e#?d!B6ANA5y4D)K|`9w)pIJEgx!Zx9>C>5u-"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
