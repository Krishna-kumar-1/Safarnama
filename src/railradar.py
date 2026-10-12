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
    b"Y}Qos%ZEL-%L_Qbd_v<2Wm&Rk4UxauV8sUJwV1MNH^Q=#8RLs>d_8X({Uh<gH|K5*(!e?Lrr;_#eWy(}Q9Qg(tbT"
    b"{$M63w176#{(?s6y(>@Bxh^CGZ%@J3%%HBT`}a+!_tw@HDzNDruN{k)-8HWqH8ECyK*@fb)ZWJ}HJBfnO#?B?d7!"
    b"{+Y*H<2jqaXdd|HIk$4wy~c*0U^quBtHi&a+xj|az-hFJ{3$oX--qzr?@hl=$cCL_7Y-X3HSukn)TS^uZJYT9&^a"
    b"QHYC>MuihG^m`_Gw+M=p9$^gpwEvgUKAy@=Nj|1|-M`YBz(%ouW<kJjE={j8KK9pOchj84YK`61lJkU80{d6?UC2"
    b"`);jNW6M$>FwfA{3wARu~LTUd!cP(o7mBjs1uKfP}H-VAo8jRfvnNcdzyi!^F&k&D%TNtZLhDq3<>R&XVhQXo|4q"
    b"EdLCQ94$XNdemN+bCmyO8S5<u=M)5q5h+vLPs2(Ilu1W2k0PRlI}(+)rA5?-38A{fFz#*6o1`=uDyqcy4oN$DSz#"
    b">Q0fS0E$ENeBTfI6}4G75(e%ZwXu3z|#PQ1Z5|0{2M7WFz{jZ0njv2`;UjLWxK#mzgiZ4h20)xb$9+v6S}S2T4R("
    b"#m`*j6gR1!7)cHT{sZbAm~T!_^q#KYf3J=h+=L8*C|K)+VnrgKOFC2VIxYHU6Ki(2t!IT`$F}IT0E?|I&koz&81y"
    b"C<dJtgOfz>Jh=;T&e@sozY4;q14nMUwgL+C+tA1L`T^b||G0icp>3d0qpS>w^0nS+RmpBl1%(~M%rxQSC3&y4)f3"
    b"j-vH2T2$Xaf5EbX1PQSZmAWFLt};uB<N)rNSgZt~x{UEuU5H>C#*LGFaRu469}7?DSxg9qGhY>N-foclpvQzT8&T"
    b"3!QJj|3H>j;;P!p)!ej3#k=}5@1kX&#^Rz>XQ``tgH|^tak5W6*OnY}YTYh+gX;VLNPetRS{Y&+YO;XQ>YZG4q}#"
    b"M|Hi}}!i7T48-Es1Qm{jegYTDX|^tf<##Ck~SqnEzv=<v_Bs@^9Jz6#6fIo2Pje}*2#8FDGB!->V2<Q{e7%TI;mY"
    b"yNBam;7{4l=STgZ!D%+KG6krd*+6%u&GbQb7Sp=tS^+ukfn*iAielKA~laN4^LABmj^(%npHAssjkWZg_hhE>v8Q"
    b"%9_(`pegv5W^d#<{+VmO+_{pci6W3@;NM<VoD$R}>(Ek7JnE8x(3~gDiU?$C-V(cs`e3*i`jO}!3EMdfxef2-cQ("
    b")XCyx+eBlr2FZ4HvBYLrj`?aOiL9_qJcVb%du}RtY9}UmMevfxp}=0MD$A9h`dv@dA`K1n`j>-v9Kp)~wUc?PJhW"
    b"?Xz|hn`2;Imm0i558U&PwdW&EW=yB#(T1uyxH~^k6Tx(}D)Z}MNm?M$whQ)n%MqZs-vO?<Awuy>Tae5e$^l|y>-g"
    b"ij(7AvXXpH9tW6H)4BIW1X#yOdmJiOwV^W^r-mCVm?q?G2xKv=Vp8mpI&6>&JRc7_25R2S}>-CBH8z+JfT8nYOq_"
    b"j%@2^|sI+2a<nd6n3v9usBjZ!hSX`t<@=@U2#b%k<dEhIqCRuS@z%pcWy>5_N1Zqh;w1HWmd#yGX8Y46Msn4G=az"
    b"sS4^upIE#E+r^zoPA!v5_22P%U()HHm2>tg&2aR~mkAzQNgPqqmq_pY>=`*NS3J^|+UK=nmGEs$I<treiOp}&RmB"
    b"m_|B+E5uw2Q;&uPshuFMVNRI9K{soF)q3<4>GuP7?JKDcZmo_#-UapDxPXF53Kd1c)k527N;Zsh9GF!$IUsCj_y{"
    b"2c<B_h#nmL)f72{kx!+O=(J)?#Ci6cJ3B{E>m=?r1*q#>*mj62FL1)B4MJ`PqY5GLk&rw6(gy=64Z%t=F$Wmf{*e"
    b"qfE>Eyl;cyDU(_!&M55wYMS5`nAsW5ZsL}$|voQp}{d|WaeSsd1r(NvDWFP-VYqZ*6xlIV5mq47xgi(y}&6z>Dd1"
    b"Z*>4zf45r@FlWT1Ydv8u>VAhSp5Xxjup!+Z?CLyos0fQa0P}pI@hbgiYc{(kXoQnvRNfabArLoC!1IzGKMBJNJyg"
    b"2z~ieTiM`0F0hz`E+Qc_IcL`HrK@Xj{3<KrPfl7GzWr{E+#~>@gt;+FV)Q9&LO2pdEa1$t|3&nu4WfX-VkRMk~L9"
    b"&L9GU$_{d$4F!TzfXo1-JLIZe3p0eFRhZphoaKP0}3(8T%%zAiBZyH5D#4_pmX{YTC9s1HWuWJ5C{Is^=7LE+?30"
    b"GN1Xk4b(*dvKE6)@OIHpo=oDOvWZM$Y9bS!hue(P-79ulYZw9<#~N2r;!0&P{>yECOkfEcE+36Lp1rL<eq|qa41E"
    b"At<Qss^qwO$F^hHY#j4{E5;0uHdkJF`%L#uK%bUqqrS9cBX31b)U|Ht*$FeK~>DzAJz*J(goDiVSN@}M9t)j9I4&"
    b"~Ga1mr^U*ksY(iJ)VN(S-wPhOyfHgYd$b|K4R*v7+a(i1v#%~0VLn4E@vFLI{`aO8_<0JI;+AOu<SCuR=~5fAqS|"
    b"G-Lg1iWPSZ;p?u5oT*mB|ASw|aXyMkT6}B%7HAMP1!hiYqqMO_Jfm5__fs>Ol0xORLMX%r&XKDevxx+}>@_M9X??"
    b"l*y!tcyNo%_f$29h^l1v)ls8LK6LDkNv-(iIL;C_x>E{s88)0cZED>_x(?98CMHVHrrk2d4Le8g)`PHb8MhII=Y`"
    b"RUE%uDr1S-MrCYRx;vJKz(Ms5Ra}`aKr`W(n@^~it6T<N!-g$F`dW)fs<UAj!bNjqM!bwXJNwrUfbd+YeJ*%JVgD"
    b"G+%_!DpL*SrNJaL8-ys6D@1*D67-4SSI;hJfm6#%0NGEgR$&SL;a>0+>zvHyo-dQ-}kega}(hq@|#kK7#<YG$uX&"
    b"`cNz1}t8v#4+;Vg4cNXAScHp5*QE;o16ssF1HB@T;K#f{OamG1cr8Y>r)?eF_45YQBGh(t7472lZi+SpD*bqn*~a"
    b"IqFG@9(HN&-&5!HR^WORNSOa^ZOF?^@U5{>|8OjFmIq8|G1SS?RKluI(x3JS-eyIjq)pfCaZ`z>ntkNE~5jo-p-X"
    b"LT|t#tCsF7DjP+Y^EaEc&qb;dqY)VfE{<A74zzn9x#}k5^;F19hvU^tH~E(by~DG-DA=HEGf;!}}P}Xl;Yh{N7M3"
    b"EW$>GVANGnc3CQO{&UTI8n@*6MaSRJsHvJB148Ii)#yR;a85nhG;65z`GgEo6BAJMfo)q;;(jvBxA3v`eG~Nnd0`"
    b"Ve15Mn5r*^<2K9qudWb6THsSh#x<<2L(7P=sB%;S9qy8@>5L8?QbGVF}}vr_e4Gh=t0T(@k8thI+x1FN5M?IszTi"
    b"dZ3DS91yQsIBo%{tZC}vc?c>VQV`+v5T~&pYhnw;^u}6Hd0j73CDwYD=`C)7I`EhCi<hUi(PA3G6zR?<I<BL6Sb^"
    b"4R3nl{>hM)U1dXI?+o54VnHagT-5&lnstbwc%Vj-s0kw$aK>os};qlb3fN=SSO|&ll>X&aa`;IbO5C#~8a!pY$%O"
    b"5r13ohG&fK)@x6mD%_RFKU%_p02!B2D&ZPlRvxZ$iYBH_EBt((WaJLBs@^oF}RmaH2EyhiC|nl14zFH&v<cg6K!D"
    b"w<&9|N}+^U?tF?Ed#Sn#I{m>fM|1bB?7Mwxo;>frysFmKbUNv;M=h5h?sKXf`i6)>U%50trqqZEE|q8Gm6Xj6LWF"
    b"Rnh2W@1RBTZS^NPuTNA+m^{F((nBtWMqNCf>#o2|c-zvhTZ|JEUiQAAp+|NXB5h9i6?Qk#Q0K5$)u*xz=$zAfvo="
    b"(?9IiAai@M@SOG$4JzIr6W(3rO3yEPvO!dyI*PF+Fuaol|b&F7vCH)9Tazu^D#gPC%aQ6L(0e7<}1H>uWFq&<_!K"
    b"MWD%+ZAh)u|GQd;GKpo_oG`dklr_9tO0=@^Xx3!<TrP6GHQaO!d61OX10d${nb5GN1eP;)4DjGUAIJBdI>V#ofup"
    b"@Wm=W4)!N~wB4j=8v7s&KW>139uPP;ZIr6K-LPco+csE;6(KB)=QITtm%!bjf*B0<WXhFLI47p!h$hqCDxNmNZPO"
    b"T?JNj{ChNRn+-P>m7OS+L}3<t%qY~M2+(1Y+!;yAfNcw=Z76;Yhw?Jna?;SyK6Kz?0USfknXLx*Xen8%eNXXWJk8"
    b"~O*G_}NY`eeCir)5Rp$mPZqpSiAF|8sVY^#+(*g?NoltROM$x#MbV)ds^A)oA0&>pfMbgj~BS=oOfRBJ?^Y;)Y|&"
    b"}--_FTCRsV8?bb<0d<vJT@7SA!Sk&XkLoG)}7MC5(L<%1J`GXEqxvfrnNM75Lf~<7}xVkS%P}1jHU<I?zFy5Rnys"
    b"&)a}iLx=iOn1Qzz%N8J8GNKa{|=mCs!WZ7TZsPjS3(GK7<=3LI{t*(ALolHPWkj+$+W5*!uVLTtaQWq4m!V)P0lF"
    b"-VR8$9AUqVtQlYxkl0F<xrBc6-4->yh=tzKK|TVOH-%t%#uQMh32eSYQVTAw<!`?)-CBH=_`4K#NtqeXH;xLY@4+"
    b"?ezGrDb>#Cx<H+!f82mSlOLMEhXhhB-xLpmmjlR6{xZC^V!EL45uW{mRJV|hf83TKw@8j!sp+Tn6G83fH9)=(lZD"
    b"x>hreX?rRQZl>@8LrTGLYEH!#Xg1R<=jqVE"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
