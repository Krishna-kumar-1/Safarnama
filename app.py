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
    b"*FDkqeGVnC;S*HUkJu<(bMlPZ+d>024M|8I7`#-$&ZVZxd|dv<NW^rNQwh;O{{IpgTw}-;K=QNZNKbe&GT_s4SXw"
    b"cGc^;I=x;%Q%ky(X~y=I*5FCoZiQ$*XYx=Oa}3FATzN_C8$yKCVBXXnMs_IcqXV^}ymay*sxseM|fyXikh8zx^xW"
    b"a@lb02l+p5Pok48BUlcb}62=0E`?}Mi*4T=r?ld=2T8*v$~>e+i55p!LaNq4E?hU>;TQ&?kk?_OI)myTO^^_%h@6"
    b"cJFb|@{jeX76^%X2Acb>3@0GHKuht*|9KCU;=`Q7QrzgDc32DG9(0c5Y1s)7nOCn65+tgi&+b^Zb%XzB`@KbHx6%"
    b"~XK1E{*Ai1u*{ACum&V&AA46C0h3f(EoxtNlaw6N|8Clv1GzHbAnNqJ{`A)<pY}?r+e%N9MuxLp@ndNQ<rf83N-a"
    b"NXA)@!J2qd9j0#xE~gXCdW#Uckju#G;H3nzS|GU+j3x{MYYvbme2h*rCH_1qXyly@ci4Hzb@Wf%mj~>84Rh^IF(6"
    b"Og%HMg=$)&Fh^CPLQ&P|lc=)XGyx|oJvU~wRpvR@{Sp@&5z1>qPBi`%Z9CygPoJeg}@HwV?8FSd|XpwK(@O2<wiO"
    b"7HCX`+9mV;iGt37S@~m>uJpwh|?26p{EH5HgWmY3#eV9rE}CQV+7^(&t8l)u(e{z%UVhBqL!s1w&4Zcec&*F(6${"
    b"MdEjQ~hgXV>f@rPiiC21payQb05r%V>`zcE3Qn4rO44b=&fg4QY>cxX13-{aTtGuuvgo1L}9;LwuSe?AI5Y_qHLB"
    b"I=XMAGhM@N&qPmq6or+}Y#^8Nnd<qUX950+yQOQeT!kSQ!oDZP^)GKxTq?o^BB<RnsgHjJT<*_G=T)rLVOG>7_8t"
    b"ZSn?qa1;DxVFk!*tex8fTiPTsC$A(d+2Nm%E+jS=g}PA9qaq(Rv$n4I<W-c#>GQ5;C1dKb5c{Jk_vvriPpzDYm2G"
    b"dTCT0>p(fSu?hkdV_(IA7USEYz2*0SHxhQl$J_p&@&bzHHkqUgBvh~*&n6zjHT@}GEDK~Dyv{dUJsMhI^BYc?J?g"
    b"07D-t>|}~oK6oEKJqc#*tsfpp!27adT5w8n)ld6BJk#dbl>?sy_<ws_g#>bpG+reKo?CjRQ&$1Dvf}hw>lPsji)W"
    b"x5c~S$p#Mj>t_&;tCC(ZIw5>*1^To~qGN4_%P>HjYHp~jH!3XLDzqFzvGzR2Dq?CX+c4Hy)bE|N()XV~zL@GVf<~"
    b"R-q!iy3=o9I5vY3Ddk)FST;p#myX+2uWCHyHZjtz$C1H59wiRr@|7f3{j_&!G9*pI~p*tKo|hUDg<w{`?GzwkTWS"
    b"=f{WI#ai65h<n&ZT#9SL^#{a>bmX=v94Fd+kbe*8d-W{7K$~=ga{Z5=w4PY3S10#}qTmjHLt4`E472NJJm;lG&Jt"
    b"iymB7a)%v^b2nk;#IE<(TZOLGqZp?l;F9U}mIX?AYZc^KFuxuvhHjVt^T8fOTvf&H_meQb@k-6&rc72=H0q~eeb7"
    b"cbuNH|_?Wb2piioOM>pUN0$BDNC+qvGKUBt;74}traf++|eM27Y^zGPU9<(#rM?Q@%T{gysXC2?7-a_ZhUBUD;gX"
    b"wDMWxSv53`b6n^~O9Svh=G8^Q3?09a)J1gj7yF-%S<U|31Rbq+&=VP=dU|vKIFA=v?wfuZSpnD)eqLopiF>`0D+w"
    b"&<;ng@Vs@QcUxuQ)=wq#7l{Ell3&lGpO^uPGeRyX`A{drYnUT{XrpaV@>#gXh9n0%t~vmcyKWK}(pyEFi)B4%eBH"
    b"F*G>|Y9Dq1Fl=Any#+b^ZJd#CnX{(-A_I=q8s+)wG5Ei$B1#|^_dr5NuuRz#Pd?Ss*zv|;5bniRdLq1{A5a_hzVB"
    b"3g<QdryQe4o4ia_tfe!U*mW|C6q+b54(RqkXHXf+M^>TFZEnjNsT<cwstc=4EFN)SWZbES;#7cIl4$R!J`l}<Wbn"
    b"hQG@>F|vxVS1wVYJPKH-0TBcr+lX%=L|6Hw0^U8tfpRuN|C0fLN>%cG5LO@XYn=^E)fY!p}$I@IGqKFS8>Sdj-c#"
    b"k_4=fecOF1LdCFhz6QtCf<kg-?>a3l+%!s5PtZZJgnhCTh;QASsSn8~q#0wpU3Y41b3K~QLj4ko(Wd~U;`-b043v"
    b"RWGy#mGZHJs(nkTh=qB}rXm+rACEhHH;?=mSrS2WFD{iL#!!YbZ&)3Ug#>TBC}y=!a&+S_eLV^)_`OOY2Ev%i-7J"
    b"pJWY-jIEeB8v^4uCiN%3q9@<l+2^B+vwt#8Txg(b8FkG1@r(6h5&h!yVMEO1hrGyF|LNr~4?l9VaS<xWbh_`F1wv"
    b"kdPQHgpb&vv>UG<Wuq$;wJ5xdpQGc>*vT-R*AN?!nOf0N{k?X&--NEOMwmxRw`%drlVkSrA=FQL7*N~?P)Pujy9="
    b"-rk=DEhkJdYA4e3Z@-KnFVey;;lP_1YL~td;p?rM!?Ay(sx(SwP%gGem{7vx{ob#KMnSa_F%cC$N*GuQ3d>;@ttU"
    b"qqy2tvL2&h?uT=h7vSeV)zk~Cvpn)p`hvZm$%_)fc)tJ=dAo6R55^rYXLJy>M|K!>5_Z@MyTyOt82|~V+@atK4pP"
    b"GbE61%G<Pb4LFHHoeZzyHO?YQxrxHF39Xl|!g*FMd#~_m<WmLr7FTGllU4>Hu;;+y<Vvl6ji4x0mvAUNC)wqPF~^"
    b"co}>Kdmwt*g!L(Q__gfIeCuo{=sG#z_4Ut}d65PjE14A%oZ{tD3yTyT2nIFgJ-9m%l%usC8DlXNMx%tTaBEOvJ%O"
    b"2Hh4wu!jqS3rN<IlJrpPakAtNxWg!k6)du@0QRNFs_SDrdoZDL!l?Qu$EJE5!S8X;hViYS2Ayj_d7NXwSHHi4Zs!"
    b"+Xf{SCM@8F-)KHesP<Hs2d^4bq0GNYKwr|X!*o~6+xKDcJP&=X$=@eGRF6K>2Q*Un-H3ip3UfXvaDvADUcai@wzk"
    b"F{;;98IUI}g{I)UFQ?Ung?XCiKXdavGyyB?gB-m-gZ~>+fL4^Nj6B>WsvD_A>HW*zy9Z7nSfzbQpNKwCP^a&^k=L"
    b"}MQjQ4eusz7K}RQ<1tcZB~Uv#SZg&XA*-Td!~)<m{iZ6J_AIvX`vcw^MXWNhfaFmE&%d%bt31to=a;Zz!{+ulh{^"
    b"mUWwcrui#%B8Ny|h;g!ISC!0x7`BDnZKm&M+KQ0^Gbav+as=XF(2_JC2{Tf@lK&*-c3s{qIkQ5VIt02<dga2>d3U"
    b"*;1w7=b@K$AhYlL%`!A63{T=nxj<?HX;K+N7$l2wpzD1-`0#ay!an=M;Pj@!&NScld4TA>2k1EUGb1rb=RXA--(6"
    b"b)Nw6otj;EB#Iq-ulMYYjarl_Y-CsZcrprYrG+3rR<}5c6J$^GY@-AEPS*h<E(0Luy;|lIr7tA=zx|3mXo~`g;`_"
    b"CtJyu9n$pJ`VgR)vytTZmT9=z)J%Iz5EV^|vq;*(|1a3!R=oXr17=mqEu{6Omh}l~6MF}4qQNH`RB_Ur<s|`tSI<"
    b"xEpzi|f~&t--8D_%G%TyUk;z}J}2n|+VTE&x_f99S7+2a?EBM_!wi)}z><F~^U^QI>PM`+#MfDM|pl=DckC8lrK}"
    b"AO|^GvG;YWKmqPDJIYN|v5IhzZE2$YT#1-V-k-~(k%Ve`k#s6Jm~i&%MPWao;S2>9mDyLsCXS0073j^j_+em$)=y"
    b"Y&ADHO2sbd*fm?!nAS}MME`fzH)m{3snfifj=A0@b*l>1K|Z&4`+Mv4MRpSuhv$U;)-e|4(UhYI6|i~gSJi{)=d^"
    b"uvjR^5vA$4DxD^ZULbsvK56L0h8cLam7<15sx~3_rP#hM1)Y|nCb>7=~(V)xDCflRtj>&&=$608$q3yJ)~|u-iWA"
    b"RvDO$9w;C6_l5smc#FP4WZMR~WN0-vgjQ<L~tQ@{S|Mb-<YUC(Bp|TOPt?4l#T0PUT%xMvpAs*xfWGTGvy29IZ&i"
    b"78y;x(5|gQ1Suc%Tt-z?^WkfkL*#6W@2q(C{Kw+xVUWvyz*kOT-u|+iIqsU_m!YQWI<?(JwMw!J-RDC2d?0{LnpN"
    b"z>TB;)-r_WY%YQNPLxNi<ktqQ@LL3OYI5Z60yHqhA?Q|6`spE90FqQ}=1`A+8)<bOXJ{FRVNSbTs>Mj#!?1%s0&P"
    b"C3a028PL@G@f1!cusUjy+gh2?$@`3D_4*o=w(yFiydvY!Fd@NPhJtQ^<|CwHIBjP_*g(f%|s=AZM9<$hCxTqqSkp"
    b"0KvUyBJtIup%8{X)m_U)?GK-z?%re$&8kpfq4gqado2Z%V37d!%FZ2W6|LQHUHZVJJ<Bd54J-lM5mfh%rJm1vY^l"
    b"dn2^X|rwaCC$(d6P@1|Uvyl+-`J@#aWrHVgjnTbJxgjdN5(|$wofZ}4SH{J7H?JA&EvM@)IFG076^FYnAX*AhQuU"
    b"yeH^#_Bna#BlM`a-Zg9=J|5p`;qQb0Z3viGK2T%%oQ5w$rA5Kdq_ymj8riCv|R_nHbv_x5~-?560WpnbiVa&}9Nx"
    b"VTSS9f;98ZKI7ZHJu1+)-Y=4yS5&f_C~&N0`f{Nj8+N1)N7HeF+dfX|5E6g}Wqld0?01(rkeT5W@CImHiA&8YqP#"
    b"xqdF!wAlz)x9*%MqkO=nO?0PdG^VyZ*p)6eNP{g{PwwS2n*n&xaPqlC0%mOR2O(3{%#x9;C$d)br+cQ!jDf6s;$o"
    b"LHb4tB%mdaq&)%MA{?f9HSu=fQK#XB5*`U7sr&gwZCIpc{8i{{~};|;?&`-?UK$eD62_ZY-G-p30V@C)sZi5Gc8i"
    b"oRjhAI(#B;%i<=|GVy<nVWlaAP3*<P^dnMiOs=;{enSLjWaS}wdOjjr)(`eU4n-E?ZM!=%NQxzN2hLF`M#)qfgzD"
    b"w5Hw%>jD?niHR_i^ofO7q9-UUt;WzF-U{P4nIxb(W3PY{FS2%bZtFYVK&lA&Ea$;DEVh4z6&}OssmOKKCiA{=>JD"
    b"Y*aj3mwtwBAASR1q>URB*l>qkH=&UtDjR2C$>0}$J223P_}y|ZrNbZW>?y3Awkfgx2Hb3zFl9<E``h2Y4o+O>x*^"
    b"p{Gx?%vfu6cPDDT8f+Oh+4?a$4blNiQE0693M-cmG2@EoLK*`+AQH<8L}Qvj7j<YZcbz$Ews*o&7XMknvp=j#RIR"
    b"v<A=#nt?{uYpgIm@2WWOP7-dndts#a$-2X(zg>4-piO=)9qu{Ym`V7FbAkRHt2p{"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
