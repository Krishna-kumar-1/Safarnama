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
    b"0=*?nCe@L)UdFh+tZjiEDvHgLBclpvq>wYdC;bcRMTVVhA*g(rlwO%R`L}mfe^+-QG;tt@8nZfv64PF@Or@b5C5R"
    b"bHzWr{Fn`eMK0tGYY-lx;DI2k_0-*Un;ubs%pITQh|L2~A1%Z2WXq`JcDBp?a}`c{IB6L@6OCOQ+P4X5#i`kpcD("
    b"%Z7DlpUwb7FN)_nP>nnqMG82|5Ap@I${|ch85KDt;+Jx+mUKti7IELbbsIh!3Huz!Uup|Tigk9bp6p%8j7lqJq9O"
    b"s^vt>|v<JWCAtLdZ2a@WRUBqi6dWdDl8x7bLke#Cky-C=iM@wq)00lC(FY<t4qWKEbQxE_uO`Hh@-PI_X7bDoj8!"
    b"&6%kNPEvhx8ik#%9ZCI|QRkIT>Ld_WkA^9STX^@WA@5qT{{MeGQ~ZEqsW1<nGf!O1t3NphzA_cbcG;Dl6+XM0;>o"
    b"UkXS;+7f5UE>+z|?I43FjoGh>ctbTVV~{jj%C3soakMfte3<_PkmrZ{-iJs~p(?0b1o7bVWkPy=NQ*<AE-prGy62"
    b"}HJ7%E>;@qpjTN_2AXRT7|z@+`N{ne6f1F3vQvse^&AX&AbuEM8gw_#AV2*f=9pDPl+7tp@8>cx5IoU5+2jcW`6t"
    b"d9&nDQES%+;;A!6z#XP91m@$oC;rGoog7FEeEqvWek+z{E)7lOg-T0EHb3R?Yj~D+t}#=ZJ;9h)z>!KIl!uMi;NT"
    b"|{#3>^KMgp_!ir!>DKP64ba@T!wk8AgtGJNK1RLCRa)?%6YR3=S=UY=|MF1&Q-3dcYhl{|>@Lr0xV6nsQm4-X5T?"
    b"|Z2Uql%@llw_m%6o%O?&EoE7$M8E1wekfCxfs$S`4v4?qsD)Y}uU!T#yZcb$CXjaOZhp#}YJ8s!l@Uz`aRhbBEC;"
    b"%?RuAjbvHZELDJ$@SYS84Ak8wD1D;^aoW88$<|#M9eNZ3QHDe=Q#4-}S@F*{&pQEn1j26#UQ9V_;-!#H%J&IPttV"
    b"@2%{pcg!(>!a)YN+)RDCUB;?HwRO#|4<XCSa;8Ge4xvXRNXpnu!*2fHhCtX3d-5^RZCUj{_1YKZL{CA=-}bY5G0Y"
    b"+n7cVK2P$`lGzYBRQJRD?`&z7{tXt%OMfFbQc{H2>CcZ{y|26%FJjnCv~g!5yQD;;~~%a<vg}Pu}NyKQrBrl!6w<"
    b"Kpo`2rKS|8v+>nY=<Z!|>(q-V+szC!_JZvoFhym$_Bw8ro;<zr&0^qx6vBB*1%3e}?&U2Z&J=GghR?%{w%93<f$Y"
    b"sp}C^f%BQ^epDLRHFOqJPxg(yhMyr@2a6b@-Jt3K8VatNPh&1S1%rfd|DUY=CdnWj6FE#=FT0L?9`kB$vjqtHw@Y"
    b"23c?`&crAYJim1A6c!ogu(OBW9uJ>`2(9q3pFj0D6pXS3i^uTGM&jICTvyx)$#k$AQ!i2JcK#-NMrD06!objjd^T"
    b"ct@izEucabJtcem4HWB0O6s>~AaBsXS<w;f?k@Lo>`g|tQz18qY^y7cYn9Yzvi`MWleX+5-VupV!&Ied3$r{b$G-"
    b"K}Q(;utHT;(`^u2X-5imhf2P&YZ;KmYp%u$Rn2x&jb4KB(oqrI13{%2%ZtunWl9QcQ#7(7JQ9&IFf`4SYP(X@V+f"
    b"J%OG<<VKG4m7z)g)vK?ozRBCqg>mb86(g7}7WhT*QvwFw3gohHJJA;X-unMKt=46g2S=qL&#(^i65HA0uczTzJQ+"
    b")MRl*6F`y}^gr!Z=U(+_ijiVpW8}ri}ESWv$P0__$#f;`3cd8EGzj_A{s`=%!nAcnS%-EOt*KN1PJJvR2ec)mV$J"
    b"cG4d<M7-#Hw!vsCs0y6^f(YXpx%aywpFt}Ib}@YPUB4d_jllGhy!;tG;2hJgJ5*G@2{bZgv>;;!_)TI!mpRBc>c{"
    b"+8W8xQOgXrr?pm7B0QL2H{lFPG>e#F(8)(^Nh<vI;53SYU6IY5OD9?%@8v%(MuHd1W_VXXRhyXy_jPg-1E^lTep2"
    b"Q5OPGR&p?AebsAlex2d^h%^yfL5f-(__&aX2>Q^*FG{uX`m#w1uwQz-fvuYp_$##y3sF<xugKv5_D7W^?@Zsn@he"
    b"x79M)XhH7uuw>~eqLGleAHxrxel@ND2OEeT@Ef#m$u`ZpTXRI~B(QCK}?*~>WaL0;pPtA!H*J|N9n(OSE7fhfpZ9"
    b"c&N?10h=QKWWVUOY0Zg{B4dJ+izy;W&9g>opujO8?_RpDU~%?LBD3UaJ27F$965Oo+9_*+r-65%3rh4aImwEGB|%"
    b"a8S)3gq+)nky&5nqsU#{Lw?{m<2%@2*W2>@l2=JvK67~cBNOvJ{KcMCJbfb~XDmw}SO!`fs80;#vU=kT25|H#D{D"
    b"F~Q;Jt9>EE~=3mH$%P4Wr}1J+oTm`>i9r3mp|_9RsYx5O{*d_mC>yuHE9(4$AT45m2XD|$w1is{wJB$IIaxb)&tK"
    b"_IHdRVYS@Pxf<RjxE&4Zy0nkQGd<9k6f$<Wx+t4%FxaIbr#6ptQi2IEORp1@moe<2;P_e=p=<A0LN2X=i+S`rmDa"
    b"+u<fxEe6wOv(O)f!Dgpg1vd7T5wg0QSznB$ULjjm5nD#(xThu1M1KW!?_ytQ~w~oAq+$e<XQLG<9>9<Yf{;ZGVa{"
    b"96}P$pBf!4UVh#bDJY-;xMHjX&36?U!^=LNZT?hM4;6HckIS1!^#7gK@`^<8;7IO=0C!5&R&6euvCCBDMGJtAr7;"
    b"66s_DFm9bimWz0TrX!vtdhf@$P^<vw!wF_0o>!Tv&Ua4$Iu#pQ-@n3hYcKZF<DCR&;m8~kE2WC6WkFBLL77S$6Xz"
    b"xSMIT%q%|$V8yz90JM0WSaf$OcTtCe=fe%XGL{hu&%24}h)>jQ#6Z6D940`KKiajcl9VRUumJmejt>MNKArYXzkh"
    b"-z_{-x%1De|IHrAuy$#8Hyk19_vE<-4t&Zzw|c?NN=^o(I)6AI5vSG<Zskf^V?i23TcB#^&dI~I<$kU3$TugH4LS"
    b"=pvn!pcn{JGarBYGQ$lwy_Gs)ceJ>s(BQS!9frU-fw2Hk4fIcOW&1#->Mx#Q4L7r~il~-r$ZHvg+H(gV)IhjpUDW"
    b"G2)AIc0N=~`_EJeino#6{(l(0IAXNlRMnKTL;BM~NFLi!w=wTkOhPPeHj5@<Lp6bs{k7mt3IH>d0aW=5>V@S?KPV"
    b"(RqtYat>fh0VFW43{t6PIj!(lvAu&U*q(v6#Y>H^jjPvwStu1ns{@tu!#6~Ig?$BBhZ;#D|Epa<0i(VJ4vc9s@e*"
    b"soy|W)->|=7k`UB2Y2;7Gpo@zi7SjU4a<1fS1DF!NyX{Nn23tp(&OtzoU@`>Lx4{eB+de#q3E&X#ysG`VCewjLvV"
    b"AF)n>#kKjJAr+mjGV+w<?~bJC=+t%!%+aT_?%_Oe9jU2Cf%5h|2aPc1(g9Rx-Z?~uO8bM-SiT$m>1eb1$eMNJuai"
    b"uq#B8;f19k-`nQ;XvdM`5leqB-efCI^ijUV6S;yPqr^$xQPbiy{Oa2BvgYKb$dMhE;%5zlGtdhO}l>Mx#?ysKw3f"
    b"0?p=*qAk;qbTf9Iy;E{4Zy|`tTY&R4|v*){FP@cD9m2HG7fTS9&APlsr5^gm~-T_VO79aUgCcfnl2VSM&_lI%$%g"
    b"mQi9Kdnf|MPWtu@*F)*>3EkmtWzp(HJec2dlN?pcZ?!$HYypXY>yI9r^0=w($X^ILl^7vMd!(-$p3^Cv*3lcPe5s"
    b"ixF!z8YYZ`8a$RJ>olhxs&*bfr4x)DP%GKKtCAj^yFY+_&X+-2D~d7pO<LHY&!D_G_z0G$K05)3^`uTAs3l#|bu>"
    b"cPs>LQN`t9i!lVuL0UfabGqbTFVK;QffnVq=1BGZTB@-<ez)sITf9@dML!ppk3z78DQvy=T8akZ#|AJ=CLO!uak6"
    b"RK;+E}X^6E3h>;W-NELTfm1sM@WNaXKr@+)4MQvpd-&&g|V8Bh7Il+W(eG)~B$f|QX!Th2AIg^(ESf+b8Vp~d+eS"
    b"h&<eXctEcxP~)m%DK4c(CzJ3^##)7d&U&JCHV28O&(xrY(#B!4I7H|CdVHLI9KvDm756jl{|0m6|Xuc}?qT701z`"
    b"(Qny3u4~JO<V-C0Pv7b}d(rK(H=mphou5+MP24q@)3i70yeln&;?fMa|C|6-y!StM*}T^16RU;~MT?%CD*L_2iDH"
    b"@SHN<IitTbN$7W%{1>gN$NOFI3%r?my@*}XwClaUd%;%SK=(Aidj4<&ig`jubfj{`S&)h3XaTI<_z*nnvy?k4@YA"
    b"O3{1nwAKG2-+56qz{l$PQ{o+9b6HnQJbx^o<{t#UmM~#B1kbZMWtbaUSn5}bguUWa*i_=CE@tzD+DoW*t@3"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
