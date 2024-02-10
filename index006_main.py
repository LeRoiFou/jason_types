"""
Les surcharges de fonctions / méthodes

Contrôle sur le terminal :
mypy --strict .\index006_main.py
"""

from typing import Any, overload

@overload
def sum(a: int, b: int) -> int: ...

@overload
def sum(a: float, b: float) -> float: ...

def sum(a: Any, b: Any) -> Any:
    return a + b

# Sur le terminal : ok
# mypy : ok
print(sum(1, 6))
print(sum(2.6, 3.1))
