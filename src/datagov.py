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
    b"G08zH`x4<a+3)p{aNN**<E&FS@K5yw0}7O}c4}5sh__I?=U$VIQKE}KDxQLHWRe+vmh}Eq{{O<DRBG7zOv$~}tJ="
    b"44*5!#jLUBYJECJTW1IK#p+iI8VjBAHNQ?CO8CNV1MHTi8sLNnC?_*g0vIolb($g+^F1%}Kr8yatYOZsqSTKc`hZ"
    b"GiHzuI9<iV&u&8yzJ$+HF!-6%2#sLVT=L?!qzMO8U1!w3lMa!qzRD!Fuz9{UHyi?C=_FFUP*c`%ZT-Pa+3gh4(Tw"
    b"Uun=M6kDD2v?I*Rj{{q^Uev~NbMW?-k(12Kya$m1OFnt*{F{CO@#0dvwG^oR3Hqyparw$9oHF`hl0vpDzBLaA8I-"
    b"rAmdc_JC(Cl`!^TsMj^cO@{V#(G7KkRFMexJ?WQZK(8)g@xWY}Bmt`G~lVpzfXP?itB#E@bZsXewr%P{V}x1;nhs"
    b"W8xDpF|ye&8S;1sK(10Z<0F(HA`9>dSiquQniN@RayP|T^D_EH2cUp#qc<0_RM3jTFic-W{Q=KxZB!2&7W14UVHL"
    b"z^!}U}sEZPcJi=9?XqU`$CSc0oU?GplY#GozTW+#*HO!<|+o*ufQnhFQz5AYSFPCb~K#We9fBZi(|R5jTnL5EsBQ"
    b"ZS9xV!;j4?$|hx<$y|EpRBLtZUHM>n4?jsKA&M)4MvKs>BPQ}{Onea#Cg%T#2E2hfwFP6*DzK(Pa`BsIi#c`3TQ-"
    b"_Ew9;Kk(Jk;MbIMj>62h*m|l(VXmv0M+rWP9xnlOkY(FbbWn@Y3-F#ajvsYgn)cTPrw#ol(dN^sw8CD6!Kz>ZJT9"
    b"bgJ|Mjx_F9!XL2tN)mXSjuTV*`|+4+w>Lq5L-m!2n}~8Inq`tPmx!l-8DmV~pLam@gEV0V1<Sf|!yLLG#zw=FKtY"
    b"bDve4XVxa39f{EkL;Ft&20rtJ0sD6ZVp64i@%YL`GKgc0bU%-R$1Qu=v`zJsYc3bU7+j1sZPz$^s!D}2QIEDbYlB"
    b"@J?UH&!^%;LWiAHWs-rlY)N*i@Y6QG2NX!vZ?UWq1BrB%?NFQZ<6eGYZ<38z`2KB3Hx*<a*OO+cLAnsJAL+}zrui"
    b"LL@(-qM}HtUlDR2kx!9zYee(?>i3-%YWnK_-!viLos2q#zB?-*4M+IfV1Ku+x{p{R=%=?v*H-9>EbGy2&ybY!2ed"
    b"mk0g*Veh;|V_2*g?TF!Kdlz7m^c%|*7GhlpYwM!0Yql<F`K4eXIg-4_E1P$j1@SD3M1~0XFd)J+!RyOnS_0yCq>$"
    b"h!5)uzkkd5#P|?SCh&3z*q8Fy)4X8v?gWaeP{fX(ft`g@znF>fYI3UX)Ew;|E(*;WEc%m_dr+P{V6o?2nD=JZV!2"
    b"{MDQkrP?M#$eVssY1~7k^2glpIPn15Cp#|5-xjsC#|+L>yQf_>`W2z7%{p}5>74Gi3JljL4ZLl?kP(RBf3~Kd^2T"
    b"?_MoE$MP=>skyu+%1E!xOOTBZ;348q{%gpkAP><yT`#$YC_u9-IB#Q>gJyQJrQfb{n|`}PMbDqQkuY)W$1d)$bMP"
    b"nMV8?nlt|O#s<8h@6Yg+eSv}icnXIbjxlIABq(rQ6Tl$|MHDjOA#EtTrG)UQd&W9A0P~o5@3x=5&B4<3*;NQLN|_"
    b"vv5|4cC~px7lPz#R`aTTa4D|S7Z6Ns%-;%qEXLamkrhO-!okOkWxWSX%q2&@*(j2dXLiq0YazI#-t(WfVS+oHVnN"
    b"K?oni0Ok#1#m$?n-?4nOY)=F70!mWO%<pWLCF7piKGegKb7N6B4Izf>D3QO^;R1>{=M<U?DS2&P=88iY?m(TCCi|"
    b"l%HiQ`oXzxwa7wL4z&&AN$okx|8TtA3W&L)wbM#m#n^4qFWIMHqNXTzr2dq>ie1M(><Gss{G@G-85Xt#(v-XS9Q9"
    b"FlN_7V~#^Szt3BVZ9Cbl}@l};`va?4E@(YT(mLvC+RK<9-!hW}c+`=%X=x=5zy&izbfVP-`)#y@r~gdNzqpuS<gV"
    b"dR?mg%*n<v(uh$5^S#JoI}R{Cl(97%S9Ybn*j0o*o7@{r$$<G7)erdIk@N`CM&bm{G@6*=51xj-W~G71#}AAT0$8"
    b"PHIUNdJxvJ^v{lNMw6<aAtN|J_?L9ojl~-U9w#hl!&>NbOmT5J0vl0HhO^j<k_ehq934P{fWy30l$}X&a<}m)}Mv"
    b"Ez=`%PW!<3)57G|GvkB&>nfl>B@A4x$_y6b8-9=L>#6G4SC~YVHnqG>qIRVjew!Y5t54iTA(hCx%=*0*28#<?|$I"
    b"lpy)@))q-Bt^nOT(>YDnHhVf?fO{t-fl?u})QhzA8nk7+FA>&c^ZWSXG#vjoTR_TgcgeEn11!Y~xl297!iS%ilL>"
    b"-_1<>JBgjoleIR7@&h%RD&)3WuwgT>@cAHrS26Z3{Xt&4qcxGBNf|38%IOIJ7qg-oI<naG$XUOQ=Bu<oWLIRxbZK"
    b"yX6~r31X9YOL5k(%H|;21k8zW3;L;g>*fp86g5_^&YsXxQ_bUZDn4#RU0>sNM^{IK>G%(V8kaFispHoZ~@a`p_6N"
    b"+ls7b;G%YS@W}LkVON+v>apHg!srl92`>tr>ZGBf;EfM+*mJi!{2m)FcI#MgceF+eAhng0H@=g_jsO!%l(A^q@{T"
    b"T4DV8?J~e|5cO)=iHAN6Jd9{&%G%-J}VvIITv{X0cYa_8Q9It|x+E>J15Vt#=@yyK&cAvl{Lj8>wuo;(7qYNWOG!"
    b"Aw<v@$*s_KF3T2~sq<|)TX8O?&Zk1Sa|8NA<%w1W>z1h(<|7u=3e@!AeSjw>J8h#m48&|A{M<vuCq;kJ2L8CKD#2"
    b"PUI5BVX{#*ALC^wYe7t`(sy@J-<X`X=i`BLIz>PQM7DQH>-J9r}f<Psp8A^}O>B4IuKNJQji_3tj<_5GK95H8)XO"
    b"}2@?KWI&u=%;dA+<^1g8hggx21A-4_Rx2;tmTH&qccTRn!`g|!(lLP8Sa8-)9C~rsBBL<ecFh76*AA9b@{Ba40u7"
    b"q|3|9<-aqOb8ySVk9VERCM&Um*zvf^KuGntCRMp)hj;h)Prc&&^b%K5CEO8~Um>)JYo1(SyR03rd{%{M9<gB~PM?"
    b"TVScqx$hnFFSP<RHom#yE*bHUyb<;eK0CZbo#cpWcGRekU=%=R?kdt*4))=c{A6`Z;FQ*5O<EV}ZpzXjT@eFV>og"
    b"niW{^{SNZ)lZPPxBMCHM;6*LJ{m>-_j@`~6YbNthi4{JO$BFHCUr)vRD)RHra}wBtzJy!A&~Cj;AM>?$sKc-%{M|"
    b"Rb5yy<+>D|a?B-HOQtbpa33{4fbxnhFfg&Skg#NH<wC@HA-*2J_(DW4I8LPRy{)|hTZ)7gNu8XSt?8ZqIYq+g0!Y"
    b"p3D{Y+xSYL%ud#W~kD{0L3f7=EN6HG)TW<P!6BvcePZ7n<KMEv;I0PHjR?qKZwDsxMkHVM;xZ<0Azg9tPhTFhpNl"
    b"ZZhHpm*!u+_dC0p7ZPy=PJ(GZA)a;m`(~$bOlSvC(O-M)kcjTZSGheNuuwJu@Pw@hn!aCWy5BTS+QsN{%BD+-n;<"
    b"K&2ceC%*Y|%PxnC!d=XL1TX8iQt*gEerht-uh)*UtxI!M|6q&ea+fj;AjG10pH%WxR%@4%4Qz?*wrW#yhxrt?)*G"
    b"!P^<peHa4L?z`iDbYrfi@c^EN;jYNMnIY~88}NcMA&qOqBDaEPYd`N3)zR-@iJdG-Fv44nR!dn2lV)4MGcK|Krvr"
    b"zQRt9<u*(GjE^d9VrH5W7?-4?Mc|0%Ksy3^Fj4TvxGDPf_8@~>uwT#x~wH9h&{WMgsUxANP&%*h~}Gprn7&+KEL*"
    b"HDIm;YN(#79ckgs@$QPGD3~GiEM`OV=IEG9~tLbY@@NM<o5N{URLx57wR49bi7#!Z*2#rP8)pgitINNV}vSa#dok"
    b"nZk|lae!`mcFI7s;e)U3qd%O*Hj8fP4cCtdsK)Xg6-xGt%)m^){4KhGN+7P>egju)Z2l)3p-X>CqXK&D<S1k?h(K"
    b"m$3WH{+!UU^9&{1{{S_r7&`T_kcLFWC<`KVW=>|D&Y%9Di~!pSprfQr&CAZZ7&%J$V@59pLr_o*7t>Ss=8lkrbM^"
    b"n6V#G>O(b>MQXl<5@JB{eKz%$Y3(F4xu=*n)@b7?yW5avOEBcbIh=4MTv28lQ*Qzue0bLr71o}!sc)q`<kxkFF;d"
    b")94uuLZG(}!bFC39n`Bn}sxfTVjgT$KYTVj+}#7&Y)45j6lc4Y@UHeTw}HXeE4"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
