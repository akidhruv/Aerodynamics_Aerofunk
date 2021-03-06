import numpy as np
import matplotlib.pyplot as plt
from math import *
import aerofunk as af

N = 200                           
xStart,xEnd = -2.0,2.0            
yStart,yEnd = -2.0,2.0            
x = np.linspace(xStart,xEnd,N)    
y = np.linspace(yStart,yEnd,N)    
X,Y = np.meshgrid(x,y)            

Uinf = 1.0        
alphaInDegrees = 0.0       
alpha = alphaInDegrees*pi/180


uFreestream = Uinf*cos(alpha)
vFreestream = Uinf*sin(alpha)


psiFreestream = + Uinf*cos(alpha)*Y - Uinf*sin(alpha)*X

NSource = 11
strength = 5.0
strengthSource = strength/NSource
xSource = 0.0
ySource = np.linspace(-1.0,1.0,NSource)

source = np.empty(NSource,dtype=object)
for i in range(NSource):
    source[i] = af.source(strengthSource,xSource,ySource[i])
    source[i].vel(X,Y)



u=np.zeros((N,N),dtype=float)
v=np.zeros((N,N),dtype=float)

for s in source:
    u=np.add(u,s.u)
    v=np.add(v,s.v)
    
u=u+uFreestream
v=v+vFreestream

size = 8
plt.figure(figsize=(size,(yEnd-yStart)/(xEnd-xStart)*size))
plt.grid(True)
plt.xlabel('x',fontsize=16)
plt.ylabel('y',fontsize=16)
plt.xlim(xStart,xEnd)
plt.ylim(yStart,yEnd)
plt.streamplot(X,Y,u,v,density=3,linewidth=1,arrowsize=1,arrowstyle='->')
plt.scatter(xSource*np.ones(NSource,dtype=float),ySource,c='#CD2305',s=80,marker='o')
cont = plt.contourf(X,Y,np.sqrt(u**2+v**2),levels=np.linspace(0.0,0.1,10))
cbar = plt.colorbar(cont)
cbar.set_label('U',fontsize=16);
plt.show()