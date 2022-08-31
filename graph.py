# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 22:56:31 2022

@author: rijuj
"""


import matplotlib.pyplot as plt
import csv

x = []
y = []

with open ('example.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
        
plt.plot(x,y, label = 'Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph')
plt.legend()
plt.show()