"""
Les callable

Contrôle sur le terminal :
mypy --strict .\index005_main.py
"""
from typing import Callable, List

"1er exemple : 1er argument en int et 2 argument en float et retour en list"
def sort_like_this(collection : int, other_thing : float) -> list:
    pass

# Callable : [[argument_type1, argument_type2, ...], type_retour]
def some_function(collection: List[int], sort_method: Callable[[int, float], list]):
    pass
    
"2ème exemple : argument de variables divers"
def sort_like_this(*args) -> list:
    pass

# Callable : [[argument_type1, argument_type2, ...], type_retour]
def some_function(collection: List[int], sort_method: Callable[..., list]):
    pass
