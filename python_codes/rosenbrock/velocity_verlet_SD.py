#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 11:26:48 2023

@author: leothan
"""

# Imported modules
import numpy as np
from rosenbrock_potential import Rosenbrock_Potential 

class VV_SD():
    
    def __init__(self,r0,h):
        
        #---- DATA INITIALIZAION ---------------------------------------------
        POS = [r0]                                         #<-- Position list
        #---------------------------------------------------------------------
        E0=Rosenbrock_Potential(
            r0[0], r0[1], h).rosenbrock_energy #<-Initial Energy
        E = [E0]
        #---------------------------------------------------------------------
        F0 = Rosenbrock_Potential(r0[0], r0[1], h).force_cart #<-- Initial Force
        F = [F0]                                           #<-- Forces List
        norm_force = [ np.linalg.norm(F[0])]
        #----------------------------------------------------------------------
        v0  = np.array([0,0])                              #<-- Initial Velocity
        VEL = [v0]                                         #<-- Velocity list
        #----------------------------------------------------------------------
        Ncycle = 200
        Np = 0
        Nreset = 0
        #---------------------------------------------------------------------
        #F = F0
        #vel = v0
        #pos = r0
        #---------------------------------------------------------------------
        alpha = 0.1
        t_max = 0.3
        
        k=0
        i=0        
        while k < (Ncycle):
            k = k + 1
            #----- FIRE --------------------------------------------------------
            if  np.dot(VEL[i],F[i])<=0:
                VEL[i] = v0
                h = 0.5*h
                alpha = 0.1
                Np = 0
                Nreset = Nreset + 1
            elif np.dot(VEL[i],F[i])>0:
                Np = Np + 1
                #--- TIME STEP UPGRADE --------------------------------------
                h = min(1.1*h,t_max)
                #h = min(h+0.01,t_max)
  
                
                #----- TIME STEP UPGRADE ------------------------------------
                #if  Np>5:
                                    
                 #   h = min(1.1*h,t_max)
                    
                    #h = min(h+0.01,t_max)
                    
                
            #----- NEW ELEMENT in the lists ----------------------------------- 
            POS.append(0)
            F.append(0)
            norm_force.append(0)
            VEL.append(0)
            E.append(0)
            #--------------- VELOCITY VERLET ----------------------------------
            #-- POSITION ------------------------------------------------------
            POS[i+1] = POS[i] + VEL[i]*h + (F[i]/2)*h**2
            #-- FORCE ---------------------------------------------------------
            F[i+1]=Rosenbrock_Potential(POS[i+1][0], POS[i+1][1], h).force_cart
            norm_force[i+1] =  np.linalg.norm(F[i+1])
            #-- VELOCITY ------------------------------------------------------
            VEL[i+1] = VEL[i] + ((F[i]+F[i+1])/2)*h
            #-- ENERGY -------------------------------------------------------
            E[i+1]=Rosenbrock_Potential(
                POS[i+1][0], POS[i+1][1], h).rosenbrock_energy
                        
            if abs(E[i+1]) < 10**(-8) or np.linalg.norm(F[i+1])<10**(-8):
                
                break
            

            
            #--- LIST position update------------------------------------------
            i = i + 1
            #------------------------------------------------------------------
        
        #------- ATRIBUTES ----------------------------------------------------
        self.positions = POS       
        self.forces = F
        self.velocity = VEL
        self.energy = E
        self.alpha = alpha
        self.h = h
        self.min_force =min(norm_force)
        self.Nreset = Nreset
        #----------------------------------------------------------------------
        # END of code ---------------------------------------------------------

