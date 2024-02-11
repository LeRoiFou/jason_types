"""
Les génériques

Contrôle sur le terminal :
mypy --strict .\index007_main.py : pas encore pris en charge par mypy
"""

from typing import TypeVar

T = TypeVar('T') # Création d'un type 'T' (type générique)

class Group(T):
    def __init__(self, value: T) -> None:
        self.value = value
        
