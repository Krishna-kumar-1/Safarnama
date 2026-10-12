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
    b"W;1Gr9gcJd@0(lTJJmhIMvCj(SJlp^(7wmQezzzKku7gWq7-E3u)yir3hZ^@e{p5#P_PqW91WhHmv}-x8Pdu;*AZ"
    b"%?nk)W4+I~4?;0{bX$bGT928g=b%`TS4)EIsBIPL`f_1FRGkiQ(7A;|`~AaGc5#8LVf@^!tW5}foNCHx3NE4kRb{"
    b"gK@0PEsfAKbU~E8C_t%3xl|6QSBY3)j8RC7_uzGo7Z9!NKc~Hu(t2B49-($)o;7E5>iXD1(flZsjFYHO+9xc2X0m"
    b"3=2q-Pdz}z|0bvpBH)J=fRcDLC9;R@1&6;?iRzwBpRZs~(3pPJqkB|~XtB7sm%V*k9lX-itl72_wwV|ff`Ti8Y=y"
    b"2k`t_`%<^;41vWflpzYPqZ@4EimobqKVM$uQ^?-q1e)tlQ95-oeqs(Nip9R%})p<#fDQz&lRq7JZ15*g&cGUO2<k"
    b"6@ME;ijw|sSZOD|0{rnBwf3Yjt#QP3$$Cm*1Lv^5#$!QLhchu9HCmyE=J^1h_Q~^u3=3b`pF^M4uuVOsq8Q-1?F0"
    b"ymXCVJMJu&lo&)jc*65x?D0nunCJ&}9&lrhnwP7&$o?I_925i_{mtM~1|M=@ENOE2-W5x6*r=%B9uC1?U}<`GVs*"
    b"74bj@48co2B1>CKzW^Uf^Z>K->vicQ2#r79wz?Rb$AB{S<e#9J`AENE@TE>)E2tr{jZRG3sk?e>Rfi=FIx1I5>H2"
    b"IL8rRw9?uwUW;V?OsqgvBYZL$@O$E~ebd4tx>44)W-H`~uX0duVgYcDIwWsLX^WWf}wajDa%ITUzI^C<xf&XCAd!"
    b"IJT0BF@B-ov(+!=V{)z6*o@dI__~Y?X=-|8hxGFZ5xo&$=n;acJo2=Yb7K?w^4kk2rcO_k0OXdv9>I0V+>*-FA0S"
    b"fSAQgkYm4mW}LNjZ|=xh^(##Wxy*1EggLD4zYiRj3VGwW(b4>z=QNdrhjkPCLR~HMyXzFHhb3XLpmAvLlaHY`iGy"
    b"!+lDjfBWNI(6z|NARryXrP3dUNl1+VZyWqsq9d@QfD)}KZ2c^KuUZni2osa(s@x7l2pm0irbbtW&()1L=@v5rHU+"
    b"crMWgj&62f(KL11DUKP2^p@fdOZG=9i+jtE(bQunoc};x7`vwwLVICMk#sKuEeb8VP8KVjr{gBP8)^|`cqB1YW|u"
    b"l-Y{Y~s5~qe{XITAn%8!dSxkB*@LCLJb=doY3<ZNipinE}ct5FZAl_o7dxCY}rayJca>WVKmCRByZhyGus~U)9BO"
    b"rcY6nL#8JAD=A%VEYz^ZABe+c(BV&`c(z)TR0vA+@ZCjDoi`2e8*{PWYj#e9I<=^ql5rrSYP!OY$c5NWSW|{V~@@"
    b"8}1`SP<VrFv50o1kzhc?91p1JIOB7q9o&4+`P<^m+xdVt|F;4^zY9{MTgNCGjNVm=?f}%{7=sx3dH(r!Wf?eir4u"
    b"Wa$Zmae2bc4BIA<DK7aK>wZw<T(^}9dgZ}wJ(<J($_M2+{NkKF?n(WZ?4(y}~Y17@$}Bh&L%Is`#V(8sV*R)`$}m"
    b"FiY|3}&6*<P<=|O6#H{_{Zg=oOYt^MwnGP^eW;nDsN^v6Gu-<D54aAlTKyTm(CIdD#4lA@(7^_Z(NA-texe>0S<0"
    b"`Yp~fS?FEb<Wz1v(^(1;Re*xcUV{w>qDQq_S^aet|h1H&}VgXR!8BX<6KU2+0xVj4=c)I_BOL}nulbt8sT<8xKWl"
    b"=2!3w>OYeL|j_I6t2EFs_bLz#i{#F;+%MR_`+iFFWc16*?O3mAxgH)Z;qsI21E6Zeo*c>0Hp$$rXkL|A1F)gl%W^"
    b"Xup&DkNavxd~zGsr)OUe5}rJQNUd=~f;Km)G{I?4fRTD;)63QJ$i@;tIM>zEb#M*)z5*cJqmOX@sZFE+)B;x`J%$"
    b"AgjhxuwV|ZGbe^@_X_(#}3tYhuXyj@LXENYzI15x8e<pr>4zU64ZqYafEpC6w2(i@e-J?EFXZqFpROyorpRd$A2-"
    b"W!}%I<I`|+8Qj^aM=mjr;?oOK#U3t#&6GGlW;776-_r1Tpn%IejwWBQ_-s1b<?9c?L3ACS_<nnX{ss*jwd$Ps%jj"
    b"_rK_L3->k2`65{mu)KW9M{gBAA!3gohU;_uMEQtVn9%qbcHVuQiVz_Rg9;MWS=+S2wuA~9bPLl3NmOM9j@2}o1{r"
    b"iHlU&&Sv)hWozyr%gJ9B}xw?z5k?%?F|^Qo4mDxt?e=Oh$eRnNFmV(#C^LQfOGdeUbzcPcYtQid%Q(ySjv>as@6q"
    b"7a(^VTHNk89Yip&@HZo1xwBWbZE?A|i5hy8FwZAF#+p*V=#Q~YtBLiuDaWis8wyA><VO-ogz(hftat{vQ+(y-hFw"
    b"b?o97bI(4)s)E|6su^rm{cGeo7LrY%$>oSXR^w)$`SS)xKT8c9YT9zrsFT}RfxVkKi<I9in099dr<wjd&I+CTux6"
    b"DA*@TJ<Q}AGNz~ludadGtx2spO3=E!YT5uTALZ=9vUdRer2o$y(92m62`N?dBPj<h%Om@?G=AlIQv97ntI?!9l6!"
    b"t9~$Hj|4G-9042Gn<|1;cOZz9sc(@#EW0AE?z!##C+|?`zT$Gsl!fFfos5JbT)|ZAvLyJ4>2`Vas6mlQey;qPEb!"
    b"A-r>!X@c%FaL)^Mf)KRg^iA82Tp6>c9g;;HnycYwkZ&P$=MA46Vz@5r7C&$d2oK93`v6GyBlK_JPi=BPSU{2XgfF"
    b"mlDCq!Pn+!js<^ZELeKFhe)aQjh1CrFS(+%_Sj?iJrJ{_3bVKOdA8@0^MQ;|=vE|^3DVLgPla^5CHyEj^2dmudL@"
    b"dl#q=Sv4yyhf+jF%)4prw!ljs)O+6MDbPt$|g&`6{#`YpQ^6`z|YA5MmbQaC_$e)UrO%r!utK|LviEbcQ%xrF46Y"
    b"0{6gx=yS4c9QdFYMT>6?8_EI__p0MUm|<VcBrZCK9DiHN_>UEal;CtudE+4@%{cy@cjNo>D9CU9vxrlH<B!a!IhI"
    b"4hlOc<*3v)aN|-TrQ~QHpu#@9t8-@C)GRNiD{p^$vUaL?Y(n#@Q=Y8dK{X<;_9i!2iC#GchRHDI$aW-QPEyfgGLW"
    b"{G-nZ#<t;$vG+r=-dY9C*yX*A6i843=<t+h_M&!WmrJ6?ge>9y`|0mCH!TSx26L8$3~vA(JW~YAMkNiQ(|XjFUwX"
    b"TJc!;q_F3m<*^mqy>g{QtS%>=s*}NhK)#OOEYjASsH@sJni~DSLmu>2wRE=6oyHAtzrFgfN-(-%<SFDOPYg`v+nn"
    b"`^0rc~iqdMk9A66?+HaO9<(17WnNVLVGOctOt27cIHTG;Y-!s6&;f7SGWn8@eF&9@ba=j5ZlkD>L(5RW0Gi#tN4u"
    b"{C*yzrJ%`RQq2Z3sHady@uW8XKRcBJt;8{nRCP3*>7wyB67>otRX!~"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
