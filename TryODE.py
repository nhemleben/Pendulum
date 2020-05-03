
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
dt = 0.001
T= 5

t = np.arange(0.0, T, dt )
s = 1 + np.sin( 2*np.pi* t)

u = np.arange(0.0, T,dt)
u1 = np.arange(0.0, T,dt) 
u11 = np.arange(0.0, T, dt)

#initial data 
#u(0) =0
#u'(0) = 2 pi
#u''(0) = 0
#4 pi^2 u''(t) = - u(t)
u[0] = 0
u1[0] = 1
u11[0] = 0

for i in range(1,len(u)):
    #standard Euler method
    u1[i] = u1[i-1] + dt*u11[i-1]
    u[i]  = u[i-1]  + dt*u1[i-1]
    #Since ODE is cylical
    #u11[i]= (-u[i]) /(4*np.pi*np.pi) 
    u11[i]= (4*np.pi*np.pi)*(-u[i]) 

fig, ax = plt.subplots()
ax.plot(t, s, 'y')
ax.plot(t, u, 'r')
ax.plot(t, u1, 'k')
ax.plot(t, u11, 'b')

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
               title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()







