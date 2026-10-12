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
    b"s}}Zv^7+|&s(qjfEkRixv;shPJD!_;Yb|q9i%5hRsjHrf$LJ(8VlY4OEH;j8erg%E#%4&XJ`bda9jGt+cou$R%?!"
    b"Yzr>q@E0ltJ~`F8%53|{-!C0o}C)6xy^M?9P-YLBiitC-k`$S}N*G~>~6K$#4*W%b}OZK+Yw9lEZ|&t!?8Uud=Z6"
    b"ddPLg}oBzc^P8t1v}|54ih+u3d!ob!-$HbFrOrRvEuL1%%yXj-L6bUPUkr?^YPYQE$;09&ze+pi^2E%y#Q0uZIyA"
    b"j)8Aw%qDZvYkQW%O6R>2%7)ujE@SvQ7_9|88RaYo%7DC*QQ`+*Ok(i9u$_!P2--Kh;F1WL)>aSB}n+JL|s^FqmVf"
    b"mcEz!UHRmKhG^52ipLfu6>{Bnm?awRz#nWKLK1?E!5Ov<C9ZDALFDoLqM*xN9d0^|&Uels6z|RjT~@6h~mAN9^@p"
    b"xqoEZgwQ(X+p^DOkHs+ifo@m>0bnc&SWyKYcygqGtR&K@+dgJConpDOtMO_HXggux$%(tyd6WT7r9B<sFD?v|zfw"
    b"5CUuY*7PONCDEc|ykjj}Li=E9U@inL7W>F4sdiB>3^x!6>rQVgjA`d3>5yGBR`!_5YJQh_n%&j3voW0raN5}fAc8"
    b"JiFTrvmw5!w}a_Kzan@d?sEy*n`cuq3M5`&{X6bot<IwzEq-qL}pxSV#uFImRH_TapEX9SI3vkvH9%W`@Q+}BxN5"
    b"CH0()p{|gfz25_$~Joc}3ewqmt5zKxtc#Wvli2Uq7jK8b}Wsu2E02J7AUi`Y8l%CV3pCM3icnRM^f2YrLN}Vq2)B"
    b"HT3x?LAcK)tIUdkAI1qYt)%!At_}tX@=tj^YMe1l&zcm4cL?2#Y44_2^K_6N?UxFCbqa?;dleaIv8?J4=1!?U)(!"
    b"9suIz1}<0M!v5_*q<}rT*zzfM*2BnCr&=J(u4(_(wr$Cqjc|)?Ch^JjGA0FSpXH+}NbQo*1OD$w$WabT6lsPJOP#"
    b"Q1Ibof%F2LmV17_Uv;o}!YK(YiXHymwArez%+qsPHT`u|X{am^|_?j3`zhG#3M89_@OCaER?`9mh<!R@QcIy;8!v"
    b"$^!oUao-Ar_p&^;Ol!yWeniRjvg1%i+0od;9-+>*Y7T|?<&aPsLK!2o7l!4^(3n6KS>n6$#B9g7-UB%%rB8OLN7W"
    b"5XCwv72^IL1t>#l9A9!!BpfNyxJ=GrRhoh>p#~kGDWuW&}?{#xwVxVN$RhTcxme*|LDFIWhy9dP73$nS^B$_!)!<"
    b"uz0mD)B$Q>=Sq{ln!Nt++cbRU$Ia$|vSn)9w%NO+e9f#0Q002Ag%6j47zh4`7B@3#hY{F?&3BYQBBP%0i_S08(vj"
    b"8U^UJ)H*d2u%Q947n=L=0u9g<Q^w-|!IImU5fh~mL#8&@_R|EcE6jh^i?+GuA4?jwT5fGl5U%4%APSs|30%voG$^"
    b"Ucy;g<2PAFaApp}D|;1wTi4@BH1TWCjas}du6j-=>r%$!F!r~2^Y3pj0&?pX|KU-O>o8_II(?vUIw)7C(?$u8xYu"
    b"kT+jgdlNd+y;alRChjL43wp`RqzQ!UT-iB4mXL{d6W<@v9v&QQFD~J|I(eOr@~W~rk%x|k6J_osxi*5qU3r9MIxU"
    b"wFGMtoUcKR3EAgJxt>iAb@C_F;qa4mhHsB2Pn+*s>>xa1vvN-D9qFuI+Xq$eQ3&liLvoldF#!*#%JXYqvs5AjP{Y"
    b"zQ#s(GkS`o`ijpa2p-sJ1h`%zFLmL;Q7+dy~;63~{}UmRdgWZ;uXBX)!-~P@de_bn``mmg)L%+<9n?w?&*}9!oP$"
    b"y;RyL743r80(_k>F-6ZoS)mH(Xj%ruOFWowOtkYP=SSv+=H&E%$TN*bGj$nM2lq)y166P=NJjMwsY)i$U{ACQJ8P"
    b"4o)|zGC?W5~e%>=l7yI{UGXCQKa&39%H5;NTVh?fC9t{y=NS#LBmWdLM}&Qq3^N2%8tS`8o?h6e{US82OC_!n-jG"
    b"-<o3sSVn-EOr)zHMjscK1&jeV83H7#Kz*Buas{LV}fB>66{j_+`uw(+4x;RIN=7UeZn26=gi8#TL+opWn2S0nn*w"
    b"}gwV%|>X^sW=YBbex5A<|WSWZucIEH*LkB5PUz;yUs_89c0%b26Y$+YFt!7YLi<N1P+5GWB(9D(8_e?96*p(QrZZ"
    b"x!&bF294;%X(-@HdSyQn!U}8dT$GQdgpCPJ<b3WKGD9^%F#j)%cMbgjwuR4Fure1C~ObTGH&<LU>z>qb$y&+ad^t"
    b";%A*<_~f3eb7<4(UuvZsH45hAG5KsNxO1%(PD*j370HA!7hRfPi4Undel*SskM~C$-RCnZ6Z+wRhy1;BlxpJ*)yU"
    b"Y_5W>)g#=|Y|rRh~v>Ws(a^(`Dt-$A1SJe|Z<^U=eG2u*`+v#6NseOQW;k-F!Ow5vurW(E)#uuI$yf@|dTtH36Ou"
    b"v6^R$sK^qt5zXVrD#R_HcMj~3`}Gej;wEht&GVWnK~0B!&`<m-7&h2?5)AG&cb1jL^A71kmfAFxG3a&lV|KEsyEh"
    b"Om)%I!Ae#t9)DcFI><8Pt<j4gh2zpsd>b>`#&|Z2ik3PDqlAsw~)!&4dXMV72+om=Zcb*>P3M3K^fR2?Ax9@>Tw0"
    b"W3vvSVs)3+V>(5a|G(jx_^e85bd(m?So=%DDFeFz%{*Zu|`cE=*Y&(v-h6AN8nCYn8<WMO{D#5-4WB1YeC@Kx>VU"
    b"BbV!P#5)|97eHHgXr<^rdsQ9wWnp_}9bdJ7vU<`FVq9dQ`=le8Lo%Yxu+)CXyQ(eV;dZi^odArS^N+P=hwH%-#~*"
    b"1f;P`r9ii#mWHDVbRP3xVUR$W@Ph#VrrrDky~_}sZgd(LkIDL<1?ilCRJ"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
