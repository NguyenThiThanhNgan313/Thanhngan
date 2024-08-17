# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:21:58 2024

@author: ASUS
"""

player= float(input("người chọn(1. kéo, 2. búa,3. bao):"))
from random import randint 
com=randint(1,3)
if com==1:
    print("máy chọn kéo")
elif com==2:
    print("máy chọn búa")
elif com==3:
    print("máy chọn bao")
if com==player:
    print("kết quả hòa")
elif com==1 and player==2:
    print("người thắng")
elif com==1 and player==3:
    print("người thua")
elif com==2 and player==1:
    print("người thua")
elif com==2 and player==3:
    print("người thắng")
elif com==3 and player==1:
    print("người thắng")
elif com==3 and player==2:
    print("người thua")
else:
    print("không hợp lệ")
    