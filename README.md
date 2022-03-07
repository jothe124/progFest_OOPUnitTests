# Atelier - Programmation orientée-objet et tests unitaires
Vous venez tout juste d'être engagé par Rockwell Automation, une compagnie spécialisée en automation industrielle. Pour votre premier mandat, on vous a ordonné d'écrire un  module Python permettant d'importer puis d'analyser les données générées lors d'expériences d'encabulation qui sont menées quotidiennement chez Rockwell. Plus spécifiquement, vous avez été assigné au fameux *Retro Encabulator* ainsi qu'à son modèle réduit, le *Micro Encabulator*.

Liens importants:
- Rockwell Automation: https://www.rockwellautomation.com/en-us.html.
- Description de produit, *Rockwell Retro Encabulator*: https://www.youtube.com/watch?v=RXJKdh1KZ0w.

#### Étape #1 - Importer un fichier
Avant votre arrivée chez *Rockwell*, personne n'avait de compétences en programmation. Ainsi, les résultats de plusieurs expériences d'*encabulation* se sont accumulés sur le serveur, sans toutefois avoir été analysés. Dans le dossier `Data`, vous trouverez les données de dix expériences effectuées en deux jours à la fin du mois dernier. La moitié des expériences est sauvegardée en format `.txt`, tandis que l'autre moitié est en format `.csv`. Vous devez donc:
1. Décrire les étapes 

#### Étape #2 - Visualiser le contenu d'un fichier
Afin de valider que le contenu du fichier a bien été lu et interprété, il vous faut maintenant afficher un graphique arborant le contenu numérique du fichier, ainsi que les métadonnées textuelles.
1. Faire un graphique (`plt.plot`) des colonnes 1 et 2 d'un fichier.
2. Comme titre du graphique (`plt.title`), inscrire la date d'expérimentation ainsi que le nom de l'appareil.
