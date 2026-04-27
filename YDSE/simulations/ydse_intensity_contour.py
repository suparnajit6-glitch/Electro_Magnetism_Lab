from matplotlib.animation import FuncAnimation 
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

#continuous vars

y=np.linspace(-20,20,250)
x=np.linspace(0,100,250)
z=0
t=np.linspace(0,1000,10000)

#Position of slits

s1=(0,5,0)
s2=(0,-5,0)

#Position of screen

S=float(input("Type the screen pos. wrt Origin (x=0):"))

#Screen coordinate system

χ=np.linspace(min(y),max(y),250)
γ=np.linspace(min(y),max(y),250)

χ,γ=np.meshgrid(χ,γ)


#Setting up the constants and parameters

v=3*(1e8) 
A=10
k=np.pi
ω=v*k

# Defining the EM waves

def o1(x,y,z,t):

    r1 = np.sqrt((x-s1[0])**2 + (y-s1[1])**2 + (z-s1[2])**2) 
    return A*np.sin(ω*t-k*r1)/np.sqrt(r1)

def o2(x,y,z,t):

    r2 = np.sqrt((x-s2[0])**2 + (y-s2[1])**2 + (z-s2[2])**2)
    return A*np.sin(ω*t-k*r2)/np.sqrt(r2)

# Grid

X,Y=np.meshgrid(x,y)
Z=0

def field_intensity(t_now):
    
    wave1 = o1(X,Y,Z,t_now)
    wave2 = o2(X,Y,Z,t_now)
    
    I=np.where(x<=S,(wave1 + wave2)**2,0)
    
    return I

# getting the inst intensity at screen (x=S)

def line_intensity(y,t_now):
    
    wave2 = o2(S,y,0,t_now)
    wave1 = o1(S,y,0,t_now)
    
    return (wave1 + wave2)**2

def screen_intensity(y,z,t_now):

    wave1 = o1(S,y,z,t_now)
    wave2 = o2(S,y,z,t_now)

    return (wave1 + wave2)**2
    



fig, axes = plt.subplots(2, 2, figsize=(14, 8))

axis1 = axes[0, 0]
axis  = axes[0, 1]
ax0   = axes[1, 0]
axβ   = axes[1, 1]

axis1.set_xlim([min(x),max(x)])
axis1.set_ylim([min(y),max(y)])
axis1.axvline(x=S,color="white",linestyle=":",label="Screen")

axis1.legend()

field = field_intensity(0)

plot1 = axis1.imshow(
    field,
    extent=[min(x), max(x), min(y), max(y)],
    origin="lower",
    aspect="auto",
    cmap="magma"
)
plt.colorbar(plot1, ax=axis1)



def tavg_int():
    δI=np.zeros_like(y)  # 1D accumulator for intensity along the screen line.
    ΔI=np.zeros_like(γ)  # 2D accumulator for intensity over the screen plane.


    for n in t:  # Loop over all sampled times for the full time average.
        I1_1D=line_intensity(y,n)  # Instantaneous 1D intensity at time n.
        I1_2D = screen_intensity(χ,γ,n)  # Instantaneous 2D intensity at time n.

        δI+=I1_1D  # Add this time slice to the 1D running total.
        ΔI+=I1_2D  # Add this time slice to the 2D running total.
    
    return δI/len(t) , ΔI/len(t)  # Convert totals into time-averaged intensities.


I1D, I2D = tavg_int()  # compute once



plot=axis.plot(y,I1D/np.max(I1D),linestyle='--')
plot, = axis.plot(y, np.zeros_like(y), color="red")

axis.grid(True,color="gray")
axis.set_xlim(min(y), max(y))
axis.set_ylim(0, 4)   # intensity range (since max = (2A)^2 = 4)



ax0.plot(y,I1D/np.max(I1D))
ax0.grid(True,color="gray")


cont=axβ.contourf(χ,γ,I2D/np.max(I2D),levels=50,cmap="magma")

axβ.grid(True,color="gray",linestyle="--")
fig.colorbar(cont,ax=axβ)



def update_sc(frame):
    t_now = t[frame]
    field = field_intensity(t_now)
    plot1.set_data(field)

    intensity = line_intensity(y,t_now)
    I=intensity/max(intensity)
    
    plot.set_data(y, I)
    return plot1, plot

animation = FuncAnimation(fig=fig,
                          func=update_sc,
                          frames=len(t),
                          interval=33,
                          repeat=True,
                          blit=False)



plt.grid(True,color="white")
plt.show()



