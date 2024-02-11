"""
Les alias, les nouveaux types (ne marchent qu'avec Python 
version >= 3.12) : remplacement du nom du type

Contrôle sur le terminal :
mypy --strict .\index008_main.py -> non pris actuellement en charge par mypy
"""

from typing import TypeAlias

# coordonnees -> c'est un tuple[int, int]
coordonnees: TypeAlias = tuple[int, int]

player_position: coordonnees=(15, 6)
print(player_position)


# Même situation avec cette classe
from typing import NewType

coordonnes2 = NewType("coordonnes2", tuple[int, int])

player_position: coordonnes2=(17,50)
print(player_position)