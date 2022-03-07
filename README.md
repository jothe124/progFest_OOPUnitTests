# Atelier - Programmation orientée-objet et tests unitaires

![progFest Logo](https://github.com/AntoineLegare/progFest_OOPUnitTests/tree/main/images/ProgFestLogo.png)

Vous venez tout juste d'être engagé par *Rockwell Automation*, une compagnie spécialisée en automation industrielle. Pour votre premier mandat, on vous a ordonné d'écrire un  module Python permettant d'importer puis d'analyser les données générées lors d'expériences d'encabulation qui sont menées quotidiennement chez *Rockwell*. Plus spécifiquement, vous avez été assigné au fameux *Retro Encabulator* ainsi qu'à son modèle réduit, le *Micro Encabulator*.

Liens importants:
- *Rockwell Automation*: https://www.rockwellautomation.com/en-us.html.
- Description de produit, *Rockwell Retro Encabulator*: https://www.youtube.com/watch?v=RXJKdh1KZ0w.

#### Étape #1 - Importer un fichier
Avant votre arrivée chez *Rockwell*, personne n'avait de compétences en programmation. Ainsi, les résultats de plusieurs expériences d'encabulation se sont accumulés sur le serveur, sans toutefois avoir été analysés. Dans le dossier `Data`, vous trouverez les données de dix expériences effectuées en deux jours à la fin du mois dernier. La moitié des expériences est sauvegardée en format `.txt`, tandis que l'autre moitié est en format `.csv`.
1. Décrire les étapes 

#### Étape #2 - Visualiser le contenu d'un fichier
Afin de valider que le contenu du fichier a bien été lu et interprété, il vous faut maintenant afficher un graphique arborant le contenu numérique du fichier, ainsi que les métadonnées textuelles.
1. Faire un graphique (`plt.plot`) des colonnes 1 et 2 d'un fichier.
2. Comme titre du graphique (`plt.title`), inscrire la date d'expérimentation ainsi que le nom de l'appareil.
3. Peaufiner les éléments du graphique afin qu'il soit plaisant à regarder.

#### Étape #3 - Compiler les données des expériences
Les réplicats des expériences ont été effectués afin d'observer le comportement moyen d'encabulation au fil du temps. Vous devez maintenant compiler les résultats des expériences menées sur chacun des appareils, puis afficher la courbe moyenne, qui devrait être moins bruitée que les expériences individuelles.
1. Définir une classe `Dataset` qui contient en attribut les objets `Data` provenant d'un même appareil.
2. Sur un seul graphique, afficher le nuage de points (`plt.scatter`) de toutes les expériences, ainsi que la courbe moyenne. Au besoin, une expérience peut être exclue si les données sont jugées inadéquates.
3. Ajuster les paramètres d'affichage (`alpha`, `linewidth`, etc) afin que la figure soit lisible. 

#### Étape #4 - Sauvegarder les résultats
Vos patrons ont bien hâte d'enfin pouvoir observer, après toutes ces années, les signaux générés par leurs appareils. Vous devez leur envoyer les figures générées en format haute-résolution, ainsi qu'exporter les valeurs de la courbe moyenne.
 
