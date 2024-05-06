# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:28:36 2024

@author: Formation
"""

def statPoke_init():
    
    # Stat de Bullbizarre
    stats = {
        "Total": 318,
        "HP": 45,
        "Attack": 49,
        "Defense": 49,
        "Sp.Atk": 65,
        "Sp.Def": 65,
        "Speed": 45
    }
    
    texte_Bullbizarre = "\n".join([f"{stat} : {valeur}" for stat, valeur in stats.items()])
    
    
    # Stat de Salamèche
    stats = {
        "Total": 309,
        "HP": 39,
        "Attack": 52,
        "Defense": 43,
        "Sp.Atk": 60,
        "Sp.Def": 50,
        "Speed": 65
    }
    
    texte_Salameche = "\n".join([f"{stat} : {valeur}" for stat, valeur in stats.items()])
    
    
    # Stat de Carapuce
    stats = {
        "Total": 314,
        "HP": 44,
        "Attack": 48,
        "Defense": 65,
        "Sp.Atk": 50,
        "Sp.Def": 64,
        "Speed": 43
    }
    
    texte_Carapuce = "\n".join([f"{stat} : {valeur}" for stat, valeur in stats.items()])
    
    return texte_Bullbizarre, texte_Salameche, texte_Carapuce

