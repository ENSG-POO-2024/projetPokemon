import random as rd

import math



types = ["Steel", "Fighting", "Dragon", "Water", "Electric", "Fire", "Fairy", "Ice", "Bug", "Normal", "Grass", "Poison", "Psychic", "Rock", "Ground", "Ghost", "Dark", "Flying"]



# Matrice des affinités de types

affinite_types = [

    [0.5, 1, 1, 0.5, 0.5, 0.5, 2, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],                  # Acier

    [2, 1, 1, 1, 1, 1, 0.5, 2, 0.5, 2, 1, 0.5, 0.5, 2, 1, 0, 2, 0.5],                # Combat

    [0.5, 1, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],                        # Dragon

    [1, 1, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 0.5, 1, 1, 2, 2, 1, 1, 1],                    # Eau

    [1, 1, 0.5, 2, 0.5, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 0, 1, 1, 2],                    # Électrik

    [2, 1, 0.5, 0.5, 1, 0.5, 1, 2, 2, 1, 2, 1, 1, 0.5, 1, 1, 1, 1],                  # Feu

    [0.5, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 2, 1],                    # Fée

    [0.5, 1, 2, 0.5, 1, 0.5, 1, 0.5, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2],                  # Glace

    [0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 1, 2, 0.5, 2, 1, 1, 0.5, 2, 0.5],            # Insecte

    [0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 1, 0, 1, 1],                      # Normal

    [0.5, 1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 1, 0.5, 0.5, 1, 2, 2, 1, 1, 0.5],            # Plante

    [0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 0.5, 0.5, 1, 1],                  # Poison

    [0.5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 0, 1],                      # Psy

    [0.5, 0.5, 1, 1, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 0.5, 1, 1, 2],                    # Roche

    [2, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 0],                      # Sol

    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 1, 2, 0.5, 1],                        # Spectre

    [1, 0.5, 1, 1, 1, 1, 0.5, 1, 1, 1, 1, 1, 2, 1, 1, 2, 0.5, 1],                    # Ténèbres

    [0.5, 2, 1, 1, 0.5, 1, 1, 1, 2, 1, 2, 1, 1, 0.5, 1, 1, 1, 1]                     # Vol

]



# Affichage de la matrice

# for i in range(len(types)):

#     print(f"{types[i]:<10}", end=" ")

#     for j in range(len(types)):

#         print(f"{affinite_types[i][j]:<5}", end=" ")

#     print()





    

class Combat:

    



    indice= 0



    def __init__(self, joueur, pokemon_adversaire):

        self.joueur = joueur

        self.pokemon_adversaire = pokemon_adversaire



    def est_mort(self):

        if self.joueur.pokemon_equipe[self.indice].est_ko() :

            

            return True 



    def commencer(self):

        print(f"Le combat entre {self.joueur.name} et {self.pokemon_adversaire.name} commence!")

