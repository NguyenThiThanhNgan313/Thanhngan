# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:51:49 2024

@author: ASUS
"""

N=int(input("Nhập số nguyên dương có 2 chữ số:"))
if 10<=N<=99:
    hangchuc=N//10
    hangdonvi=N%10
    Tongchuso= hangchuc + hangdonvi
    print("Tổng các chữ số=",Tongchuso)