import csv

class PokemonList:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.pokemon_list = self.get_first_gen_pokemon_list(csv_file_path)
        self.initialize_pokemon_names()

    def get_first_gen_pokemon_list(self, csv_file_path):
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)
            pokemon_list = []
            for row in reader:
                if row[-1] == '1':
                    pokemon_info = {
                        "number": row[0],
                        "name": row[1],
                        "image_name": f"/Users/samy/PROJET_POO_REAL/DAN_MONAT_SAMY/CODE/image tiles/pokemon_Combat/front_black/{row[0]}.png"
                    }
                    pokemon_list.append(pokemon_info)
        return pokemon_list

    def initialize_pokemon_names(self):
        for pokemon in self.pokemon_list:
            pokemon['name'] = "????"

    def print_pokemon_list(self):
        for pokemon in self.pokemon_list:
            print(f"Numéro: {pokemon['number']}, Nom: {pokemon['name']}, Image: {pokemon['image_name']}")

    def modify_pokemon(self, number, new_name, new_image_name):
        for pokemon in self.pokemon_list:
            if pokemon['number'] == number:
                pokemon['name'] = new_name
                pokemon['image_name'] = new_image_name
                break
        else:
            print("Pokemon not found.")

if __name__ == '__main__':
    pokemon_list = PokemonList("data/pokemons_fr.csv")
    pokemon_list.print_pokemon_list()
    
    # Modifier un Pokémon (par exemple, numéro 1)
    pokemon_list.modify_pokemon("1", 'Bulbizarre', f"/Users/samy/PROJET_POO_REAL/DAN_MONAT_SAMY/CODE/image tiles/pokemon_Combat/front_black/{1}.png")
    print("\nAprès modification :")
    pokemon_list.print_pokemon_list()