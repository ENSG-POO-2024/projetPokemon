import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextBrowser, QFrame,QDialog,QVBoxLayout,QMainWindow

from PyQt5.QtGui import QFont, QFontDatabase,QPixmap
from PyQt5.uic import loadUi
from Wilkommen2 import Ui_Form
from abc import abstractmethod, ABCMeta
import visualisation_pokemon as vp
import random as rd
import math
import copy


types = ["Steel", "Fighting", "Dragon", "Water", "Electric", "Fire", "Fairy", "Ice", "Bug", "Normal", "Grass", "Poison", "Psychic", "Rock", "Ground", "Ghost", "Dark", "Flying"]



# Matrice des affinités de types

affinite_types = [

    [0.5, 1, 1, 0.5, 0.5, 0.5, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],                  

    [2, 1, 1, 1, 1, 1, 0.5, 2, 0.5, 2, 1, 0.5, 0.5, 2, 1, 0, 2, 0.5],                

    [0.5, 1, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],                        

    [1, 1, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 0.5, 1, 1, 2, 2, 1, 1, 1],                    

    [1, 1, 0.5, 2, 0.5, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 0, 1, 1, 2],                    

    [2, 1, 0.5, 0.5, 1, 0.5, 1, 2, 2, 1, 2, 1, 1, 0.5, 1, 1, 1, 1],                  

    [0.5, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 2, 1],                    

    [0.5, 1, 2, 0.5, 1, 0.5, 1, 0.5, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2],                  

    [0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 1, 2, 0.5, 2, 1, 1, 0.5, 2, 0.5],            

    [0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 0, 1, 1],                      

    [0.5, 1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 1, 0.5, 0.5, 1, 2, 2, 1, 1, 0.5],            

    [0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 0.5, 0.5, 1, 1],                  

    [0.5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 0, 1],                      

    [0.5, 0.5, 1, 1, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 0.5, 1, 1, 2],                    

    [2, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 0],                      

    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 1, 2, 0.5, 1],                        

    [1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1, 2, 1, 1, 2, 0.5, 1],                    

    [0.5, 2, 1, 1, 0.5, 1, 1, 1, 2, 1, 2, 1, 1, 0.5, 1, 1, 1, 1]                     

]


