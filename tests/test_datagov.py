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
    b"t=i;o>!5t-+a-c*NGu6ARj`Frnp58|<7!<2oaa6(yfrOEXM@%vSV<-?QXo_)Bxtb8dLF%~sEt!2ny&7RC}{+nQm$"
    b"Ww>c5`<)`&Eo-VfXA@l=rk2O^`31sH6S*AW)<*6II5jGWSWAuy(CwpoU4UqsfQ9?5{XMRGpXl+cvM3nZ~72<vxcB"
    b";Np1i(+&G?|s;dc3;NBAUGk&8HD-H5KO2u1jz))qq>rk^*WunKVa3cO0!veP7Clae_<dvuNMA3-ojfI;;<SYeJx7"
    b"YWtmteirQ$%JbAi1-q>YCaUTz#Lf2xYC;tZ@#}HxHBl?9M3rj-FpG0S2tYBl^1#3><b`wbu%CM#wZLu*fb^$lVn%"
    b"u2>n7x$V_-c1keng@kw%Hh=n`0jpQ=U;#$EK?j(`%&#Irg^xE{&TW5?(T%AZbU32*o>&B;62NsYqq^kD}>>fxmo!"
    b"aSZMZ=*E^8J*gY6AhZ4(gKh$s=kzD=c><Er#WSxa8Kl*VxS(X;czfyFA;ZXH>7W3~t#%@18;mS?&e$2Y!0nC7=7%"
    b"^4{*aJ$Z`P9B6ma^^uX$cm2>qg-!_h`lW7vcfV<}-4u_0Y?ski~llhy~{^{qOT<1rjdq2ut$2z^pVaG_MDHfG(+&"
    b"9Uu{wM$D_Nl=rtU51R{9jvHN7$JLid;XEnl0_!R*rrTGP_8Gdnj=`#*Y{a~@g?fEG1s#NQ$|xvdraYli|>aKQ}<r"
    b"zLy~<YYBxGmFuF5iPa2bX*A_K`GQQKqxuqLcFaYwp76@Z6-h2p#I+?dvg<fzgV0<^u`^5c7gS2aNK6$81X4j*mUB"
    b"y*Lyj2ECai1wj`R~S>$ZX;+DUd>qDmGQjmNIg)?s`fa_2*S&<qnqOLo|Z#qUMsM7IV@ucT_U#Z4%icT#hUUIA0W`"
    b"GnG5!C!}~?igMwd7M&*B`tajI3Z?s6er+olkRpGn<yk#%9IB<=$~(m2bO*2}l)4|xzK_K}kZYGFTK=>|rn10|xTv"
    b"d9a+iYRDRWGmNW$Qc{!rkZ(<;1iz`T1eL*wnR(C$YxW7Yc}%4Dc9QUR395YE?ldI1E8dZaSE*2<tI<S|8Wl18smD"
    b"~K7KR{$L!8g5?m%>%qMUn7F(3++)sA=05W9woRH-s=i~4tcmO!CO7y)|8)A^-A`hwPY^{11>#(IERpzuNK2AZJxE"
    b"~rb&HrD~Eo3*H}-VS!l{be}e4kbQrB@$CAUeLIeR3*ZEo@q;`pa%9%WL!Oz)qsCYEK!GH>3qL~qP@$UNj8r^&u2w"
    b"$9WAHv+cbRcttV1{Enz3HFv?5P2uBPaB-%`w0n{PAtLVua~J(fL@emiFF8gE&c}bb_~%G6`<ky*f2xl^+?qXc)WG"
    b"_gEaNTriuc6)vYqgN0O7R#>$u>32G${#ev(8*#+CZu2mI_C_W*AzY38c}EjY83}4hGe34aGM^(5GuX|0RBQ38l|C"
    b"W@J)`AL32~_%BtDBW+kd_NPjeuKybj8Ups14rP?9fx*|<>__s0G$Xrzz8tw8SeS%0Yc#5#*^n?z$)-f{Jrk`fs1k"
    b"D2tUpogFrWOD8t57@A)vdus(eU@;#URCd2@$SH3-pvu-tA2S_cq&G0xdhT5_s*ATj=#|p!GFNiUcsp^3}Lp3+L_%"
    b"C$V0Z;PcZA@ZlB3BmL%Ml_4p&El`j)Ch9eFoF`k)Cb#eKLm>O(+^<kC&S$1hkKb@h}$978Vziw~L&$bcuQ#arX-t"
    b"7Vg<)5xO8Q(!*Y5D~b6KX%xBTlh(?pevOvk6iWDpcTLKSLFeu**m6n)CNJqXXLzvVx|cVko`2uQ_PNG)I$ALPw{Y"
    b"W6^M@Q>03eR4W+o5DY`%X8kSni|>8SV&vP)J}d8n5uNrNr&Ctir3ydz|1$hAk0ht@4VR@9ubZZyoO@CqCrf5KLSW"
    b"U&g?5%K{DIfar_xT(8pwm<d)@_Ub#L)bij&t>V_XhXXIPvU@X^*hv_JG3i-I}I!7g}?z7BcCx8HT{FQ*P0ekJkd5"
    b")i4!yET_lYGmb;^RO}M7UNxlhwXg"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
