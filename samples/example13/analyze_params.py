# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:19:06 2017

Script to analyze behaviour of 3 calibration parameters out of iterative
algorithm (NCC).

@author: u0078867
"""

import numpy as np
import os
import json
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


variables = [
    "alpha1",
    "y1",
    "x1",
]

# read json files
folder = 'figs' # folder containing .json files
unsortedList = []
for fn in os.listdir(folder):
    if fn.endswith(".json"):
        fp = os.path.join(folder, fn)
        with open(fp) as fh:    
            data = json.load(fh)
            unsortedList.append(data)
            
# sort them by iteration number
sortedList = sorted(unsortedList, key=lambda k: k['iterNum'])
print([c['iterNum'] for c in sortedList])   # visual check

# create params dict
p = {}
for v in variables:
    p[v] = [c['current'][v] for c in sortedList]

# create metric values list
metric = [-c['metric'] for c in sortedList]
print(metric)

# plot parameters path
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x, y, z = p['x1'], p['y1'], np.rad2deg(p['alpha1'])
ax.scatter(x, y, z, c=metric, cmap='coolwarm_r')    # red: low metric, blue: high metric
ax.plot([x[0], x[-1]], [y[0], y[-1]], [z[0], z[-1]], c='k', ls='--')
ax.set_xlabel('x (mm)')
ax.set_ylabel('y (mm)')
ax.set_zlabel('alpha (deg)')

# plot gold standard
xO, yO, zO = 16, -99, -10.9
ax.scatter(xO, yO, zO, c='y', s=40)


plt.show()





