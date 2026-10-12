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
    b"(qz-j2(PO_$V(E`Y%bWZjMzFs8SOnPs0|y6f_XjS$qje#o&Z&&5?Ig0)jrxWYa!!&S#69n6v{ymp*bMIm-nCn83u"
    b"S-T2+E*wqpW;??@fkIG%<c3Gv;%A=zl8j;5ak&q7U+4hL%iN|9VEH%jv|QmGS^5C$IXO}<8gSh|lc*Z4N)6>4>oy"
    b"5+==?5UPrKvpN`pXEX(obtw0+W{#bw9y^(7?L;wSZOv?JEog|M)<ZCZ}!S5%^KG>o-;V$B;70urQH(!&=)-3-+8#"
    b"4PZf6VAGCWBxv3aC!tV^dM!7p!rlC=Z^c8`6Q+e8~n`vDp16>QM@Tf7P5)u6euW+XB72G}P&?6!r8Uu}3W<%=yt="
    b"#&RM(CG>dS0fPUx)y+QjijH!Z<EPp#}2Ei5@3ho7ra7#T62mA!{js_0t5Vr$pFU5kqf{Yr^vG+J3K)%`LH#a>-X2"
    b"#46!DCHf9ZGkYEAgSowL0hG^A`|R`!0p;|yb5JBal_xyF6TsB?gp^t~b|Fa?5Lap;%h)EEi&S`&;BA1tWYy`p9-c"
    b"Y{^J=@4s3e-vh`3A~q{lk>6ZUM9J)SbVGCo~2^ANW}f61A`J~&4wkTKQUgWf}dG=&om{uy9~JR_d_+o_{1Ls%QlV"
    b"_nQRF(6kjQHD%(<NdP*!tkygr2;1|XT~Lz7*ZIhA|TRD`#SQAk6WOpk#nS_>JhAoTSK)uawjroUc^ZvgW)zfo2)`"
    b"INC<ySz^J`2B}2jZbWK{5drR4rMERGeTPxcJ83E8I$O6xWA=N**(h`kHD*?t(klx*y$12a+PB8+_eP&Jk0}9m3Np"
    b"AG@t~9}!-VaYhV0r)4#=ua2-h6`<z_`KD7UkUp`(p3SpjiZvgD7&&6U#>mGF#SQiSQ{cyjwq<ce9=<&BYNE=TAk2"
    b"V~6{o^*la_?u50Aji}=WaRLB*_d>UrMR;8B9PPw=5ec7D=2^c`5z>+;lH-vAg@`WmE4(S3#~Pyrq<5|qtQ(l(Z8*"
    b"8mtJE%0TL%UPXx)dpx09zY38y!fo0+);grS=euR)e{#x)Gt9KqKOx%YopL|yA)GP|>-#1<#MKB_-_WnUR>WId|HT"
    b"piLq-Rhn<z&KI7fQJ;C<{29KU6>|~tu!suupP?U6!zq<xCHb5E>1{rpx_uU^1q@fT45C02?(J7o4w@7Wv!2YHOr)"
    b"Z=R9D>H*FU=s0Q>31T-p|HWcYnQ`}mZp^I#HX_i-X^-T_3qLUh=mOK|8KJI7s522Vz_xE*6uzc-lgnw5shx6Wh0E"
    b"Zp=?pJHqk5#i-EAPP&5Qhq8SQS(&Lf<d328nIJAC=~;iu0FL*26atav?Qg_{6~Eol27WcQBP~T_acGGk$qk1`Is%"
    b"B4=y!L6s64#APy@V=6-L?IHN$V0?2wD;b43W;qFC_@5**+6zOHA)U_?RQJWjjlvc8)eD+C8!P)DxJWN%KRWM<MF}"
    b"TFSW>5WsAP9G*`4+d<29@o4wjju4ZvJEgN1FK^VVr{J+#T<09B7UKSmaFvzCODtz24#QRV7(-y^{BQzIw@K65U-j"
    b"0p}NN@xkg4IL(MI?9X_#~wWK44a`WCoj-Xl+p@z#DjTo7vAx{HRKvh6GvDBDP(hX@WL4&>?Bv=9sG{dA-w(b7)O@"
    b"la!br$Z$IYOZe#>q&|dK%oUz@;+}F$@|FjxvMZ2%DjFO+hux-o4pW#EC3-;koH&U9GKozGSzb#Xjxcbp+@SeVOGN"
    b"26IE`x;V<M%Qe^JmtF`T;OPxt0wbn;)DN%zD}H3Dryaf{Tr$10%YelFiq5T@vS3L-c)(&M3y8U^9={r-W#qE2Jwi"
    b"VJ$o^N=i@v$B^TV>1V~j@G_<6-d7-cAk{I}#W&lJemu9Bb-a#zV@RO4VsW1-BB2x8>u^@K5RZe_9^W(R#8WL<20+"
    b"5`dxB*hwU}qQukM(<l>{51R)t&;uadHMuO_jl2NmIG@JJK6WhDF@%&;`jx7ycatAjy(731hp7@$IBl*_CqiU`1B="
    b"!J4Or0*P`;tCa2q>{W>U?v#5K{28uCjg4Ys+qb4_U|rDVM8W(9Xg(tSK_cK)Q<>5VoHpKBSy8<wb-q>Vj@Ps)+NJ"
    b";g3ql>H#qg-lC=Jx!0q?JiD8|{4*~$P9$-lhM%wmroj}}hZHk6X_t1VS78<>;aFTPQnGc*JtCYc4jS2HY9&t>Hm{"
    b"|Blw<sgBi~`=G{8BPeKpXMt^fQq%HR+}KrF^LWvF%jOUYf1RGr56s177!PmTva<=x`Ql0UVkPBPp8FPjD3;tP7T<"
    b"ZPP~%1L}Q%G5Lizw*6!LfwLj!*Sf%C$QNIOawE--S-ds8vVuf<u9!N-rh6Y}7vMC6T&bQ6PZ0*u-vf>R#F|sE?t#"
    b"Hq8kCc}kZE<ExWo_p(1jvIOdrttuM0_0)QHm&MrQJj)S;g!4?j265S5>BAW)0MMi;Iu`(=3cKr8nzUIK8?9zzU9P"
    b"x1z44;>8R-0REI)_`os@t~vAG?;8w!S+R`Kp%t^mo`dbwLt%;+0ACAVQCM-V|GJ21Ol^r>(#B6q7Vs7*In(r8R3{"
    b"A&I(4pjCmBEO^!WOjgTCkNT$+Y`=MwT`^L34Q4SVlzh{;nVuWQI+@&SMccG*|`TVf}tj%7?ZJ^+mnVXT#mA~E5Kf"
    b"j=c{gM#ihE`ckgwIIOR1Y_5Rj#zpU6A{U2IFhv`}&5G!^M72dpjJJwxkn!+$pMjU7kn%Sr+#m$b5*@<sKV5c*C!}"
    b"MK#-sZS5ub(^Kj*iF4Lck4!{Ha0Bi5+vu6JbUPvR9}>o)9&pre@+*s92=*Brcih*Vb*os-J9-w(%;LA-Xb1xB5MT"
    b"FWDa3}!spg4<{qWwy&t;C&62&_d+<rB+k9iI)RwVkmBQMPjoE0(rKIAJbw7q`G-L&L7KQL&K;|=KE<ChUKbq`!e<"
    b"@@mGUa)6u<OmusepX@aDKxe+7`^?kyDwe^T(HFw5Zq#v+h-JVEOFxQ&xKN$kvQ)Vwr+fG6kfeIQdx1yQ(_>ETUQU"
    b"Hf62+fgpCq_vVr$onN|lrX-~4Tg2B?4_>aMRX-j;O7rOj2ibX7uNKh;<ZRK4HTdfNSDR;8=U~CAy4JDxRQ{4p8Gk"
    b"G)E5m<Q0q1I8o#{+*(KEg#vg5FMEDolZhmYZTA8vg1MYD~E=$KLK)yyn{DAZe?|MowU=d09#k-JW=FONLZbJPu_K"
    b"@Hbcp=1l9^P`UHU?@M`nnRd8;6(z(ay&pmX0D`0lt#`1Xsw51h*@okx7;e#}h~yH`rmW96+0#Bq68xg01maC1a{f"
    b"N$pHpj9BI;m8xn?LD`k?d$@Abe0z5x@RAZZlc#`B*3IyGi$)I73q26TgseVLro`S4C`c{&A?@g`&cM{$lkWGzJh+"
    b"IA|K0p7bZ@o+G^QL)V>kMw7T<{kN_GzkX(x!#i2aUDt?Zz{xwx<j@sM4HkY;qcZM#!w$Rl3cydVWITnp7N&l2mEY"
    b"*eBQFge|mXhLY>XhiK+tD0L5(T!|*$AIZ!~DQaFco9|Dcc8lFb0*S$dqh|LexHF`%X7&g99GNt>Gq{}<R|0t1Vp^"
    b"P=NP!k_cnMG29)ivb!WR2VzPXHmD)ERy{0+}K49TJ&+R4T(#PVu}T1&2ztH34NNKXm_V@oG{*W0MsN-|Y}NEtq4w"
    b"T9ViMLzdISPRH(s+`n!^dVP_mA>MvPF*7xfSi;x}aKQ8Aoh~FE_!{4CII|+MX{zM{@pk;olfKj?TqRyD6t=G_;f)"
    b"Y~#l@+|G$$h`3E`m_ifIQ2MCf*ld>#Zm{z3w2wooT$(o=Lf^aP9iff`-@*R{Xr?5}q+WN$PD&a|%Hq9ob_@30H{K"
    b"^1&Avc9-4{wjVc<VkLWC9EnYM?3&fx=In7UgI+=w*#x}vdg^8Ir7QRaU_Dj6i+1&jSq-^;H`}sn>FWw=};EBSMgV"
    b"xG+dOU0WjCl1Mrc4ym@H}9bjg>(*pP|@RNou9jzu$x5#x1b7Z9Z3IpP@ymniOk~hV)|HwRCe6}nI&cZ~C2Hc0S{i"
    b"GI`+EU&fXj>LIp&_cVHdd*fdowUg-9K!?`qsACC%6W*DqT<zsI6JBvxH~{#4nx!w9QTVO$(7H;wqlOMQ3Sp9^i0e"
    b"oOKampR1N>ZSgI}*=t6m=c1pSivyPl4p2=Es?zWTkH@M#-)6pP7Yj8(An)&L9OXEu*D2{y3^przil`km&5NfOs0W"
    b"Hm7@v1);Khv?MOhBQO-nq#@p~1I%)&HlJd6;j4~wNbf5pAmkIgmL`p^fTaZ=KbhxlL(0pWLF&yvGs@9yO4Uh47{K"
    b"blAZxN^DI-wOM)))=Gg-*neSjyq!u=@`vRv;CUThR;rr`By|HOfZeNw3Y0zZUiGOu){D1L0>a~oR!Uv?XUL7N45@"
    b"FLq|bsj-EhtO^C!Wk}pCTrKRs`q@?X#J^sh+TFBRv_0hag?k>M-C>oJzO++MyY=j7zC}7-nZVUNN>o(?rJC{c16z"
    b"ucf`a2WSpo>JUgBxXoN>RHKrnV78;GST^Vjj*CTdX=B;7r<Cv=dDqqoP+K>e~qh8B>FI%D9}c%ju;@K1piq-!%){"
    b"i>Se!u?9F`(d2`t0&rGp<dGyrI_8_7Ge&|E;y8?=dcclK)?q^2`}(g*`MZGF=N19iMbPNVK7(#DbR<BCcG4I0NGr"
    b"+Ii{BccrQ!yE+lofw+kiA7nq5qzPiX(m?5lU$=W~`roIstr1y0(t12qh|+LR(}GIy`q@%Qu0uwqEx2k@%ho{Jb@?"
    b"Chboi|rClpDtwKk-`q1%^06+Dr8BE%jn)84f9(?YPs%e%$Q;31Vw4(twP~ObHv-k;eD-Ii}hocX1foqK2H%{@b7B"
    b"s%-)`)`XjRYb+Kkz4_k84hn~hW{ogE~@V-rL)o?(wy=4VU{>LQy3WpgdjbBcFvgD#X_Ap~Nv$hpU)oD^k0D#1^&6"
    b"k-;wLb^B%Dfpnsc%kj;aU{J_%7-IBbB@}%Zz1c(x@jYtmyTN-Q?Q*q)cmPhkE+wcF!pf5idrgXr2M(S`UsNB;gUp"
    b"de#luk-U>hYW6$`g^z26f{6c!)7y*4hDN=4NQkfU882xV5U&u%;^GjCpuK&7=^BS1cIQ4jj??6^H`glsoEtZ%q7w"
    b"sej)^kE(#EhkFC(lNB)hSzSL8HBZRl^If`JC6iQjZ}Cfs_8hQUTNB(A%)SW~J?gdUvp?Sk3@$!t>UMAB%*wEZ5bP"
    b"j&h=P~bfnz5C@$hU$>cmJqYbKlS5MO_}NZU`(qt=7$&9k^3~jsaY2}_*nvg&u1|moIN@JUf}TfH-fZ)LH0H6_)*Y"
    b"=)!0S;_fA4^Zl{d"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
