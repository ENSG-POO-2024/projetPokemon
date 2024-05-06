# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:50:39 2024

@author: Formation
"""


import math

class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def NewX(self):
        return self.x
    
    def NewY(self):
        return self.y
    
    def NewCoord(self,NEWX,NEWY):
        self.x = NEWX
        self.y = NEWY
        
    def distance(self,c):
        return math.sqrt((c.x - self.x)**2 + (c.y - self.y)**2)
    
    def proche(self,c):
        return self.distace(c) >= 10
    
    def __str__(self):
        return f"[X = {self.x} - Y = {self.y}]"
    
    