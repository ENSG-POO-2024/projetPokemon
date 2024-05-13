# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:28:36 2024

@author: Formation
"""

from pokemon import dico_poke


def statPoke_init():
    """
    La fonction donne les stats des trois premiers pokémons de départ

    Returns
    -------
    texte_Bullbizarre : TYPE
        DESCRIPTION.
    texte_Salameche : TYPE
        DESCRIPTION.
    texte_Carapuce : TYPE
        DESCRIPTION.

    """
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


def statPoke(nomPoke):

    info_pokemon =  '\n'.join(str(dico_poke[nomPoke].stats).split('\n')[:-1])
    # Diviser la série en fonction des sauts de ligne
    # Supprimer la dernière ligne inutile
    # Récupérer les données des pokémons
    
    info_pokemon += '\n'
    info_pokemon += str(dico_poke[nomPoke].type1)
    # Récupérer le type du pokémon
    
    return info_pokemon






    
    
    
    
    
    
    
    
    
    