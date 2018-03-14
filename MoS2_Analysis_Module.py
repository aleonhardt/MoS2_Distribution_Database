# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import os
import matplotlib.pyplot as plt
import fnmatch
import numpy as np

class MoS2_Analysis:
    
    def __init__(self, path):     
        print('Any')
        self.path=path
        self.MaxCurrent=[]
        self.Length=[]
        self.Width=[]
        
        self.loadData(self.path)
    
    def loadData(self,root):
        for path, subdirList, files in os.walk(root):                
            for f in fnmatch.filter(files,'*.txt'):
                
                Data=np.loadtxt(os.path.abspath(os.path.join(path,f)), delimiter='\t',skiprows=1, unpack=True)
##has to be made more robust
                deviceLength=Data[0]
                deviceWidth=Data[1]
                deviceCurrent=Data[2]

                self.Width.append(deviceWidth)
                self.Length.append(deviceLength)
                self.MaxCurrent.append(deviceCurrent)
    
        print(self.MaxCurrent)
    
    def createDistributions():
        print('Any')
    
    def calculateStdDev():
        print('Any')
    
    def plotDistributions():
        print('Any')
