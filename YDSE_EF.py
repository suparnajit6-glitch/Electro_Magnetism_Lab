from matplotlib.animation import FuncAnimation
import sympy as sp 
import numpy as np
import matplotlib.pyplot as plt


plt.style.use('dark_background')

x,y,z,t=sp.symbols("x y z t")

#position of slits

s1=(0,3,0)
s2=(0,-3,0)

#Position of screen
S=50

v=3*(1e8)
A=10
k=sp.pi
ω=v*k
k_num = np.pi
omega_num = v*k_num

r1 = sp.sqrt((x-s1[0])**2 + (y-s1[1])**2 + (z-s1[2])**2) 
o1= A*sp.sin(ω*t-k*r1)/sp.sqrt(r1)

r2 = sp.sqrt((x-s2[0])**2 + (y-s2[1])**2 + (z-s2[2])**2)
o2= A*sp.sin(ω*t-k*r2)/sp.sqrt(r2)


I_avg=((A**2)/(2*r1))+((A**2)/(2*r2))+((A**2)/((r1*r2)**0.5))*sp.cos(k*(r2-r1))

v1=sp.lambdify((x,y,z,t),o1,"numpy")
v2=sp.lambdify((x,y,z,t),o2,"numpy")

I_avg=sp.lambdify((x,y,z),I_avg,"numpy")







y=np.linspace(-20,20,250)
x=np.linspace(0,100,250)
t=np.linspace(0,500,1000000)

X,Y=np.meshgrid(x,y)

Z=0

r1_grid = np.sqrt((X-s1[0])**2 + (Y-s1[1])**2 + (Z-s1[2])**2)
r2_grid = np.sqrt((X-s2[0])**2 + (Y-s2[1])**2 + (Z-s2[2])**2)
r1_line = np.sqrt((S-s1[0])**2 + (y-s1[1])**2 + (0-s1[2])**2)
r2_line = np.sqrt((S-s2[0])**2 + (y-s2[1])**2 + (0-s2[2])**2)


def field_intensity(t_now):
    wave1 = A*np.sin(omega_num*t_now-k_num*r1_grid)/np.sqrt(r1_grid)
    wave2 = A*np.sin(omega_num*t_now-k_num*r2_grid)/np.sqrt(r2_grid)
    return (wave1 + wave2)**2


def line_intensity(t_now):
    wave1 = A*np.sin(omega_num*t_now-k_num*r1_line)/np.sqrt(r1_line)
    wave2 = A*np.sin(omega_num*t_now-k_num*r2_line)/np.sqrt(r2_line)
    return (wave1 + wave2)**2



fig, axes = plt.subplots(2, 2, figsize=(14, 6))

axis1 = axes[0, 0]
axis  = axes[0, 1]
ax0   = axes[1, 0]
ax_beta = axes[1, 1]

axis1.set_xlim([min(x),max(x)])
axis1.set_ylim([min(y),max(y)])


field = field_intensity(0)
plot1 = axis1.imshow(
    field,
    extent=[min(x), max(x), min(y), max(y)],
    origin="lower",
    aspect="auto",
    cmap="plasma"
)
plt.colorbar(plot1, ax=axis1)

plot=axis.plot(y,I_avg(S,y,0)/max(I_avg(S,y,0)),linestyle='--')
plot, = axis.plot(y, np.zeros_like(y), color="red")

axis.grid(True,color="gray")

axis.set_xlim(min(y), max(y))
axis.set_ylim(0, 4)   # intensity range (since max = (2A)^2 = 4)

ax0.plot(y,I_avg(S,y,0)/max(I_avg(S,y,0)))
ax0.grid(True,color="gray")


def update_sc(frame):
    t_now = t[frame]
    field = field_intensity(t_now)
    plot1.set_data(field)

    intensity = line_intensity(t_now)
    I=intensity/max(intensity)
    
    plot.set_data(y, I)
    return plot1, plot

animation = FuncAnimation(fig=fig,
                          func=update_sc,
                          frames=len(t),
                          interval=1,
                          repeat=True,
                          blit=False)




plt.grid(True,color="white")
plt.show()
