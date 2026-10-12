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
    b"_*^=1$qqiw+v(JVzg$dlAOP5GFxKV-30X%n5$?Db)r+pl(~nHH5K`_bJNvmWh3Bn{3Q0m`!ZNf^&kGED%IXES_^)"
    b"xPo1umgKa(dHuGVqqGCcw8m&VDq`av^C3c;@&#4=Vak0z&^MvHcg+D^R`%=`kX9v%8?$0ZlW!d>mv!t-&%yNp7ic"
    b"qb?(z32c+NpXE;rI`?I(WH31+e=j_W$Vq(H<3r%mK1S1pGYv3RzV?BS_Cji3KxIGd%mhXApVzPzWF}c!wG;`r~DU"
    b"!T$OVP3YJ!$fOoV*EBk8_J~p>ngj-^+P|5Uk`4SVsK^gMf9S0wAknBqLGC6t7@p}i%7p1upOygW7*PbH?zP{p4AD"
    b"yLebQFln1ES@(iw=c_4SyPez<xp#$AHe!CMId=ZPV7sG+4*V1Yhzs<!&^(D|U#B0DN)?Y%RV#N%t!5{H^2O#)U7#"
    b"m!SE+nRYQ?_{hfvp%Sw%4>l26d$8e70z0inJBF4(A7WSX_}hqhUfcU0D^4D-)@-*rmDs$rYaT&X=jWT#j>o}svZk"
    b"#MP#@%5Thr}!d#i5+h5Rh2$OQ8%B5bg=+;>giJl`0oxUZ9;H7|>vdE7M}n)!xWscy+EI(K5NX6Gd-2!gTan-_8@Z"
    b"8Ul#Ee9<kFxX`>^$B0kW~pk;!3!$p2zS5u&iAzY1fO1?gR1x#>sBG5Q|?KocL<@xSxXV3xY1+%xu%@_J~t3{UJ$N"
    b"izU4LUq4Xh*Onb%#LkBMGSE>!>{-<o_muEcRU1%je%LnHkQSePEgT-%ebV;;%yWL4~%-6vI3DS5B{MJo<&cUeQ|6"
    b"<>OL>ufNoV+CGuQwQyXgCepjO2JztX&!Q2AT1k+>-BJVq}h9SH{;!(Sk8rzBMnY$z;Kq7qjaQdtZRi3apSAelH~y"
    b"Mdk^t*YTpv$wP&Nh_X9if<>C-_Kdoe?(VUymN|WLEc9@m#9FA-YnFk!?A_ph_l(-}lhG}PpMWeeJ;Q(^@<^?Cfy$"
    b"rSd6BY}sk;#&`Vt8AF8q0Mbe9v6Z!Dh>7$rlmZq9nTmYZ*$N$62NaN?^{*WSAYD113A`^$sWsnz^A!BJ!UqnsGbz"
    b"3dEp{>=6PuJt|dv$Mxpgzl|Kr-T-k({2>WNWIEj55vO4WyW=)pYcYhA{6bo^6%*l5#3JO$IgCP=PAZ~Q$5WMrzz&"
    b"5{_eY3J|Z+Y`YC3Sm$2&NO3R$Ow!PS2wW02t$QRSX*9XJkJJjR@Ez@rIGPTTI5pCU{VTG3*GpF7mCf9Jk?klB77<"
    b"u5^x%{HrOjv0r6NQ>XUW}+_2Fd<gs=n?e7;EC{^2l9LZ0k_cJQP3U&az^B>{$`ejF>K-6fwV9h?=V95%$i1t>O*&"
    b"^w_5&AsD)r_sN$#b8#;d<J^2?rvl(N%%(Y@Ehf;U>0Ws!i3EMe%o*cdsB)SAh%{wu;g(&XPlN}jsAgchcyT~Jq^)"
    b"N6cQACL^|V<p9XVphyH8&C+-Nwbe)`VE91c2BF7`N+U8zd&R~F0(!|8sq-R<&iF3>eM^)EdlVTVH#{p9@K^kLyvs"
    b"qNl>?BdkLu^)E!Q{fIVwg"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
