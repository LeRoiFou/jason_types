# [Tutoriel Python - annotations de type](https://www.youtube.com/watch?v=a5HGF_ELI1Ehttps:/)

Python est conçu avec un typage dynamique, c'est à dire qu'il nécessaire de déclarer le type affecté à une variable ou à un argument.

* Types natifs : bool, int, float, bytes, list, dict, set, range, str **-> fichier index001_main**
* Autres types :
  * Final : variable déclarée inchangée **-> Fichier index002_main**
  * Iterable(types qui marchent avec la boucle for) **-> Fichier index003_main**
  * Iterator
  * List (List[int], List[str], List[bool]...) **-> Fichier index003_main**
  * Dict (Dict[int, str], ...)**-> Fichier index003_main**
  * Any **-> Fichier index003_main**
  * n-uplets **-> Fichier index004_main**
  * Callable **-> Fichier index005_main**
  * Surcharges de méthodes / fonctions -> **Fichier index006_main**
  * Génériques **-> Fichier index007_main**
  * Les alias, les nouveaux types -> Fichier index008_main

Avec la librairie [mypy](https://pypi.org/project/mypy/) de python, il est possible de contrôle les typages appliqués. Pour cela, il suffit après avoir installé mypy, de saisir l'instruction suivante dans le terminal :

**mypy --strict .\nom_fichier.py**

Grâce à cette librairie, on peut constater que même si le programme fonctionne, une erreur s'affiche dans le terminal lorsque le typage appliqué à une variable est faux.

00:46:45

Date : 10-02-2024
