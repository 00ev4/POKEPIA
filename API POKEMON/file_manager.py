import os
import json

DATA_DIR = "data"

def save_pokemon_info(data):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    file_name = input("Ingrese el nombre del archivo para guardar la información: ")
    file_path = os.path.join(DATA_DIR, file_name)
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def load_pokemon_info(file_name):
    file_path = os.path.join(DATA_DIR, file_name)
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def get_stored_files():
    if not os.path.exists(DATA_DIR):
        return []
    files = os.listdir(DATA_DIR)
    return files