# ajout de la condition que le joueur à pris la fuite 

        choix = input("Que voulez-vous faire ? (1 commencer combat, 2 pour changer de Pokémon, 3 pour fuir): ")



        if choix == "1":

            choix = input("Que voulez-vous faire ? (1 pour attaquer, 2 pour changer de Pokémon, 3 pour fuir): ")

            

            if self.joueur.pokemon_equipe[0].stats['Speed']> self.pokemon_adversaire.stats['Speed']:

                

                self.tour_joueur(choix)

                   

                

                if not self.pokemon_adversaire.est_ko():

                    self.tour_pokemon_adversaire()

                    

            elif self.joueur.pokemon_equipe[0].stats['Speed'] < self.pokemon_adversaire.stats['Speed']:



                self.tour_pokemon_adversaire()

                if not self.est_mort():

                    

                    

                   self.tour_joueur(choix)

                        

            



        elif choix == "2":

            nouveau_pokemon = self.changer_pokemon()

            if nouveau_pokemon:

                

                print(f"{self.joueur.name} a changé de Pokémon.")                

            else :

                print(f"{self.joueur.name} n'a pas changé de Pokémon.")

                



        elif choix == "3":

            print("Vous avez fui le combat.")

            return 'Fuir'

        



        while not self.joueur.tout_est_ko() and not self.pokemon_adversaire.est_ko() : 

            # le combat s'arrête si le pokemon sauvage ou tous les pokemons du joueurs sont ko

            #ou si le joueur à pris la fuite 

           

            # Comparaison des vitesses pour déterminer qui attaque en premier

        

            if self.est_mort():

                print(f"{self.joueur.pokemon_equipe[self.indice]} est mort")

                self.changer_pokemon()

                choix = input("Que voulez-vous faire ? (1 pour attaquer, 2 pour changer de Pokémon, 3 pour fuir): ")

                if self.tour_joueur(choix) == 'Fuir':

                    break



            

            if self.joueur.pokemon_equipe[self.indice].stats['Speed']> self.pokemon_adversaire.stats['Speed']:

                choix = input("Que voulez-vous faire ? (1 pour attaquer, 2 pour changer de Pokémon, 3 pour fuir): ")

                if self.tour_joueur(choix) == 'Fuir':

                    break

                

                if not self.pokemon_adversaire.est_ko():

                    self.tour_pokemon_adversaire()

                    

            elif self.joueur.pokemon_equipe[self.indice].stats['Speed'] < self.pokemon_adversaire.stats['Speed']:

                self.tour_pokemon_adversaire()

                if not self.est_mort():

                    

                    choix = input("Que voulez-vous faire ? (1 pour attaquer, 2 pour changer de Pokémon, 3 pour fuir): ")

                    if self.tour_joueur(choix) == 'Fuir':

                        break

            else:

                attaquant = rd.choice([self.joueur, self.pokemon_adversaire]) # dans le cas ou les pokemons ont la même vitesse, l'attaquant est choisi de façon aléatoire

                choix = input("Que voulez-vous faire ? (1 pour attaquer, 2 pour changer de Pokémon, 3 pour fuir): ")

                if self.tour_joueur(choix) == 'Fuir':

                    break

                elif not self.pokemon_adversaire.est_ko():

                        self.tour_pokemon_adversaire()

                        

                else:

                    self.tour_pokemon_adversaire()

                    if not self.est_mort():

                        choix = input("Que voulez-vous faire ? (1 pour attaquer, 2 pour changer de Pokémon, 3 pour fuir): ")

                        if self.tour_joueur(choix) == 'Fuir':

                            break



        if self.joueur.tout_est_ko():

            print(f"Tous les Pokémon de {self.joueur.name} sont K.O.! {self.pokemon_adversaire.name} a gagné le combat!")

        elif self.pokemon_adversaire.est_ko():

            print(f"{self.pokemon_adversaire.name} est K.O.! {self.joueur.name} a gagné le combat!")

        else:

            print("C'est un match nul.")





    def tour_joueur(self,choix):

        print("C'est à votre tour de jouer.")

        



        if choix == "1":

            print("Choisissez une attaque :")

            print(f"1. {'charge'}")

            print(f"2. {self.joueur.pokemon_equipe[self.indice].stats['attaque_speciale']}")

            choix_attaque = input("Entrez le numéro de l'attaque choisie : ")



            if choix_attaque == "1":

                attaque = ['Normal',30,'Charge']

            elif choix_attaque == "2":

                attaque = [self.joueur.pokemon_equipe[self.indice].stats['Type 1'],self.joueur.pokemon_equipe[self.indice].stats['puissance'],self.joueur.pokemon_equipe[self.indice].stats['attaque_speciale']]

            else:

                print("Choix invalide. L'attaque par défaut sera utilisée.")

                attaque = [self.joueur.pokemon_equipe[self.indice].charge,30,'Charge']



            self.joueur.pokemon_equipe[self.indice].attaquer(attaque, self.pokemon_adversaire)





        elif choix == "2":

            nouveau_pokemon = self.changer_pokemon()

            if nouveau_pokemon:

                print(f"{self.joueur.name} a changé de Pokémon.")

                

                

            else:

                print(f"{self.joueur.name} n'a pas changé de Pokémon.")

                choix = input("Que voulez-vous faire ? (1 pour attaquer, 2 pour changer de Pokémon, 3 pour fuir): ")

                self.tour_joueur(choix)



        elif choix == "3":

            print("Vous avez fui le combat.")

            return 'Fuir'

        



        if self.pokemon_adversaire.est_ko():

            print(f"{self.pokemon_adversaire.name} est K.O.! Vous avez gagné le combat!")

            self.joueur.ajouter_pokemon_equipe(self.pokemon_adversaire)



    def tour_pokemon_adversaire(self):

        print(f"C'est au tour de {self.pokemon_adversaire.name} d'attaquer.")

        attaque_aleatoire=rd.choice([[self.pokemon_adversaire.stats['Type 1'],self.pokemon_adversaire.stats['puissance'],self.pokemon_adversaire.stats['attaque_speciale']],['Normal',30,'Charge']])

        self.pokemon_adversaire.attaquer(attaque_aleatoire,self.joueur.pokemon_equipe[self.indice])





    def changer_pokemon(self):

        print("Choisissez un Pokémon pour le remplacer dans le combat :")

        for i, pokemon in enumerate(self.joueur.pokemon_equipe):

            print(f"{i+1}. {pokemon.name}")



        choix = input("Entrez le numéro du Pokémon choisi ou 0 pour annuler : ")

        while choix not in [str(i) for i in range(len(self.joueur.pokemon_equipe) + 1)] and not self.joueur.pokemon_equipe[int(choix) - 1].est_ko(): # choisir un pokemon parmis ceux de notre equipe 

            print("Choix invalide. Veuillez entrer un numéro valide ou un pokemon vivant .")

            choix = input("Entrez le numéro du Pokémon choisi ou 0 pour annuler : ")



        if choix == "0":

            return False

        else:

            self.indice=int(choix) - 1

            return True

