from matplotlib.animation import FuncAnimation
import sympy as sp 
import numpy as np
import matplotlib.pyplot as plt


plt.style.use('dark_background')

x,y,z,t=sp.symbols("x y z t")

#position of slits

s1=(0,3,0)
s2=(0,-3,0)

v=3*(1e8)
A=10
k=sp.pi
ω=v*k

r1 = sp.sqrt((x-s1[0])**2 + (y-s1[1])**2 + (z-s1[2])**2) 
o1= A*sp.sin(ω*t-k*r1)/sp.sqrt(r1)

r2 = sp.sqrt((x-s2[0])**2 + (y-s2[1])**2 + (z-s2[2])**2)
o2= A*sp.sin(ω*t-k*r2)/sp.sqrt(r2)

v1=sp.lambdify((x,y,z,t),o1,"numpy")
v2=sp.lambdify((x,y,z,t),o2,"numpy")






def f(x,y,z,t):

    a=v1(x,y,z,t)+v2(x,y,z,t)

    return a**2


y=np.linspace(-20,20,250)
x=np.linspace(0,100,250)
t=np.linspace(0,2000,1000000)

X,Y=np.meshgrid(x,y)

Z=0

fig, (axis1, axis) = plt.subplots(1, 2, figsize=(14, 6))
axis1.set_xlim([min(x),max(x)])
axis1.set_ylim([min(y),max(y)])


field = f(X,Y,Z,0)
plot1 = axis1.imshow(
    field,
    extent=[min(x), max(x), min(y), max(y)],
    origin="lower",
    aspect="auto",
    cmap="magma"
)
plt.colorbar(plot1, ax=axis1)

plot, = axis.plot(y, np.zeros_like(y), color="red")

axis.set_xlim(min(y), max(y))
axis.set_ylim(0, 4)   # intensity range (since max = (2A)^2 = 4)
avg = np.mean([f(40,y,0,ti) for ti in t[:50]], axis=0)

def update_sc(frame):
    t_now = t[frame]
    field = f(X,Y,Z,t_now)
    plot1.set_data(field)

    intensity = f(40, y, 0, t_now)
    I=intensity/max(intensity)
    
    plot.set_data(y, I)
    return plot1, plot

animation = FuncAnimation(fig=fig,
                          func=update_sc,
                          frames=len(t),
                          interval=10,
                          repeat=True,
                          blit=False)




plt.grid(True,color="black")
plt.show()
