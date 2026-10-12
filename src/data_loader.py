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
    b"BACCfzb0p}f?YH$yVkuU7S)zx{v?TJGAUo4Zj8;xvd$x(5ql~N72*M6s$u|DS81u8@7Q@y)ft!>t6!Yj8sVsNoiT"
    b"?2S*5Rc$vEmAPvGBII3LsCw{xbN)$J>aPlH4>kxtXafIdo`(mB62v`R42B7X2*{YH=>6N)yEp%&19ZDuWe`?9nJ3"
    b"P96knVVHpuL^KWn^JoEP~r9l$&r@UbmwP(z|QC#5Y;M3V9>6{z^yx)97PZkt^%4tn<?X*zQ^ZlOACc$3Ca53G<(t"
    b"w-`%rODXZ2ZJvx%}P7-7ff99nho&&roBSCbMEf*XoiE)q$j9#R0gtvYZUut3O*rWa(Ms*QPpXZM+zpX6&mQ5g$6m"
    b"El@=Al+aH?T(rL=JN^cF9v=Ez^+t;d%~UXHgG7E38n{K_C=!C7&%L14ztWc||djKN4E<bDp1!9>S7i{$r%bD1ruq"
    b"t_JoMB<K<KK6&cDl}16+&sLnPBasNP*6^l$Yv+UZ?2{)42FoYAyZ+AQJI$SsKipI?8uaa!GOE4@jEoM{(zQo*;#7"
    b"i_QEjEyfIwoPUOsi;@-u=d<_XU1@BC)gtSN`SN(y3P6768w#R|0y1ca!Tiu4VY{BKEL=hAi#c>Zt>g`e$$@X>{RU"
    b"6mah#zD6wu@>($rd%#lED?+xPn^kj(w2q)fW!lAyxEfnKV5;o3nNGHhB?ofzx7h+qd<I&-tmFrTAK}CGr$jL$Hv$"
    b"NF?O<A-CaTuW_PaE9mBQK<su>!0%Pb2CQWrSdlvrgV1wL`p<QiBg|b^iQ@ils@C_cvbu1WJ&Lj3^e)!CY!s<;m%q"
    b"1MeLpLjTdRgbyAvV<dh)V|*XYCCqT0U}|x(zIfkH-Iwibbp0X+%Sg12F4s)*w!W%d#ZeeIiOuob!fD)H1GDVa{4Y"
    b"!ukET@?<W~wPNS5eYln)XAOZCFRW0Hrc+6uCQrv9k^5o{Pu)7relADUFn>vywJ?j5O>sPtbYn~;tWX|>cKUak$tM"
    b"mCo0;6pFL=$lUl#fDYecO#hcg6w+qKP#e`D)YjnelRPA1cdk%IVr9{WbOhPPHVH&a+<4v+3%wY|Vb6klK5z!$8^L"
    b"jJxQmh`jz)+|=!Z57q)Wk>D=$&oQWFzdWc_&;9`WDClP*zFpd^4irgG;_357lEP^rb34*FIe5V9<8`+M1Qrh8?(b"
    b"yuUL2sXCV8?9V6W*zZLlY1u2?CdOne^J&&7XgJrLOp{Y`c@q^2Eze&M^vEuCd%h<={@LE!4ffpTd@joi{gPb{%+A"
    b"72pc_&f{Ll76vs`&JnrzwIDi5q19c>b%s4P6D61vZ$7&aUVU`L((A@Z$t}#+hcF!Y_yM*&O3tz6}p*g(;sf#t|64"
    b"AH#`<!?kZb$8r{Z@XiP`AJAIcqe3aOdaDjh$2}q7IU{XKa=}6RV~rMOO6cVOBFkaTAGw6;qH#$07R62|AfAv`&8g"
    b"KCH?;GJ%q9#h7Lh~9+@d*hHz)dWz%d4JJahIpM&L@ob1oBv26ak7InKuW3vVX;17bRv;qcN!qD?rC!BZrp7*mB&n"
    b"y^RkruTug0}D4~;jmz`AP&&%#?Jx-jF58ewGLR<{u!U~iF?>~*+Xsh)!m|YVE&q*(d&;r7mgeJ6z6p#$Jo<&M~$W"
    b"+{PWKwv1e0wgjNL6f;*yLm+xVIqrzdfq~?8S<a{N`Xs6IXIssQOpNy*bTb26Ib6>s@AIHmvT=hkxfEkf+u%})mq3"
    b"j<S-GOeGbS7ciTBrtIR`b0`y~lCTB8!;ettmPP`a=H{hcOpmZVeZ|Y4E<=<x5h_2SVQ}B7d}QRp!O<^SCqcK=~Ra"
    b"3?a>8S>8}#RNln3Rmiz${y^-|i9)J`1A2lI?f7{UvT;ExSwe?5$fV2_#}gcC{VhEMhcOl4-#-@+eiSN+CeQZ@S0&"
    b"mq=q<=U9MTQ#hsCtnq$hv0R$PYT=csBTU1CNp@Gh3LA;c+&N2cCtkW$+o7pHHOf%(wa=~IUQN}Hdj2H6lE9=R=%^"
    b"sIT0YKaVn$wVT!>FSoU807bq{gdG<t87aRMi>0!3|*DDh`t-8Js}pi=`WP;nZnB@<@DuD5JvK<)1RcLf+?5Y@~|t"
    b"LDLl@AXIEdDp@Uil7cmvDw%V}P9xBW^ZFd+6z%USW1wF#o$NWX0!vhKf!3H>j8H~4hvr5_Cm}KEAIrNoc$Ble7eM"
    b"l;V)iOGpt?LpN$4*6xmlXWs25>($w>|M*%Q`VP>cRQ3C?R$0WG`0kWt}G1wkv8uuHC=uia^}~F~!|Huxf?5?u9R3"
    b"kzNrWzJBH@;D5dS&FpjMteAo0dc<O4D&h~*Pm}n(4@F}SV9Geh*gaOd1AJKWM~sn069BF%rNiO**pUgu!lkZCI3b"
    b"^Ob?BiZ=kqf31kRqx>^*M8%CUm;k-q<=VMmrEpNg_-vjgCdpoQ08ZXRPS9rShOm-h!!N&5B*cjGFL?RvqlGS1XDr"
    b"f~hgj`s;D=Fndbsu&;eS<E=D#DdBhVAw*MOaw)JaxzyE=o&^TZ?$fh!RAO<%ubOa_RyVQgMheC#)m-}s*9WkFQ-X"
    b"uI+kQUXHHNG#l$EGr6I0eTR)~epSxBVeWog9&0q<v1Jb;TMT)7if2;mAueM)|3Jczhmh5F>ispsnbZkZJIeVx0Hl"
    b"|E=(EPLv@TFm@Qp8K)xJJpV+mQ9r38Om!kjPLI8zH9MGLP#||NML1K3ovzVR8pAyod5L*YSq#7Poirp+$gC>&gF|"
    b"Ir<}Wx~h+&(S+x=Q8Gp(MOEXX`JuZqKi%fmkMf(R_$O*<@lwByNB^1AxH+0lLRjj>-qAGUfhXC-n!&UsT+^FD_<s"
    b"2p^U|Pysl+F_u;B06IoiKA7h_%l(UdGapYH_W2=W$bt?^pqUS~8Vd?J6nduWi!R+@FZ$&d;`ON6Y~uwhEisGqHIm"
    b"{%>xI_d%N1Lb+n2b#Ew6P3>@SQ@;z7|NtK4yT6%J!O_lhM3&G?HeU^+ugZnfh38LkT=R;D%|Wfp1}Lthb$e;A=2J"
    b"jbkSGlMyfDQmyt%e{vyO@<&O(|I!@}jTmdZkGRw>lc+T$lgd)Xqa@cAd%H}Z4Vfu{e8K|LW6JAhzYM$43wqJoF!~"
    b"QF12(pheK}9IT`8?0iB>T--ZQpfN8Yt`2+RIEycTK5r-<#WDI2tsNBSdg;0KDN_wTJ^VrEvG$3_i0Rv|`nX!7vP}"
    b"{rW5E3M7rsn^lZihX*&B98Sy1C?;;`PGzd=2~DyzKd|8>sWqmG|6A&}WXXwij1Kk^VpyB<k%1e)y0^-itVv4yO(+"
    b"pwvJ=#QjinQpQEU0+`PHM{pQfX-0E47BV&ZIxPZJSGY!t`PWj`RWnH-=w7Bl79a%`lXD{*8dV=J6j+`OVgYgJpd<"
    b"^Am_;2!8utAE{uJKEO;o-PUZvIj9+XVB8x)VK^zBEn(jp@1)aIVfH)6gv3t?VDW=RhbSNdC_4LZ;L6?ARL*&Qfa@"
    b"pBX1>q20$H436u_qfVUflNwt@qV}j@Zl|NOXh-;VhW@iz(WVpt#U+6wQIJ>TVI!G-kB#*#H0Awk4)Z;D&J#tzINP"
    b"^^~gxMMg3Hs<ZBFZ&ToCeYsMS<$B{grt3yO8r+eac85+8a7`+X6x=UcLR2#HLn1#)NSHY0KAww2CEq7#uZ(+P0(>"
    b"qkNNAht%opBe8m#5oh+hP^&LkEhI?k>26*#YF9A3LA`E&xcF6dc{+Q{)-8M%6X8RlGYH(P?<gYVqBI~#rl7<e<}%"
    b"5IOukz_;j8c=U6qgL!EM9lyHv5*&RB?NjPcj4btJG0+5ME!3B8eN^ey8eWRVN~7T{KCaq9|2fQ~MQD{xPeR!$<~9"
    b"f5!DY0~;Lt)6ycTFFbkbWc`Ve?6@G8i9Ey9=W4Dad#7n0d0rW+pZ~y3u;gZ5AFk1Uh3d#YH11T``lkAUOi(sUB^Y"
    b"+w)R~uAk3)o^wqfAVx&wvvRy#~j<bz<{~FvW2ttfYg9(}x;m6LudQzt*#GC%^N{A>sbQ~P0{PRb`47LL$`JS%GeD"
    b"q<j1`T_n=5!qsM2A3=+j1foB&IsW^~(kliC!Uaro3v<+G1464Z7-fI5Pkf9u0k+eS4#e_6(vl#8XhOmybth>p?s@"
    b"fTdkG%%gr`3g6PuzX6$jG7s$>5?(wP>0qb)HO5-vX3~M6=OK5YPA_gzkcro7i*cRzD-QMiKbEj|)y*u5e?z+s$GM"
    b"ulOlQ5ND_~O!jlf>RE(qzbY`}mE0q7}5-`#fKcu$G-d>C@5(yaan#K}r=ey&P*_Bsfg#`5DJE3UnM3WczY=&Dlq+"
    b";BnJ(OaT0^m-IbbV9jHWeujI30@YmqcMc{p%W7^{h>*5Vtt+|yKz6VN~y_|98(o|YR;2@L%afM&yDuOEIT0^KZ;I"
    b"9b~1KevrI9^oN;@_6<cr&fN1bOsCl*b#Khxl-=AcV%<(XX_8{-0q>Rz9<dCON+cSFLFJZD;dT0DW_VLR)9yvv%H|"
    b"s3<kc^m`K`sn7=CcrXYxjR+rZ@)z9uO$o#ZVwuW97fy6tO*DF0L=tzE`djoTo|06@O!IbDmsyGiqoMbW?S}jRB=Q"
    b"m5XlA6ShVpit<o^OtKA*GLto7XOlM6Ke|2)@gPLkjT4yhZ%)x`E~}{NEF3{w`V7Urs3}jTF2X#cQUVMEPC~Z=ZCa"
    b"@XNE_Ir3gO6>$~G#*Zd_t5l?X<ASJ;2`VZDyzy#^LK_#;8qa({-VQhB~*K}48AGSvRA0B0ISF-3ypzmcJUxO?Ffx"
    b"xI#+yFwTWe=bRt22<+`O}0?a5gk&w-`rfkv1@_dX;z3UC+TP7m+kR@<{+S$lD2Okj!9pnD}}b$<YY-1s||~-gaT>"
    b"?J3w6|(fAmMo`bi)@_rM^tE3y%ZrQf?MDdjG(E!iM%s$m#sZxPHNEKL1;#3#Y*;+S+lj6ZR=<p}U9eame4P#)m?3"
    b"Vk7%etSOBJ)RteRSBL5tDAWQc8tcBDJ9YuwJ|Dy95#0rCJLErbjzw60L|<II9-QY2qNpHstZ1R54ny#RNRW&#Bn^"
    b"yM>A1$o6YPnxb&dLHXj$_U)XO%^OoHSQ{;mxq#CTe5<JA;$?lNnuGXcg$|Y{XSd<e*Cb<`o83pnQ+v77RY~ePYfS"
    b"l~0;fCRatd~l?m3j&)19)N=1iW54M2Y|a25uxMwC=Cef)*LWPhu3%HJBJDM`EouL2dX>|ey6a`LM>fR3JxIS~KwG"
    b"yi!lasBhi#xuHU%tKXd%f!&v*(UeOFa8zHqW<&mkLX$)dt}Ab8xGCK&>2DB4eYrWoStIS=|<1HRHq!ZQ-gDiXf!i"
    b"7;3CUZo@a#X5nTI7S&$vHL+-=0!!<?z3=RHaF(dDGhzSj?Y$tIZEp)$2#p8727o;M|6fr-tleTB0L)y*THHFZ%h;"
    b"_vNt>g6G-lBQj7yv?rQ9Er~{|boy;r2G(eaz83+R#NsJB+X9>xu)YnYL~$eo3yXdPinPDt-6~f~aVjnr!Q8V=jEV"
    b"C*siqxVgt`zRJDs@-R}gUIUiXMYtCqY>G@akAJT<GOZULmCFFlBY~_69K2<V3-2C;gcOu4t1)u{M=?Y^G4=LS$S="
    b")3*os<KU*qqh<Dz@#qjBopmrQoiHY_={aP;Gw?MB>N9dWzOmM5pZpA)>EFqHV!DKP1*(kDt#C+`g$tE7z}z(xi2%"
    b"x*oNBCxdbTT&_=#$r2Y8J4^?FrqcvG{Z-raB=my1&U$$HJ|0WQ4FFT=GFE_=ayXfg;JR`Rbjk6ndu2MlS!X*N0Q("
    b"Q_|OS4gK6;@wIY_o#J~9~Ai4<9+y(f&W%nLsRMsMRNG3#8=dttkz`+_+TTTNo4N(*(d4!wuW2IL)M}hq"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
