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
    b"Yx|BCLFK^#X;B}~Q2h@j#luW+yI;Ofw}ZJZbbU{k(x7`jFQ(mUaZYLNw4FJ?kd1z}eRnFHK5~55eTIJ?$_e@0&#&"
    b"8{cJS9%(Ul35p&H;iM%1QPc1HIZjmT2<2J1l~ry<1V8#7z)O$Xtk|AI-Cjk|DNp4w|cv?`sI7`u_=$~vBN7ml7iv"
    b"E}Sjp(XspM_m*GTD`;U$QgPc-upnkfKAuac(R^(ryPkJ!5v00Y1#vKsKo}mLM0=tk{M{=mbb9?gWi;muZXm)+bXZ"
    b"s0@H$}U_L$GP456q!aY;&wW*Q7Cc~A_8JM(sAl0%DJA_(P#fu<4pe2kHl?6^?XpA{1seKiR)-pfTWKQL)^sd?}lZ"
    b"e|s$G`R?pTnf)r!q)*kb3L55C4&(Hs(>M$QG>vNlgInK`rrhFDPY*j0Eei#UrJ*PY*J_1aZ}tv755FfOVh(F}uNY"
    b"WT+PyzCrSMG{#g~nMfRRWCml)CEI?8&!0}Pn9a<T-VZvXPU;MRMAyY#n9B`On(RZ%E7BJ>V!v$tHht6)$6_oPaFW"
    b"XmmG=rgZPg(!an(NrO~X(VT=c~h3>%bH*!=%d@EYo#Tz%^1oOD?ykn{GA)^TTace+xN9#s=8_IvRy5-NyYksEJE6"
    b"7^xr2cJVXk({>!2(t+bhR5&fukK4N$ynxkdp3d|WUoM^oAOwH9*vcKNAPV}x_docj;7O4?^Q2;FZPSwRQBgzX#0u"
    b"Nv-7qzz7YWw3o8S3Ri~!>@{7L(y^8vd(a-`C!4?e2T{Tj>M+p_=qW=PS=YZYNEIL|p3uHzprNqVeIjlU`(lb_SQT"
    b"EA5=E^=$dkxSGd=Q9&nnEukm(~xa-p+S!i0NELtqKE5hYMZQP@>`iwH({#O7e^uE!>9=DA*px{9O^yDkf8+#(vjJ"
    b"(&HIeI(RT~{^bb1SWQX;?C{dw<j0WMHq;Oevr}Ob3ie$Lt~!Olx$X<zrk2TRw4wDYy@u+?M=BJg5a@@^XH{3Vj*F"
    b"F3qz4}QD!)&}7NhjDp6N(ShCKeJ@FJwKmLGMTC<?V;)5CY0mb0}%y47t_xZ(e(UXo8WnpGBur173E-plz;D6dj+T"
    b"7kxJ;<A3Q2&zf>`s==c^8%GsETV)D{|m|~N?Y?XGP2PKTMFdcMj9W<;^grc5|DjXpV)p+=ToP&3$cSM=hjNeHs;f"
    b"3`DDGx!p8KZo1B^a`2$N~&)hE`XtO-U{^x*INjQ25ll*QgBpcI^oP_%q6W_B~ayP=CfM#<z3If7l3q+ClLlwlxRw"
    b"3}r!i?}CPXWyMr=UCmUbtL(ru>Wc;(VLr%sWg9MR`SbZyNjy(RNp!MPyzx*SjC!L10%=*Wk0gUc*!Rf-V6i76P>T"
    b">5!-V!c8GNU^YH#l7*ZG{}o^m6{n$V^EUcsft|}inhoJ*F@IjmRQ>h36jY_iV==E87}>Gz{^005)czTYFy^e#Tpq"
    b"X5U0}<Ume~$&(>}ebu&RcF4vNIpyKQP=q1J->5qTQYvoX}_ypR`2MlTe&$CJVmIt`I)UFCFjyN-<jaWrR?kErIDA"
    b"|Z&G>JcH+^KPEsorj{iU$3wvh@tur$v%nkv5H_u*>X5uQ#6|sNLjNaGq_ibeLs95XjznPL#YebXvs`e!~#DLaD)|"
    b"9lQzL0Ha9Lvi47V@$~kBy;3gFgteuAj0}hW1TV+Ph4@L=zGj~FdO9p;Z2_RwfBt))w+}R|1pSrM1SKU=uxP)~^Ao"
    b"v|ME=b^IQTKpy_o{fw2&{RSFsmL2M4;;o`cHSk%vN*GS+=`Kt(iDd^$=RX$y~@Wwd~(=KiHcGCtc=_fqG6F+cob8"
    b"L0g<XJJ+0<-$lxKalmnk0oL@ua2|5tSFV21C$2iKOgtQ|@agj#DYnT`AfkF=e1|{x!4+AwAkOc-RdOVCO8>6J=`g"
    b";iq5O3mwv#57X%cn~BuX>Bf1LdS?j%gqNti3q5HR)J=#2!Kg|W-b<{_%<-A-s&dj6<NN}#X;e)~Ei6=3~Z65f=CD"
    b"L*|VIFYdHJNGk({;_FD_GkYDYark40(Hs4I_H?&%t<Tng8+Wl38o~e1uuAUq`nk<5hd3~X~c3c1Q)&Lf*TRbI`@f"
    b"AY(FM%o<L;KM(%vYz`0Qn^ip`<?!3k<00YxpJLfg*7aB??0b74SUr-0PO{RWj58*A!1^^4;P+C?&B2-daw4KJ2NW"
    b"bd0|5jK-e+^|8D(oo-FqY@`eVByQ?^cZ6#P=Oy1;R2xp=<}oiT{!^kYZs+2>Ma&`!dHso)0i3iV^qz7hFuct;fi#"
    b"fv(G1p!=M7zi}d?7t7&7h;rr9AdKB&W$3ituLo1xS%WW~+N_=51onItiX)DHqw(LR*jgyzXMh5|m+j9ee6gt=j>J"
    b"O47&Wd1dzllHRopw3q!nuiMV!0Y%;75DQk%=LeYbKX^Rtzm_BD01K*`<Z!NpJFRUU72^FV4(V<8dOjfpD)Vx_!It"
    b"+A3L10|iJzW6H7YoV`bs}(ZwVPXTX2Dc-wkd<L{?Z&L)m$6&9_|`#7flj%eY+C9Wh%`s9*9WXD{8wt!c|W|O(PTy"
    b"8phFmzjCg~Ngi`$ZSCNsnDe`ILX*({Ctt0+1G6<Y4h9i)N2~i-B9p0{$snn(^#~Do*&gZ?DH4N)!-;cbuOBD0Eue"
    b"L=o6Q{AgFP%;9uNK=fyVB9T#^bPb)4t*=`)YlfrOOm$>Xl@;_~R;i>$@kgUrUYK_*YPD!a$uE=zZqfhE*63C^<4l"
    b"vo$waf!3Q?Wl+-7+-`zatw64hA@MW@by+eR^@Yb)7geee2l%1#z6Ya0kk1lK0qXYjqK~eu@tFWXDHYLiC_YnU4Mp"
    b"51*Y4|`@PoDHmBD_}TVYX)+*DYIvMp;|jcU1ITp#ts578XBRPGK;PKk^0Y_o&EiTT4$gmL{=#|M4@A(f4>=33App"
    b"`tf?kAny8$4x`{wdq7RJ5m6vN22i9M1gWoNgSfeoJvVlNM8;yRdSSgF!KSd)Q{Z&WJA=;!(#CGA1wL-VP0rxRMC%"
    b"2M;>t?#kN(RVJ5nMS~8+PqYjg5MG=RLyaeU2R-WKL@q8dE4+T=Lb#;Uxs%YX|$AHsR&jRFnro<ag<J#9Ctl{m~yE"
    b"><H9TmDnqcf*9&Gc*UV0G0306Vkdq;SxI&ZyS#OG#2nl3ylbdoGGt+0d1J=u-O70>TBl5FZ@o4%ww142uklG$#l4"
    b"z&Hirgdj?)=K1I+)0TU_?r(l}nD#;0NJvFRC+a$lIt`Lu5WGe#19;b(tiU7bm^q}Kdf0X?X!yw!iWazB8>J$9V(7"
    b"4&jJ-vRivVYk;St>qBy!XeBgA@##bhnaEOrgA&f9vTso;*Xr}bi8YE>*>(u~!6k{~v;2=a@;7%-}1*W4<vOUR$La"
    b";xh&dK|L+M|Ww0Kt|_Z#wfZ%%(OXTd~-o}3x)Q8!LqM!=%Hr7T1}}QteL6$`R?8_5o1U`XYpP%Kdpq`!gKT{YkQm"
    b"c;fVZyKi?|Ki&>QZE&MM>*65fjwSjrXmZCPT-QpASEsJ5C8AINE+%bfF7W0ej^>7&*>b%-*9N4m{yK5;3F(^aF)k"
    b"r_wzL$fem3lIsW2BRn2qyca!3<9rvjC24(>9(HwBJUxK;*FS+@%6C2@aj!@*Nxey_;1}RKTeKUiBMZPxFlxQ)FY@"
    b"rDyl4$=YcUNp9iOMyk(3mK7lBtbgpA&5)5$S4%rEuGEIH%kX#wkuIGuN8xWjqJ~6sOTiN%+|}0{*-fIuv0JgcT>*"
    b"^jW|4rLx7DQ!9P``yiLLXrHu;9#x}!cscLzVI>9ddDvH*gKL8q`jO5=+9<F6ksgVcijp2q_Xx(=j#csN!kO|KE4F"
    b"V^F1S$_z9au0hT7JLvlwZMP-)=QFBuDZ;s*(^+DOc2iMpwlqR@>xDg?|GT)@RrSpHunemFxcl}E_-{UkBTqFRc*%"
    b"v=4?3%j-+KgsCAmqHCQg5BXoy73sVD3Z-)yo-3I4b9}+Mii=MSwKSZI`0fg`{-~pKJR6CO~QWo8j-T37rMgCM8e0"
    b"8q42B{F{%&2u<e)x`Xz>)l>BgxSl+qRrL`YEggyz-a<Oag4H(Kq%MYhuAE?%w8?ip`@8FkQqV1J8^+5u{NJ?@tHO"
    b"zIKTtYmS`8GN>7T)?p6)Z&-{kOD%z6f=F~3lPD7lz+ZwvagFW<$7kI2U)-L?SJmRQ<uQa4N*qVt(Xx($?9)jbL#B"
    b"%0pHU@Sq<IToAQvVhEZgIm5&2sr0{lg3bWLl}mw5jKz#Rvac_^TI;cd)BMde3UI%eB+45;_|kuq#D&=RPCse!sIL"
    b"@WKqZKG*0r>d7NH-#O-_v_-7htSZqJJIu6J=m8~2iGv?-DVZ4v6smsCz+n-Af-A7l%ZQ7ozdlVqrt2Mm(&X<zxU1"
    b"A#eVfTm}A_iqb0E=*-K--T$6BUf4S=P;{f>@c*UP^b-@H}{b!AjQ<KiaS2-8suIYjDlRFk$S2mdD#y<C01mJXY0A"
    b"p%5@>hvg&ozDq6E`_Rn{Z2qIrxmjfoJ#Fkbu3IQK5<HJFqEpi~"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
