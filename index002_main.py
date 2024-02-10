"""
Recours au type Final

Contrôle sur le terminal :
mypy --strict .\index002_main.py
"""

from typing import Final

# Affectation d'une valeur définitive à une variable avec la librairie Final :
# Le programme s'exécute correctement
# Aucune erreur ne s'affiche avec mypy
n : Final[int] = 15
print(n)

# Affectation d'une valeur définitive à une variable avec la librairie Final :
# Le programme ne s'exécute pas car la variable déclarée et inchangée de n est 15
# n = 23 # en erreur car la variable de n est égale à 15

# Affectation d'une valeur définitive à une variable avec la librairie Final :
# Le programme s'exécute correctement
# Une erreur s'affiche avec mypy : la variable f a une valeur float alors qu'on lui
# affecte une valeur boléenne...
f : Final[bool] = 22.50
print(f) # l'exécution fonctionne mais en lançant mypy, une erreur s'affiche