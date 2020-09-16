# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:14:40 2020

@author: kalya
"""

from mpl_toolkits import mplot3d


import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

t = np.linspace(0,100,1000)
a = 1
b = 1

x = a * np.cos(t)
y = a * np.sin(t)
z = b * t

ax.plot3D(x,y,z,'gray')

tdata = 100 * np.random.random(100)

xdata = a * np.cos(tdata) + 0.1 * np.random.randn(100)
ydata = a * np.sin(tdata) + 0.1 * np.random.randn(100)
zdata = b * tdata + 0.1 * np.random.randn(100)

ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');