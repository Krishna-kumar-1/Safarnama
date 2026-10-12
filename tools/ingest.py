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
    b"<}aOtp|V!h28N;>?1cEUCOuN!m$rok2XWa0)oUvX7=n(JAKJ7_w1O}QlAH=Jjg+oL>yAtmc}<sBEAED)njC$Mzh~"
    b"WfNOf&#YY>t=MJ@HTwna`+<_(uXwhMO5-zla*P8h7&C{YYNea8$fQTsj`fXY)deStW$*9qWcRn@AWfz_LcCrbK{="
    b"NeQlMnwL>z720g(7EuZJLH&rijE*-HK)9Men{854=-j`T^CkI^cVIuB5?#_S4}YxlVDYC(tt_nm%ZKm{cNmXbrfI"
    b"#(ayfX&`>#y9=k>p6J+&?$Df)IfOoFMvqRB%HO!ZkDT*D%j@m_GdSll?AO0YA$&E{mC%iJ~ebBO=u<GTs=xnkt0?"
    b"0TRk@m@K>(QU>-g03(bUJk`g<@Vq$GE=%yZvYT_Fiy~KT>?YEJy?m<Fa8zm1G}SyfEJ|!K)gQRHbLzBGCg2<(r8y"
    b"6{YA1q~LF&70tROL|<)j=b?i4$qO{BjAB~u`J0NGm<(Y}WgRhBwzL&9E6&-cy1oMaMUQS%<S@D!cVAAG^;+N!pS+"
    b"uG)gT;MUv^5*ZUu>?mZ*AKesN;i$LZXeKT$x*1#Oz4t?6FBlS|i@I$S-!{RR6j`<Y>nSxatit+1y@TF*ko<pR8rB"
    b")gnCS1lSBgJld;E_$85NV{0Ks4W7Y5huX&3UXhmZ_`5XQPY}l5fs>j-VaVFZ9}?Y3ee1r^HI|dI2NW`#J6TTeHo9"
    b"M`sY9EO(PTcp9p7Od15~*T`GKYb{Sx*hFD9tvur3sMkxm>&M9>?g+yB+x{kl}5&V2nVc;;7ndef=o7V_L(dm@z#O"
    b"YeDG<Rn^(<ExT_FUq#^x!9gvxgI?YF*han7*Yav_3^pH;dA^(yNR5lC7p<lr1?OzN&dE+G=tn#nfI2Ktjh$T^#G*"
    b"Zmb?H;~67ryrepgK-+V-+iMsgdFg-C>Wmg`yWf&iz=o!;XMY};H;DD-RW-o?W3}T;ncL|*N}a8~9yD08q4;%c3zZ"
    b"zNdGtw82K<({!Z`0%Io$93X8ZjYJj<u-)h?p7E*Cfa;A3kP>lX(L-^Ma;_CBiu-#{JSK2d>~Glg0alm0x8R$WEKu"
    b"~I^ScY}6QKJSU|ubW;IaZ60m3>zQ0EJn;5mg_B((<C&k-Z4H#oGl1X?OQ&0cnl27S5En3Z{<Z`iQS9II70tEpCZh"
    b"mX>%B9coE&SFWBPZRlgJNx8{hNb*}wYW=%YKk0+W;M=s9$?-;b(4DWF`Gr>ZK>BPON#n*aHT?c*CE*8H`2|N}sFP"
    b"m3$X@!07-rCBostF)iHqmXTk3$44ByQrFv}&y%auRU!0J!mT+wf9-1jNt+D&)82@U;R%-NpTo<4hk7d?LHmQQ9in"
    b"v+PpOz{7LX;xpCaq;Qh)3zWU;@|!at=AKLP-0q(N^>hi!{AwO?6MZNaiHucvC#(IFTjXMJ)YrM49~L2wuC>;_#P7"
    b"zez6eOQ-?pbTzpy(t@m6fOgAu=5mkY9+j;c^Fh4+jRZ<MazO{)Kdm9Ku6EzLYw0!Ww$2KW44j<Cs<(lyC!SS8T`+"
    b"t0onELF_=KmKOV*G)o9J!#TY0eF0&(N49nrt;-;8Sv@Ny|)SCy9?qU+}j$8u5x8vVNEdPZ8r9a`%dwiW?n7z{`T8"
    b"jU@VM(BD`=A^rxzK-7(Cqx>We3&iA7rQa_5*?^4H264}>o{}CxkIP(>>T6yStwkSK^X2VEch--tH-pd42VtxM8-y"
    b"6cFw8$!s?i^R61qOR)C?Ur`Wa*utF?Mu$Qn4Yt<|!$3)mdB2Qn15l6RURbyGV!^geI+vs1=K+a#YXv>Id#<p=X7Y"
    b"Yyx4QEUU6$^{|YLw47CaTHDP7U=UcfPpJb}5+x0{@3+qE^q%kZMUp@Er6=zvL=@iRS&x>LeGE;Fq^#YG$v_a~@Ex"
    b"BLsiKM;XzTX`1&4s(8!O|^nVA-iD8!^*KB<^nhC_h=RuXh{BK9mEs+|FN1-X}lW(XHXk0?HK6?13U!YWBfm?*bjw"
    b"R+-)4hD34TwzU`%kFm8_c%tAkiMH=rrPT*4DTJtF{xflhjMFBFIir-x@9I}PTZa$Z)LIgwI|RshxkIcuT9o{d{8U"
    b"o{1|m0_{_gtMWWEh5n>L72zNXnDOg`?X}TE<AZt6?FJGKbAPvx#Z5t@e8};BG26K+Yi!akA_FqxvC*+&npgI&~*D"
    b"N~7AT~9c-HqqweJInJW^In7Gi5<AQ{3>;mz(HdTxxoi<jn)CKGvMu)&E+Fq)q|)H3Npzt8sF0odRN=pp;*qE7{1+"
    b"{9ryhf)L#37f<5$@msV0XM$8;<=KFQMU?qG_~>J3RM%Kh#ABh^e7H5l`-rdBy)|5D;sVy+AZ;v6c+p$u6%}gKZ&x"
    b"4>d`9#F*DocU-tof2f@b0)!JGy$H9+6<*{imEum_KB=7Cr#!ZfF7x&U_!o|jYS>FWfsTz6*Pk*E&S-`Eit_!Vmhm"
    b"?&0c=`cxZ?hK3ZJNx1Qdut8xIeSs(m)D@ka{ucT%E{W>AJvybSC%eG4i)7)^k@|lRgKC=Y6DE(1iEIDkUPD;|I}T"
    b"neCdXr0sgw>*V)tZfTIB~uE(!`DS?j~Cb=bt`)B?LLBL*7ji3*rd$%*I<}RHBc-~NGihBWtI(jgaf2zcFC*Ym((m"
    b"b|3hgEh4i#asF@-D5fW-mZz2tg!n_hpl1h>SA`w5F^J6qitU>bNEGH@0%}x?fE}s{EJxKc~8;dYeddD4Dec@`zcQ"
    b"NLs%0i;zIt;d2ExQ~*ZnB_XUT?kqL46g=BG<0&uP&YizypNcj2RNd^Jza&W;k!hNxN6Z-R*8M;eRwYpdWh*COW`5"
    b"cP`{eP+^cfjBR|U2wQ9i~PUD^4Wdr%{t-uCxd*EU-+g;^@lYr|pwSkY#bhTcAEFgNP)#rwXq?jpr+^|o};M=z5~I"
    b"EY|Y^u>=5YTx2~v8oert|F)!$ua~}I!XU+x>_Pj*M72=z1Csco|2-?LIV6x8*`bqyFsDfLVp+-U^xcJ{*ACO@xEt"
    b"B0iuy>EAim{B~$5hNZJ01=qXb<Bo{SSFG&%7k9s*dCE2_b2g0J-!W)7WV9G#(eb8p-`&T{ltrwU9r%-r~%?3Q3{H"
    b"1|a#)f8~Fj+W>M%CV?*qEXPMLhmoO!>6HBzz*jcX?#l;D1k*%CXDjng{oU5=q3$8=>$M)3hS(W5qzcBpROCn?Q3n"
    b"VZ3p?XD*77b`O*TIE^WOe@FdCCq@KDP@IfOip2_Upqz~@OhIWz%ccyV#Q{MWB8mE}D1!%c7B6(g#p<-nRc$op^W2"
    b"|}c?Ap@WiYTq-`DLj$bU5EqH>nIM8<tLEk^lpuo6REXcZA>iN_+%teNX^1JdLewv?pt-YnC*V5wTe#)t2;LR+K0j"
    b"U;-S=kNBKV~=p0yfy<~6*s})>+%#AqHJs6>%LvnoKo7K#X~IWH0*wV>xQ7BcHRgt7sDnF6Mh^Q$9Iz|=_q#e;Yq2"
    b"-PQ7v^68+z)$ZBKsgoP((Rw#*y@z6AKWTVg}_}%ZBp{dm$RRZiXfR7L0*+TZQv|y&feq<qx_4BKb!uodnO-E4%><"
    b"^o4+E|GwlxjB%0~mqVR;?2lf^)GUesq>rd{WuI((c;;13Z;_pMJ&UgmJ4q6ITM~h^9|%7uz2RadcIzGHOP0w^Pj-"
    b"SADXQ6*n%VT<3{{u{7TL(3t5;pM^H+eoy}n|C9#e;WG-L98AU5o^XIK@8xo^j~lScW0kyX{yF+y=3>Z48QF@H_wa"
    b"RK_vKE?>0Gmxql|fU1j5f`>pVOX+c44;Z_WFiH!8;ebOjUivsT;wXDb*+<<@`5p)BEf-aOjh!{3W<w88gey^v)04"
    b"C?HL7+2uSfPpp!i#5awvbsD@mbVFXJ1}rlIJMMcaMk<n)cX1K3lRx$9H&f(jvR|MfFz|4_R#3Li4_olG$V!s{hYt"
    b"{x|2-EF4Ub(RNlW<E%snNoO%Z|by%10x5d^g`=IOh1*f&F9_OmWfXGY~v6(*f<dz`QE$A~{(Mi0uWGgIhh?CELvH"
    b";u`eT48e`PeUvAU8`nkc39ytYu(LyN)ReNVWENYBSJlpenXDrGhjaMd1zQ_77PAX`<ak=VEC?Tme?@>bnc;x$a(z"
    b"P5Stz9?dra%O}c*4y_iZ0h7|CIV9JrgUbWfAQhJ4g6xmbd50qkB`Z2WZ3JJ_wh&-MS%R^iV@e70&9+M&90;CkDe>"
    b"#0e(4w^Clg&7BW%M8|15l<oB+GnR)yLLF{dpQ>FU6lt>rS>LZYQ+P^Itt@0kkWs0<R2R`Y3x9v!-&ZVZKjxFD5Sh"
    b"`<>C-ot!v?ddxdJCm)mWj8UOgIGp_kF_W)fgRP++a$g%Q@$+9(s$K#`{_n4>C!btAy65+z<JW>`a>#DI_aj#AqT^"
    b"75h#Jl0~wa9*TZTSp9E*5Q^=BumV^Raka1U0@U1`hdm4lrLDKc(uS~yzoX;J??N(_~4yt>%IZY`{4F@a9iFgLcd2"
    b"d}MaBzL}t*B`r)w+P>SaGxu`$>WMN_RLX+(m}n6xjHmcNz?FC7?88BDnU+%&lg}PK8r>tOZ#Zc?xCd)6QfwW%8wY"
    b"hKt-VM`s;><HT&L&jZHOPW;R%v^`_Y{Ms;!btYQM>oa%$S9hb79Z*mNu3gaD0VgzXcdsbv(+KE!?&s!id%g0BF3K"
    b"#knZH$`_zjjmabqq%RVQrD)j_5z2zJq>eJGBuW`#Ga`ieU9LW~Nv<%r1;XmjGr-}EVwdo-P@y-j6q@r}p+jH};aA"
    b"(t@+A&B}iA@!V&US4D$ibk=6yYE1^N)ms^D<%909bX=3s-+ZOwkD|tV8wTR`3E&3?2?e<?bv?xRNH8*6QqIQS_T3"
    b"JQiaw>wSRzu;-h$SUf7HE2D~S`o2kp*HyoX7vt4xykA}tUlSHaSfW&W2fHZ3lM1jAX#1M=+Ude^@e+0TCey4o+B5"
    b"T{kA`RJ*8#gcqD2cE5N3e5yuk1PkMW}fT`D-OdKO-^WHY1y9(9ge-(y4|BwVHM6D<rwDyT&d@=Eb=R6?0^sv-3Z$"
    b">sj=z5T5d(Or)E|!bv-WWHqutfxJs+3&9hz!oyiq6a+-2=FW8`(8A}AZL;k>LvwF@_(1k>VK0s>paneCO_)wwBjs"
    b"ZEsK3>U6_j8%NfK!=mfUd+x@Q`G_ahlYkFFyZ@BWb%6uk9^+b-6Mjz`m3)*SMnD}q*fYE%sB80TxA#i$7_63fBl7"
    b"$d4PHtl$@j~pfJ3vEV~3|n2SG8)FatGtZcQfx#uJN$=bJCfYoCz9WGH^s31h;<(|O|no!-};eo5!h3`h9u?d9^{3"
    b"*=eGsjn#l||^kgF"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
