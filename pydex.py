import requests
import requests_cache
import argparse

requests_cache.install_cache('poke_cache')
parser = argparse.ArgumentParser()
URL = "https://pokeapi.co/api/v2/{category}/{search}"

class Pokemon():
    def __init__(self, name):
        self.name = name
        self.number = 0
        self.type_1 = None
        self.type_2 = None
        self.ability_1 = None
        self.ability_2 = None
        self.ability_hidden = None
        self.catch_rate = 0
        self.lvl_rate = None
        self.weight = 0
        self.height = 0
        self.stats = {
            "HP" : 0,
            "Attack" : 0,
            "Defense" : 0,
            "Sp Attack" : 0,
            "Sp Defense" : 0,
            "Speed" : 0
        }
        self.ev_yield = {
            "HP" : 0,
            "Attack" : 0,
            "Defense" : 0,
            "Sp. Attack" : 0,
            "Sp. Defense" : 0,
            "Speed" : 0
        }
        self.base_exp = 0
        self.base_friendship = 0
        self.color = "white"
        self.evolves_from = None
        self.egg_group_1 = "Undiscovered"
        self.egg_group_2 = "Undiscovered"


    def lookup_pokemon(self):
        global URL
        try:
            pokemon_response = requests.get(URL.format(category="pokemon",search=self.name))
            species_response = requests.get(URL.format(category="pokemon-species",search=self.name))
            stat_response = (URL.format(category="stat",search=self.name))
        except:
            print("Pokemon Not Found. Please check the name")
            return
        else:
            pokemon_data = pokemon_response.json()
            species_data = species_response.json()
        
        self.number = pokemon_data["game_indices"][0]["game_index"]
        
        self.type_1 = pokemon_data["types"][0]["type"]["name"]
        if len(pokemon_data["types"]) > 1:
            self.type_2 = pokemon_data["types"][1]["type"]["name"]

        self.ability = pokemon_data["abilities"][0]["ability"]["name"]
        if len(pokemon_data["abilities"]) == 2:
            if pokemon_data["abilities"][1]["is_hidden"] == True:
                self.ability_hidden = pokemon_data["abilities"][1]["ability"]["name"]
        if len(pokemon_data["abilities"]) == 3:
            self.ability_2 = pokemon_data["abilities"][1]["ability"]["name"]
            self.ability_hidden = pokemon_data["abilities"][2]["ability"]["name"]
        
        self.catch_rate = species_data["capture_rate"]
        self.lvl_rate = species_data["growth_rate"]["name"]
        self.weight = pokemon_data["weight"] / 100
        self.height = pokemon_data["height"] / 100

        self.stats["HP"] = pokemon_data["stats"][0]["base_stat"]
        self.stats["Attack"] = pokemon_data["stats"][1]["base_stat"]
        self.stats["Defense"] = pokemon_data["stats"][2]["base_stat"]
        self.stats["Sp Attack"] = pokemon_data["stats"][3]["base_stat"]
        self.stats["Sp Defense"] = pokemon_data["stats"][4]["base_stat"]
        self.stats["Speed"] = pokemon_data["stats"][0]["base_stat"]

        self.ev_yield["HP"] = pokemon_data["stats"][0]["effort"]
        self.ev_yield["Attack"] = pokemon_data["stats"][1]["effort"]
        self.ev_yield["Defense"] = pokemon_data["stats"][2]["effort"]
        self.ev_yield["Sp Attack"] = pokemon_data["stats"][3]["effort"]
        self.ev_yield["Sp Defense"] = pokemon_data["stats"][4]["effort"]
        self.ev_yield["Speed"] = pokemon_data["stats"][0]["effort"]

        self.base_exp = pokemon_data["base_experience"]
        self.base_friendship = species_data["base_happiness"]
        self.color = species_data["color"]["name"]
        self.evolves_from = species_data["evolves_from_species"]

        self.egg_group_1 = species_data["egg_groups"][0]["name"]
        if len(species_data["egg_groups"]) == 2:
            self.egg_group_2 = species_data["egg_groups"][1]["name"]


def main():
    #testing with cyndaquil
    cyndaquil = Pokemon("cyndaquil")
    cyndaquil.lookup_pokemon()


if __name__ == "__main__":
    main()