class Pokemons(metaclass=ABCMeta):
    """
    Classe représentant les Pokémon du jeu.

    Attributes:
    ----------
    name : str
        Le nom du Pokémon.
    stats : dict
        Dictionnaire contenant les statistiques du Pokémon.
    niveau : int
        Le niveau du Pokémon.
    exp : int
        L'expérience actuelle du Pokémon.
    charge : str, 
        L'attaque de base du Pokémon (Charge de type 'Normal').
    """

    def __init__(self, name):
        """
        Initialise un objet Pokémon avec son niveau, nom et éventuellement une attaque de base.
        
        Parameters:
        ----------
        name : str
            Le nom du Pokémon.

        Returns:
        -------
        None
        """
        self.charge='Normal'
        self.name = name
        self.stats = copy.deepcopy(vp.pokemon_dict[name])
        self.niveau = self.stats['Niveau']
        self.exp=vp.exp_necessaire_par_niveau[self.niveau-1]
        

    def __str__(self):
        """
        Retourne une chaîne de caractères représentant les caractéristiques du Pokémon.

        Returns:
        -------
        str
            Chaîne de caractères représentant les caractéristiques du Pokémon.
        """
        return str(self.name) 
    

    def monter_niveau(self,exp_gagne):
        """
        Fait monter de niveau un Pokémon en fonction de l'expérience gagnée.

        Parameters:
        ----------
        exp_gagne : int
            L'expérience gagnée par le Pokémon.

        Returns:
        -------
        None
        """
        ancien_niveau=self.niveau
        self.exp+=exp_gagne
        print(f"{self.name} a gagné {exp_gagne} d'exp")
        for i in range(len(vp.exp_necessaire_par_niveau)):
            if vp.exp_necessaire_par_niveau[i]<=self.exp<vp.exp_necessaire_par_niveau[i+1]:
                self.niveau=vp.exp_niveau_pokemon[vp.exp_necessaire_par_niveau[i]]
        diff=self.niveau-ancien_niveau
        if diff!=0:
            print(f"{self.name} monte au lvl {self.niveau}")
            self.stats['Total']+=6*(2*diff)
            self.stats['Niveau']=self.niveau
            if  self.stats['HP'][0]!=0 :
                self.stats['HP'][0]+=2*diff
            self.stats['HP'][1]+=2*diff
            self.stats['Attack']+=2*diff
            self.stats['Defense']+=2*diff
            self.stats['Sp. Atk']+=2*diff
            self.stats['Sp. Def']+=2*diff
            self.stats['Speed']+=2*diff
        else :
            print(f"{self.name} est lvl {self.niveau}")

        if self.niveau==30 and self.stats['Evolution']==2:
                self.name=vp.pokemons_liste[self.stats['Numero']]
                self.stats['Name']=vp.pokemons_liste[self.stats['Numero']]
                self.stats['Evolution']-=1
                print('evolution')

        elif self.niveau==30 and self.stats['Evolution']==3 :
                self.name=vp.pokemons_liste[self.stats['Numero']]
                self.stats['Name']=vp.pokemons_liste[self.stats['Numero']]
                self.stats['Evolution']=0
                print('evolution')

        elif self.niveau==40 and self.stats['Evolution']==1 :
                self.name=vp.pokemons_liste[self.stats['Numero']]
                self.stats['Name']=vp.pokemons_liste[self.stats['Numero']]
                self.stats['Evolution']-=1
                print('evolution')


            

    

    def attaquer(self, attaque, pokemon2):
        """
        Fonction pour attaquer un autre Pokémon.

        Parameters:
        ----------
        attaque : tuple
            Tuple contenant le type de l'attaque sa puissance et son nom.
        pokemon2 : Pokemons
            Le Pokémon attaqué.

        Returns:
        -------
        None
        """
        if self.stats['Type 1'] == attaque[0]:
            STAB = 1.5
        else:
            STAB = 1

        if pokemon2.stats['Type 2'] not in types :
            a, b = types.index(attaque[0]), types.index(pokemon2.stats['Type 1'])
            type1 = affinite_types[a][b]
            R = math.floor((rd.uniform(217, 255) * 100) / 255)
            deg = ((((((self.niveau * 2 / 5) + 2) * (attaque[1]) * (self.stats['Sp. Atk']) / 50) / (pokemon2.stats['Sp. Def'])) + 2) * R / 100) * STAB * type1
            deg = math.floor(deg)
            pokemon2.stats['HP'][0] -= deg
            if pokemon2.stats['HP'][0]<0:
                pokemon2.stats['HP'][0]=0
            print (f"{self.name} utilise {attaque[2]}  sur {pokemon2.name}  et lui inflige {deg} points de dégâts.")
            if  type1==0 :
                print("L'attaque n'a aucun effet !")

            elif type1==0.5 :
                print("Ce n'est pas très efficace ...")

            elif type1==2:
                print("C'est super efficace !")

        else :
            a, b = types.index(attaque[0]), types.index(pokemon2.stats['Type 1'])
            c,d = types.index(attaque[0]), types.index(pokemon2.stats['Type 2'])
            type1 = affinite_types[a][b]
            type2 = affinite_types[c][d]
            R = math.floor((rd.uniform(217, 255) * 100) / 255)
            deg = ((((((self.niveau * 2 / 5) + 2) * (attaque[1]) * (self.stats['Sp. Atk']) / 50) / (pokemon2.stats['Sp. Def'])) + 2) * R / 100) * STAB * type1 * type2
            deg = math.floor(deg)
            pokemon2.stats['HP'][0] -= deg
            if pokemon2.stats['HP'][0]<0:
                pokemon2.stats['HP'][0]=0
            print (f"{self.name} utilise {attaque[2]}  sur {pokemon2.name}  et lui inflige {deg} points de dégâts.")
            if  type1*type2==0 :
                print("L'attaque n'a aucun effet !")

            elif type1*type2<=0.5 :
                print("Ce n'est pas très efficace ...")

            elif type1*type2>=2:
                print("C'est super efficace !")


    def est_ko(self):
        """
        Vérifie si le Pokémon est KO.

        Returns:
        -------
        bool
            True si le Pokémon est KO, False sinon.
        """
        return self.stats['HP'][0] <= 0
    

