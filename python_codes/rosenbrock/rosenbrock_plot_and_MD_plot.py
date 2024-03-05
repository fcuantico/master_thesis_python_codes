#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 10:20:29 2023

@author: leothan
"""

# Imported packages:
import numpy as np
import matplotlib as mpl
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt 


def rosenbrock_plot_and_MD_plot(points):
    
    # Activating latex rendering text
    plt.rcParams['text.usetex'] = True
    # Turn interactive plotting on
    #-------------
    plt.ion() # <-- To be able to close graph and keep working
    #-------------  on the console without the console get stuc

    # Definition of Figure and Axes
    #fig, axes = plt.subplots(1,1,figsize=(12,7),subplot_kw={'projection': '3d'})
    fig,axes=plt.subplots(1,1,figsize=(12,7))



    def title_and_labels(ax, title):
        ax.set_title(title)
        ax.set_xlabel("$x$", fontsize=16)
        ax.set_ylabel("$y$", fontsize=16)
        ax.set_zlabel("$f(x,y)$", fontsize=16)
    
    a = 1

    b = 5
    
    x =  np.linspace(-2, 3,100)
    y =  np.linspace(-1, 3,100)

    X, Y = np.meshgrid(x,y)

    E = lambda x,y: (a-x)**2  + b*(y-x**2)**2

    Z = E(X,Y)


   
    cp = axes.contour(X, Y, Z,np.logspace(-0.5,3.5,7,base=5))
    #cp = axes.contour(X, Y, Z,7)
    #cp = axes.contourf(X, Y, Z,np.logspace(-0.5,3.5,6,base=5))
    fig.colorbar(cp) # Add a colorbar to a plot
    axes.set_title('Contours Plot')
    axes.set_xlabel('x')
    axes.set_ylabel('y ')
    #-------------

   
    
    #for i in points:
    #    x = i[0]
    #    y = i[1]
        
    #    axes.scatter(x,y, c = "r", s = 50)
      
    x_coord = []
    y_coord = []
    for i in points:
        x_coord.append(i[0])
        y_coord.append(i[1])
        
        axes.plot(x_coord,y_coord,color='red')


    plt.show()