import json

class Combat:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def take_damage(self, degats):
        self.vie -= degats
        if self.vie <= 0:
            print(f"{self.nom} a perdu!")
            return False
        else:
            print(f"{self.nom} a pris {degats} degats  et lui  reste {self.vie} point de vie .")
            return True

pokemon1 = Combat("Madafaka", 100)
pokemon2 = Combat("Bricodépot", 100)

while pokemon1.vie > 0 and pokemon2.vie > 0:
    # Pokemon 1 attaque Pokemon 2
    degats = 20
    print(f"{pokemon1.vie}  utilise lance-flammes {degats} degats!")
    if not pokemon2.take_damage(degats):
        break

    # Pokemon 2 attaque Pokemon 1
    degats = 15
    print(f"{pokemon2.nom} utilise pistolé a eau {degats} degats!")
    if not pokemon1.take_damage(degats):
        break
if pokemon1.vie <= 0:
    print(f"{pokemon1.nom} a perdu ! {pokemon2.nom} vainqueur!")
elif pokemon2.vie <= 0:
    print(f"{pokemon2.nom} a perdu ! {pokemon1.nom} vainqueur!")
else:
    print("It's a draw!")



class Pokemon:
    def __init__(self, nom, type_pokemon, defense, attaque, points_vie):
        self._nom = nom
        self._type = type_pokemon
        self._defense = defense
        self._attaque = attaque
        self._points_vie = points_vie
        
    def __str__(self):
        return f"{self._nom} - Type: {self._type}, Attaque: {self._attaque}, Défense: {self._defense}, Points de vie: {self._points_vie}"
        
    def to_dict(self):
        return {"nom": self._nom, "type": self._type, "defense": self._defense, "attaque": self._attaque, "points_vie": self._points_vie}
    
    @staticmethod
    def from_dict(pokemon_dict):
        return Pokemon(pokemon_dict["nom"], pokemon_dict["type"], pokemon_dict["defense"], pokemon_dict["attaque"], pokemon_dict["points_vie"])
    
class Electrique (Pokemon):
    def __init__(self, nom, defense, attaque, points_vie):
        super().__init__(nom, "Electrique", defense, attaque, points_vie)
        
class Feu(Pokemon):
    def __init__(self, nom, defense, attaque, points_vie):
        super().__init__(nom, "Feu", defense, attaque, int(points_vie*0.8))
        
class Eau(Pokemon):
    def __init__(self, nom, defense, attaque, points_vie):
        super().__init__(nom, "Eau", defense, attaque, int(points_vie*1.2))
        
class Plante(Pokemon):
    def __init__(self, nom, defense, attaque, points_vie):
        super().__init__(nom, "Plante", defense, attaque, points_vie)
        
class Pokedex:
    def __init__(self):
        self._pokemons = []
        
    def ajouter_pokemon(self, pokemon):
        if self.rechercher_pokemon(pokemon._nom) is None:
            self._pokemons.append(pokemon.to_dict())
            return True
        else:
            return False
        
    def rechercher_pokemon(self, nom):
        for pokemon_dict in self._pokemons:
            if pokemon_dict["nom"] == nom:
                return Pokemon.from_dict(pokemon_dict)
        return None
    
    def nombre_pokemons(self):
        return len(self._pokemons)
    
    def afficher_pokemons(self):
        print("Pokédex :")
        for pokemon_dict in self._pokemons:
            pokemon = Pokemon.from_dict(pokemon_dict)
            print(pokemon)

# utilsation de la classe Pokedex
pokedex = Pokedex()

# exemple de Pokemon
pikachu = Electrique("Pikachu", 80, 20, 2)
jérome = Eau("Jérome", 20, 7000, 0.1)
pizzaMan = Feu("PizzaMan", 35, 35, 120)
weed = Plante("Weed", 25, 45, 90)

# Ajout des Pokémon au Pokédex
pokedex.ajouter_pokemon(pikachu)
pokedex.ajouter_pokemon(jérome)
pokedex.ajouter_pokemon(pizzaMan)
pokedex.ajouter_pokemon(weed)

# ajouter un Pokémon  déjà  existant dans le Pokédex
pikachu_bis = Electrique("Pikachu", 35, 50, 110)
if pokedex.ajouter_pokemon(pikachu_bis):
    print("Pikachu ajouté au Pokédex !")
else:
    print("Pikachu déjà dans le Pokédex...")

# Afficher les Pokémons du Pokédex
pokedex.afficher_pokemons()

# Sauvegarde des Pokémons dans un fichier JSON
with open("pokedex.json", "w") as f:
    json.dump(pokedex._pokemons, f, indent=4)
