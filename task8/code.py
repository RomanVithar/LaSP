import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


M = 1
Phi = 0
A = 2
betta = 1
k = 1

def update_m(m_t):
    global M
    M = m_t
    update()

def update_betta(betta_t):
    global betta
    betta = betta_t
    update()

def update_k(k_t):
    global k 
    k = k_t
    update()

def update():
    t = np.linspace(0, 10, 100)
    w = np.sqrt(k/M)
    gamma = betta/(2*M)
    y =  A*np.exp(-gamma*t) *np.cos(w*t + Phi)
    ax_1.clear()
    ax_1.plot(t,y)

fig = plt.figure()
ax_1 = fig.add_subplot(2, 1, 1)
fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.4)
change_bar_betta = plt.axes([0.25, 0.1, 0.65, 0.03]) 
change_bar_k = plt.axes([0.25, 0.2, 0.65, 0.03]) 
# change_bar_m = plt.axes([0.25, 0.3, 0.65, 0.03]) 

ch1= Slider(change_bar_betta, 'betta', 0 , 10, valinit=0)
ch2= Slider(change_bar_k, 'k', 0, 100, valinit=40)
# ch3= Slider(change_bar_m, 'm', 0, 20, valinit=1)

ch1.on_changed(update_betta)
ch2.on_changed(update_k)

# ch3.on_changed(update_m)
update_k(40)
update()
plt.show()