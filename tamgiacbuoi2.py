# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:47:26 2024

@author: ASUS
"""

a= float(input("Nhập a:"))
b= float(input("Nhập b:"))
c= float(input("Nhập c:"))
if a+b>c or a+c>b or c+b>a:
    print ("Ba cạnh này tạo thành một tam giác")
else:
    print("Ba cạnh này không tạo thành tam giác")
if a==b==c:
    print ("Ba cạnh tạo thành tam giác đều")
elif a**2+b**2==c**2:
    print("Ba cạnh tạo thành tam giác vuông")
elif a==b or a==c or b==c:
    print ("Ba cạnh tạo thành tam giác cân")
else:
    print ("Ba cạnh tạo thành tam giác thường")
    