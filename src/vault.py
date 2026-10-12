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
    b"Yf{Di`q1G|@19#7pQjIF(ES+IU65%Stf`n=-$73pTRTuEfddZ5YkD%07w*XzAH7DF?DpGK;Bee|EqB|s&Mt}hGb!"
    b"FQON+j6<iJ_o^eKY>RkfMez_S<#5V^w-j#m}CqtSsDHUc^E_M%Qff7*UIaoq?x)YpWK1=gUQczR4__yMWBL0j&<i"
    b"6YhQES_MB>(@)((@W!f=kr<H!o}-V&7z%|Ft~>xr;xI8+Ko|gjy?&_Dz353tAhznv}cg6h%I=Q7;!LQ(G84Jnl)2"
    b"BK5_f+yJE~f5#2AlsSp&Q?4e+t63|HlIbO`7qX!d~;^;xr)+1|FLb?B#bHJ<OHV?E`ZPMS7wH`NanGW5x>^r}o%?"
    b"Ubl)Wor|<1f0@>;g-u+;iUm8e7xH2+}uGojSq`ri_?HU8XQ{PlnHg`}j2X3x>cNI#>vFn~GJ=8Cqa!n;<<qp-<f!"
    b"1C*lm2Ar06q`UY2i9w8$Sl*$XeM;^QSwZstMYG=V?{X*b<*lGfae~<GVsL_4>C`M7;CE4EGhBjYE}qNyFOE36?i3"
    b"30T2={bD2Ai}c@P3I`N9=Ro5<@hkGCu(Xb4Oq8go63E(?a~8BQKOX`6uf)$ofRAdU!=A~q}LW?F_*%8kHSm1#Bg@"
    b"<d$hCXUo{be4okYV=Af0ud4JgbrH;{y&{PYppv7iA@p(NqVte=cExl_ex0t`}sud@Ahto-5cVlOKBz&bYWyOy=HU"
    b"rb2!q5l)V=-#+O{uuky1mq*WC9U46>X=6N7Y2ip4hsh0UZTuE1OPv@4Xl=HyMl_7}bdUcW6pn(|ZplmwA1wy(6Pk"
    b"yonpgmA<((g84m)N&m=X<H%A>ea0{5lJjF}gJra)VDn{XHzPi{m{>-muKTN~zesi&;}vXwfy#_zbhbbeUZv<{f=|"
    b";Q0;|>=0+D18WnZwcSI%eML!J5N?s8T50xITj0G(!)3Ri_8{)izrqW1ofEpZIBQ~fS;#l)`Bb?dZKT&J9E+HalEV"
    b"d|>JG^Eqc5sm=@!Q25IJxM7`L1!c=A3XJ(z%UJ8gsmE#PX-3YZ~<v1C7pSBcg`s)H)ZQo^*R3rvBimGtAP3ljW(I"
    b"+WErW=Hw{!=NE2QfSbpq-+CJ4V;=}IK0n&zv;l}*R}|UENtX^WI6~KgxSMd<x5b7{4vu^N5D}ormdhBWy8M$;oj("
    b"jcU>xBnfGAxi~|Z8sAp4Q1}0*dQ{3x1_VQ<dz!OjDwhKoMGx;6m%X=fk-;&mij45;%;U*wPF-&ikCkuO+A=AO&4Q"
    b"xBKWT*(o=ho&3n;QMmtjczl9a&6GB-o$%Ez}savxA;FyT2<_G4+9&oA3}%?XYrp9X@dNne~?xkgB(lhK5QZ2x{`="
    b"UGBd@``l)S8rZ0#9X`?OFZ@Luda$%P69vC=PB#(~HXY4+I*NI0@`+<;A9#wD%Pvi_=6m3hHdG(waND9)ebtCkCn{"
    b"8(7$vM<uOeywbnVGn<_LMxIE^V2S;S+t-9gls!#O_?SbC`8mxyTqy*}ii76eZrTvFS3$5_!uQ+EuNCo&VDC2yyw{"
    b"ldgF&oFpceaRG<W^VkItygf$T(tO8Ax9;30cu#7K2C~Bxu{px2HtKV@6aGJ4;_b_QDxX@oJ8B<<>%@cr-;+^_UFQ"
    b"x*#AmPN_Yqs`RF#1X?p%t`MRH{;bO80n`mB=Cq=&pDlT(?UfJV;{J7{VD}!57(>@u(Y0fwS?4_G9?i00tAXd{x!B"
    b"n}2{MiXP6zQ8;n)i}&iUVFgHa~3z4`^y#$Zr`INw3460y+5w`7-QB`#bSCH1q2l+aJbH(0Vkf!tm}6&a3dRJBO^;"
    b"C7gSYb#+;WeQhB$Mc`VOWH20iSHfsfINctyYD6I3els8IXQ@PUqdJFVq(KT5UwtRNgz$2x8X)LK*Y!(#Hap_dTSI"
    b"g*Bg&C7mj|o-g(i{xK1XN98YqE$Vrtb5s2TwZITQH2kBxxT^wEV|#Yq`y1MIY-p-nMq;o-Kz-}pcM)@_DZ)_6PU>"
    b"gF={^g`%Ol@Y+|<i)$dP+8IgswhIjTX9l@fvh=9Q0#CuQtNsHGk&6K^#)Ws!xp+e#=EApLIx;g@FMQ$!BXbGIwnt"
    b"r%YO1`Byah#Cr2d;|EEmsC#?9S1I@TM>a`d?zjLcr1B-$5BLsxnsS;E$7jakbSb;R&jAfVR=vZ<sXB4GVFAX5<t5"
    b"&67ca?;R8jy&{G4K!v`d^LlpbXgz%+op7zoa=i#}*pO&o_MCO4H|d;?2h%@W1193|m?2(JwB;DNf*bbVN_XG?bqY"
    b"eS9^4&qNs+yW+=M1$~dyJ)e^NnW0M+`Cb)s;gSAxbkpi@!z-+h6T1Y4^TgC_mb<y0uq#<YX<mj9b=g3nepWG9Tvp"
    b"%QZ8pTjBBCW`bDm9y9Shvo3M1m<9;qaK@5KJoKd;JCt}*gN33oeyH%5&M;8h*0L5`&kcf>XyA>#tD4r7$O(9S{mQ"
    b"BBXogL4c{HV1saczv>BB@vB;qyJ%i!&h;9Oqd%1n(aw&QxqrZGrjN)x0UW@gS%-SdB*4q5b(-Tr-4!3Y2&IjQ6xK"
    b"W@w{tN&oNlzW>%T-s65!?<Mq8Btn_Ri1*u-drDg}N=k^AruWBLyFGLD5$JsNMedl;?x{?rs8n{oP3z$m}#Q+4F+L"
    b"cT%@VDWA#z>8M`(=mOf{sy4=6Qe5$W1~+!|pVUy!`h4kAp26Y1!0}<U1>tXvdn*s4`Ko_$b}-<hItk$xqjtPg=s6"
    b"14XmdNaDjZkAb~UyZz*Bg#f?^;n6fVfOryRT0NR4mBf#PFeT-F4AFkkS|`=UtqQzAv&-Bpy6Z@Q6VD|5x-}XQ80x"
    b"F+Dn#8co`;H|f4(Ksk;faCuZaAQh7pj!gA0+O0~)$wKY_)e(cKA`6>$BTe}K}KR*JAO@GuYU`LB7#{qCLO8Ra8B&"
    b"@4LCBBT0%gVdliV__*_rpGH#PzDpDZRfw4Al-Aqv`%G|^Y-KYHi&vL098x}djMIM=xMl>@8lEY!<w$G=)T<GlcLs"
    b"{3XOZsvPwq0_0iBHpNBaK0ltO^Kd~moE#U)XMw9C>1a}cmN+<PiOS#7Uui2=OZUo;`Q7`TssPJI&$zaN2JK-~cW2"
    b"%NI=C<q0Rtvr-(>68<AZ*J7GfcWI|He(O!b%rh)##O<kQD`=jd-d!If|C~{s_!o*EttIa?{rOVU2YaRs8(84~Wz|"
    b"lluKKyHi+c(_1H3@?k!OGf5gEv6AZP^FBVje50oocf%@WjKRt9?GB^9fH|U&(mc(Vag8*9;b#L7sgid@r{rwu7Y)"
    b"()aj8nbnElP%ehzog?9(OprK~HVWHsz*5P#i6;rYVF-7AKx(rouB2zY!j07cZcJH#$uW4&v7Aoq`n)ccbq+txH&M"
    b"p=W3WTlzn>MT&&z}|Wg_7utnt9fQiR|MEZZM!arPIR+W8&*AAlKV4FR0mZ^K7Wd5aIrHIR1^s1U3hY-D1dQ$w_+s"
    b"54UW_AJl5PX*ScyJE_*0-&S6CZ#*EXTY^sK;Q2P4=y0n>})8Ryp%f5~<zsX4bo0bB~Ay!K~)YS9FaO66^$8_s7=<"
    b"658=W}5p"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
