# cyndaquil
----

cyndaquil is a python wrapper for the PokéAPI RESTful api. 

## Important Notice
----  
cyndaquil is currently still in development. As of right now the basics are there, however its still very much work in progress.  
You should have no issues using the package as showing in the Usage section below. However bugs and other issues may show up.

### All info is pulled from PokéAPI  
That means the info provided by cyndaquil is as accurate as the info on PokéAPI.
If you do find any error in the data provided please open an issue on the [PokéAPI github page](https://github.com/PokeAPI/pokedex/issues)


## Python Versions
----
This module has been tested on the following Python 3 versions: 
- 3.9.8 
- 3.9.9 
- 3.10.1

It has not yet been tested on older version of Python 3. You mileage may vary if using on any versions not listed above.
As additional versions of Python are tested they will be added to list of working versions.


## Installation
----
Installation is done through pip. Run the pip command below to install module.  

```
pip install cyndaquil
```

### What if that doesn't work?  
Make sure you are using Python 3. You may also need to use `pip3` instead of just `pip` to do the install.
If you are using Python 3.9 or 3.10 you may need to use`pip3.9` or `pip3.10` respectfully.


## Dependencies
----
All the dependencies for this module should install when you run the above install command.
However if for some reason dependencies are missing, they are listed below, along with their install methods

- Python Requests `pip install requests`


## Usage
----
This module provides a very class based lookup method for Pokemon, Berries and Items. 
Below is a simple example of what you can use the program for.

```python
import cyndaquil as cy

#Create a Pokemon Object
cyndaquil = cy.Pokemon('cyndaquil')

#Create an item Object
pokeball = cy.Item('poke-ball')

#Create an berry Object
chesto = cy.Berry('chesto')


print("Cyndaquil's pokedex number is:", cyndaquil.number)
print("The Pokeball cost:", pokeball.cost)
print("The Chesto berry's firmness is:", chesto.firmness)
```

### Output
```
Cyndaquil's pokedex number is: 155
The Pokeball cost: 200
The Chesto berry's firmness is: super-hard
```

## What info can I look up?
----
I tried to include as much info as I could. However, a few things are still missing.
Below is a list of all the info you can currently pull from PokéAPI with cyndaquil

### Pokemon
- Pokedex Number
- Type
- Ability (including hidden abilities)
- Catch Rate
- Level rate group
- weight (in Kilos)
- height (in Meters)
- Base Stats
- EV yield
- Base Experience
- Base Friendship
- Pokedex color
- The Pokemon this evolves from, if any
- Egg Groups

### Item
- ID number
- Cost
- Attribute (Describes the type of item, and how you can use it)
- Category (Generally the pocket its in, but some are more specific)
- Effect. This is a long description of the item's usage
- Short Effect. This is a short, more concise description of the item
- Fling Power
- Fling Effect
- Wild Pokemon that holds this pokemon (Currently only lists the first Pokemon on the list)

### Berry
- ID Number
- Flavor Potency (Currently using Gen IV potency values)
- Size (in Centimeters)
- Smoothness
- Natural Gift Power
- Natural Gift Type
- Max Harvest (Max number of berries per tree)
- Item attributes for the berry


## Whats next?
----
The goals for this project are to make it an all in one look up for any info listed on PokéAPI. This includes things like type, abilities, sprites and much much more.

### Roadmap
Below is a general roadmap of planned features and ucyates. 
- List all held by Pokemon for items and berries
- Allow look up of sprites for Pokemon
- Allow look up of sprites for Items
- Allow look up of sprites for Berries
- Allow look up of evolution tree for Pokemon
- Allow look up of abilities and types
- Allow look up of moves
- Allow look up of movesets
- Include info on status conditions (This will probably be hard coded as PokéAPI does not have this info)

