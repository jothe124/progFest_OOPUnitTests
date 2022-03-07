# Atelier - Programmation orientée-objet et tests unitaires

![Logo](/images/LogoProgFest.png)

#### Avant-propos

Cet atelier a été développé par Antoine Légaré et Gabriel Genest.

Les étapes ci-dessous servent à vous guider durant l'atelier. Rien ne vous empêche d'en omettre quelques-unes, de nommer les variables autrement, ou même de faire autre chose complètement (par exemple, de faire une classe `Cat` et une classe `Dog`). Par contre, vous devez garder en tête que vos employeurs attendent un certain rendement de votre part. **Si vous êtes bloqués, un code déjà fonctionnel est fourni dans le dossier** `reference`.

#### Contexte

Vous venez tout juste d'être engagé par *Rockwell Automation*, une compagnie spécialisée en automation industrielle. Pour votre premier mandat, on vous a ordonné d'écrire un  module Python permettant d'importer puis d'analyser les données générées lors d'expériences d'encabulation qui sont menées quotidiennement chez *Rockwell*. Plus spécifiquement, vous avez été assigné au fameux *Retro Encabulator* ainsi qu'à son modèle réduit, le *Micro Encabulator*.

Liens importants:
- *Rockwell Automation*: https://www.rockwellautomation.com/en-us.html.
- Description de produit, *Rockwell Retro Encabulator*: https://www.youtube.com/watch?v=RXJKdh1KZ0w.

#### Importation des modules
Vos patrons ne sont pas trop sévères quant à la modalité programmatoire utilisée pour réaliser le mandat. Vous pouvez donc utiliser un `Jupyter notebook` ou coder dans un fichier `.py`, au choix. Avant de commencer, veuillez simplement importer les modules requis à l'aide des commandes suivantes:

`import numpy as np`

`import matplotlib.pyplot as plt`

#### Étape #1 - Importer un fichier
Avant votre arrivée chez *Rockwell*, personne n'avait de compétences en programmation. Ainsi, les résultats de plusieurs expériences d'encabulation se sont accumulés sur le serveur, sans toutefois avoir été analysés. Dans le dossier `Data`, vous trouverez les données de dix expériences effectuées en deux jours à la fin du mois dernier. La moitié des expériences est sauvegardée en format `.txt`, tandis que l'autre moitié est en format `.csv`.

1. Définir une classe `EncabulatorData` qui prend en entrée (dans la méthode `__init__`) le `path` vers un fichier à importer en mémoire. Ses attributs devraient typiquement être le nom du fichier `name`, les données numériques `data` (vides initialement) ainsi que le `metadata` présent en *header* des fichiers (nom de l'appareil, date d'expérimentation).
2. Ajouter une méthode `read_file` qui ouvre le fichier (avec la fonction de base `open()`) et qui effectue l'extraction de son contenu. La méthode devrait faire la différence entre les extensions `.txt` et `.csv`. **Conseil**: Les méthodes pour manipuler des chaines de caractères (`split()`, `strip()`, etc) vous seront utiles pour décortiquer chacune des lignes.
3. *Gare à la poussière!* Les fichiers `.txt` sont reconnus pour accumuler de la poussière au fil du temps. Il se peut que certains fichiers soient poussiéreux et que des éléments indésirables doivent être ignorés lors de la lecture des valeurs numériques.
4. Ajouter une méthode `__getitem__` qui permet d'accéder aux valeurs numériques contenues par l'objet. Ceci facilitera la manipulation d'un objet `EncabulatorData` par les autres classes.

#### Étape #2 - Visualiser le contenu d'un fichier
Afin de valider que le contenu du fichier a bien été lu et interprété, il vous faut maintenant afficher un graphique arborant le contenu numérique du fichier, ainsi que les métadonnées textuelles.

1. Faire une classe `EncabulatorPlotter` qui prend en entrée un objet `EncabulatorData`.
2. Ajouter une méthode `plot` qui affiche un graphique (utiliser simplement `plt.plot`) du contenu numérique d'un fichier (colonne 1 en x, colonne 2 en y).
3. Comme titre du graphique (`plt.title`), inscrire la date d'expérimentation ainsi que le nom de l'appareil, qui sont contenus dans l'objet `EncabulatorData`.
4. Peaufiner les éléments du graphique afin qu'il soit plaisant à regarder. Les patrons sont **très sévères** à ce sujet.

#### Étape #3 - Compiler les données des expériences
Plusieurs réplicats des expériences ont été effectués afin d'observer le comportement moyen d'encabulation au fil du temps. Vous devez maintenant compiler les résultats des expériences menées sur chacun des appareils, puis afficher la courbe moyenne, qui devrait être moins bruitée que les expériences individuelles.

1. Définir une classe `EncabulatorDataset` qui contient en attribut les objets `Data` provenant d'un même appareil.
2. Pour calculer la courbe moyenne, compiler à l'interne (attribut ou méthode) les valeurs numériques des expériences dans un `np.array` de format `NxT`, où `N` est le nombre d'expériences, et `T` est le nombre d'échantillons temporels. Utilisez ensuite la commande `np.mean()` dans l'axe 0 afin d'obtenir la moyenne. Au besoin, une expérience peut être exclue si les données sont jugées inadéquates.

#### Étape #4: Visualiser le résultat d'une expérience
Vos données étant maintenant réunies au même endroit dans un objet `EncabulatorDataset`, vous devez modifier la classe `EncabulatorPlotter` afin qu'elle puisse également recevoir de tels objets en entrée.

1. Ajouter une condition dans la méthode `__init__` du `EncabulatorPlotter` qui vérifie si l'argument est un `EncabulatorData` ou `EncabulatorDataset`, et qui définit les attributs en conséquence.
2. Définir une méthode `plot_all` qui affiche la courbe moyenne d'un `EncabulatorDataset` calculée précédemment, tout en affichant les échantillons des expériences individuelles avec `plt.scatter`. Bien ajuster les paramètres d'affichage (`alpha`, `linewidth`, `color`, etc) afin que la figure soit lisible. Encore une fois, les patrons sont **très sévères** à ce sujet. 

#### Étape #5 - Sauvegarder les résultats
Vos patrons ont bien hâte d'enfin pouvoir observer, après toutes ces années, les signaux générés par leurs appareils. Vous devez leur envoyer les figures générées en format haute-résolution.

1. Ajouter une méthode `save_figure` à la classe `EncabulatorPlotter` qui exporte une figure en format `.pdf`. Pour ce faire, il suffit de simplement utiliser la fonction `plt.savefig`.
2. Montrez vos résultats à vos supérieurs.

#### Étape #6 (optionnelle) - Sécuriser le code
Afin de s'assurer que les méthodes du `EncabulatorData` importent correctement les données, vous devez écrire un test unitaire qui valide les résultats de la classe.

1. Ajouter un dossier `tests` au *repository*, puis générer un fichier `test.txt` dans ce dossier.
2. Dans le fichier, inscrire quelques valeurs numériques connues sur plusieurs lignes (par exemple, 420).
3. Développez un test unitaire pour la méthode `read_file` qui s'assure que les valeurs retournées sont celles que vous avez inscrites dans le fichier.
 
