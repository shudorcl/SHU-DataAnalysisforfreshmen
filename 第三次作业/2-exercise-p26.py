# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:34:13 2019
"""
import numpy as np
names = np.array(['王微', '肖良英', '方绮雯', '刘旭阳','钱易铭'])
subjects = np.array(['Math', 'English', 'Python', 'Chinese','Art', 'Database', 'Physics'])
scores = np.array([[70,85,77,90,82,84,89],[60,64,80,75,80,92,90],[90,93,88,87,86,90,91],[80,82,91,88,83,86,80],[88,72,78,90,91,73,80]])
print(scores[:,subjects=='English']-3)
print(scores.mean(axis=1))
rnd=np.random.randint(-1,2,size=(3,4))
print(rnd)
print(rnd.reshape(1,12).sum())