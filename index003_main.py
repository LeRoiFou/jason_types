
from collections.abc import Iterable
from typing import Dict, List, Any

"Fonction comprenant tous types d'iterables"
def iterate_something1(collection: Iterable) -> None:
    for element in collection:
        print(element)

# Types itérables
# iterate_something1([1, 2, 3])
# iterate_something1("123456")
# iterate_something1((4, 5, 6))


"Fonction comprenant tous types d'iterables avec uniquement des entiers"
def iterate_something2(collection: Iterable[int]) -> None:
    for element in collection:
        print(element)

# Types itérables
# iterate_something2([1, 2, 3])
# iterate_something2((4, 5, 6))


"""Fonction comprenant pour les dictionnaire uniquement des entiers
# pour les clés et des str pour les valeurs"""
def iterate_something3(collection: Dict[int, str]) -> None:
    for element in collection:
        print(element)
        
# iterate_something3({1: "Un", 2: "Deux"})


"Fonction comprenant pour les listes tous types"
def iterate_something4(collection: List[Any]) -> None:
    for element in collection:
        print(element)

# iterate_something4([1, '2', 3.156, True])
