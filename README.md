# Atelier - Programmation orientée-objet et tests unitaires

![Logo](/images/LogoProgFest.png)

#### Avant-propos
Les étapes ci-dessous servent à vous guider durant l'atelier. Rien ne vous empêche d'en omettre quelques-unes, de nommer les variables autrement, ou même de faire autre chose complètement (par exemple, de faire une classe `Cat` et une classe `Dog`). Par contre, vous devez garder en tête que vos employeurs attendent un certain rendement de votre part. **Si vous êtes bloqués, un code déjà fonctionnel est fourni dans le dossier `reference`**.

#### Contexte

Vous venez tout juste d'être engagé par *Rockwell Automation*, une compagnie spécialisée en automation industrielle. Pour votre premier mandat, on vous a ordonné d'écrire un  module Python permettant d'importer puis d'analyser les données générées lors d'expériences d'encabulation qui sont menées quotidiennement chez *Rockwell*. Plus spécifiquement, vous avez été assigné au fameux *Retro Encabulator* ainsi qu'à son modèle réduit, le *Micro Encabulator*.

Liens importants:
- *Rockwell Automation*: https://www.rockwellautomation.com/en-us.html.
- Description de produit, *Rockwell Retro Encabulator*: https://www.youtube.com/watch?v=RXJKdh1KZ0w.

#### Étape #1 - Importer un fichier
Avant votre arrivée chez *Rockwell*, personne n'avait de compétences en programmation. Ainsi, les résultats de plusieurs expériences d'encabulation se sont accumulés sur le serveur, sans toutefois avoir été analysés. Dans le dossier `Data`, vous trouverez les données de dix expériences effectuées en deux jours à la fin du mois dernier. La moitié des expériences est sauvegardée en format `.txt`, tandis que l'autre moitié est en format `.csv`.
1. Définissez une classe `EncabulatorData` qui prend en entrée (méthode `__init__`) le `path` vers un fichier à importer en mémoire. Ses attributs devraient typiquement être le nom du fichier `name`, les données numériques `data` (vides initialement) ainsi que le `metadata` présent en *header* des fichiers (nom de l'appareil, date d'expérimentation).
2. Ajoutez une méthode `read_file` qui ouvre le fichier (avec la fonction de base `open()`) et qui effectue l'extraction de son contenu. La méthode devrait faire la différence entre les extensions `.txt` et `.csv`. **Conseil**: Les méthodes pour manipuler des chaines de caractères (`split()`, `strip()`, etc) vous seront utiles pour décortiquer chacune des lignes.
3. *Gare à la poussière!* Les fichiers `.txt` sont reconnus pour accumuler de la poussière au fil du temps. Il se peut que certains fichiers soient corrompus et que des éléments indésirables doivent être ignorés.

#### Étape #2 - Visualiser le contenu d'un fichier
Afin de valider que le contenu du fichier a bien été lu et interprété, il vous faut maintenant afficher un graphique arborant le contenu numérique du fichier, ainsi que les métadonnées textuelles.
1. Faites une classe `EncabulatorPlotter` qui prend en entrée un objet `EncabulatorData`.
2. Ajouter une méthode `plot` qui affiche un graphique (utiliser simplement `plt.plot`) du contenu numérique d'un fichier (colonne 1 en x, colonne 2 en y).
3. Comme titre du graphique (`plt.title`), inscrire la date d'expérimentation ainsi que le nom de l'appareil, qui sont contenus dans l'objet `EncabulatorData`.
4. Peaufiner les éléments du graphique afin qu'il soit plaisant à regarder. Les patrons sont très sévères à ce sujet.

#### Étape #3 - Compiler les données des expériences
Les réplicats des expériences ont été effectués afin d'observer le comportement moyen d'encabulation au fil du temps. Vous devez maintenant compiler les résultats des expériences menées sur chacun des appareils, puis afficher la courbe moyenne, qui devrait être moins bruitée que les expériences individuelles.
1. Définir une classe `Dataset` qui contient en attribut les objets `Data` provenant d'un même appareil.
2. Sur un seul graphique, afficher le nuage de points (`plt.scatter`) de toutes les expériences, ainsi que la courbe moyenne. Au besoin, une expérience peut être exclue si les données sont jugées inadéquates.
3. Ajuster les paramètres d'affichage (`alpha`, `linewidth`, etc) afin que la figure soit lisible. 

#### Étape #4 - Sauvegarder les résultats
Vos patrons ont bien hâte d'enfin pouvoir observer, après toutes ces années, les signaux générés par leurs appareils. Vous devez leur envoyer les figures générées en format haute-résolution, ainsi qu'exporter les valeurs de la courbe moyenne.
 
