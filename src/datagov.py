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
    b"!;UEI)a^g=H-L>R?>}gHALGMVF(-@kXBPv3%rizOMCg{1vFuS4UPS?1Yni6cO;bqh%|3%cIA5_1$8|X_EXo~XY1>"
    b"F9nT2h|6eencP|8Lo!Y`!#e|LzxHnNxfpMYJ<@R#Ut`d;7X1Bm&eQ5AcIas`~$4ick4mf3A)yBQDn3H#r#mD;&St"
    b"6SVFQmt96qr9>M81=G-j~!jG21x8E7yiJK?J=RE*gDeqqRpi|e^(V2_Ma@HuF@ydNE3tQoJ<W^r04<gB*-S@aw5Q"
    b"h@#weHE2aj|SMFtmGZBR6xc2IB>O@bdkvnuT+aCU}do!G1cSK3xS5~Gml&7QA^wT+lNbYAl<DF@A{!~`Z;+h_Mo}"
    b"m=1(9oJ>oV)Oer9^1ayL8rhBW`jdmZ`ezrO`;I6c4nKM!Lh+4AV@3yM;%%&yHDks6OBCQmcRIDbkRQ^uCkFUs-&7"
    b"uQAPD=NKER7M0>80SR`PO5#P5$<=lIo*<FW2|u_zQaGjFu``X2=s@)Kb>uNDsD~Qj@iaL!SpdMi*GYe0TBJhj7qk"
    b"BH?2^WVZCxJtB47vJ$u@Vt9^%NWp1`A^q@T@Iq$UKVBUxce_<58(=E0W+P6+Fi>O_a?AL$_i@0Ca{qSG6m?&R>|6"
    b"N@4C%Y@uuwF<q3BVcLJ?6*#_jsi>B+M>Q*u|E~h%aNon6^kzLJ(NJ6Ac($)9(|!7P2u;5p_&}OV92&*c$bI-qa_s"
    b"z_JLd|*R|Xa)&qkeiIjltT3`C52NlGDeVeFn#i?c`E!Wjv0bSO=hoQ^ef5-`OB9POtc`l98yMsmNFc;WUYc$E@oH"
    b"KJ7jA~OS&jnoyN<M++h*<IRwb;5o^G_8RV5DL7B>^<FvkO`b;Ger(;&j~pOz&?HSqwP0sAFQ&smc!n2UFZ;H3HDG"
    b")1Y-3rPrD0Qt2g@6`*;Odi7&vz$2mb22XM<TOC^Z{+Inh!pYV5Xvz_Gb!yo(!tcf~(}oFPEB8C{`4uE)agdh2DT3"
    b"<i0&@1gBfhDkbq)S4AGXLn?j|Dlx%Ct_B&YH!82@a?3bH!;ZkWoTRL`V<VtL$i_`&BNN_0g-Ek8U}SakT)lYAB)&"
    b"*?0{q8SZg?ba&5WAj=HB?n;TBkWngjR_%LHwvBJ0)|Z#Zv;ea4GBJWMibGDNKuJecD<4k@#Cju1_DM8&TRtOJh;Z"
    b"APJHG-+7jm|Pp(R57TxN!;t~=(H$q<ua@)|z9ExB1$kpx=_ylGK7MubmWDW<8GMY?rX-`4$9fY$yD*a;+v@2>mPp"
    b"X=EZ*N-~wVhIrD+%p1B=bWW@zNqAGDGIwIwse8FU6@L7TJAh3f+0t9Fe+(4CfckH|62?WC|L=k=qqbNRs**rZhvg"
    b"u*O2^^Kfjw=Rgd2C|~D;+Xjt-^FM{FVH-s>EXh>irwcCO`KIb$b#+xAi(Ohjl~aCJOY}iEsl}S_It-W_vt>Z;Bt*"
    b"SY>8|@%5it-sm4f^7b_h*AoJJ&je~m%1WRIh4t`H{&DS%2fXg&~oIkyfudi;@W<n5>mQJ<GkW=m|8D!?#eG=CB$j"
    b"-j(a$A+O}7BXC4&b+8!NSWup>Q8qJHp<~RQ0n2R2YcH_gE<|y3h4r__%xOf_`}i5(+^TSMC!-S9$nIWO4qL%>-Jw"
    b"1`d{?VZcid~03s1n+C6MoPVtAdg1~*6IYpHen?8I5XBAP6IX>DJ65Io#?Y7LP1g`b>ZIfKoGyC+i1Xe$I5`KgQ-|"
    b"sk|3BF&?q!#EwEK3Vc*80u>XsTU47{4#!CB9)VL{%oc>8REU-vL1#w711O;_Sz9EnT$A$>d_&6_y|*OpVxh$+tbv"
    b"G@u2kIK)P!Iw&s9$YLXTwWg`6J_zE>u6gEC56W5}3CHt$X>aY>4MDP5<vF;XBcPV7H(E;ZI>d$`ipf_Ha+4c=-uS"
    b"*CB^B$jkhSRJb$5s{XI|vcF;n4J*izl(9cM_~_1v|}?}QiN$GmPCQfJH<@tP|h2;FDcviam|CP3Dw#vo@4PaYLRw"
    b">Pw7d0iWVa;x}%wsqkZMq1XqYlT&h4Z~K{6kA)?8L|P-4u=Z>Qy0&o|Cq~-b+}T&T%(G+ByjS6kv;xLQzs-rCW(p"
    b"ebZ9KonN${F4!~Mzcx4BcYKPdTLYmHM)MQMupNwcn8^srdP)R-rU_PJdt&0n|HAN{s=3R>0vls*zHf1~>CrFt0qL"
    b"y}4QAkaXuU6{mf<Q|gi%$#rRX@*Lr{hhCPh3d4p(}N+;^RO>3hnOwc8P0V4L-REFIl3E^*}EPW^TeOW_v!0e=78r"
    b"SPyT?AhZjwfm?6jl73<JAG&MOD<!J&M{*KMN7z*$y0Zm3Z4_y;{M&qI;=d`Sr*~Qowz16jXEo9~6H;yW4j4&hMSn"
    b"p2sw-=FMcyN~k-q0e;{@M_m6HB25E?~UKf!%8(en8S!s~hZ-frhagZKmp3cud;;Z=27GfjxulI;I5W?XEY_Gfn+0"
    b"ZV7Bj6&@-LH1oo6#3+0l^h(VgR{z}$8pMV*1>M!Bl(UqM8#^mtPMD*@g`_qqA%FxjI3Z{7DjEMC4uArF*bL<2vWK"
    b";&*`yf@(o4RwMSeXD~uu|v*Qm!##td`o#{S&5w^#>Z0RH%G7>CGVjIfj_QAFKyMI#ds6B+JGikXZfhr!78xxn2yS"
    b"M{Avz!q!Uv{1Elu!WEs46Bk*rbcMA?umV`Nc5b0<cMiOoQ5+;&|Mxtb5Du0u-wL`o?ql8rwgOP<QFtq}ua2+YuEx"
    b"K|?T|3$Q;RL95yj@2EqgC%V2yk5AmF*ZvK2f0V{LCxt&|Fs0m0B{ya}ygP%160q{8*Y4@_y8JLWbQ&JT=KYu{XvF"
    b"Q;x6uQ4*nrW7)PMxO)~kpY8Gp$P1NRWawLyHEtis5eh6C`adcy`@&C^j0NiWQ&WC1pC+mA&tRq)PLw*V-|Urrf13"
    b"*nz2L$BR<sZWedc!4CSu%cEWO4LMcKsvoHgMt)zVu)#Tvx1V%=#RCR-_CK?Kz5}HNNX>=zuWgo+R~#XqaK1R@ISG"
    b"mJ}=erdP1Gdv4j=&QF9|ekY|Oi@PX>G?_=6ueHe_j)p%DB;PMABCQTf-Omf90S{}(_)WSh`0#!?hf~T8qrBr3xqe"
    b"DeL()55sRTMx?GOCD{Y10$r_qR1xNWY5WHJtI@S^jZ34Ls1(2Sl#)@1`(v2ulwz9Ns`mDyqwwq8ZyQ%u9(_mA?u$"
    b")`kupyL_-}9OSB;VlEiJ$%y<hCZeDZ$bIFFxVe%<=@y;_1&mtF5HB%?Y^B{$57|g#|D46JbaP4@#VTdQWK=d;I&1"
    b"wz9wh!dDB9#j4UxXT_cCB>%55G;YV9MlWgG)WhToX%$H~lc02i9p)!3oq16)h`a)}}JdBhM0R*TdvT$iI73;Y0eD"
    b"wIYgMV(Ji=yba&Ajsi4lNyTDhQqhWc12J$A8u1zA>w)$=j<b<@)qPgl9YvwrHxTfbhe9P5w2`-F9!~7ZLB&_u4@`"
    b"$H6@E19^3AXDw|pzjo3fc|B?@}8w}hj1xwT>ZvvY;j4(0l)7|gSnKu31{7o&hiC4fO?VUpv&O<|td!zNMNoCOoq?"
    b"5)lBp{B!4APqCTIowZ2omPRJlH@8|Na0>>{#ZtbJ7?SD^|ygf=0w>$RYK4EXA`;r2irVCzAIjw66380Gqo5USsE!"
    b"A>27bzZI1P0UM74qPUnh4Yv;FAjYn&Js_buv857?Z65V`R8c_kM4Vl?6lPn$AYlF1`*7BH5bIiY0C~F96D<;UWdi"
    b"ub8D@5se{xvSh}C>*bpOf`c?({9W%Ob?c0`KwO9J(51_mpsGYmo{_06ykZgYIGqJx52WL-MvEXqI{ajC1eAPf&G0"
    b"gIp;9St16*LYzf4(0A@m|GnKMLXaf6`epZkiK<wEts8(&9@{*1q^WyQA!q6CnvZa4{ql$j2a7=<&3+IHP;07xxhf"
    b"9FLtup+P`hYmB89@vL>8Ry-r8#qqRj;w*_YD>3Wxk1l|6-6MeWwejVXf`VX7)##~4==oov(IPrWHn<!ubmPK>^bt"
    b")5j{$05p5-OkUy0RgGxEbeG92eFCh8$k1<P!OjIm3^IZ&VXxzqw+{kl@^r0Z#VK8y+rxVHalQ-vPd${UKxfI|+(|"
    b"RAR||EXD5!>J3b)Q&nuz)c2$WLc^hA|3{m~Mf*bi8{F{l2`zIHwmbx!x`sf3uPBm!y&%COvCHv;LnifqsL1QKXSk"
    b"Nmq2hpxb@IyYhS}i8G7OVge>Uzw5D)vk`(ZTT22ch3W5p2?ATlALN|kyuclMvq"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
