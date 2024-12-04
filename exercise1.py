# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:33:57 2024

@author: s_nguyenlan21
"""
# Übung 1: 
 # jährliche Rendite, also compound annual growth rate 
 # a) 
def cagr_berechnung(AK,EK,t):
    AK >= 0   # AK_abs = abs(AK)
    t >= 0  # unnötig
    CAGR = (EK/AK)**(1/30)  -1
    return(CAGR)   # return um Variable zu speichern 
    
cagr_berechnung(100,700,30)  

# b) berechnung von Endkapital 
Rendite = cagr_berechnung(100,700,30)

print(120*(1+Rendite)**30)