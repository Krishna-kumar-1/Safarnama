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
    b"ZGbKVjI4SY|BC(2r6i?%&K9t<_k?bS{E_=LQ;VJn%NyG*tId@$2JQx|CC7KBT!{LY7Bvb+d9w&CI2t+SJZ*nFsVW"
    b"P+N-F^dogaULXp)c9XxtI<%1ee=0D=&}4k8iXQ8V?!LuTIlFJunf0>Gh1#`R&AVeh0$O&h-Zw<pOR+au|jJGs{h`"
    b"ZQvP#?EAfpF!YwHF6|0)~_yWi`%i#?05*mjs#1hwESq%YdSq8b}#18Y4ojm`VqijH|_qhJFAeuIjdmwD&WDxkMfo"
    b"}MgvS~SF+Uk%ng_7Emp(HY^qxQ2$+wL^0jhi^);H8lhqJpZVc({u<|L}PWzzb^-%k#<9U2{Wgqc^Jw4^USzEMj<Y"
    b"S&Wqv1N<?`0<LTwB<JJnPFoGu0pNR`DzSpSAJtJM!t$6E*A2dp>-`e{4<prfgYDlF<UUNT-bvw%jP%^b=itbBs;V"
    b"Pl>NFgU|0N&bvsbomcx@mIFKD`~1C+Ea<fFTuIAiBjAivISkOoMOvOd5nQ&wepR^ZtginQvk>E9ouRXzxFT$v)V<"
    b"l&QI6nD;*R+|?5+3>R7HqTr0>48qVIs9vCe#<04j)&{V2wnW|ICsBWo^L=ZN{!ha@#XJPfXm@~Rru9I5j(P$MyG`"
    b"A*Z!OwY{v-~~(C<>v$6-4Ytk`Vz+aei)i$P9^~kg4MBT(NkHao~=RyB5%6d3F<WB=b8Lk0*$V1yh@n_5OwxZu{z)"
    b"y=RU&-d+}~tiQKN7%v40n6)RypodwiG12B>CVdN;!eJH5yYM#ctPQ)8muaQ*z+9DC;gIa|B<wlSJ8LTurCuUi-9>"
    b"LIkU&`ir`#=Mj4SKkTt_y_5eXI?r<O$JeU&ra0Bi|)Q0*0UKYf@AT-ay<ExD8%Mu$ypc)Qz6Kt@dfrq?oy50vv?L"
    b"<tunhzC51emYlLN2v2UheYcM98Ew#3NEUdBl4Fvc(2rN1xRCAUQ37&eDB2l0;ViO*?Sc)>B0I;QzYkNWHuP*YH=K"
    b"@(;=48Qlgo+GNK)C$2fWSkMu{d#*n@UMe~VYWg=M~O;0+=b*1PB6O~bXvf6>yjQU}6FI>WDF(3x7!eRyW(L5@Vro"
    b"R|18490$q;<EFf&$f7y)MYrQU`~p{BweuW_%&I%HSsRKl&p=;^QTjr;};KukzS85gyf1KLnGJA9vg|+{qpnK;$q="
    b"Leu)D0q!)Oc(DBGQz~KVHaD{8z#!Tyf+WYZDuk;+z#?>;$9ijhTzeHL7-u=kn*jN;?g2e`t;%V&B=Hqh?3%@7`FE"
    b"hf^NlYUlA&aRH!l0LrMJs8C^c=+hb3MUR5<mm~go{$zvmnIl;u9ikfFD3q?8_-X136F#Ep6$>>qmw-gpsyF(EU+B"
    b"LEM)zIXQB(2R50&u0u)!zxqF#?n-KZcm^T?)-~Bveum98QQ%`3FAG)T9A=LB1VWZ^PFZw|G*HZbWU_B?e=o#eoK8"
    b"ARUcg$CsJ!{U8<K^o(UMN%3NvC@T2(weiix9zEyR0qG>!OUXh6MnSvt>_atEA^&uQ~dE+2hRAok5HxeCDtU^Y7Ay"
    b"2VsEuag2WLYX<>uhsmu*J;-Lxe3?q_<uAZ1S;irP0rBTo7;@Ch&Qw?zk#7*%A%YCFt;W9+ey&Uxyok~6N2Y|BK!F"
    b"cJvHC~h+Fb83T9WC(4S8-Q5yb_6LFWc&dGq8e3}W@C4@eIZq5``M5239C1pV@(f8WdF6`iA<W+maFl@js3VjChz;"
    b"Dyj<Rf1R*uCqV23Wsfz^;)Kw|_~GxypsG_DYjwBN#SzNQRW?&&!#<?H(($?jlrFQN5X}N-b9;ACQkCn&PqE>l0L~"
    b"jYMYrK_rWw>~b6rP{!GCngV|s=nT>8P8n+sDQ(|XTBi<>x(1{u-uU$;7yQ>0R+*BFXlog_1~C@QMzfcfaeX2o6Rl"
    b")(U7XjX6xHN<_ssmaSn_yopl~^AkrBgUHefLL3J?-|Q#a3j;YwnLfcy$>NrsmmH%04}B1xoTi!|A{g1e;YC3cC68"
    b"M-1ivNJz}dcTYoT=u<Qx?U3L8h(E1zcQYgB|b}JI&wACf9vuisD<Ofw(nH!S}mC3h{v-9Br%Fjd8#cw>4tzfBKF@"
    b"f1r9&)^QUt;KaP6-4rs@j1ksu3cQy{8KOhBZ4}fP3$o`d%(=#2Y{aTIpyBaBk7V3t-zNG#YsWV6@9;kF6PYQkj(b"
    b"zska&^!Z4<9tF#p~!*iar<7Q4p>2?(#j`6f=ARTtvR6bL@SQys_DleC^^kqG(r#`ZK!m$Fv=eD*o4qmzBU0U%9wD"
    b"O)3L9a~1!A3-V9Z&m1YHn#RyZJN&@j>_{ZW4>1(xBPFN57N}6RyNU8{&SnxMla>QpMDntvNaK)Mq0E53iH=zie<T"
    b"{?4b}CuZve%Yjd}WGGCzae)}H$?Nz-S1xhO;%h#?MPiK0buUF`7vmfrc4{qlD1ZYrPIB_<l)MsMpi&*4)vOzz*Ct"
    b"O+e;`2@cy$uPo+@$(Na3@}QiI`sF&3=$Jn3Y!)n*}IO}_WAE^9kx)9K8f!%WNwx7QXHjM)Ld?%ZmA<owN>hlzR*f"
    b"ANt505ns+fk-;2WVgPq5z^(02HXt*0X6f_H~NQ-G{e1wc-aKB7_j~0ddvPO`;?^;)W^_d(RrUf9uH;0HQ>&}Vr5c"
    b"|SQg#Dq)FENc49h}qdC6qQ)-&>HYVkAf`fDgK@XW@h3ecWbQ)|)@A_(9nX-XIKW1B#&mkPcT(Fzm<5hPiK*=nx04"
    b"vaO8AkHCiyUIl<4OZCKA58PrMEkgwtBbHu5>#XhmC;CUx18%0luZRe9%$|N0OC!7H-&@N8s@n>UN|qDf*E}_#L=J"
    b"06we%iy=?l1fQ}6ayt^`M=zw1g}2ReOL73KH-xrx>Gtbd&FIs}nzygMQF6s<Xu8_TTC^V>W4B*IjKV#QJ~DTL$L4"
    b"s$6~GSYA%)+bX&X1LF_;rEb1;>2+wX5VTSz?Q}sVY54V>5UpvH!2f_N|uQwPNV(S)rZSQ7rs*1P90zzz%!EMNeS4"
    b"2Cp5{h`u&4a7i_n1i4FI5nNAX(jW^xB4eaL~-W>~o2trBvH=37l2qV@kSimp^b9}JE*QR5wBLjD6`KqYqjdQdR4#"
    b";mZ#PH<7_*L&Eo?V;O3dXCZ_%S*&FJt!#4gUT&XGg+_IvD~eyT~KZYxJov2}hwt+?nU^sSj~@%8+s9#qP8(!C%W0"
    b"fCuE>o$>Z#(*yDeVoj%l4_m<Qd>Xi;<s|s=lQ883%^0sb<N;izvmWyg!qEUQ6<W@S9~@f!h9id7`BiEk75=~w@>K"
    b"*-H$oI{{1xN^JR`KfaIMJDHR3<ACr-Bcsi|!<xRv>Z3fT3pHA7AV_er-HIB`d40i03p`VcL+RhNmd`BG3`9cd-Nj"
    b"+%2o9Lwyj5^`4gZf_~$A}roM0@%R<6B1BpNpr-hp3c(Js_qae47i;n"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
