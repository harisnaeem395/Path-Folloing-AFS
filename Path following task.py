# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 22:56:17 2022

@author: Haris
"""

import numpy as np 
import matplotlib.pyplot as plt 


#v= int (input("Please enter linear velocity"))
#w= int (input("Please enter angular velocity"))

# linear and angular velocity vectors defined
v= np.array ([10,12,13,15])
w= np.array ([10,20,25,30])

def getpos(x,y):
    x,y= (0.5,0.5) # robot initial position 
    x1, y1= (2,1)
    plt.plot (x,y, color='red')
    plt.show()
    plt.plot (x1,y1)
    return x,y

def getpoints(v,w):
    hi=w
    xi= v*np.cos(hi)
    yi= v*np.sin(hi)
    epf= yi # Path (Pd) is on x-axis so Qd to Pd dist is yi 
    lr= np.linalg.norm(xi)
    lf= np.linalg.norm (yi)
    for B in range(30):
        u= (w*lf*np.cos(B)+ (w*lr)- v*np.sin(B))/lr #rearranging eq (4) to get obtain u
        print ("Control output", u)
    #plt.xlim()
    plt.title("Control Signal Output")
    plt.plot (u, label= "Control Signal Output")
    #plt.show()
    plt. title("Control Output")
    plt.plot(epf, label="Error")
    plt.legend()
    plt.show()
    plt.plot(xi,yi)
    plt.title ("Robot Path")
    plt.show()
    #plt.show()           
    
    return u,epf

def error(u):
    epf= y
    return y

def plot (points, error):
    for i in range(50):
        x= plt.plot (u)
        plt.plot (epf)
        plt.title("Control Signal Output")
        return x
    

getpoints(v,w)
plot (points, error)



 