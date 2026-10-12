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
    b"Pi&dyJi5JM+&Jcgr0nR_b_9}b|JCX-I$yPpvJPqMT;;wl51Q)#*m{((|G;ZGu#L)fY7R<1#p)U!Cc^X+Rh<B_MF~"
    b"if(P9@9y<iFa{i_HCp80Yy34D9P_rN^W-s~mhG-T|2Qx0N~N^~+5dQv^Eo+zbGk5q}pnz3=iU@nn`I!qZrS+My8m"
    b";jOJB+Llsqi|}iPi)x5u{(Uds)ok=0(NG<7T#5|aH+HUxqtA*(SSgZ#3CZPL$C8t^0%gY@RP%$FCWK2WZlB44XWt"
    b"1M934YRmjmzkJVM-F@>hu+%+q6$!+v;BfFNo2x-<yZ}PwJ@oQRqKlZh#?H?e67xx@e5+>^d8otj~FO?Yu4>);5e~"
    b"XQ(n`pQk;>Nm71j#;-veWl-Tqt*@RiZxMrO$gT<5r<>%X0O}QDIL~UL3hzRtmc!2C?0=zq9*g^E>#KH0(gXUj*xA"
    b"2OJ2nis+uR-j{{4aqpcSo`I2m&q5DnvLA!`v?g=skT3&H=B4Fz&OCw-?w_(>8vL5k;<`Xa0eXjF9VAzGrEWJC&m7"
    b"H<Wk@+`#Yt&U+*cm0CAPX--S3rARSH4uN*(=^)}XNKgC9-BMj^YNqOcPi{vUENU$^jzdX_z;K3h!%%^JVXv-gfL&"
    b"?Vl}3)Yf_86!M^ej>mEivey7{LJeE61{ON{VZXje8VXd$*CXD%}~0jJNY5sY8(<Dqi9BsEqj#a{(sjGI1_4FN>2g"
    b"9Ohb(D@1^HDBjSxod##Z%kd)i=dzGS&SQM-~xTku_FV4w?%eVT4-tkfebXqOWr-%7`^Yin}&Q(dnAbFe~vv}RjT&"
    b"P;(&(HbSY-c`V-M7&)?IFBCWRTqsz3~qPSLR8{)Z}={Iwi(#!nIeR^c{W3Xz+f&?vMKFnuBPrQj9xj)X#z`Wo;jH"
    b"4?L?J*2`HYcVz8b{<2ao)?(U0okob~T)bJFU?cGQsIfZ=H*2o1Gto!QXo9Q)1ccv*aM0JDc`tIg!52C3?z|w^&2a"
    b"OAqr`P!(!u;t&MeY&Y8b$55JZtL^De9Q?;T9Vh29^7jH|Q^sDZV0Ib?64A?Wmk+*B@)a@SDK$8ZTY4XLt|K82D&u"
    b"xO2tgdtQ$<~Trrl~PrqNn4inkU@%(_H?c%7pNASuG9uE7f&TgxQ`2Q!6QGWbb6}glVbdo!}4``9O%8J&TzW@_$<v"
    b"y?7%hxBpTwZ^QtW#v6mL3E)+&9cNBYIN(r%httYB-XwVcvyU)DacibS$WWy0cdtd812|kq#N0*WTKfL6j4>9V%sY"
    b"VaZ%Vpeze+o7Ho8C=vrw_@|a*OSfaA12wUDDi;bw9RV#I7ndg_@vGSv>1qsPc@Vs_gRK7qzh*EUUR(tWv0^`sqv4"
    b"#@KpyjT!+D^IfNB4L51_GK~kd&U)O4a#WfdQx5j=7brLv(^xDKytFTLU11my*v!DbttETW`&>GsOcu|YVJ2?Jy*+"
    b"|6G=5_&YUg!*<Rs#Ex>p<zB@anJ=M5V<_k}XAyg!hCF}nF+8?M!P3G%mv=QVX%44|s7Q;jVfwmo<^W*8ZMzWD3?^"
    b"%iuja$sy`FGQ3FH)NkOTM;W9##?gHL~`cP=$lr2O19jKDm2(*D>4m=jTrR?@hbXuqnK4!L!TuG);W)j5#-V<v+Lw"
    b"_fBM*Uo4rhV{2+$LB>}QlZ@J-cN1w?+Q|Fni6xdkDeJC2X8Hc2QqdGB%!dR?29L2BZ`e0L+Fs>J-V!=FJ<Uws4wi"
    b"D{Qf1V5pux<wfMw*clnpbYa<1HLMkN+yxv71pKv}{J(9#q?y69_0j3Fj-1${pv-2J5i4ffr|g5v3t1AQ$wCeB}rz"
    b"1H^2k@u^$vKsqKO%C*CJ`{_bTHZ8MrVc~Qr+^Q|Mt^?;lPCx0y%PXM*51s6OBxF69sXj<CanVyNcBu0ZHR9Cs*Y?"
    b"XNn}wh6Iu`7yz`W5?eP;(KtuX7<p0+4x@5J9L3eu>J*q>1YTX#h3R=O%khp!s!KrlPw`2kD_rC0=0^5!5=fu$5%P"
    b"l8p5tPy1LB7yh3p2aMuw}saWGnx>*m|!Zx3+&fgpXi*g_iv)lBIVd^sh_3N`|sKDwt(rQiUt0kvT;X)>EOs*Tb+W"
    b")(g%KObLVqW1{2kSF=sp9F;ub(rA)?>4q$gS2BcJwO}t~uBr2N|Rv*ZM(Bd;WGe?~s<vBP1P#@k}c1ficf=d#`TT"
    b"C_PHC~7!5DRQL%0ibQVe||bYy$i(`fB%(xOgM*?g%YVa!yapBp?0PoU-voVrCwBv9wrH5N1qJNt(<bP`&5IIh_ON"
    b"*?j#|n~9`uR#9N{@)=8~8KTDL3cELsNjSqe9PTyt*-o<c60=3gQglf4xugTx?UGG+z6@mZR0ZCGsYh<V6+#ml8aQ"
    b"DVfM8?up^~b#bFc4rq@&WQgT2&B^mg3rM@}}HUCG_}!kzk7(h2#O>>kzKV#q;)(ABT>(BoU%0rie2v{k{tG5!&j("
    b"iE_h5WJ5vDKFq9o~%;xvMYU9NQVD663K69%Pid(L$SjA7G#fb6G)0-RJ~6CEQ{dFaO-%R?D8YjRIgFvR3j-%rfr1"
    b"mbtFp%2TM)v3e9p)SR*hrxt-2V-7CrezR=NRCYjnj(5p0$cmWVVhS}%vs(7Cbr1I`*p=<*&Wd)l<J}G1}%FJ(w%o"
    b"YezY1;LlnO=k#Z}s?(kQ6D}LP0}lIeAC$Kv7$|Qrk{135GQ@szmz`I*=nmxR2--V|LOwfKXEkLPtUK6^h{z)0Yep"
    b"QN8<r)96Nu)300YVNrPB)11`@Cy-QT+DQsvjMeiPfWHdD<<HElUY&U2s8IW0MXy&IZi;tsm`w-8E7_$;c}uh>_>5"
    b"N^IBv<m7zVz&FD#}ZPW_;!pL*al>YKCW%KdHo6SYEP){8wc%mA9NZVZg=iOqZm*@b$)C1)D}gCFi<W^dYM->{(i3"
    b"nKPl74d$qw)Hotn61M=C!N%!`SS!a4Pj+-%5>TvUW1m!dxXx#thkLj$OW%r+BrRtRVy4Q(&fr42E$jm^wo#Xh+t}"
    b"Za19IztM1eo+7&QSn7RF!&br!5uZCzaU-ax*o+KieA=_$%XS7Bp<WV<mvq=|wS02d=K%br|q_jSmzY9LVgY5^7M2"
    b"45_y85Y01xeUt%}V2D$UW0h;~Ncq=AX}4x9vA0J9>gW^m3Xd2h{J!T~d)`M1CAZUx{y|CN%OYQLj}v5|=os3uw!%"
    b"hviBs#tF2W5*}Gi{18tBon1(g?e(;riyx{us3(#3(E)u8iMe`-p`o`?BI@co0LpLz6S<B%I4B7uuy*QomiPf2FPw"
    b"6;X9@?Xr5Re=x%wsqOj;5}3OS+KKKsrc5}#ZQrD(eLPE5H_8bl>XA+fCbVHUWxNx4MSYb~z_2hxjeCGtM}iDBw6h"
    b"`YO{&>1C|kRKu<UAqxbS)*wUWsZNLNC0!yDjUakIe=(mC5v?8dn2Y0(MvdI5%YJV4IQtN9heFe)<hi4;VlW+lwT0"
    b"hd@+He$y$Y!pFCZT-^d*sz_WHiXm}Bi@!{tV*gzd*6Y=FNS}6I>=6gpkD@*+<+v(46j#QMG`SGZumvA)v%6~%pXs"
    b"IQ3pc|s!gms59z1gY{!A81_9K<@-F__kEJ*c{mm0WjRFhufTIY}{{XL)5)ION$eay_Yy01l+~D)>`Olmj{CDFJR0"
    b"vrsR~GbY1`The{4AVb{ZDX5_(wKuY5mSHXusj@6T*A3davV({{qiSr4><}<yeek5o_X}U^#Rk|+)wB+Uku?$Vn+L"
    b"Dd5H`2oe*&*!;8W>!H8I7NCImM3BgXWo<0tv%4QL+O8zEcY{W-hw)~bF}*H7fGWi?E&xh^`GItd}(fo!=eOK02`v"
    b"sC%SnjNZ{wIo+d-QK4<qN&Uk4&%!n*_<=U9~^qg*aV7?64pxRKkeuJKE~(8m>BtJBOaH^nmq`MbK%g;WCVL%_0ir"
    b"k7S(@?`pt=NHAYBD>-z9^a)Yp{Lyxci03nrDFkd@T4TP61aSuIlc@olq1=ZUQ3cQqh2rU@car9i?E9rxC7$^*|%K"
    b"1c$;N)8XVGed&m;@OSPAks&0oEwe*9E1MD_}C;+rm&>)fb9lAR6Byb;t_q;R9y!+0{k8JgcoI@-*t-cw!Puk-ASS"
    b"wjx@Xs>0O(KT1q2mqN1b!wa$l<QBh8t9o%nN3d`wgbYu~1f#*;5}YM$DLk$?EhzwT6HsPF16Q@bU!%e+7Hs7`>Ij"
    b"7IGl^j6ZdhG54LDLAxw(eNz#dXZ+MHWEXiiz10mc9b0gTit5<BQIaWIESb4x)wDu{{Kb2rKBvOaVDQnIB@2)GA8("
    b"g<?Ws8Yvycy*0^05pp@=ab+uB?J~X5$Vk?L-)mDN$R#g5RONS-ziH2{7;8I7tR^9bF}|v&pX>h=;7S)>`z>^(m8e"
    b"PeBZXHnSOT^pEEyqL;bp)vAm|%UCVpZud{)&yDA~Y!`cm7JVG52x;P!WcJDOr7KpXk2ZTdbW7oYz)qS{H8bn&IF?"
    b"#wvaE%+7rdH3C5|rNRq&Qt_9g&~b_{`POOx+cfJFvWLy8e4@ZK0wb&J|{6#fP%p?3d}Tut_Wy7&$(1-W^~w>C8o&"
    b">D9DR&~g!YPnN0xRI*+tfX2GE^(dERMQYr-kcrdH71g*|M1w(oby?=9R$L19_%bqSANGZo3ST$hc&HQuF&TPn>H?"
    b"NM5|wjM?)?MQ|9EyBsFxQiP1d0$1FLT^3Cs"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
