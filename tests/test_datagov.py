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
    b"aEa?WDPa8quv-*C1P~j*YOPPr9ZSI-p@~cj9Q!LZy0Q5GG|-}c%i@ui@#AW9W&O4ap&Gk*{mCllH_*h_aONb+SVq"
    b"y2MKnef_k_>;;SQO9W=wC(MS+q5g-n6S(UptOMV33*9}`{7f^(3zcf_ErG&tB#OAV=XD3tX73`2AuAw2&tr-%=71"
    b"?yw4v}3-WXmz&1G{Co6pe#(19|$aYqxbZOH)5;afORZQw4;OgR9w@5pLZ}nb1A|lC++|(b-u7iQ7wZ4!@T)ILNEw"
    b"Y@}agUNV!?oyk(Ci*i=A&!gNb}ap28>gv2rYhLuN``2K^<UXNRk!eSkB^wUEK9~0pAxnLm!>%7hRQncf<0r^>n*g"
    b"L$D7?HUI{_d)<Ef3a$g;JjcxS*NJk_T6jtg@|RCa-+Slo$+Xb^?1x7<PoGkA|O&DZ$w58{k6EE>OeRO##>%0h3W$"
    b"caXEUJNaS*ZUPjSgYY;&!uK544CpDqtj24Ns8NNmfiJaM^0?CWH~4}00LQC_)}1n7Dt?4#S!+F}P7E}x#%Y*+wY-"
    b"G1EvF|?%$Y3z)%D~K#C>2R-8p+=9<zJ_yIZ7ENzu>${?3JFh_vFatk+FSf~DNLAyN%NA@ALf4*5@f!|n)rg-ud=?"
    b"(S33bkbEAGE9{O2tsw7K#JOhfUcWvu~r|(9V$M|`JyMKZ?Ek(9UC_Jl^AG_aXJ62H&bpxVEKn|sN>cks5CLol5R+"
    b"-ScZF4Kl5Xljog9p*OhbZ&Ax+^eK9M~n4$PH5B<O|p%BF#92@x<y2X-$gW5G%(?<hxsOvJ_An(<v|Kz?4jpL<L2m"
    b"veup*K96DHI8vGly8KX9s#I2%I5o6*r$%Au1G^teIQ!b^CaJ<BE$VaNjn|kxd-|HL&b%Hpwijh6dMCiON;Ol|A0F"
    b">l#~u{X8aUC4C9HH>u6O#qF`DjjbJYybd~s5H4!3<K1W!57k*g*>r0}SIma=)guXv)r-S#<u7h(_aJ_f{ypGW^3e"
    b"T6z1-UH2zMuacf%4Ic}Tvmk;$!_K&VbBMQ1ou;~|rX&|b8MX`c>mlbnhR>&n@vFGU?hSAu}5PDOw~zRB}u9jRAE3"
    b"WWOoX#H1;oo2w<52USW-!EtK4QW({68&8XjgEgXy{I(YPvoxc+Fv^nqgaL*SZqv4ZSN1=DMss-_w4w5juN2GQlEc"
    b"<F;N>_X{c|KSB!eOU*uN+EX}ah#~%VcWX=8OgPG^iy!~8JQL>;rCwqqCSwy+=f?$HjZgcW>gN^bN&hNNpoz<E%%0"
    b"P`9pN{dSa-1$d(>a&m?!uT<&*nFK;=bx~rX{}2DYcYz|Dv0eNp?6lj9ySrEIT2vRfgPe4Gg4EIzm%v*8nI{=uD0c"
    b"@ze=jPvhSdCIt{&pvr28m(8nb5`#R{s}!v;wv+Cxwtx`kEUtJ?j+b>8SVQnDCJZRxq&Jum@Bk8ivkahRQt!0bhLP"
    b"4DZVXEIsxFU0<)@YMz<ax`8aD~bq40QK_$zbbTIzv^R=YU?*1~1XSD{5IDmakW8=#pZL?&Kzoyfki&7P?Rp&6got"
    b"k%l);U0$9k7n>p+LYPv53h1JB^gkwM14VLJ^?6pzuEG;lz%(R|1zjzd!yrRcLK6+h&$A9a#Vb1P3n#ouO5Kbn*_s"
    b"8vp2X38f+4s(|voP4zIjUFJP6g8boU!rzds94xd}p0%@1S+WCEwb#1uWU-G>DY;xV`biHNTT(L<H4lftAC_~;`3n"
    b"?4Q2z>-AfmC4yL*lapoQ0>r0$NfO(Oio;BoVYb=rhqSzYjRdwoh7@iJ(K{5Uf-+5j~K6qrIbf#64#90fTA`A7$N1"
    b"yIxQ}S-jkZ+emQaF#sR{Spes44CfpFAVbPQzBk%f7a1$(^Z+8pmLYh}9PPquPPxIc=A)xz`rm(BL7AX6f5=8EXn1"
    b"41DtT@v9fdrsn9~GWozSK1xxMr=^<&%=j2Fr>&?idgR9}-W(+*(Yb*AcCaCSEubZU{(qwvcQZ&a1{_0OOxF-n>7G"
    b"aSk)gg9N;?OemTu}?rWmhW&_foZ4"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
