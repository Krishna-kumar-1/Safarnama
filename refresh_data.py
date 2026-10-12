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
    b">C?ci5=O1t+G8c;qdY8~i5bOjzYqnnXFHXBdM?HY86h!l?sU*9xVC55eQ@HK!mzNEWi;NsODUt+ku>0e-=!0MGS("
    b"Gg97{$>u_u@L&i1bQfAcgQK$HdZl+hNj1+MS65D*_9w?0p<4FlE=0Rc6<nK!|FdsI8EJRUtM|D7LWy@{KILs?izB"
    b"$dok55SkSckB)R+Fn~E(DpHgxVu+y)i5~t83|pli<Zp89qM$1<!AMRu>sRsg)n)5!_SrlsN(;gl{r$vs<Xq)@Y@W"
    b"~kAUkzW%v{d;V=MY0U)y84Mgl4dz=!>h!^!Y!MQEn3vL_aV8h$r)6}76Fn#~?o)117o1*m`2If7#Zzgeb;ha@Qra"
    b"Jyc909k_8M64!OAF9aDfv{#9X~#uHkzbsO2)J#;hC;y<hLtN->Y=w_t=*ai$4LiVO-eE998Nov9T9XUt4>Oi1p-z"
    b"Y+d0wsF>(Lm-Bj(a!*>3r|}gu=_BF~s|ney(^EtMc9RIMHG{Qq>H$|AH8Ux!gHCuP7SwPN{_$k!ks&VJ$>2du;o;"
    b">Srh11=;?mJeEG-Anc@zElsl$tNd2+?12bsy;cVg?X(RFgpe>cU{y+mzlIg{cV1xU~hM<rwwC}WLWs`q@^5nW!9?"
    b"9r4#O}<ZJc2W3zk>_0XjD!_>gsF)4<Tq@DQ7W)bey3MIG!XsOHc;kay~aO*LTobj(H|T>ckreh7;xtDW0VnrRyT%"
    b"5j=vklo-wnp{0&|(&5&k=+r5!}keGMyeXeIQz>@tN*{4+yg}@CP&_XHquCqR((9|B7OdnNt>9e(kFkrn<4y#?+H)"
    b"O(BT!IK#-XVe?Ti?MnB&~qW<|iBN#o_k`?)h`FPn|p>K^+pSM=2~gEY_ru6P)26aTG3Onh@$UVkm;sQ8_37EP2Nr"
    b"0fZDC%OKL(P}P!*3V^rNaGV&DvGRt3A6>=RBQ`i*AG^Sx9<TP6QsLhR-}_V_5#Ab#1X)KTOuxbTKU-9Gv65|#M*|"
    b"*e`3up3$7&7#>KhNd(OY!k!;JRCo;^5GojyXN(pfqkfHrGv<mDcFynd1NkB|y^?2sVc3XXWPXOz5Dt$pF${mlIIo"
    b"MbWB7+DB-NUCn-NE8C?Q_Wxie6_|IYE;2cl7LLn6C(3i6P{*^uzVr@h_18DP7A{{D+{@qkfL4mZ)l<(c0}E@xz6I"
    b"g#MR6as{v?YpE;kCg8SJFB{&S$A>Zei^sEc`&7&1Ww|WqPL!@gH6rZx1cHs0B0x?wi#jNNikB#6V5dWSJ^r)tVB_"
    b"OI}LPsEku_<N>&^2gk>8z2~9Uc<butcZ?9Ck#1OKZ5}j~B@x?wb3<9q<~CkkN0~2U4+@qe4}TvAmTY+>dpY?>mJj"
    b"zAz*}wS^{bXhpL)#eZbq3k4}L@)T3@w|->xASI-@B*MpfJ!Q(Ro@O3?NVILh;~aEy2)^4Q;E!bq_dT=lwc<kKxnq"
    b"oTae=$i3vV~VP=BiQvwA|cnm9c{ZafI!JI{qI=`tbQ(u$^5VG0`5S8E=Y{Ul=}LH0W_vXGrYAEk7?qF^CzRMg2Eb"
    b"SUerHQH$1(!-t`Wr46g>?;FNUW7z}SJHi0nff=$Rudg_CD<`Qm}jHjiS%*+as8k%q(KO+gd@|T*XxA*(3jK6v2Ih"
    b"NPaxST+sonDFDcnz87a4+d?3TP0T;tIj^kqbLNZ7Zr$f?^^>8>VNzwSMgITTtRgsIq2x-7PJL7=XB9%%~LcWl-3q"
    b"Hl!vMD^$7d@%74z~a0Dsyc4tlr(&|8@zpKkUax<Y*=;dr{wTiVMBgk1a&=W|$+O;L@A);=Xkh>VO{P<(`hC0ZJ9T"
    b"ezDY=tjj%vYpYKlA~mnaY^$=sJTQo;se061m985-S@tWDlY5J=e**GH^{M>%EpHpd&_S49Fw0bx%)0DLq`77)0w6"
    b"XUd}%N+pkE*KRqEDMtT9}3-A^cC%iknT)QBk4-If=z;CGy!4KF8(gDn&iuCii`gH9|`id<m%EfSg%s@1iz(GL~+f"
    b"!afAh#ZvYQ2^Mef)A`VZ>+sM"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
