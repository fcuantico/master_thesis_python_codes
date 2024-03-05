#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 10:51:27 2023

@author: leothan
"""

import numpy as np

class Spiral_Potential():
    """
    This Class Evaluates the Spiral Potential Function, and calculates
    the Force in Polar and Cartesian coordinates. T
    
    The object of this class will have as atributes the force values in each 
    coordinate system and the spiral "energy" value.
    
    Also as a way to check the analytical derivatives, numerical derivatives
    have been calculated.
    """
    
    
    def __init__(self,x_coordinate,y_coordinate,h):
        
        #--------------- FUNCTION EVALUATION ----------------------
        x = x_coordinate
        y = y_coordinate
        r = np.sqrt(x**2 + y**2) #<--- Radius
        
        if x == 0 and y>0:
            angle = np.pi/2
        
        elif x == 0 and y<0:
            angle = -np.pi/2
        
        elif x == 0 and y == 0:
            angle = 0
            
        elif (x>0 and y>=0) or (x>0 and y<0):
            angle = np.arctan(y/x)
                
        else:
            angle = np.arctan(y/x) + np.pi
        
        E = lambda r, angle: (np.sin(np.pi*r + angle/2))**2 + (r**2)/10
        #-----------------------------------------------------------
        
        #------------- ANALYTIC FORCE ------------------------------
        
        # 1. FORCE in Polar Coordinates -----------------------------
        s = np.sin(2*np.pi*r + angle)
        #c = np.cos(np.pi*r + angle/2)
        DE_Dr = (np.pi*s + r/5)      
        DE_Dangle = (s/2)
        #FORCE_POLAR = -np.array([DE_Dr,DE_Dangle])
        
        # 2. FORCE in Cartesian Coordinates -------------------------
        Fx = DE_Dr*np.cos(angle) - DE_Dangle*(np.sin(angle)/r)
        Fy = DE_Dr*np.sin(angle) + DE_Dangle*(np.cos(angle)/r)
        FORCE_CARTESIAN = -np.array([Fx,Fy])
        
        #self.force_polar = FORCE_POLAR
        self.force_cart  = FORCE_CARTESIAN
        self.spiral_energy = E(r,angle)
        
        # 3. Numerical FORCE calculation ------------------------------
        #    Using Richardson Extrapolation to get O(h**4) by considering
        #    The central formula approximation to the derivative
        #
        #    f'(x0) = (f(x0+h)-f(x0-h))/(2*h),   O(h**2)
        # --------------------------------------------------------------
        if x== 0 and y > 0:
            Ec = lambda x, y: np.sin(np.pi*np.sqrt(x**2 + y**2) + 
                                 (np.pi/2)/2)**2 + (x**2 + y**2)/10 
        #---------------------------------------------------------------
        elif x== 0 and y<0:
            Ec = lambda x, y: np.sin(np.pi*np.sqrt(x**2 + y**2) + 
                                 (-np.pi/2)/2)**2 + (x**2 + y**2)/10 
        #----------------------------------------------------------------  
        elif x== 0 and y == 0:
            Ec = lambda x, y: np.sin(np.pi*np.sqrt(x**2 + y**2) + 
                            0)**2 + (x**2 + y**2)/10
        #----------------------------------------------------------------
        else:
            Ec = lambda x, y: np.sin(np.pi*np.sqrt(x**2 + y**2) + 
                                 np.arctan(y/x)/2)**2 + (x**2 + y**2)/10        
        #-----------------------------------------------------------------
        N1x = lambda h: (Ec(x+h,y) - Ec(x-h,y))/(2*h)
        Dx2 = (1/3)*(4*N1x(h/2)- N1x(h))
        #-----------------------------------------------------------------
        N1y = lambda h: (Ec(x,y+h) - Ec(x,y-h))/(2*h)
        Dy2 = (1/3)*(4*N1y(h/2)- N1y(h))
        #----------------------------------------------------------------
        FORCE_NUMERICAL = -np.array([Dx2,Dy2])
               
        self.Ec = Ec(x,y)
        self.force_numerical = FORCE_NUMERICAL        
        self.deg_angle = angle*180/np.pi
        