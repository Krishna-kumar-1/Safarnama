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
    b"(;2i=&SJN2O1u)scdH@A@MK`@mT6F-#5a@A$sWPomk6}8d7I<J^*H$y-x%%HlFe_IvvVl=uQNH#n0^t^)O(j|ey>"
    b"R=c4jCR@59!(SZ}5UTiprQ7{Z=dff0y6Js+{);r~|8pqz$B&8B1v$t2ov!ydwvPu6imnQ4=?erO$EmXHBsvPI`~H"
    b"g9YwPWLjgqp*rqx&L5ZJb9>hZPagKVr{-c=f5;etLb1*whMCE9xUJWVgJ)wOIrnCS{ZgH(8E~}yk>{mZXWa$XK=E"
    b"Zfx>`hlwcn?zkxfeRTKjawa*kf+s*~&{VqzBeFwXdDogP263dC|irj_KcQAIN2_o7x+xOO@xiHUy2S2s+qUoYdJD"
    b"1C@F&Srm)p9d4?pZXIn#x1+AG-6N8)yELiVOiP<v{tSC~k_jB@?RqcB9zWOqG4f9uKx%`Ywy60`yw^3Y1IesvNp("
    b"4U92rLj4f5&;NaA>;Dm`U_-YL??Ij0_7FdTKqEc7DegRyCx7qe7ywa&3L}owd&D(CksF#9g_+tArmTsoys$5};@n"
    b"U{nlM2n^!qtMHi2C&0I&L&6(shYhm7S)n|E>m_&;RXhyvRv+Gg?L?F-#kjmrLtzm&31xvz}Dct>EsbeKuV?4fL&s"
    b"<4*6ME&hROL*4vL2bMnrox(x1Q=PR22{v8h2UM;fuKreCT2VT$;X->42eX`Q(RjIiB=FQMYFx*H2v0dAKy6fW)cj"
    b"nX;OaWij6ywNY@W*aq{JIFQQ$G{yj}>zZAw!UU5;H=l-NBN+7R8i9DH6mwr%9HTIk^=D{HG=Dip;jVs$^5{Q#r=!"
    b"|EB<&EZ83nfpjVWe}cM*N@j?1dFD-`4BYvWe=?db1HsP{Zdq{#&#jG=p+n6dtCEX2|Q|s*EhjJx~fS6+J5K`P!ZV"
    b"RT|}#7CQ-fgf7+#lnP3eR=QBgtp{0*QGpx}C$*0&&-^{9>3N$^vfBT)KT<`uqM_*kqr_Ku>&!Z2XgptPQYjC2_7H"
    b"oHWudT{C&-G`4m$3A;fHUi0(jF?^CXhJ^`6PTfsxs+Q#&bOwjfD!>LD}zJ6I?P$LwkX<y-TIvYO**e&aoiyahD`7"
    b"|NqHJ4G=Jf9Zb9L!vrA#bg;{%0jGYb1r706+OMW4qB?d6Wd<-UCLnKGWE#bn+^s)JO9bcK4T`L`Ld)owsWt+8_-0"
    b">6@iY`AM$Lvf^R@&cJ8a}>RNXOON(Q@T1&QMWt#yE!(1RS_c%p{h;fWeY2V^cVKpM%W(>bWDRD*B47=xjPyD7b=>"
    b"BaB##W6m0YdqU+G;g@L)A3E#Ew*a$|F+X^7cLEKatM`A?GGXoc$hVDlj#}#Am5Yfs!h#98pwb(dKh$L@*}YMP(dT"
    b"RNIO4=FiXUofQ;M0=0`~-6@|`i4CU~y)6T(B@#kgjF!AVAn<^#?s>A~2=juDlNvn%##M`;R%OPLs79|v5I(6Klu7"
    b"+&kl>h6VY0m4nk~!i#Pu4ypG+a>o~oIwZv$6%J2ju_ElZG^=h>aYU>bmin7~M=*(8?y2j2EsBA|wKVTa(AMyyK?`"
    b"wskj4~{bzMT9*}()Jj<3}Gk0R))%<4R%4WU_8N<yQidce%X!Ry@A<TC`GYIHwCvO<+vlR{)h5rnY`qqKEP~89Vj)"
    b"tTpnA}^szF~lGpo<Y6Edr&rxO;L&puSHl^s@ztCI-CX|&@WZ<&ym83(SB8<#U&Tr{e__J1!&?3DS{kZ2Y?|iTMhW"
    b"!5i4vx+yW#5smX<r{&RL;`+2JzZP{NibV@Yf9&*be~*e3Xwn%j-uY9w1LuiE#T_UMZV9LGV|Y;F`KRr`F$(Pl-H<"
    b"F3=f}-{bgR{u-{cJf1>%SnhUoJPiToznY7e*wQZl4?Q*vCDV&*9nyK=_PaqYR?18?o-!J=A)ruAas(A)4`<E|LGW"
    b"z)%XvZF=R~#6`Wu-8#N@lavUC%F;NusrgpHwaO+|80YqeQ0AKwp-^Hu~gG{m@iBhrS;>ov`sW3>bK)Ip4UJd^e5<"
    b"C&Z#=ps0xm2Pn2vmz4`TIuF%(%8*Z>u@GQ2M)&X!Cj!mga$l3qAiZU>+e_KE6A#|V$UhJa(i%inhX7SktKV-!67T"
    b"&qiDdwX3@_^8D0I(lXT>T-vC4r^hOtxO%s0PK#*@>HZV2v@+>|YTXqL4HyL2wyYO0)=QdA`Grl*yKmmdDqQctRO{"
    b"E}?QlFUp10r9>Hb>3U<nU!!TM;I@46bpvd^a@Ie}B*!B{tgxHDhjq#gT4Yd0W>TI3(*ogD)}zgqGrXEgsm}l7+}u"
    b";?AUqtfz!@@U#ENwP(j%F6hX@L^<%Xf?EO97>af{=B<9oh%5t~v>tfPs44xWy~5so-2fo=i1@6y44J9-RPNmZlUS"
    b"usvP8E8@4zaZ=7U#5+Vnzr)>d1-5(ANY{Tk;dt@|Zu|C?!c=;eo&=GQDTMd_8>EIpVl#Tf)$*lYaX41fpX85)9YS"
    b"N}LgIKEyF*!WwpyRF|3^~pn3$)Upq6hl1Z%^H>@9()seuK-oRDf7B$49t?mPrQUvT425<&@b9MVGXmw@xk|)%QUF"
    b"IH}9E-Ni$IjTk=}1av$?o`S75Z{b=Pft29g48EXZ`9gzAaduzr{UA)0eYKJ06Ux6c6eeUGZM~k(=1T9r=X{t9i=X"
    b"$}M+PkFBSrP#dUN<GgS82}4dFuh@H+|_Yx7-bZW-nTzn6Aw*SL{i^8(uJMf*K(2OG0nd{9*|B>4k*Iw>A7`A<bUa"
    b"innS+dqvG79`qgx!iV^uAcay^#o{`mqp}9;KsZyL9Q7ur;wr?0ew89xZ4hiy4hJ0ZM#i*%9wn(U-;kj0*@r~wn9$"
    b"YT?Z~pGIpOE&W&tB((U8SUVN?y_MRqi?>|0lim9)o-XDu25?W7RDfQ8pFW$kUnWGtJo>)pb?<h~Q(K@`Yj4pN0*+"
    b"`cCqg?>eA`VH43L6=2vw<+!0%xNp5HU9`k9vauOPS77jyubjjuQ*9@aqr)Lc?PQpk~fWhuK23s@=HxK-yBE{@8US"
    b"t6+}-@Sh#Y6&lB6V0mNSTo?DYn+-1HBHIEPoY#&u#GmMpbRlW|&SNGA6-hE8O>UI8m9WXI-86S>bZ8yeCyz`Gf2}"
    b"l3(!RbC0d)$Pe)TTd=B@cx;#@8!IB+)`<s7gP)5(yZx0iSlO!?wh!)LJR>I+?QUk%s1OO|lKEZ$23R2F~S&_eZ>|"
    b"gZpCCN&)vXU~15h3UNE;R5$qHHowc>?H+QVKNh;w6?Ngr(hp@L16;dnr;{4`-xrv+5_FSi-xU4LUj&TuTndnRN&O"
    b"U?99h3S>crqc7n#=EpV~idtLihn(i$`fJMqmjf-Smh!95eK-^y-XmS765XM>&HFV^S>)HPi?zkgca5UnpT-}9QRc"
    b"JvNS1~^T#tb^6@IUKJ8UtT1_a1DH(XliiKu)`}q=z2$ee76N~dQ<(5<t}0K6i^S=J)rWCHQ#N`IX!x46W1cXP`JB"
    b"YLmWX@${WY~a4Kh`YS)g%7~cWsH4Tm#UONGggDp<GGDFlwZ@)VVr5(gc(Qvq`A{e%(D;czFsxef6d1tgRd99|6zg"
    b"5`aVwZmeIkLe~hlgBKv{*4lj$A~y4n_hwV*y2%Rt+-Cn;cv11^i0Yd`F`k<(`Yb;8BZ)oQ8I+=3_FW0(2++uy|#8"
    b"4o__5Fc0!0=HVcfGv_aJ(>F{I@H?>094~(xE&CU^{WlbKL=Ns<ibcMH<QF?_rNtn?5*8`CP9(%MBz{(UPR|wGCz8"
    b"oTc#zhd|E?$kl6K8`2Cp0F__(rZ6mkhgpa<1Z__*{D4Xppm`o>GRlm%~uru@x~9@x#ViZry(iWW0`^kxGd9Bc^<{"
    b"$&(Un5VxVm}#1nk6L<F&%ksk2ubi<YE_(xMONg;YuKOH2?b+Xt{1gqPpGeiD)gD>fkN)WJZM>q$0o?Nf)#PD_4(<"
    b"EwW<$>N#7M0=JM7qnwMTneOsiT1){)Jv0px%DEEDdNL(}8^+0Anvk)^$B@jzFW08ZHY2$Z>%{M@Vf>7>O*Rc?OUF"
    b"cCm<4te}>g9=r|Huau+2)b(3YZiB`l5eUtd0)EtV~N|93;CVSrL*>q<|WC>Swx@K9L3}*Q!(rAoS{FS@uh_yXYI1"
    b"gY5ujhFCOqg#yghNkDkHmP_?0u$?q~s2^eU*9C%mOYT7&XB53)N-4rG>oC^RW*w>(TvDVVGZf~2tE}v&xOtRcF>O"
    b"8))CvjOs+0AA`()c(edRgke!BLS9jr3VLE|?O7^-2@N)pefv~2(eRZrwAfA5{HuUwa<dxcu82x;;+K$8wRkMLa-I"
    b"UNo&cMu@=pWLpmv5%vQ)EsADg+>Qp+Jrq-7M;>Mi?2Mq_^!N6&|e#ee*E|T+D*0c;1C)OjqYC-%F5Bhz8pO"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
