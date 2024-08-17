# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:50:16 2024

@author: ASUS
"""

import calendar

year = int(input("Nhập năm: "))
is_leap = calendar.isleap(year)
print(f"{year} là năm nhuận" if is_leap else f"{year} không phải là năm nhuận")