class Dresseur:

    def __init__(self, name):
        """
        Initialise un joueur avec son nom.

        Parameters:
        ----------
        name : str
            Le nom du joueur.

        Returns:
        -------
        None
        """
        self.name = name
        self.pokemon_equipe = []


    def __str__(self):
        """
        Retourne une chaîne de caractères représentant les  Pokémons du dresseur.

        Returns:
        -------
        str
            Chaîne de caractères représentant les caractéristiques du Pokémon.
        """
        return f" {self.name} a {len(self.pokemon_equipe)} pokemon: "
    

    def tout_est_ko(self):
        """
        Vérifie si tous les Pokémon du joueur sont KO.

        Returns:
        -------
        bool
            True si tous les Pokémon du joueur sont KO, False sinon.
        """
        for i in self.pokemon_equipe:
            if not  i.est_ko():
                return False
        Soins(self)
        return True 

    def ajouter_pokemon_equipe(self, pokemon):
        """
        Ajoute un Pokémon à l'équipe du joueur.

        Parameters:
        ----------
        pokemon : Pokemons
            Le Pokémon à ajouter à l'équipe.

        Returns:
        -------
        None
        """
        if len(self.pokemon_equipe) < 6:
            pokemon.stats['HP'][0]= pokemon.stats['HP'][1]
            self.pokemon_equipe.append(pokemon)
            print(f"{self.name} a capturé {pokemon.name}.")
        else:
            print("L'équipe est déjà complète, vous devez retirer un Pokémon avant d'en ajouter un autre.")
            choix = input("Tapez 1 pour éffectuer l'échange sinon 0 pour conserver l'équipe: ")
            if choix == 1:
                choix_pokemon = input("Taper le numéro du pokemon que vous voulez retirer:")
                self.retirer_pokemon_equipe(self.pokemon_equipe[int(choix_pokemon) - 1])
                self.ajouter_pokemon_equipe(pokemon)

    def retirer_pokemon_equipe(self, pokemon):
        """
        Retire un Pokémon de l'équipe du joueur.

        Parameters:
        ----------
        pokemon : Pokemons
            Le Pokémon à retirer de l'équipe.

        Returns:
        -------
        None
        """
        if pokemon in self.pokemon_equipe:
            self.pokemon_equipe.remove(pokemon)
            print(f"{pokemon.name} a été retiré de l'équipe de {self.name}.")
        else:
            print(f"{pokemon.name} n'est pas dans l'équipe de {self.name}.")

class Rencontre :
    def __init__(self,joueur,position):
        """
        Initialise une rencontre avec un joueur et une position.

        Parameters:
        ----------
        joueur : Dresseur
            Le joueur rencontré.
        position : tuple
            La position de la rencontre.

        Returns:
        -------
        None
        """
        self.joueur=joueur
        self.position=position
        self.pokemon_sauvage=Pokemons(vp.pokemon_coordinates[self.position])
        combat=Combat(self.joueur,self.pokemon_sauvage)
        combat.commencer()

class Starter :
    def __init__(self,joueur,lst_poke):
        """
        Initialise les Pokémon de départ d'un joueur.

        Parameters:
        ----------
        joueur : Dresseur
            Le joueur.
        p1 : str
            Nom du premier Pokémon.
        p2 : str
            Nom du deuxième Pokémon.
        p3 : str
            Nom du troisième Pokémon.

        Returns:
        -------
        None
        """
        print(f"{lst_poke} fichier monat")
        self.joueur=joueur
        self.joueur.pokemon_equipe.append(Pokemons(lst_poke[0]))
        self.joueur.pokemon_equipe.append(Pokemons(lst_poke[1]))
        self.joueur.pokemon_equipe.append(Pokemons(lst_poke[2]))

class Soins:
    def __init__(self,joueur):
        """
        Soigne les Pokémon d'un joueur.

        Parameters:
        ----------
        joueur : Dresseur
            Le joueur dont les Pokémon doivent être soignés.

        Returns:
        -------
        None
        """
        self.joueur=joueur
        for pokemon in joueur.pokemon_equipe :
            pokemon.stats['HP'][0]= pokemon.stats['HP'][1]
        
