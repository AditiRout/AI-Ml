import numpy as np

p=[1,2,3,4]
a=np.array(p)
print(a)
a=np.zeros(3)
print(a)
print(a.shape)
a.shape=(3,1)
print(a)
z=np.ones(10)
print(type(z[0]))
z=np.empty(3)
print(z)
z=np.linspace(2,10,5)
print(z)

np.random.seed(0)
z1=np.random.randint(10,size=4)
print(z1)
print(z1[0])
print(z1[0:2])
print(z1[-1])