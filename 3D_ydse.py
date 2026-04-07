import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm
from matplotlib import colors
from mpl_toolkits.mplot3d import axes3d


plt.style.use('dark_background')



S=float(input("whats the screen pos? :"))
t=float(input("t at which to present the snapshot? :"))

x=np.linspace(0,S,1000)
y=np.linspace(-100,100,1000)
z=np.linspace(-100,100,1000)


X,Y=np.meshgrid(x,y)

Γ,ζ=np.meshgrid(y,z)


λ=5*(1e-6)
v=3*(1e8) 
A=1
k=np.pi/λ
ω=v*k

#Sources

s1=(0,0.0001,1)
s2=(0,-0.0001,1)

# Defining the EM waves

def o1(x,y,z,t):

    r1 = np.sqrt((x-s1[0])**2 + (y-s1[1])**2 +(z-s1[2])**2 )
    a=A*np.sin(ω*t-k*r1)/(np.sqrt(r1))
    return a

def o2(x,y,z,t):

    r2 = np.sqrt((x-s2[0])**2 + (y-s2[1])**2 + (z-s2[2])**2)
    a= A*np.sin(ω*t-k*r2)/(np.sqrt(r2))
    return a 

def get_wave():
    wave = np.where(X<=S,((o1(X,Y,1,t) + o2(X,Y,1,t))**2),0)
    return wave

#inst
def get_int_screen(t):
    I=(o1(S,Γ,ζ,t)+o2(S,Γ,ζ,t))**2

    return I



Z = get_wave() # keep the surface height between -1 and 1



fig = plt.figure(figsize=(14, 8))
gs = fig.add_gridspec(3, 2)

ax1 = fig.add_subplot(gs[:, 0], projection='3d')  # large 3D
ax1.plot_surface(X,Y,Z,cmap="RdGy",linewidth=0)

ax2 = fig.add_subplot(gs[0, 1])
ax2.contourf(Γ,ζ,get_int_screen(t),levels=100,cmap="magma")
ax2.grid(True,color="white",linestyle="--")

ax3 = fig.add_subplot(gs[1, 1])
ax4 = fig.add_subplot(gs[2, 1])

plt.tight_layout()
plt.show()


