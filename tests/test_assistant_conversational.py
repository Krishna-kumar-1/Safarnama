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
    b"+v3b#hx@WU25#Q@Ikv4>F5R3IytN%Rix7~DpSTfn-CrgtNC_R7+kOflVtj|>-!aA^JqS+io7NK>VC2=GAl-&jw4P"
    b"}DkpIM7gF}8JZIB8D4YpY<J1RK=Kn@pI%ZCa`n#o{AnVx3_YwO&w$1f!Mb0A9zev2iZ0_Qx-Y>tiY-ij^bL(F-)O"
    b"e3#%@PnHe_=T3;zM|*MY7P3w!(8$GLGkBTx%OLgZWgEX16<v-9i`Nn(%%uB6^xoCzRO9EWeY7iz=x@C3G&eyhgUq"
    b"5F3i8HF<1W_uu0KfJka5r*ZrctHZ;U|F32bU5GObjZD#Z;55tvwphl#cL;_Y8c}iq+1wE#fbtNxx^<-rY;fUc=om"
    b"eF@l4;+4?C#}IGC_kWz%XvbkX;Po>yAzh;lSA&oN||gY_+=%(fF-av`PFA@p}GaI^zQux4e#a{VI$A!Er7F&O+%Q"
    b"H-Bf#u-pEaZPT#6HtGHWIrxF|jgSx_;|{yK#`;{cLGUD-YpT2SuscD-YKE^^7;_q9KGDih`5|(4_q1wSXnSJ}q(i"
    b"#xGF9oanPRpp^m&YjCFVB+vTGidM#QHD7kAUh@*9#^y8(97GPaGczBPapk#qD%Ywyh_)V;-$=kj7G^c=2+caFEig"
    b"8A6gb&kio15$DrNbDn#>sA4%M3L^2XM_aT;q>=cbCm|pqolH)EEFAGE5pnP+8%rw>Np7O-cqUN=A~zy>tU2M{~<y"
    b"3>IJD)6-Pfb(bDb@_%6r*maZIua7h`-riLNvg`>bq3a3(&!`n*^v<k)fioL|#X9F8D_F(5vTYgNd>D;xN?gA>Q4?"
    b"W``@ef-H<>^ScB*f0T{T&hzyWwg&(uh3SC>NRwO#q^SWoI>G%kQo+U<J^XqJkU+sTo;wR$_I1N%L{c)>)o!OLsjG"
    b"0BoKhNzdd@cD55_I<_!XVKAsG)JVf$+*uRqmOGTLiL!UAqcv0x;%^EjCGLbdUjV;S%2?x5n{-*0*LF~CT~<+T*?v"
    b"HHE?&5?9c3Oj@!Fpclbc153J0w(8_V@J_53Js@Z4<KT)^?@;hg&EYg^kf%%?8Btk^0T6Pj!it1_}oln3)E#cnmgy"
    b"|`w{&&?G+`Q(*%jMb23sl^hSp1@g*qZr}{5v>$cNh|Jj7kqY6zA>~Ue+=eQlGJd_8=(|VZ$NX##;CUxejYLL6pDQ"
    b"5<(Ajb`xo+@!Hm&F<2_DttR)Pt4j>4DaEj>+!&$QM3~h)Lpi%aAjG>HSV3c)?GYT!$j!GxHJi@@u3@;-@M`#3+=^"
    b"?)3Se+BdA*fQf$Xr@qBCUyX{^boMcpa78c&=1Ms8S4Zl@VNJ-HE%@n*3n`ZNy_AO~e>6YE<0GR%X|!c{Im+p;?i>"
    b"uZ|_xIyddjUB+{KumDWqgQpF{%{F_D@#Nwcv)P93yG<X8783+k5w%_Ie_>Uv3_Xp)`5NP~Cgii8&3E#)45osoz1g"
    b"M`gtxcsMNRFU>tXvwbj~iXG}h7WLUys{56W`|f}e3e+*xH?D>nD%${S({<#ds$B%1<LmJcCa)LH!%pc&k*kIY4yY"
    b"k(S{gcncT`OpTj0j$YF7+5M=roh|9@$awMS#jDJ<P%dMcr<RM$Jd$h5;1!dH4{m;C5D|F0TotcXuKil-6`}xA&{%"
    b"EdtMc}3o~YpV5Y*$V_ZN(zsElm=4X>>RR3}H8Aox}pkGl;54+P5LuPSREf_gl)rg~1QUAZ>9v-ka06fw#L?Tupc7"
    b"mMYrL&>{uqP0sH=WWlzRYxdd8(hWU2`9hrc(sNRSugjpq)hLlqp(OzA|R48!q2TO3k9+ubniWdR>6()zQ4S^r?r("
    b"C`C)#8@3wHXl}WM%Nrk>l_X~x&2GY>#r!{OJqt@$9a6~wpyZBw<*G<Dcy_Ch31rI*V2)Ezp7}ST!%a}z*H<bO@Ps"
    b"%Tc|G`0kN+)3$6&wCt)FMQBLE4Q8jBfM%wiGySnk=b#g1~^U^W?Q3wFvC$26&Hryf&|&Q<|gnz&rwdoBp)-I?ujB"
    b"i^NjK1`<KXLnROhG0$5$QIz}4kjT?k|^zsok<|5jthJ>-K8C8YNi^%&-FjVzB9-?&d`*y-U3f<dYrYRDI0<x#XBK"
    b"hK<qKI-H4bAw({F5!vBBWEcYKHrCp;2^eo<h`=?`eHo<O^FzO-=dt8`a9*;e!ezLdu#exqo5B?Q<KqT{`<->j1e`"
    b"$}IDor#~Oyx2(rfAv^DJ6lvxfW0"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
