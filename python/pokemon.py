# -*- coding: utf-8 -*-
"""
Created on Fri May  3 12:07:06 2024

@author: Alliah Brown
"""
from abc import abstractmethod, ABCMeta
import csv
import numpy as np
import pandas as pd


### Extraction des données du projet (dataframe)

<<<<<<< HEAD

<<<<<<< HEAD
"""
<<<<<<< HEAD
=======
coords = pd.read_csv('F:\ENSG\S2\Projet_pokemon\projetPokemonBrown_Cremonese_Ye\data\pokemon_coordinates.csv')
types = pd.read_csv('F:\ENSG\S2\Projet_pokemon\projetPokemonBrown_Cremonese_Ye\data\pokemon_first_gen.csv')
>>>>>>> 44bc78e81b45f1796c550c59cc8f17812f4436eb
"""

=======

# <<<<<<< HEAD
# =======
coords = pd.read_csv('F:\ENSG\S2\Projet_pokemon\projetPokemonBrown_Cremonese_Ye\data\pokemon_coordinates.csv')
types = pd.read_csv('F:\ENSG\S2\Projet_pokemon\projetPokemonBrown_Cremonese_Ye\data\pokemon_first_gen.csv')
# >>>>>>> 44bc78e81b45f1796c550c59cc8f17812f4436eb
=======
coords = pd.read_csv('F:\Projet_Pokemon\projetPokemonBrown_Cremonese_Ye\python\data\pokemon_coordinates.csv')
types = pd.read_csv('F:\Projet_Pokemon\projetPokemonBrown_Cremonese_Ye\python\data\pokemon_first_gen.csv')
>>>>>>> d41a08643e826155b8b06780cc544aed7be62753
>>>>>>> 73d9419d98ae37ad40ff2e5de8256020c6ee38be
# tableau = pd.read_csv('D:\Projet_Pokemon\projetPokemonBrown_Cremonese_Ye\python\data\tableau_type.csv')


# df_types = pd.read_csv('F:\Projet_Pokemon\projetPokemonBrown_Cremonese_Ye\python\data\tableau_type.csv')

# # Convertir le DataFrame en dictionnaire
# tableau_types = df_types.to_dict()

# print(tableau_types)

### Création de la classe Pokemon 


class Pokemon:
    def __init__(self,name,type1,stats):
       
        self.name = name
        self.type1 = type1
        self.stats = stats 
        
        self.total = stats[0]
        self.HP = stats[1]
        self.attack = stats[2]
        self.defense = stats[3]
        self.Sattack = stats[4]
        self.Sdef = stats[5]
        self.speed = stats[6]
        self.life = f"{self.name} ({self.HP} HP)"

    
    def combat(pokemon1, pokemon2):
        print("Début du combat !")
        print(f"{pokemon1.name} VS {pokemon2.name}")
        
    
        if pokemon1.speed >= pokemon2.speed:
            attaquant = pokemon1
            defenseur = pokemon2
        else:
            attaquant = pokemon2
            defenseur = pokemon1


        while True:
            print(f"{attaquant.name} attaque !")
            defenseur.HP -= attaquant.attack
    
            print(f"{defenseur.name} perd {attaquant.attack} PV.")
            print(f"{defenseur.name} a maintenant {defenseur.HP} PV.")
    
            if defenseur.HP <= 0:
                print(f"{defenseur.name} a été vaincu !")
                print(f"{attaquant.name} remporte la victoire !")
                break
    
            attaquant, defenseur = defenseur, attaquant  # Changer de rôle entre attaquant et défenseur pour le prochain tour
    
            
        
    # def combat(self,adv):
        
    #     #Initialisation
    #     print(f'Le combat entre {self.name} et {adv.name} se lance !')
    #     var = True
    #     if self.speed >= adv.speed:
    #         print(self.life, "commence le combat !")
    #     else:
    #         var = False
    #         print(self.life," commence le combat !")
        
    #     ## Déroulement d'un tour 
    #     ###Choix d'une attaque
            
nom = types["Name"] ##Liste de noms des pokémons
typ = types["Type 1"]
    
caract = pd.DataFrame(types,columns=['Total','HP',"Attack","Defense",'Sp. Atk', 'Sp. Def', 'Speed'])



    ### dico qui contient tous les types de pokemon
    
dico_poke1 = {}
for x in range(len(nom)):
    dico_poke1[nom[x].format(x)] = Pokemon(nom[x],typ[x],caract.iloc[x])        
        
dico_poke = dico_poke1
if __name__ == "__main__":

    
    
        
    pikachu = dico_poke["Pikachu"]
    bulbasaur = dico_poke["Bulbasaur"]
    
    print(bulbasaur.HP)
    
    
    # combat(pikachu,bulbasaur)
    
     
