# PyDex
----

PyDex is a python wrapper for the PokéAPI RESTful api. 

## Usage

```python
import pydex as pd

cyndaquil = pd.Pokemon(name="cyndaquil")
cyndaquil.lookup_pokemon()

pokeball = pd.Item(name="poke-ball")
pokeball.lookup_item()

print(cyndaquil.stats["HP"])
print(pokeball.cost)
```

### Output
```python
39
200
```