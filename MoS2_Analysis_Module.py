# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import os
import matplotlib.pyplot as plt
import fnmatch
import math
import numpy as np

class MoS2_Analysis:
    
    def __init__(self, path):     
        self.path=path
        self.MaxCurrent=[]
        self.Length=[]
        self.Width=[]
        
        self.loadData(self.path)
        self.calculateParameters()
        self.plotDistributions()
    
    def loadData(self,root):
        for path, subdirList, files in os.walk(root):                
            for f in fnmatch.filter(files,'*.txt'):
                
                Data=np.loadtxt(os.path.abspath(os.path.join(path,f)), delimiter='\t',skiprows=1, unpack=True)
##has to be made more robust
                deviceLength=Data[0]
                deviceWidth=Data[1]
                deviceCurrent=Data[2]

                for i in range(0, len(deviceCurrent)):
                    if(deviceCurrent[i]>0):
                        self.MaxCurrent.append(deviceCurrent[i])
                        self.Width.append(deviceWidth[i])
                        self.Length.append(deviceLength[i])
                
    
    def createDistributions():
        print('Any')
    
    def calculateParameters(self):
        logCurrent=[math.log(y) for y in self.MaxCurrent]
        self.stdDev=np.std(logCurrent)
        print(self.stdDev)
        self.mean=np.mean(self.MaxCurrent)
        print(self.mean)
        self.coeffVariance=np.sqrt(np.exp(self.stdDev*self.stdDev)-1)
    
    def plotDistributions(self):
        # the histogram of the data
        plt.close('all')
        plt.hist(self.MaxCurrent, bins=np.logspace(np.log10(1e-13),np.log10(1e-6), 50), edgecolor='black', linewidth=1.2)
        plt.gca().set_xscale("log")
        plt.title('coefficient of variance (log-normal): '+str("{0:.2f}".format(self.coeffVariance)+'%'))
        plt.ylabel('Frequency')
        plt.xlabel('Max Current (A/$\mu$m)')
        plt.show()
