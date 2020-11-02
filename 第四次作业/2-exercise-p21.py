# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:13:46 2019
"""
import numpy as np
names = np.array(['王微', '肖良英', '方绮雯', '刘旭阳','钱易铭'])
subjects = np.array(['Math', 'English', 'Python', 'Chinese','Art', 'Database', 'Physics'])
scores = np.array([[70,85,77,90,82,84,89],[60,64,80,75,80,92,90],[90,93,88,87,86,90,91],[80,82,91,88,83,86,80],[88,72,78,90,91,73,80]])
print(subjects[[1,2,4]])
print(names[2:])
print(subjects[(subjects=='English')|(subjects== 'Physics')])
print(scores[[1,4]])
print(scores[[2,4]][:,(subjects=='Math')|(subjects== 'Python')])
print(scores[:,(subjects=='Math')|(subjects== 'Art')])
print(scores[(names=='王微')|(names=='刘旭阳')][:,(subjects=='English')|(subjects== 'Art')])
print('由10-19组成的二维数组为')
print(np.arange(10,20).reshape(2,5))