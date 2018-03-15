# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:44:39 2018

@author: leonha54
"""

class MoS2_Database_Node:
    
    def __init__(self, length, width, maxCurrent, mean, coeffVariance, materialCode=0, grainSize=0, A1gE2g=0, 
                 processSteps=0, comments=""):
        self.length=length
        self.width=width
        self.maxCurrent=maxCurrent
        self.mean=mean
        self.coeffVariance=coeffVariance
        self.materialCode=materialCode
        self.grainSize=grainSize
        self.A1gE2g=A1gE2g
        self.processSteps=processSteps
        self.comments=comments