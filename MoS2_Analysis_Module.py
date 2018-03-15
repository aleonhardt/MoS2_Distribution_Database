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
        deviceCurrent=[]
        deviceWidth=[]
        deviceLength=[]
        for path, subdirList, files in os.walk(root):                
            for f in fnmatch.filter(files,'*.txt'):
                
                Data= np.genfromtxt(os.path.abspath(os.path.join(path,f)), 
                                    autostrip=True, loose=True, delimiter='\t', dtype=None, names=True)

##has to be made more robust
                print(Data.dtype.names)
                length=Data['Length_um']
                width=Data['Width_um']
                current=Data['Drain_Current_Aum']

                for i in range(0, len(current)):
                    if(current[i]>0):
                        deviceCurrent.append(current[i])
                        deviceLength.append(length[i])
                        deviceWidth.append(width[i])
                
                self.MaxCurrent.append(deviceCurrent)
                self.Width.append(deviceWidth)
                self.Length.append(deviceLength)
                deviceCurrent=[]
                deviceWidth=[]
                deviceLength=[]
                print(len(self.MaxCurrent))
    def createDistributions():
        print('Any')
    
    def calculateParameters(self):
        logCurrent=[math.log(y) for y in self.MaxCurrent[1]]
        self.stdDev=np.std(logCurrent)
        print(self.stdDev)
        self.mean=np.exp(np.mean(logCurrent))
        print(self.mean)
        self.coeffVariance=np.sqrt(np.exp(self.stdDev*self.stdDev)-1)
    
    def plotDistributions(self):
        # the histogram of the data
        plt.close('all')
#        for i in range(0,len(self.MaxCurrent)):
        plt.hist(self.MaxCurrent[1], bins=np.logspace(np.log10(1e-13),np.log10(1e-6), 50), edgecolor='black', linewidth=1.2)
        plt.gca().set_xscale("log")
        plt.title('coefficient of variance (log-normal): '+str("{0:.2f}".format(self.coeffVariance)+'%'))
        plt.ylabel('Frequency')
        plt.xlabel('Max Current (A/$\mu$m)')
        plt.show()
