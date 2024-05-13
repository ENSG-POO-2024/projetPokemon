import pandas as pd
import math as m
# Chemin vers votre fichier CSV
chemin = "/Users/samy/PROJET_POO_REAL/DAN_MONAT_SAMY/data/pokemon_coordinates.csv"

# Lire le fichier CSV dans un DataFrame
df = pd.read_csv(chemin)

# Afficher le DataFrame d'origine


# Créer un DataFrame séparé avec les coordonnées x et y
df_coords = pd.DataFrame(df['coordinates'].apply(eval).tolist(), columns=['coord_x', 'coord_y'])

df_coords *= 10

df_coords = df_coords.astype(int)

# Concaténer les deux DataFrames
df_final = pd.concat([df['pokemon'], df_coords], axis=1)

# Afficher le DataFrame final
#print(df_final)

x = df_final['coord_x'].tolist()
print(len(x))
y = df_final['coord_y'].tolist()

res= []
for i in range (998):
    res.append((x[i],y[i]))

print("le max x c'est "+str(max(x)))
print("le min x c'est "+str(min(x)))
print("le max y c'est "+str(max(y)))
print("le min y c'est "+str(min(y)))





chemin_sauvegarde = "/Users/samy/PROJET_POO_REAL/DAN_MONAT_SAMY/data/pokemon_coordinates_modified.csv"


df_final.to_csv(chemin_sauvegarde, index=False)

print("Fichier CSV enregistré avec succès.")
