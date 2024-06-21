

from math import pi, sin, asin, sqrt, pow

v=8*[0]

v[0]=174
v[1]=300    
v[2]=1035
v[3]=3
v[4]=4
v[5]=2
v[6]=100
v[7]=40

a=(v[0]-v[5]-v[7])
print("a",a)
b=(-v[1]+v[5]+v[6])
print('b',b)
d=sqrt(pow(a,2)+pow(b,2))
print('d',d)
print(b/d)
alpha=asin(b/d)
print("alpha",alpha)
beta=pi-2*+alpha
print('beta', beta)

radio=b/sin(beta)
print('radio', radio)


radio=(-v[1]+v[5]+v[6])/sin(pi-2*asin(sqrt(pow((v[0]-v[5]-v[7]),2)+pow((-v[1]+v[5]+v[6]),2))/(-v[1]+v[5]+v[6])))