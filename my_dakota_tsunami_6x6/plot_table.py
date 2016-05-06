#!/usr/bin/env python

import os 
import sys
from matplotlib import pyplot as plt 
import re
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import optparse

stat_file = open(sys.argv[1])

stat_file.readline()

x_axis = []
y_axis = []
z_axis = []

for i in range(625):
	results = stat_file.readline().split()
	#print(results)
	x_axis.append(float(results[2]))
	y_axis.append(float(results[3]))
	z_axis.append(float(results[4]))

del x_axis[619]
del y_axis[619]
del z_axis[619]

fig = plt.figure()

fig.add_subplot(111, projection='3d')
ax = fig.axes[0]
ax.scatter(x_axis,y_axis, z_axis, alpha=0.2)
ax.set_xlabel('width')
ax.set_ylabel('length')
ax.set_zlabel('obj_fn')

ax.scatter([81250], [1e5], [-0.863353], color='green')
ax.scatter([1e5],[9.6530598955e+04] ,[-0.863828], color='red')


plt.show()