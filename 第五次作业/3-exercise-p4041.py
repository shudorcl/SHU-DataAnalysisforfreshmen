# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:46:33 2019

@author: AliceKiller
"""
import pandas as pd
import numpy as np
data=pd.Series([30,25,27,41,25,34],index=['a','b','c','d','e','f'])
temp=pd.Series([27],index=["g"])
data=data.append(temp)
print(data)
data['d']=40
print(data)
print(data[data.values>=27])
#newdata=data.drop(data.index[0:3])#看来drop只能用目录吗，，，
newdata=data.drop(data.index[1:3])
print(newdata)
fdata=[[1,2,3],[4,5,6],[7,8,9]]
ddf=pd.DataFrame(fdata,index=['a','b','c'],columns=['one','two','three'])
print(ddf)
print(ddf.loc[:,['two','three']])
print(ddf.iloc[[0,2],[0,2]])
ddf1=(ddf[ddf['one']>2])
print(ddf1)
ddf1['four']=10
print(ddf1)
ddf1[ddf1>9]=8
print(ddf1)
print(ddf1.drop(['c','b'],axis=0))