class Combat:

    """

    Cette classe représente un combat entre un joueur et un Pokémon adverse.

    """

    indice = 0  # Indice du Pokémon en combat dans l'équipe du joueur



    def __init__(self, joueur, pokemon_adversaire):

        """

        Initialise un combat entre un joueur et un Pokémon adverse.



        Parameters:

        ----------

        joueur : Joueur

            Le joueur participant au combat.

        pokemon_adversaire : Pokemons

            Le Pokémon adverse.



        Returns:

        -------

        None

        """

        self.joueur = joueur

        self.pokemon_adversaire = pokemon_adversaire



    def est_mort(self):

        """

        Vérifie si le Pokémon actuel du joueur est mort.



        Returns:

        -------

        bool

            True si le Pokémon actuel est mort, False sinon.

        """

        if self.joueur.pokemon_equipe[self.indice].est_ko():

            return True

    

    def commencer(self):

        """

        Lance le combat entre le joueur et le Pokémon adverse.



        Returns:

        -------

        str

            Indique si le joueur a fui le combat.

        """
        

        
        print(f"Le combat entre {self.joueur.name} et {self.pokemon_adversaire.name} commence !")

        print(f"Un {self.pokemon_adversaire.name} sauvage apparait !")

        print(f"{self.joueur.pokemon_equipe[0].name} ! Go!")

        





        while not self.joueur.tout_est_ko() and not self.pokemon_adversaire.est_ko():



            if self.joueur.tout_est_ko():

                print(f"Le dresseur {self.joueur.name} est hors de comabt ! Le {self.pokemon_adversaire.name} sauvage a gagné le combat!")

                break

            elif self.pokemon_adversaire.est_ko():

                print(f"{self.joueur.pokemon_adversaire.name} sauvage est K.O.! Vous avez gagné le combat!")

                exp=vp.exp_gagne_par_niveau[self.pokemon_adversaire.niveau]

                self.joueur.pokemon_equipe[self.indice].monter_niveau(int(exp))

                n=len(self.joueur.pokemon_equipe)

                for i in range(1,n):

                    if i != self.indice :

                        self.joueur.pokemon_equipe[i].monter_niveau(math.floor(int(exp)/(n-1)))



                self.joueur.ajouter_pokemon_equipe(self.pokemon_adversaire)

                break



            

            

            if self.est_mort():

                print(f"{self.joueur.pokemon_equipe[self.indice]} est K.O!")

                self.changer_pokemon()

                choix = input("Que voulez-vous faire ? (1 pour attaquer, 2 pour changer de Pokémon, 3 pour fuir): ")

                if self.tour_joueur(choix) == 'Fuir':

                    break



            if self.joueur.pokemon_equipe[self.indice].stats['Speed'] > self.pokemon_adversaire.stats['Speed']:

                choix = input(f"Que doit faire {self.joueur.pokemon_equipe[self.indice].name} ? (1 pour attaquer, 2 pour changer de Pokémon, 3 pour fuir): ")

                if self.tour_joueur(choix) == 'Fuir':

                    break

                if not self.pokemon_adversaire.est_ko():

                    if self.tour_pokemon_adversaire() =='Fuir':

                        break

            elif self.joueur.pokemon_equipe[self.indice].stats['Speed'] < self.pokemon_adversaire.stats['Speed']:

                if self.tour_pokemon_adversaire() =='Fuir':

                        break

                if not self.est_mort():

                    choix = input(f"Que doit faire {self.joueur.pokemon_equipe[self.indice].name} ? (1 pour attaquer, 2 pour changer de Pokémon, 3 pour fuir): ")

                    if self.tour_joueur(choix) == 'Fuir':

                        break

            else:

                attaquant = rd.choice([self.joueur, self.pokemon_adversaire])

                choix = input(f"Que doit faire {self.joueur.pokemon_equipe[self.indice].name} ? (1 pour attaquer, 2 pour changer de Pokémon, 3 pour fuir): ")

                if self.tour_joueur(choix) == 'Fuir':

                    break

                elif not self.pokemon_adversaire.est_ko():

                    if self.tour_pokemon_adversaire() =='Fuir':

                        break

                else:

                    if self.tour_pokemon_adversaire() =='Fuir':

                        break

                    if not self.est_mort():

                        choix = input(f"Que doit faire {self.joueur.pokemon_equipe[self.indice].name} ? (1 pour attaquer, 2 pour changer de Pokémon, 3 pour fuir): ")

                        if self.tour_joueur(choix) == 'Fuir':

                            break



       

            if self.joueur.tout_est_ko():

                print(f"Le dresseur {self.joueur.name} est hors de combat ! Le {self.pokemon_adversaire.name} sauvage a gagné le combat!")

                break



            elif self.pokemon_adversaire.est_ko():

                print(f"Le {self.pokemon_adversaire.name} sauvage est K.O! Vous avez gagné le combat!")

                exp=vp.exp_gagne_par_niveau[self.pokemon_adversaire.niveau]

                self.joueur.pokemon_equipe[self.indice].monter_niveau(int(exp))

                n=len(self.joueur.pokemon_equipe)

                for i in range(0,n):

                    if i != self.indice :

                        self.joueur.pokemon_equipe[i].monter_niveau(math.floor(int(exp)/(n-1)))

                self.joueur.ajouter_pokemon_equipe(self.pokemon_adversaire)

                break





    def tour_joueur(self, choix):

        """

        Gère le tour de jeu du joueur.



        Parameters:

        ----------

        choix : str

            Le choix du joueur.



        Returns:

        -------

        str

            Indique si le joueur a fui le combat.

        """



        if choix == "1":

            print("Choisissez une attaque :")

            print(f"1. {'charge'}")

            print(f"2. {self.joueur.pokemon_equipe[self.indice].stats['attaque_speciale']}")

            choix_attaque = input("Entrez le numéro de l'attaque choisie : ")



            if choix_attaque == "1":

                attaque = ['Normal', 30, 'Charge']

            elif choix_attaque == "2":

                attaque = [self.joueur.pokemon_equipe[self.indice].stats['Type 1'], self.joueur.pokemon_equipe[self.indice].stats['puissance'], self.joueur.pokemon_equipe[self.indice].stats['attaque_speciale']]

            else:

                print("Choix invalide. L'attaque par défaut sera utilisée.")

                attaque = [self.joueur.pokemon_equipe[self.indice].charge, 30, 'Charge']



            self.joueur.pokemon_equipe[self.indice].attaquer(attaque, self.pokemon_adversaire)



        elif choix == "2":

            ancien_indice = self.indice

            nouveau_pokemon = self.changer_pokemon()

            if nouveau_pokemon:

                print(f"{self.joueur.pokemon_equipe[ancien_indice].name}, reviens !")

                print(f"Allons-y, {self.joueur.pokemon_equipe[self.indice].name}! A toi de jouer!")

            else:

                print(f"{self.joueur.name} n'a pas changé de Pokémon.")

                choix = input(f"Que doit faire {self.joueur.pokemon_equipe[self.indice].name} ? (1 pour attaquer, 2 pour changer de Pokémon, 3 pour fuir): ")

                self.tour_joueur(choix)



        elif choix == "3":

            proba_fuite= ((self.joueur.pokemon_equipe[self.indice].stats['Speed']*32)/ (math.floor(self.pokemon_adversaire.stats['Speed']/4))) +30

            if proba_fuite>255:

                print("Vous avez pris la fuite !")

                return 'Fuir'

            else :

                aleatoire=rd.randint(0,255)

                if aleatoire<=  proba_fuite:

                    print("Vous avez pris la fuite !")

                    return 'Fuir'

                else :

                    print("Vous n'avez pas réussi à fuir !")



        else :

            choix = input(f"Que doit faire {self.joueur.pokemon_equipe[self.indice].name} ? (1 pour attaquer, 2 pour changer de Pokémon, 3 pour fuir): ")

            print('Veuillez saisir un chiffre valide')

            self.tour_joueur(choix)





        

            



    def tour_pokemon_adversaire(self):

        """

        Gère le tour de jeu du Pokémon adverse.



        Returns:

        -------

        None

        """

        attaque_aleatoire = rd.choice([[self.pokemon_adversaire.stats['Type 1'], self.pokemon_adversaire.stats['puissance'], self.pokemon_adversaire.stats['attaque_speciale']], ['Normal', 30, 'Charge']])

        if self.pokemon_adversaire.stats['Legendary']:

            aleatoire=rd.randint(0,100)

            if aleatoire <10:

                print(f" Le {self.pokemon_adversaire.name} sauvage a pris la fuite !")

                return 'Fuir'

        else:

            aleatoire=rd.randint(0,100)

            if aleatoire <5:

                print(f" Le {self.pokemon_adversaire.name} sauvage a pris la fuite !")

                return 'Fuir'

        self.pokemon_adversaire.attaquer(attaque_aleatoire, self.joueur.pokemon_equipe[self.indice])



    def changer_pokemon(self):

        """

        Permet au joueur de changer de Pokémon pendant le combat.



        Returns:

        -------

        bool

            True si le joueur a changé de Pokémon, False sinon.

        """

        print("Choisissez un Pokémon pour le remplacer dans le combat :")

        for i, pokemon in enumerate(self.joueur.pokemon_equipe):

            print(f"{i+1}. {pokemon.name}")



        choix = input("Entrez le numéro du Pokémon choisi ou 0 pour annuler : ")

        while choix not in [str(i) for i in range(len(self.joueur.pokemon_equipe) + 1)] or self.joueur.pokemon_equipe[int(choix) - 1].est_ko():

            print("Choix invalide. Veuillez entrer un numéro valide ou un pokemon vivant .")

            choix = input("Entrez le numéro du Pokémon choisi ou 0 pour annuler : ")



        if choix == "0":

            return False

        else:

            self.indice = int(choix) - 1

            return True





