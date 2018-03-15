# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import os
import matplotlib.pyplot as plt
import MoS2_Database_Node as MDN
import fnmatch
import math
import numpy as np
import re

class MoS2_Analysis:
    
    def __init__(self, path, plot=False, plotNum=-1):     
        self.path=path
        self.MaxCurrent=[]
        self.Length=[]
        self.Width=[]
        self.ID=[]
        self.MoS2_Database=[]
        
        self.loadData(self.path)
        self.createDatabase()
        if plot:
            self.plotDistributions()
        else:
            if plotNum>=0:
                self.plotDistributions(num=plotNum)
    
    def loadData(self,root):
        deviceCurrent=[]
        deviceWidth=[]
        deviceLength=[]
        for path, subdirList, files in os.walk(root):                
            for f in fnmatch.filter(files,'*.txt'):
                
                Data= np.genfromtxt(os.path.abspath(os.path.join(path,f)), 
                                    autostrip=True, loose=True, delimiter='\t', dtype=None, names=True)

##has to be made more robust
#                print(Data.dtype.names)
                length=Data['Length_um']
                width=Data['Width_um']
                current=Data['Drain_Current_Aum']

                for i in range(0, len(current)):
                    if(current[i]>0):
                        deviceCurrent.append(current[i])
                        deviceLength.append(length[i])
                        deviceWidth.append(width[i])
                        
                
                self.ID.append(re.findall(r"([0-9]*-[0-9]*)", f)[0])
                self.MaxCurrent.append(deviceCurrent)
                self.Width.append(deviceWidth)
                self.Length.append(deviceLength)
                deviceCurrent=[]
                deviceWidth=[]
                deviceLength=[]

                
    def createDatabase(self):
        for i in range(0,len(self.MaxCurrent)):
             mean, stdDev, coeffVariance= self.calculateParameters(i)
             self.createDatabaseNodes(self.ID[i], self.Length[i], self.Width[i], self.MaxCurrent[i], mean, coeffVariance)
    
    def calculateParameters(self, index):
        logCurrent=[math.log(y) for y in self.MaxCurrent[index]]
        stdDev=np.std(logCurrent)
        mean=np.exp(np.mean(logCurrent))
        coeffVariance=np.sqrt(np.exp(stdDev*stdDev)-1)
        return mean, stdDev, coeffVariance
        
    def createDatabaseNodes(self,ID, length, width, maxCurrent, mean, coeffVariance):
       self.MoS2_Database.append(MDN.MoS2_Database_Node(ID, length, width, maxCurrent, mean, coeffVariance))
        
         
    def saveDatabase(self):
         print('Any')
         
    def plotDistributions(self, num=0):
        plt.figure()
        plt.hist(self.MoS2_Database[num].maxCurrent, bins=np.logspace(np.log10(1e-13),np.log10(1e-6), 50), edgecolor='black', linewidth=1.2)
        plt.gca().set_xscale("log")
        plt.title(self.MoS2_Database[num].ID+': coefficient of variance (log-normal): '+str("{0:.2f}".format(self.MoS2_Database[num].coeffVariance)+'%'))
        plt.ylabel('Frequency')
        plt.xlabel('Max Current (A/$\mu$m)')
        plt.show()
