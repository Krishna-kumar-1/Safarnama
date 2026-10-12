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
    b"8y4|!P|=atqPJOnKJQ!zC??ZfxZ7EK5R7)(7oxhA{?tp*ivASCZE`(42%QlY=TmJGobpAL{?Jj;#(5*PZ>@j<^9G"
    b"GE$E*e9Z2LS7%zsA)MM%+e(M`B*ZtFMq>L(Gak_oNHClANM;Rnfdh~QGOY%X_HUI^Yt?-lvJeP0NP=HpQ2rb_Jc3"
    b"=7%LOvGdOMA_@k{Z@n+>-LW=^0$yr6;%#egbo788yum@Hp5kvh)?WtXq(f;2^xPx_kHpGdS1SYGMYvq66%39wof?"
    b"e0Y@FF2UU8?u9U4puJNN_V1Zce8eg&EC72wn*Ndq$TIE$;1vM>0YZ@p!@S(>FL@}qC_&G;5d(d)CiK}{__bNpuG>"
    b";tW<YW^mvk%l*5_%!Ej3(EKqyM?|!Ms`<sguIz3G>bQ3PP1$iiGTCu$g@#bZ2)7@^SwoX&6eXvLDTr=N{jt(%9^I"
    b"h-~MkTj~2XC|dAmrAV}-6I^(AL{4d;4?+97Q{rg5JFBzGa#Pw7^%IxUH6=L6cMaVCC`JGp1z4*oRiZf?t1euoMH-"
    b"?ZiOaU^LDdOm1`8~}EGAbT98MSxS19m)J)m~1%!7O@&AA|10S;`k{g!dU)#VUa(9sq4{W^9c+P5K}CjwzmjR(_u9"
    b"`#9?aKTs$a1F5T$PH8#J-m~F3QEFI<-Pa^D)QKo$x(GZb{Ee}9SLetpeL%V*_hBzV(O#5%1t(}Gs-tiX!bufAElD"
    b"-(sr>uelN@pKp3A}umdmQ&N8u-Y|hXjY_czhtaFp}UcoJopn_7sfuyH(3$!gh3G$OW7r@$?nZ)fa&UP<sv$j!xk<"
    b"64r9kt^39;r!jpruw13x-{dIy@pfGb`|7i*3US3IRmkBq*@jeD0Eq;FJ<aR?avmf!v?i-wF)^9n2Ql>O6+1eQ`Ua"
    b"H%Fj#RvkXzuc6X$^)q*#fr(A>=TqnOk-JZMP%um!<~pr{i}Gyk#ZouRnwH_aLx1KM+#?0zhnPv8+uJLq!m-|%vNB"
    b"`F6~k;rhaqBJ`$lVroo%mw;nP8all_Uix>H3mjiS8G&)-XqDzlxFO$&Z?*+}TY9<X{V(Q0~N0hJfe!g6Q3dFzP2_"
    b"uu>JkJss(3ob6zU8Dgd5S{o}KyI{s8Y82GR>x0&{<8UAtXTJFCyxl=BK}+v*`pc#`ZV`0%j!8LnswQLN<4Q^+XGB"
    b"f`q*LxB~3Gc_;+;j)z5qD>eMz4bPs5BvgfFOzG`v3a&37=WJLy==Wmy=b~`$CPTsUKF(Rphr(o~-W+fKHK%v_N@o"
    b"KNQVJDp{BTamUl87~|VvNW~n*1Xmm8Otjt*&Dqg=ZLSG$oj1G!ovwX}OT5X8&zV+=6PzIyo$nT{o=O<>fvBbsbss"
    b"1w_}9*HuXJT#91X9)+~fh|5c~^g@P)GYrpM%93ZQ|EXAq4HghS<vAw>xh{}V4p=xP8(qfYS+}QXH=%Td94cHsxdy"
    b"J=VZ?VOs@b-<B;>B1(LbSQ&N!LN@Pft)1TqU#EhNl80`-PfVR9<btICUn#0OnIod!;qK1!K)mqI;`M0|dkll;1=j"
    b"v=5+ozDvI68nkD-Pt#<B*aw9Ed_J!<=59>0M4rUbPx^0K2-!KOWn*Ul;0Tmo@5a#gq399)`8;IbanV;cmiid2i^w"
    b"oa<iric8ME8LLzn`Z{6`oypQ91{aMwyp7f%YwuIpV4ASn!l%NH3Xep~%<y0|=k!-iM;KhKh6S|n0paVv1+2wjGU`"
    b"ntn^*cn4w3GRZ8x!U@ned|{jl~m@Dfx6j`O6@UYdti&y4lV~!Bq&nAQ+SF)yQ0ciR{Ou$cm6VM$7@DL1_CB5K5C^"
    b"<i8alS3XK8PJw{N%pyb&>@#bObDE9p@MXa@gi+6+Ab4ya#liX#H45F}jH1#s3t247;FM0iV07BU4t;=L@0%wn#f7"
    b"jL5J0Do8|@nl1b6X4C(cZg*z>xk4S!+UC0yG(CHVZ&^syi)xv}G#k^jM0yxV_KI^?xLfs<5e8=tc~`L*lkqZ-CJg"
    b"rNw%)p$4GID^c?Sz4ytmCPy%hg7d$mo1=cM!PIc;7J3e^rCI+=tB#@MG<9p-?4C0bb(%{MOg%)wNnpSA9W;FSCSr"
    b"rZ@W=jIaedJ<&hD`taSl?A=+`z@@QIpECc%r%sD1l_K#%?!G+37q+_d)=mPf$Gd#ODx4c14?YL{$&$Z2Ow;3_F?^"
    b"rEMoVm40Q^6IekHkPGEGoN0F_^3Zn2ew4rE(HSMWClg>Q}2EESnq4th*1onLc|$R#5uc^J=#liG`rjurmwiPVD8O"
    b"ZDM=mbu-m9!_EE{E6d3g|FHIU0UgpurTVGl^!%@MyeFo>wh>EmwKC4CC%vN@P8dj;+uqOZ0GCB+^b$HIQ2p7jE9@"
    b"(3B#9C<N0~c8q6RQA#gv311;!4~m(GUuxBo&-p<V>FLia}!TU$UaEwDn_!ci#h@^vr}5Mw`GkL^KasG&luUU_I-f"
    b"w4OAbo-8`-*H9SD?gfIU@Fd9#KwxwDqhtaAyF&GP%N2udRWAT`(oCA=EZi354ArNWPo=a!k@(f0BcrdML(4ECO%f"
    b">fu;|e%*s}jzg?Kpvh@fT1xxpJxc}TC5Ir-fUtt3wg_q~Ut~y`z{=wUq#UNIbauFn!(mQD>2@J!qDABKyDwX`N?+"
    b"h3>*ql|CiuuHklYb4LY8HEMYyE}oK3jbj`0k>%LPXQS$$H7Q)UR3u&htKfV|O`D#8>z_HDZpe3G4yZ#_PoyV@A%c"
    b"R?)t6oj=X#)C>q{K@_jcz*#xMB4ta;(lT{!7AoRcJDFO0GBC)y!W(~ZoX@%%b~xowgBrQTu}4ix;wm-TjoR7?G4K"
    b"kSW-6f)O<jO{cqr-qSk<P#d%KsM(bB$BVI~RgIfwjd6YYqJXzn(exmTdojW%qm$!8W+zkZp0Vx#xn{Q%n_S04I~{"
    b"J;w4;^v^?#K~OL5~71k*e$K0D{dfW@u_=WRS16fkV;_!zX2T;H20fvaLr7%52QI~!RKAF-@E>aj_^>fyo6oxxi}b"
    b"rM4E;yB3+V-LJ3cBc7D>$_Lf@1IjtL=@B~ffp+w7r5bXy)Pg{qyu8JVa55#MM>lLNNUPd;>3!Wy^j=xYWuT_%s98"
    b"u^G{(8?!&;M7)Xgq?xT*+~-EIS)CQ?lE|uR+oIi+2Y=SyYM%9*P6?wPj-rIhIgcpCB+F{rZF24PAONtAxvUR}3Qf"
    b"tbDa=F^D6B+NHc2-<H$pnK5lrd2=Sv2pX6>T-DZQ->DmaEMXX(vNQ!H5uy%o^<X=(d1N6W&z}Zwsd?2>H)+xlw?M"
    b"fPkYV8-w*WuJmQT()Mfckm;~vj}{!fXci4ug)@<MDc_#C|b3L8(vhqSY6(GV(6HTU^Ys|}vZG-TS@!qh{4SKI@GK"
    b"C44+4aTX+Ch~q~037mZeH&J(X;{E}pvo@_n!zM1T+o8*g~$PnS;@{a3-acU8j;I9J+JuC(m98DLy@4%Zgbr59Ho#"
    b"<z#;Q$e*quBKxXh&h@hq>x=lux1VtlyJ3tFGFb9m@E)TY_zRV%1zs{+0I=?$&pg2$x_UOjEkl330Of@pRP{AzXl^"
    b"TlXg{&V;@E*HAKl$YZnPSlwTxMc{-kBL-(8BpQ6S#@d<G<bh@M$ufEEd$y?g0m_ahrVwqhhi|KXepRkIldfm`}fR"
    b"0K<O7<wJLY*s7~&>qz3)d-R9Zulp0PYKKm=H0aJg!k{)A?znL%jgkogd*RoWRa{q3DkvNXoNEFml4AZWRKF-8L7d"
    b"uM*VRf78oQ8|ah62JiYbhkk&;QtSpaKFTT2fUOnX+&t|Xo~?WY*%y*;5$!a4{;L+;lGWxSteU#czPl--D$+-o}vl"
    b"044!w3?q$af_rZv6Iis)?=#i`iJ7^3-YCd<(PQXU=Vh^R}DM&6VNGNFXu${JE>`3)02+V3_W@8f4@-}GUx(aI1FG"
    b"o<?vocDeEF=iyH6V8JylQ_Pkzj7w;ck!-u2hDqQsK{+BliOGKzpgf9htq$p`kyqrc{<$uY3@BHWpFcEqeMtZ9@+n"
    b"#YurH1|JpzKBP8?aZsye+7ckI8w-EbNbm8^FWud{9LP7wyPIG}C{#N4u|>KbkZoC$o-~T|8SZ088@_w(Aaf3^bzK"
    b"lDfH>&X(2ZE_^L3YGJk~7z&>gD!gV$LYnChSQ~F-WxER;O(+19cB8IJ!Zwpzx-@-==B1lA?ehpqvQ2x80H1lWR{m"
    b"p6qiuoC7<nUz*U2@XO-{^^QD<%*NeAJA5$WPBdmV9=aaq+T)Jm1#j0{tFMsYBDoh_UY?+cRjz5bk>Wg5XPwVh^t_"
    b"$$?r8hvsU#y^lmcUv&Xtk^!jB5X;RS8N66>=eb`syPL6FoTMgvLh}hz;a<bgNn}uxa}*h_}L7(pWPTWE7T)>NU7f"
    b"Kr0e=I*!}UM=o(edJn!lsKq~&(E`1<JK4Q#&6{HAUb~T$}S}@A<u<*Odd-dm8i$Q3+kLM~*>ozbjG34az<w<*fz<"
    b"u8_xoj={YSH&+FW#rm3akM%lp48SY=Us)ll)?|_G-pGSW^UfU;"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
