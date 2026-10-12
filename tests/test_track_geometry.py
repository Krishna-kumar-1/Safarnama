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
    b"#;N--_C`l|()y;jheleO`Dk*2azBbmPaS2RviB79A}1@D=`{C>R3u*y?$;m@z#JE*4?%P0H?y!dMNuM<CG4v7R{_"
    b"WW-GAVz%Ergkp5cVq&QR?c59ww}Oi}kR{Oi3UkgOGJ{fJ1>(qBV{PV$(!8)pA3E@A+)R~r>BX<OIa3=HbpHn3W<J"
    b"{NLdLfs(dK|LqY`{$=A&V$yiaeYk0oR7R40T5@esZOzSIyGo;S{yqc?ys4oQ|{ywoy!P6&7g<JhYekS+?LIPVrV0"
    b"ZxVq%ms)Jkto?H7L{(a~-(aH^bHe^jt@eJ7;#g-ty^*Q}hC3;#$Fz|03t`;{Wy7t{<bGE{3^F}<f(cD#p*?ev2>J"
    b"vxX_t@n<<*OE?$c}!1o%uB0+5ZUVGi(r`rS`3xGu1jLxmeWj0D^n3{$3eJc~^Vp#mhcE4i~e7QC3d6Em$!H?g`R{"
    b"O28pxpAL_C-$El2VuWQ|%p7j^3u5}!BmrU=KiU^d@L|@q;p<f2tVzHDqtQ#v!8}`?7}7R$qv_6CZx4hOU7nM0y{9"
    b"%GwDsdbW>@*EiQ#KyTtU_Q!4|cs56>FzXg*H6ld`#if^boiJN9S)_W`LO1D2mhlNv!tL1<);fTc=XHz9}65!mT~b"
    b"u`V)bXE7JH=NRWy#u&;qLGasoPvI4q)P_O%$jaMRr}{p0b;aYUaS2VMl)y2Ls!xC%Z<kJE4F&XVcqidq1mT(=bJd"
    b"C6G#HCt6bcN=e+%-m1oAa)f30PIwu-RYKH$^MY^5l(*C<yVRU(kk(Q<^rK}_qNj>Wvtm2k(2~VWPMULm#^MrCYb;"
    b"1g23wsrOHVP_y<k$U9K9pdNwRbZ^u6q#DXRTcwM^Vp%<p8t!ixie&W(w}LUxqZbU)L7ubl!5`ph$sMa;1drfDooL"
    b"g#ThWM{B-&^LWTvJ`!o*^&)$t*C0eWK3C66vM3HTbwC0^ZHH4z*ff&YNc3iM(;CB{02=T?s?raR%&4mca_yVh4Hq"
    b"bGM-&V(0X#iAHC3Aif~e6HF=Mi===5);emK6$iu4z%{Bv;$bW!6}y^00KC7==h;;ujm6zYKB+@PWjxqp)Q@ydpr("
    b")GgYQ@#{xn}0m%n@4C-M1$Sggb7J7{MYQExa{C)x=xOzUFj_h2@S!P)@Qk-fgaC2?UiA&OMSdRAL(ACa+}CIPZ*V"
    b"LbOBw-3jMMkv65eoNpqQZsqr1XYyQ(J245dWD{XBtg#aGaRw$=UM?63EKE`<C>C!h@|1=HXyg;#MHt^PBw3i_H4O"
    b"=CTW^C426-4gk(EDWLXhFv$V;UCSgl~N=syeK&W<8}TIX`h<;M=FMl&b`|UIlq#o%DY_dC)>S=r5Z0*)>}%3dsnA"
    b">^=fSTaVH0cOlAc1d{!wRJLkcUUk9Po3duwm=kAN`0ximn>Jdyybnd0le(yUX}Tick}YGBN8t{f6mMO$jsjf&>e+"
    b"Z#t+4{f%lqkV{$dOrPU+tdN=nMjc*L{FTCCV67*h`"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
