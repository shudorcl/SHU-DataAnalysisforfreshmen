
# coding: utf-8
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
stu=pd.read_excel('studentsInfo.xlsx','Group3')
data1=stu[['序号','性别','年龄']]
data2=stu[['序号','身高','体重','成绩']]
nstu=pd.merge(data1,data2,on='序号')
print(nstu)
nstu.sort_values(by='成绩',ascending=True)#👴佛了，虚空月生活费？
nstu['身高排名']=nstu['身高'].rank(method='min',ascending=False)
print(nstu)


