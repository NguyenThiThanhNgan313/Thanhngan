# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:25:37 2024

@author: ASUS
"""

duongdentruong=float(input("Nhap do dai doan duong den truong(m):"))
if duongdentruong<300:
    print("Duong den truong qua gan. Thoi!Di bo")
elif duongdentruong>1200:
    print("Duong den truong qua xa. Thoi đi xe máy")
elif duongdentruong>=300 and duongdentruong<=700:
    print ("Duong den truong khong xa. Thoi đi xe đạp")
else:
    print ("Khong xac dinh")
        
        