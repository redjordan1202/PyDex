# PyDex
----

PyDex is a python wrapper for the PokéAPI RESTful api. 

## Usage

```python
import pydex as pd

#Create a Pokemon Object
cyndaquil = pd.Pokemon('cyndaquil')

#Create an item Object
pokeball = pd.Item('poke-ball')

#Create an berry Object
chesto = pd.Berry('chesto')


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

