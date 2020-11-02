import numpy as np
np.set_printoptions(precision=2)
steps=10
rndwlk=np.random.randint(0,2,size=(3,steps))
rndwlk=np.where(rndwlk>0,1,-1)
pos=rndwlk.cumsum(axis=1)
print(pos)
dists=np.sqrt(pos[0]**2+pos[1]**2+pos[2]**2)
print(dists)
zmaxo=np.abs(pos[2])
print('zmax=',zmaxo.max())
print('distsmin=',dists.min())
