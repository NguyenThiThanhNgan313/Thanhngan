# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:57:24 2024

@author: ASUS
"""

d= float(input("Nhập quãng đường đã đi(km):"))
if d<=1:
    print ("Giá là 20k")
elif d>1 and d<=4 :
    print("giá là:", d*13000)
elif d>=4 and d<=8:
    print ("giá là:",(3*13000)+(d-3)*12000)
else:
    print ("giá là:", 39000+60000+(d-8)*10000)
    m=39000+60000+(d-8)*10000
if m>=100000:
    print("giá là sau khi giảm:", m*(8/100))