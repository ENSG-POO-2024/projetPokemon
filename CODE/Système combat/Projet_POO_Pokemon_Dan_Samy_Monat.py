import random as rd
import math
import visualisation_pokemon as vp

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
