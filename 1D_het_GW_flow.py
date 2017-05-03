# -*- coding: utf-8 -*-
"""
1D Heterogeneous Groundwater Flow Model

by Patrick O'Hara

All units are SI

The following script was written to solve for hydraulic head given boundary 
condition hydraulic head values for both ends of the model. 

Hydraulic Conductivity (k) can be set to different values for different
lengths of the model. Currently there are 3 zones of varying hydraulic
conductivity.

Porosity (n) can be set to different values for differnt lengths of the model.
Currently there are 3 zones of varying porosity.

Distance (x) is set by making a numpy array of intigers from 1 though 100 and 
and then multiplying each value in the array by the number needed to get desired 
distance when multiplied by 100.

Darcy's Law is used to solve for change in h for each time step.



"""

import numpy as np
from matplotlib import pyplot as plt

h = np.ogrid[444:430:100j] #sets generic hydraulic gradient based on boundary con.

k = 1. *np.arange(99) # hydraulic conductivity - 99 point resolution
k[:33] = 2.84E-5 #(m/s)
k[33:66] = 1.69E-5 #(m/s)
k[66:] = 2.84E-5 #(m/s)

n = 1. *np.arange(99) # porosity - 99 point resolution
n[:33] = 0.40 #(-) fraction of pore space
n[33:66] = 0.35 #(-) fraction of pore space
n[66:] = 0.40 #(-) fraction of pore space

x = 100. * np.arange(100) # 10000 m from h[0] to h[-1]

dt = 10 * 3.15E7 # years (3.15E7 is seconds per year)


for i in range(int(6000)):

    dh = np.diff(h) #change in head between points   
    dx = np.diff(x) #distance between each point on x
   
    q = -k*n*(dh/dx) #groundwater velocity based on Darcy's Law
    q = np.around(q,decimals=10) 
    x_inner = np.cumsum(dx) 
    dx_inner = np.diff(x_inner)

    dq = np.diff(q)

    dh_dt = -dq / dx_inner #change in head over change in time
    change = dh_dt*dt
    change = change[:-1]
    h[1:-2] = h[1:-2] + change
    

plt.plot(x, h, 'b-', linewidth=2) 
plt.xlabel('Distance m')
plt.ylabel('Hydraulic Head (m asl)') 
plt.title("Hydraulic Head over Distance")

plt.show()