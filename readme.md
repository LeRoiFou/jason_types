# [Tutoriel Python - annotations de type](https://www.youtube.com/watch?v=a5HGF_ELI1Ehttps:/)

Python est conçu avec un typage dynamique, c'est à dire qu'il nécessaire de déclarer le type affecté à une variable ou à un argument.

* Types natifs : bool, int, float, bytes, list, dict, set, range, str
* Autres types :
  * Final : variable déclarée inchangée
  * Iterable(types qui marchent avec la boucle for)
  * Iterator
  * List (List[int], List[str], List[bool]...)
  * Dict (Dict[int, str], ...)
  * Any
  * ...

Avec la librairie [mypy](https://pypi.org/project/mypy/) de python, il est possible de contrôle les typages appliqués. Pour cela, il suffit après avoir installé mypy, de saisir l'instruction suivante dans le terminal : mypy --strict .\nom_fichier.py.

Grâce à cette librairie, on peut constater que même si le programme fonctionne, une erreur s'affiche dans le terminal lorsque le typage appliqué à une variable est faut.

00:29:15

Date : 08-02-2024
