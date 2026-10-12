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
    b")O_JQDS0XpH!7@c)1$Y?j~KsF^d7KpD3;MrSD~W1d+!}A$PX}+IJ}IWbM5b4uP*F9I}@!Gc{y<FC~9(RbTSmR*lt"
    b"=sKA46l2o-KzxMO_`EG$xHlqRccrdRCsHJS^d`)$wvM%Z($cO9uR;ZBhEfpAQ<VT=>+!D6TC?^ggY6$~t4*LR#%7"
    b"_kmASX!+lz-$>u`RBuxeF;Mm?2t&vR%k;19s+UhJ{_0D>+7jC*b39ZrmFQdO@|@-LfBjJ&=9p%sM;3nTiXj&e;Ex"
    b"!I`MuNF`y#cIQIAzw@*2fieEEe?0vVU1bLqtvXV$oA&wPa&QdS<(_@lQ5lGi}N@TbBJ|TCzAH`)tQii@3V1268&f"
    b"W)I<=B;$qU%pzOptWvAf$)3ARjDB&a|C48v=c%j!ukghI#i=3^#XC(~1#a5{97L77oXJ-E`ohbxz4pTv_HPihP=w"
    b"aW`>j{#%!D1;Ib1=q9zoXRcQG%gMiEm=VHHCM?0Z>)$>Q@_ZBX%BGj`Bd=y{+Y#d(4%eURHwp~RGWWx!8~dEv(<M"
    b"HfsTAfG^7ylPTG08Nm;Y%@=`yg^ZQ_$}pYmcl!wHb@-GVP_{`lR78*<SNjH!RFP)hRY1HLz-oOl9%1*FiAToTdJg"
    b"#mkT`F>D4$A@dM?RHDqK0;g;`q@r;+Jxc0kzrPNfIddGKx#ERcN#KH#Y>zUm02yyCh$<Zx@d$CfPSo({_AS^)9US"
    b"z4?X`%W*W;Xnxs3wL}S2!khW0A;ZE*Ynn9;!34S>ll9;xS=<g)C7%A5=W=TQ2U_V?nvog;AK%dIPxTtx2AqNhs=Q"
    b"i=4M4>R(p|Wx})RYYE1pLNyflWTcCz;4IhGQ`Izm|6eo}Pv=JN`;ERLz{^vD&bOCZ@6J=N(Qzlz?5*>mKGF`_;SD"
    b"Cuwy3?PV!JzfXrmw9RX+@stHa=?Q5VW==WS^H_pRzwf%pOgfwa@B4<qByK9-CV8t1qe-IlCQwwpvZ!$d6(gp6p?S"
    b"FfNF_&WEVrtY^<WB?K*QVjF9mFcW-qkVRfZCNQ}KX$ht((UQ|OGmc2FZ#Gt~=1kEJ*N@Z^E*hO4Uulo-56hKtn`f"
    b"KqA`>Kw9I!1zT;fB7_U<bc`_k%GDVjoe@JroF^(E(*_UH}|0^yQXGa*eRopsG5SaoCi|WlN~LoA-)u{c?sy}HA(0"
    b"_2;=tCD4i#>>nipzqJH!<mGWv7s!%fHM|n=e=)KXd9|vE7yG!*s^^lHWW{kW=_<*saTJ~3uz_7s7p&n9v+i_OKYN"
    b"*jw5O%nAt4>J4it%k>2@mdG1ePb6sC8g#=HNf?FU@I|ort-70}|j~XLoKPw91=>Kat<E%GaICEQLE5ZtnhY=%HU("
    b"l1~YHZD-l-xsO{9E2w}Sf=d;hGrfTPqCz6}6w3`rD(OJJ_$`)u$`aNnU|cV}YQ3F8`t)?+Ur?kGfbD}!nHxXRc-i"
    b"|A%a4pxjswiDB|k~I83W5_L^xHILpd;^0B<6-U!23f^4rmc4Ihh}K+6e!Uid$gu`;ig*O477(AF<t;Bd79v+{wE8"
    b"dxKLHOoxim)w&V%Ca~G1Kq8s`K+CQHy)^l2r>N8y2CCEH952pE<z(NL=lN7*FAo9rvW{Q=cY%RC<LLr_!vcSK~V#"
    b"ViS4dSv{gdQuj4%j;Q-A5{xMmgYNSOk0|B=t>V2yn-v5x&YKBU4T>Syc7y8%_e|&s1k09xGwkGhgj}GoTcJ^kTIA"
    b"@puoV??glIj-7wg-SM|4y$-m4uct_O6<mM^$+hu{ucoBHV39t>QNW=hFBPP>f?*e;%o4*mu1G`LxEApTMNIpa5-@"
    b"ZVbgR?2iBe+2RG`aw7b&%}D?ZW{y6ixE>EadOJgW;c8)q;DqiA*~xLH)ALY*X)>GD{jB&hw|`@!NzYlT_aM|Q9W^"
    b"$68@-*g3%bpjL41OBa6TZ2!Pd*2S-%1+hU{&}8-?@T%}U{uQ0KsaLVA@qYgdR#IwWpS!e$FXV%GBN({q}Cizu{g8"
    b"HvrN!L>J8=@x!rsp*q@yf<ILEOdb@WV9iUce|dXwX-|`xr~bQIR1*gRL>O#K##Q~0vJ<>FIF5Uo|rT82`PF-<n3="
    b"`EQ^D7vMy7SGhAR@8+(!oPsx#lf$6lp(p?f8Mm@i}!R&K~+Crku`6H6i$MvnYF+v<Gxcg5XFbFpIIiOV482)GOA#"
    b")R%ayb6{FBnIdWdtIy#op5Nr9{wRQ&(U9qj8kkiIKX#=3a7fQ>D*X;tcB{p!=LO97)`M>@3421t|xoteZqem8*9s"
    b"r8wT_cK#PeZ;Rslv}|mf##^|I3CQc=IyLcyjWNL<S9>3V0w%j+59S*b5|4$zK$%cZK2os%^xcWSEqhV)w4#MXw7T"
    b"!`K<ECIua>CU|0VV4BM<6VmDCKbcPsj5FDe&(uR6c!O#>-ZHCn0I-Op#R;oFuc<cQ&*CdoZLUcF^R^O(juu~kWlI"
    b"b7i*E(@i%Px@wJQc!ROdQ2K*tX3jY0h2PPgA-h<;))KGzbQH<Yx=XY3&Fg;;l`cH61*DO4mj?z4B(IBR=Jvgy_|6"
    b"TNLIbLWj2{;mUEwS$J=K1^gdfqcn=`3#Vpk+llZzi-LJklV@c!PLsaFQZl-;+<SzvBzY+DG4O+fxhCvm=a$lXPJ-"
    b"#S(zful~aI;Vbr;`R+Z#14a#CuDU+08R;%XiOsxF~gmI<+OWxBTdr+_AE+@wa-K6I6lz45`x{#0FrzDYlDaj_zID"
    b"C0ONrBD|RHDEnG#{OdFj&;4PH9u<h85B4;uBIT#W0~3ju88adbd+Ki`*fyb15D87=-clv#&`#R6Cyh#__K?L=IPW"
    b"r;oHly$x1u2<X6&seh%hnoGh|Y!VLl8Gak(e2>Y<X=3z(8W#gjURBOQVqYP<rjvH&U-73I%g&-gi9+<WV0S2zSQ7"
    b"zJmIE)RDGvCeKlx1xl&B6G4((3V8C$@^~U6{^gH^C~0oS_}lt*PebSE9TQjEcK~PDMM7Qh0TY~00Hmf1)SFM(T=t"
    b"~h~eg%KVSjvCWBD5J}dZtG(YRQW5;WWJ^s+L;*Oof9>}u`1CjnuxGkS%5=hc94<du48OnD$hdEwWcXWL<G=V;g@j"
    b"0@?9o0#hwC7V!`94j$6JOD0yD@A?$^"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
