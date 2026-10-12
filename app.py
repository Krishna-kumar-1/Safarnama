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
    b"&iD4<e^qNi*|<0F7f*8uJQ@+e)dzueZlL|?wqRj01ZK|;1IzNHwbi3F>;H;fntUmW3$?<~ZXJM7G?SfD9aDV|M0<"
    b"h5<JEX@)u8?pUNHz{!($dK%vk*!?O5g=aEYHNhSV<Xw`4nh16{ft17!AGu^+2p4Lf_fe)w<}M)Gt@=Zx=w!A<+^i"
    b"*A4&PXLD44omgKdYet**zJ==%F8t&$p|2#l_I6dPF4+gS3Q~gj1OYk@8d^|Ai>TngL9*O!paV*F_Ta#G`QUy1hJ>"
    b"@HJcg;9{FO~y9r1;>PA}ga0b3)Qp0Z{l*=l$jj7fG0MX7iXQuPX+_uSd>XG7lS3}%p0h<9aG^<&Sgpn?A?sn&#cI"
    b"3g+U3AA3LN$oTprjJg|LS+SD-FJq=7ERAe49zW-H3zDsE&jx8MB<Zj%S!?tgGKCk?X8@h>koPJq+86tKRs>x0cS9"
    b"0tJA>J_&3vz_TDIhM~yM9uT`JS1rOTj%u$&W@Oy*W2xfbH*X-|X5%V*%9_A!Ck!BCdGY&-7DbXLITP6n$Fu~Bt`8"
    b"&pH|nPFaieS!m#C6GnX7gS#?<(6#$2mE5B@f@etveyyKt$DYIS7DM6)Y%DZHa^-_SNDnUmlx<@ITyAKxbvx6*+Da"
    b"`~_0pZ!t22KAB~Sh-kw*CpupXJEacjmDYI%=(pG<TRn?>YG_cUBzFstczLi4q;C^0hutQ9fi?AOZZZ~wd(7hG%+r"
    b"Vt~#WxDLm;aZmfvN=G@fZK9*v^Yi*Yul&vl-o!O!W60SK%qD~p0gwbx1LAdfPB<sXN*_S1GmZKULyc!Q9*FzJU@6"
    b"+hZIF1uV-~BE+iyc!t29k)d_Ep@x?GHbD{IeLQF^WqF_Wk%&CmKK=zqM{!Lt8$J-PP|4=rfW$F%9_#OXPlU)oE4i"
    b"0)24VJo2m``|c#e(>b5Nl(MPEDVm<{I+)_qka$a|&-p2d9FbF0PNU&i%u`3#jd&gPg0&!YUKmh|3#F2}pdvD9i4e"
    b"bRybX5uE?(m-$dxJp&nW@wG*rFZcxKXKOoT|=c!4N=2yI>pn&M;X>|!fuQ;pQ0ymY(WEt4yPQu(nmTIIez5xu&9-"
    b"74$#VvzE6qI;Fr-N$sNcHI{RYP8PA^*78JN8$(Nn)<bz5M08p>ivctIWl7+lL!h*ubiWnNLj9S(B|9~Sf1j)!cVZ"
    b"m4$gR`11kD!5D*rOZ;dn1JAN8^j?{sn3ab90v<`>^@h$-8?+i(Dv+#cc8;Oc0cyTcO42-=y3@;3C8>EMSN*}inMS"
    b")Yi91kC`QKuJ&=C~{|DL0@j83=JnJz|dYaDot{gD`<NNl@0YdU%+>vzN-NHP@A5K>Ul5<OvRFWAmEYoh{kD81!aR"
    b"t%z=(O34V&^^S*T)PS(uk%V^|vo_Rh((IY{oI~=+)OtdjY&yik2=;3i+d3p@m``$XoavOo;17?rvgg*=_NdGfQK6"
    b"JF=*buc<W3@e{;xvodDzV}C7|SXjkm!qvar@&HP^lpV_&q3RxwNH!oz`R6k>|;A}nrP<FI%|m*;k3no(G?IrqP<A"
    b"2~hi(`hvgwBd78QkoqsQgaM6M##tmeH3Wu*DT*n(t%3D6S<vo89Qh~t(JDvE2H6SJGUt+L;ISqk;$q#Ms71_&z-N"
    b"me%6ZTe~TW>D8d=NvVx6@{yJ1S7XJ!u)UOmK^s5)S>IH*8HkVgJiMPR+DxEFEup+BANDa$km~H!8MiTlF_64Qt6("
    b"CCGrpu*CUkI^NgO&1pzR}5gQqY<$UB7n<u^^TbSiE*e)lis@mv*n??tZBN-trarx?z=*@<=c3X039B0`u~EBAa}1"
    b"p1+^yHa;f9$^-jXB9X<oB6JK2mzFHMfi_bTv@r}>dpDNno!L}5ib)k`h(3Y|tGQ-jkB7vh-XU(_hThqNFvB%e@($"
    b"#>e$q9kEx@cmMObPrfQ+OQ#pe&3b#tQZpRJAG=Vsa3mtBOIA}i~vfDczCFNbm@Bm;0<f9a{txS}mX)JU6ZZzUeob"
    b"&tPWrU(#HUr!*j39GK8f-vst?YquYXd6ThNsDAwgrvQgt`?Ow<>bb9e-^b7TdiC4L7s0ejUL+LB39`!IOVi1LHKc"
    b"z`_CRwluLz#*UnO1+2j3KYsS(lm!0Zc<bwA-NbhYyO>frijuqM<WTuIED~PjW7V!!x@KGqbbEyreD(}=o^}}TjXu"
    b"EJ&BNniMe_IR+4+DeZxIn5zW6VyW;_$rYKb1X7sVU)kb?$@M1gkHd7LwE}08DQChZ7P2m2bP5`xEcqsJ?t4CAI2N"
    b"RU_ob6aLH^#uu~~j`MWgMx^XX4v}ffeUyRcP%MQ?w)!I1z3N4z>vo1be%COd$W%o^0pMS8Z0fIY&jlAZK6wV-it&"
    b"<Pv&-0Ny_#8uxpJvEgV5Mi-`JjNKXBvo^IQU(R(`N3<y;6Ok|%p%hkZm-nMGBmC<s%~E^r`}<>Hir#r$VVvhNi8("
    b"CbB9%zY71Edd<vWNFs0rAd=d4I-6h7yukGW_QNJsa!QuouAUFyJ83U9qO%m6pI)Ebxz+$dC#rGH3<Vy=>s3Vl^W9"
    b"`#G8yKZ=*gE!;m96o$vOo^I}8lx@ym>=y)Wz0zm~8+p$h11IIQ&tSeho2++;JfYS{UiYy+LRC(MYZN&{Dw~aHs(R"
    b"DB79(RTXps&kQY3%;VC3vZBg;yfSdYLi<n+7T@Oskc6S%T}2i3fdotd<4lmkFg{R0Msc_WrR!Z~+)IkYl#-j`|sb"
    b"*Ot;_r@bnh-u}hDmm!b`vxD)`<`26f7Q~Xw*9H5l;o3Y#Bhe8sc7DVCumooK*)x!zQ}x$ZS1^L2I^Us=U+AWPapV"
    b"c1Uwt8ma%o2O1=fT{r~$Rng4XqT>LcraF|J|C+e|ZPs;dom#b^MqiS_~W?DyfV)b11UcI>6LlhWmrR4N8}Olm=Xo"
    b"ZqxBnE3%AFMTC7ok-?FMt>AKzr|A2<s5YV6%Z4mokv5~5^E+AK5Oy;{K>rj)wFM>G=ns8lCU_iNW%gl#th{hzEZZ"
    b"o0GT87TFq84Vq!#N8FKDFa((WT6)SAbbm(*Yz*Evxx0mG9Z;v$1AJ(G2o>xG_YPHSzN1|RR-b{ZWhdDZs`ar76L|"
    b"qR_GNXVbV1JRJ+pfcC3YE|T3!T#2Dhn72j7geTiYHV<A1TGy9UMaV>oUZNvrr0RdUuM@gm(W2vdqIt4AE|45gs^l"
    b"+_thhDJnOUzmgX~uy<*9vl4&uPh^J~Luo|K=0<cP9IR;RKH*X(s#(~VW~U~4U6-i~cx+_u+6I5kl$gigu%@eq_9("
    b"5pSWUBu$W%694+lsH=Cp`^5*om|*{2e_uSfWGp7<cO((7*VD!@j))WzN~knTovJF*Zf^mXrP$z<>jiXx28`Ui{{9"
    b"2)?3Z~}IB{F^+}5EX4;S1&ymSfCI$Lame(5i`Ba%5c}cxgL~rEjsy*&n@v_eehQRdN?S7w!xo)m5E6s9+ln+;oew"
    b"U{6A0H)V=JPPDIcF6FL%3Mz#y1r|M@Q(;kU->z&o`3R}$|i{odUww74z`}3H82TFz&m;ms6>C7Ob!KUopd}~8Cbl"
    b"^vEvn?w8pz7;d_kZYY28T&qpF`vnR22#@Fv;AJ{~=5uX$HOI4IQ#!SriPy%+f$*X_P3WpZit|ey|F9h}TDXCf<~<"
    b"&y1gUeOAS3nre!Q)K0Mw{$lOwb6_C5KVVImfP1zS+rxuC4#PGYMOi7!?Pnajg^xCc(myo;$bsmeDJ<yLSMK)Y%C5"
    b"*LMPCH|#`k5MS5J6PR3AjM896rqHcVxR%W+Jlpmwag=?;MXM^|zcq7Av%NL~K!rcI$sbGe7JXoU@GmtPJmagGb_8"
    b"&`F|y$u<t64&U_4LD@t3;}Si%T)P}?p7Z^Y<dkHKgz2`pa=VO&yWOd$2&#N#L?<(`Gwr2+_z>VL8?I?A~*{95%49"
    b"tuk)JKR8L9>EG0(Ej?~k;^5~Abnt}ywBni=<NS_U`sD`)f#IMV^jc)YQLT1OnMj&HzHUe!PzPcDeE5Sj8w1-(Xtw"
    b"NI)eBr9TNn&T6_mAa}9j%`gxkzQ&cU;6;mx}0*6&uxbzfN|6Bu_p^$BXvZ`l{3MEr$@{9!Iyfzo&_c20STNV$4X="
    b"icZZmS%Gi~5gSfgW|ow)fK;_Rx4j0l#GMa_?(kLQ&TD|NCXA7u+Sxe73CwH5RDt+(X<?hmLYs!CL{U9#32$n8eZD"
    b"ft4Hq-F>>v&XVd8eo2$dUZE2_1q1<UwbcL(oV=bZ=m$XMN5kLo<HV{}#QDN-d4Z^I$CZ<;~EEa2M8YAqjS0Wreg7"
    b"P{r!Uz203_jvCl$7KCz>LFUYFBtA7)#(OVTk>Nsj^S3Sgt!B*y?=7WKqw?Yn;YhRaTwhVkYz7KnX+wfWIEe0RvUY"
    b"i&+5XZNd-O8wN)-HfGP66@Q%j5C;f;o$__iMR^hytigHWHFe`qx-nLI1{hr#Ha(UD<PZ^l9heza=m%IK!KE|^Mfj"
    b"1(-2}_>PUEQUACL;iP#J?(iJ~-a}Jj;&)hf8oduT_g27)P58b#BnU88C2!x@4g_p%Q=vQ%!PkSTwN@SGqCR+^HWp"
    b"4he^NuF*q>Bn<y`BCf1*5l0twS#>a7%Q^WXR3?<I(KXFV$mE4!hD(7-s2E!q0s5jnyCHS_-gXkA{7OwcX2>JQj+y"
    b"Q$V}#2*dmC~1miysgQ)1EyqdQ8q{BAB$nUD~If`@UHNR5o5qU5hJM+b-V(cZ{t9(b93%d)~m)K<D`tC#Cy<tSpE!"
    b"^GU(WadpQZ`jmP=Z{{Y!uJ%T%1A^foj))sYSKfN{mD2)9k?K8sCX*7jK2~`0nW1y$0)CUKmlG+^AdI+It9xre8tz"
    b"kTb=a{v2&mW<$n$~C~bt)>f7`1cJ=4*!y|t1PDaCi&KzY*KmG4QV4DpCeCvTEhwaW=95+UKEP-DSN$6P5$igigT^"
    b"@^#7`upvB#4H=ctZJJx8@j2R&)o^THC+1nuV-dyLo0}fPOp#Bo~3QHjlUjyW$(({~SdjK}PMWQl0qbT|(SlU{}f^"
    b"CX*Ex7_C~2!i!WujGI6SJnOX1@b`P;g!l~AwIuqU6r-l<Bmly7zbv~%ldaHLc|j}`2<_%t(-aqZRlm|OM2&STHIk"
    b"ty&Jgv<IjrFz%xw4D4M+*HL&PQ<pIqx^@3x*r(ldmO3RB41HZjzTczI6{P00_2$CanX9{3G(lFYtw$@l}adfrmQ-"
    b"YV)(AyQ8#co#iXR%L=oH(PEdwrf}kK7;6Zs6h9rfluU^9EIjQWwpxI)3V)&n6z{4"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
