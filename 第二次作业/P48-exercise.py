# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 21:16:11 2019
"""
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from numpy import NaN
stu=pd.read_excel('studentsInfo.xlsx','Group1',index_col=0)
stu['案例教学']=NaN
stu.dropna(thresh=7)
stu.dropna()
stu.fillna({"体重":stu['体重'].mean(),'成绩':stu['成绩'].mean()})
stu['年龄']=stu['年龄'].fillna(method='ffill')
stu.fillna({'月生活费':stu['月生活费'].median()})






