# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 15:52:21 2024

@author: ASUS
"""

import math
a=float(input("Nhập a:"))
b=float(input("Nhập b:"))
bt1=math.sqrt(a)-math.sqrt(b)
bt2=a**(1/4)-b**(1/4)
bt3=math.sqrt(a)+(a*b)**(1/4)
bt4=a**(1/4)+b**(1/4)
ketqua=(bt1/bt2)-(bt3/bt4)
print("kết quả=",  round(ketqua,3))