class FightWindow(QDialog):
    def __init__(self,pokemon_data=None,joueur=Dresseur("Sacha"),pos=None):
        super(FightWindow, self,).__init__()
        loadUi('/Users/samy/PROJET_POO_REAL/DAN_MONAT_SAMY/CODE/welcome2.ui', self)
        
        print(f"pokemon_data: {pokemon_data}")
        
        self.joueur = joueur
        self.pokemon_data = pokemon_data
        
        self.pos = pos
        
        print(self.pos)
        
        #self.pokemon_data = pokemon_data[2]
        self.resize(1920,1080)
        self.setWindowTitle("COMBAT !")
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        
        
        # Connecter les boutons à des fonctions
        self.ui.pushButton.clicked.connect(self.attaquer)
        self.ui.pushButton_2.clicked.connect(self.attaquer_sp2)
        self.ui.pushButton_3.clicked.connect(self.fuite)
        self.ui.pushButton_4.clicked.connect(self.changer_pokemon)

        # Charger l'image du Pokémon défenseur et redimensionner le label
        self.set_image_pokemon_def("/Users/samy/PROJET_POO_REAL/DAN_MONAT_SAMY/CODE/image tiles/pokemon_Combat/front/1.png")
        self.set_image_pokemon_att("/Users/samy/PROJET_POO_REAL/DAN_MONAT_SAMY/CODE/image tiles/pokemon_Combat/back/1.png")
        self.set_dialogue_text("Un combat a commencé !")
        
        
        
        
        
    def attaquer(self):
        #fight = Rencontre(self.joueur, self.pos)
        #fight.commencer()
        self.set_dialogue_text("J'attaque!")
        print("Attaque lancée")

    def attaquer_sp2(self):
        # Code pour l'action de la deuxième attaque spéciale
        print("Deuxième attaque spéciale lancée")

    def fuite(self):
        # Code pour l'action de fuite
        print("Fuite lancée")

    def changer_pokemon(self):
        # Code pour l'action de changer de Pokémon
        print("Changement de Pokémon")

    def set_image_pokemon_def(self, image_path):
        pixmap = QPixmap(image_path).scaled(160, 160)
        self.label_4.setPixmap(pixmap)
        
    def set_image_pokemon_att(self, image_path):
        pass
    
    def set_dialogue_text(self, text):
        self.dialogue.setPlainText(text)
        font_id = QFontDatabase.addApplicationFont("/Users/samy/PROJET_POO_REAL/DAN_MONAT_SAMY/data/police.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_family)
        self.dialogue.setFont(font)
        self.dialogue.setStyleSheet("background-color: rgba(0,0,0,0); margin: 10px; padding: 0px;")
    


    def load_pixmap(self, image_path, width, height):
        pixmap = QPixmap(image_path).scaled(width, height)
        return pixmap






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FightWindow()
    sys.exit(app.exec_())
