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
    b"GwWNU#LzbTv{bq|ZSU{KX~d0;H$~$ZNkT+;xm>CRGe(yCFgc4czOXjgj5w{qH|zo>%up!3u`!U?{tUF5kq)1X+A*"
    b"y1d+J+rdQ@8;s*xL=hQ=Qvc_^Kx7ILKQ<(_(8!uih3d=NWql_&O<FLvn8BG@%qRPdhJ+<#rR-QARR!1Za0NS)51B"
    b"{b?nx1NfSgLPo<e6VXbZ1I6SZ9!ot86mmy+(^g%fZC1GYXKpUY;CGZcs!C<J7jwtPaI%aOL*zD%X0o`@Zk&~KuRq"
    b"PrM&r}b9qyTre$jCQdMyY|IL(B6N2CYK#Ywhcz*P+94-p_#b^$<J|2aiwNXz^m$e}J4lDtF{5EPxvVC-wT6h<EUw"
    b"X0C#Kl|+Lbp}cN)a`n<^IwvULhvKgV%~VFnGVqwiOI8(hb`4VCQs=+P1jf+Ha|B!}Qi7aHXH_c3RTT17D(`2wqZ@"
    b"S*F+7$g40h$l(+-NF}5s(XGAD{7B|e>1jxKC{jJguz&r;MHP2>n=a<d6P4;=Uv3NgwLuhqJ1^dm;ZV`-#v;=i%oF"
    b"Tnm*+i4XC9o2oTN~@)GlGOm=L96C@hBjrfA9^%&1P4(D>23%cW3?c`R{^3L~n8DdCBM0^v3#$t%)++-!gg(jW^iY"
    b"&H6E9an<~l8TH-f{&o)1@0h`wZgaANe@7l>V;513Wihj<h`Q?rv&3~>5YgR`~v^2L~VFF_5$~7!<V~M6&<dTm;8N"
    b"En@!K9Kjg%JZ~6}^iM`?Hcp=zqTcEDePnG=7LcX!$k=G2l0rdxYqNX;EBxp3skJAm8Q%<|8CBkNkfdP3gpSo0e#o"
    b"Ay~&o?^nRC-~r3Qv-=7EG-N!tyWwm6<J3v*%<%kJ2utbIZoiWwsvkcs1Vq2eb%m*VX${zPmZexGRSoe7+?_B~M%_"
    b"aeIfyXG9>LT|=yE!=>$PrZKs*UpW13o_D{!z*i?3Cu;}!yM^L|M?JR7TQVLTx21b_JD|NIF&E0=`OYy^>;+i%w-E"
    b"&OB?}L#RCap;w#SZ_2y6Sk$jK?xJ!gi&8=;uC2rN2qIc`;v4_H{t0|FlvJ#R?urZc(QEiz3f8lmfxdVDX$&U=d2G"
    b"^exh2-F0og0#z3&ih0{uj#2R@MY;5yJ%E_H2<)kH|NyRe<8AUPie|jRc~D-EPRo*s<I6gQPVG{&CwA1_bqJ5Q<rU"
    b"lZe}6=IXPa3m#Av5O=!Nf#MPQ3s}3Caenv~FD+KmbeWh;Ws<v%GvPrF2(L=0L4Rz@lg`a@bwb32)%Q7<D%ow`7t1"
    b"lA3egUXEkA33puq@2#2mc)h@F}MO5Xjl+3Fa#GBDI&sJ2^dEY}(?BbcZEtX0^OHB-2F*Eltf~-IgJvyB-Uux3wxs"
    b"fftocA_u!fIC#(XzQpFl>weLHJpQF!TSsBsjq#_`N}dK`_<+Ed`b5I!c5;Z6%OspCf@+<cWbPjc3mb_+qJQ%Jm8p"
    b"1lp#=+tI}yjYgFHWi1qMieo-tBNoX*hOewnIXoHR8q_Yk^tQYE6&jRtd}Zlp(}=Cw|+!1J2wIz){RxarCxDq7*+l"
    b"|(oN>`selh=}k3OHVp=HgF4H7casd&t!8Ha)?F$4FrZ6zb$_~OsC)5P#@QDBX6=ni=Qot*=5M>&FY1b6Xnk4$yIL"
    b"@3YP0>!PwpDe!k<j(hF%E;XDIb?Gh|<9S|(cURr=o8?T3g&6R)l70L?Y1C7ba{kRpqbS-0zP-2pvXyFzVwOT;Y+$"
    b"AR#%Nv9FLAV(_Suzg0)g8-|fVp~znr;plEknAA7eqH%wgI<X`t<5gmSVUi{(!@<G?4&BM@aZ83ze2S|29W_+QFu>"
    b"nHExn^+{HqWBU${vJ85k(mi&PMxK1Dht`vr8z->r^Gi7+xHKRZz<k`jhB}EgVYv@DvBoW+w4SV0opmwhW{C64&JT"
    b"RklB`chW)Sdu070%+ChswnVbV?OJSU>;;=6&VfSyMqU?5JFj{3XHV=s=eHf+zkEqT!C@a`aBE2l+>m7z?A_RvykT"
    b"J89}c~!Sc?1zdJ#BvEUj`~|$Ab+viYS_C3_}c_gV8_;wHGtvU8*T*fg_6YYpquGMKOc=bz>SlCkxdG$&<s}^0wxf"
    b"~yPRj4pGrJ<ppIaj>?RM#M8^@XfKUHx3h2b8lm4et$N7ljnvJ1qRrGmdui#|ApdEX3&iA+{W(`P22R-5nZd1eay="
    b"OyiEV0Mn;=sc4&X~-4j2ERd$J+7"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
