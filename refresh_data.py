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
    b"zi%izdIThKTv>5vpemZ(O<}SixC-^=ia^<<_$C&AS928eyCyjP{{LC4EUK#>3dk3hGA%}F-UMkuLu3+jK0LduD;1"
    b"Eh=ENU8&cSTDiVk53c;!UuZI?-o774~TOMucc6-uX*arfcb9MzAAN$Co{-a08L?wJ8(4(<mVp2Rmcw8|FN`SP(n%"
    b"k#I9%gE@%fbJcM7g-<uQr@8r_UUT*&}z^uU!+UaI>ZG*)dEX~vTA*{L@XJ<S71waViG<Su_1zNPtq&H#Z@qiv?Kd"
    b"Jh<f|h2=myVV<=GWPY%z681`g`y^$oixxqZWiO~|<OmmYE)#{--fyC2L(d1Vqmr%oP;VBF$>4ZiAt6m-i)}CciOF"
    b"g>Vp4lf@SL6*7Ud=e>Z?s~Zj2VX)esUXajmtbxRMhOU_UGAUJ~mvn{udg*QP^m({;n&FSgjr0rl$wS5@5ge3f*)I"
    b"qR-^8ePUpA(K@Vk!-*3UZy72!E*?tbKID^RfkW>07tU~dJj5^}u!^oJ+ErR>M>YpjA;y4)GxjJ!6FHt!2hK#5#Fu"
    b"Re;4?Wl(})<!WJSQzJ`Qy)JZe!MYohOxrbsc&exYV!3*HOY;L$FV`MjE$K84cls6z~N#Vz!k=CODMe?b(@SJ=>YJ"
    b"qO*x1=jdr!BB80Bn}>&zLZ~#CAjb^?fB`|3!zz8VZkhb@OX-*K}z;EaKU@1z;vR0pN%P_GO8X3UPagyQpVT=o?k&"
    b"kNy3wH3;g+N&i#}|Y*CJs;{Fs%O8*Y^;#{0^glY=x-mzr^D7(>yQX08%U|~Z?RfeVv3Krv$Smk{G_&9=6Nv72e!i"
    b"k8&?vgrgKS1gdVxUB3UM6YS2|;Ks0hx$(>HmY}qMCpQ!!^PriF+Bbd890))e+A`Kt^}sQs~t+l_~0<<n-m5o~ivO"
    b"pk2HS(%(-fiazU^Wok^5G-T(2rs$THQd)_zp&qE!(P_m>3u%rb6iiXvPMsa4S+*sJQ&`{6+4g&&4ND$?P|pRNPDG"
    b";^LxeblC;)cAE@Obp#$ANAZjZ8E92KbA({MjN*B{aeMt?n*)iY=L^p-aENRgtgdF9$P*nUdH#!VDOq&{RT$3tcD!"
    b"-m3_T%q@ePq2P6B^O4N(FO2_vS+){zXnNU)V12SB6vF9TXx}%XLX6H9S3<u{2OsXidLbBiQ(9$HSaqonI@)leYTa"
    b"&)8pKQh6W_Z9U(6qOsVWufP#c#XV%$k#cslW1<R^N0C$+Rw#hMm#%}<u7XjP_`|{Dp|097P@Ou+tR0nYY1G2V~NE"
    b">cGzz?tsfBRcsRRiEYFM*%2418N%cr2d=TYIcC-a>LNy$5?1PsdZ%6t9=O$~u<L=s3byXF4MLroN?V5sW!(Z6np7"
    b"@O~kw@Kc_;E^q})^w}+C!|k3gr48FgLbs-zvh_~Rg&!}cG^R&eWbH?XCsvk!r{sg754_9ujf|<FbrmCbdo(|OY?T"
    b"B*x2$coIw|f%7?+jyWOu3o4}JgG+-y45+LG=4@NuNBhyg!Oeqd=6lM`{}`W91g?D2otFvv~HQTLG~2O6omlG*o2M"
    b"e?F5eX?KM1-=GH(5&jz-utm*zg?`bUJ>}JW06k0IrZi=VKCm$pK+5Z<oC9z^VKlAYSaBRq18JTkwUWPVL_Tpd4}w"
    b"z2q95@P9mE@9r>$PcsQSsbzeS;JAfK5afJ~%hDtYrur=ZXIBRs)%L!;BO-qw#P)7rG&P47fiZw}4YJGK3b;B5ep7"
    b"#epAo+&mcBE0}2law8@Z1&b(+nn;yN>omIPTZHiDTk_`H64$#2Lton(NHJpq&-NQ3%p<D%Q#tErEs*P*=?EQ(9lj"
    b"AFzCfrHr`MF(kGpy;H;psME#IJ1UslgngLA7pBX$7pNB47Ci%lIjh7R#Ba5GWrw832S5-C#iEw{{^}Mv1t^a9``^"
    b"3mM&emDzlqed5fUk*t0zpLkWA!AN%yqI8kQZ7NMx@CCccWv9BJMR%S9^?X|Kvy_NVU0*h~@&j8C#3vz9R5i-_#&U"
    b"a&B!Ol0GiM*7IxuMF_Z?X)ek"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
