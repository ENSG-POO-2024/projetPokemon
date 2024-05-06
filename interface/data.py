# -*- coding: utf-8 -*-
"""
Created on Mon May  6 13:25:02 2024

@author: Formation
"""


import json

# Données à enregistrer dans le fichier JSON
data = { }


# Chemin du fichier JSON
json_file = "data_user.json"

# Enregistrer les données dans le fichier JSON
with open(json_file, "w") as file:
    json.dump(data, file, indent=4)
