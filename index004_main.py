"""
Les n-uplets

Contrôle sur le terminal :
mypy --strict .\index004_main.py
"""

from typing import NamedTuple

class Coord2D(NamedTuple):
    x: int
    y: int

# # Lancement du script : ok
# # mypy : aucune erreur
# player_position = Coord2D(16, 5)
# print(player_position)

# # Lancement du script : ok
# # mypy : 1 erreur
# player_position = Coord2D(16, "5")
# print(player_position)

# # Lancement du script : erreur
# # mypy : 2 erreurs
# player_position = Coord2D(16, "5", 6)
# print(player_position)

