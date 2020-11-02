import numpy as np
names=np.array(['大润发','沃尔马','好德','农工商'])
frnames=np.array(['苹果','香蕉','橘子','芒果'])
frtag=np.random.randint(4,11,size=(4,4))
frtag[names=='大润发',frnames=='苹果']+=1
frtag[names=='好德',frnames=='香蕉']+=1
frtag[names=='农工商',:]-=2
avp=frtag[:,frnames=='苹果'].mean()
avm=frtag[:,frnames=='芒果'].mean()
print(avp,avm)
maxshop=names[frtag[:,frnames=='橘子'].argmax()]
print(maxshop)
