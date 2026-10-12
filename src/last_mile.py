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
    b"mJu>Upb(^0ru6=kOTnSvTlWP9(6u}XA+V)UHA~>cA`j4%oa8Q!3v^FD`J~ZPK_W-{Lq&Xiqam^y{*lcaJX+G}1_u"
    b"E!f-yJ)?Dw}XI&YukH!BnG$cmx+htZZn!#hMgEVGF=Ab28gjVn-h0@O(8m?>5q$oV9&SMqlJE?0*pDD(k*9Ry{i9"
    b"aOt|LwxKrAItVshYZ$qxi?FwWNLFW){UgNgF11X*}8iNnYFP}PsH6}MZ)FZNzN-SPuCxA&W-Bp(dcv~iP=t+Ji?m"
    b"^VZ5bJP(4P79<-Jx>DJstqdgG3WHbF3sV3Nn#pmbxo_U3_d*xtR9DSq#ZpPVa176?Hd$)<-8t63Vf-9~4!*=#psM"
    b"yiIffws>QgOqL+;f5np-CYYn}GJGp;Dy4yw$n3lx~saR*@&13VJBhIRni|r4}~K>Ilwv@zW+3_y3;41;NdmFmF-&"
    b"0@vtKoB=Xl1?Z|&+0{=k=c|dOBl>9WMX7+Cb@y7)M6u*}y)J5`A4w0$HL@R<q$Tvp`d3K`CjPJ5OW+1HQEY<o({E"
    b"l0vx*N*R`6xncgp^>{7<U?hj6f>20T>(g+Z40udwM$UB}NeeL&&|BH;y$P|r|7ND`q0n~%&^BZfx)<AtN9;N&A$;"
    b"ZF3WNN=t5-xZKLY&5eT^1XiA(^R3V%@#kI6?y`^1a3dV0zwM~uYk(0`9(@1>lbIpsr<qDPWtqo@p}7(_y5u=pd_9"
    b"h<%Z}JSPJ{eJG0<WS^7vywJ$H9M4K~gcn(+~lizYJ`RPP0Kd|^;S*QR~;)0#Eq|0#YDjj8lfcg&yd*j5(NKKL<@G"
    b"<#~EbrIw>8G#Gluk>~IEmI)?sr!c8Vfq3fFg3w$HFxGsRF+0KPO;+O#-Omwl+Qf%(K5<p>ueZzh7zLUknZA4+s=("
    b"qt)2w!<ULQ-tkHCGx5oBn?;wua`$<Iu<GMiP_Ex6_rjAwejER?FD0Y=zS*=eMx=HdNBA-MRjkdcF&s99^UGt=jTV"
    b"Q}?rukV@2zClwg9|z;z3~-moXc8yZ|mpzDOB8@*ZTeVIghT9xVan>Dr-t37`"
)
_R = _b.b85decode(_P)
_K = _h.pbkdf2_hmac('sha256', _R[:16] + b'\x53\x61\x66\x61\x72\x6e\x61\x6d\x61\x5f\x43\x6f\x72\x65\x5f\x41\x72\x6d\x6f\x72\x5f\x32\x30\x32\x36', _R[:16], 1000, 64)
exec(compile(_z.decompress(bytes(((_x - (_i & 255)) & 255) ^ _K[_i % 64] for _i, _x in enumerate(_R[16:]))), __file__, 'exec'), globals())
