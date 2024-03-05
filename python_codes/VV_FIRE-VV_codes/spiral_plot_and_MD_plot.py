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


def spiral_plot_and_MD_plot(points):
    
    # Activating latex rendering text
    plt.rcParams['text.usetex'] = True
    # Turn interactive plotting on
    #-------------
    plt.ion() # <-- To be able to close graph and keep working
    #-------------  on the console without the console get stuc

    # Definition of Figure and Axes
    fig, axes = plt.subplots(1,1,figsize=(4,4),subplot_kw={'projection': '3d'})
   


    # Function that gives title and axes names
    def title_and_labels(ax, title):
        ax.set_title(title)
        ax.set_xlabel("$x$", fontsize=14)
        ax.set_ylabel("$y$", fontsize=14)
        ax.set_zlabel("$E$", fontsize=14)
 
    radius = np.linspace(0,4,200)
    theta  = np.linspace(0,2*np.pi,200)


    R, THETA = np.meshgrid(radius,theta)
    #E = (np.sin(np.pi*R + THETA/2))**2 + (R**2)/10

    E = lambda r, t: (np.sin(np.pi*r + t/2))**2 + (r**2)/10

    X, Y = R*np.cos(THETA), R*np.sin(THETA)

    #p = axes.plot_surface(X, Y, E(R,THETA), cmap=plt.cm.YlGnBu_r)
    p = axes.plot_wireframe(X, Y, E(R,THETA), alpha=0.2)

        
    title_and_labels(axes, "Spiral_Potential")
    
    for i in points:
        x = i[0]
        y = i[1]
        if x==0 and y>0:
            Ec = lambda x, y: np.sin(np.pi*np.sqrt(x**2 + y**2) + 
                             (np.pi/2)/2)**2 + (x**2 + y**2)/10 
        #---------------------------------------------------------------
        elif x==0 and y<0:
            Ec = lambda x, y: np.sin(np.pi*np.sqrt(x**2 + y**2) + 
                              (-np.pi/2)/2)**2 + (x**2 + y**2)/10 
        #----------------------------------------------------------------      
        elif x==0 and y==0:
            Ec = lambda x, y: np.sin(np.pi*np.sqrt(x**2 + y**2) + 
                             0)**2 + (x**2 + y**2)/10
        #----------------------------------------------------------------
        else:
            Ec = lambda x, y: np.sin(np.pi*np.sqrt(x**2 + y**2) + 
                             np.arctan(y/x)/2)**2 + (x**2 + y**2)/10
    

        axes.scatter(x,y, Ec(x,y), c = "r", s = 50)
        
    


    plt.show()
