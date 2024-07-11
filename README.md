# Video Games Sales Data Analysis

> Ce dépôt retrace l'analyse du jeux de données Video Games Sales 2024 disponible sur Kaggle dans le cadre d'une
> campagne de communication LinkedIn.
>
> Je retracerais dans ce README les différents posts de la campagne.
>
> Si vous souhaitez en savoir plus, clicker sur le
> logo [<img src="https://static-00.iconduck.com/assets.00/linkedin-original-icon-512x512-myo6evy9.png" width="24">](https://www.linkedin.com/in/martin-jeremy/recent-activity/all/)

---

## 11/07/2024

🎮 Jour 3 de notre aventure data dans l'univers des jeux vidéo ! 📊

Aujourd'hui, focus sur les valeurs manquantes ! Elles nous embêtent, mais on va peut-être les transformer en opportunité. 

En creusant dans le dataset VGSales 2024, j'ai découvert que de nombreuses entrées ont toutes (ou presque) leurs colonnes à NULL. Certaines catégories sont même entièrement vides ! Par exemple, les entrées pour les consoles "Séries" (comme "Call of Duty", "Pokemon", "Legend of Zelda") sont toutes à NULL. 

Je vais me faire une copie de cette sous-partie, je suis sûr que ça nous servira plus tard. Pour la suite, on va nettoyer une bonne partie en supprimant les entrées ayant "total_sales" à NULL. Enfin, hypothèse 100% biaisée : les jeux avec "last_update" à NULL n'ont jamais eu de mise à jour... le jeux vidéo avant l'existence du "Patch Day One", toute une époque, n'est-ce pas ?!

J'ai mis en place une fonction pour voir le Top N par catégorie, et c'est plutôt informatif. On y voit un manque de diversité dans les jeux les plus vendus (et ils ne sont même pas à mon goût 😑). On apprend que les branches d'EA sont particulièrement prolifiques, tandis que Nintendo se retrouve en 10e place ! Pour vous donner une idée, sur Kaggle et les datasets d'avant 2016, ils étaient en première position ! La fin de la Wii a-t-elle enterrée Nintendo ?

La prochaine fois, on va creuser un peu plus : OneHot encoding, corrélation, etc.. J'ai trop hâte ! Et vous ?

🤔 Pourquoi Nintendo a-t-il chuté sur cette première moitié de la décennie ? Un indice 🔎, ça a plus à voir avec le jeux de données qu'avec la R&D de Nintendo. 💡 Partagez vos idées en commentaire !

hashtag#DataScience hashtag#JeuxVidéo hashtag#AnalyseDeDonnées hashtag#Python hashtag#DataViz

P.S. : Likez et partagez pour que d'autres passionnés de data et de gaming nous rejoignent dans cette aventure ! 🚀

P.P.S. : Curieux de voir les coulisses ? Le code de cette analyse est 100% dispo sur GitHub ! Rendez-vous juste ici ➡️ https://lnkd.in/dfi3mzqN

## 01/07/2024

🎮 Jour 2 de notre aventure data dans l'univers des jeux vidéo ! 📊

Aujourd'hui, plongeons dans la visualisation et l'exploration initiale de notre dataset VGSales 2024. Voici mes découvertes passionnantes :

1️⃣ Visualisation : J'ai transformé nos données brutes en graphiques parlants. Un vrai changement de perspective ! Ces visualisations nous offrent déjà des informations précieuses avant même l'analyse approfondie.

2️⃣ Types de variables : Notre dataset est un cocktail fascinant de variables discrètes (6/14), continues (6/14) et de dates (2/14). Une richesse à explorer, mais qui apporte son lot de défis !

3️⃣ Valeurs manquantes : Alerte ! Beaucoup d'entrées incomplètes. Un vrai casse-tête pour notre analyse future. Certaines s'expliquent (pas de mises à jour pour les jeux anciens), mais attention aux biais potentiels !

4️⃣ Focus sur les chiffres : 
- Les boxplots donnent un aperçu global, mais les histogrammes révèlent les vraies pépites :
    - 2009 : l'année record pour les sorties de jeux !
    - Le PC, champion du nombre de titres, mais... 

🤔 Surprise du chef ! En termes de ventes totales, le PC n'est qu'à la 12ème place ! Comment expliquer ce paradoxe ?

Mes hypothèses :
- Les valeurs manquantes font-elles des siennes ?
- Une source majeure manquante (Steam, on te voit) ?
- Les jeux PC : nombreux mais pas des best-sellers ?

À vous de jouer ! Quelle est votre théorie ? 

Partagez vos idées en commentaire. Ensemble, déchiffrons ce mystère vidéoludique ! 💡

#DataScience #JeuxVidéo #AnalyseDeDonnées #Python #DataViz

P.S. : Likez et partagez pour agrandir notre communauté de data-gamers passionnés ! 🚀

P.P.S. : Curieux de voir les coulisses ? Le code de cette analyse est 100% dispo sur GitHub ! Rendez-vous juste ici ➡️ https://github.com/martin-jeremy/public-vgs-analysis

## 26/06/2024

🎮 C'est parti pour notre aventure data ! Plongeons dans le monde fascinant des jeux vidéo ! 🕹️

Aujourd'hui, je vous présente en détail le dataset que j'ai choisi : Video Games Sales 2024 de Kaggle (le lien est sur
mon post précédent). Un trésor de données sur les ventes de jeux vidéo à travers les décennies !

📊 Le dataset en bref :

- 64 016 entrées
- 14 variables descriptives
- Des données sur les ventes mondiales

Pourquoi ce choix ? 🤔

1️⃣ Passion : Le monde du gaming me passionne, et je voulais un sujet stimulant pour cet exercice.

2️⃣ Diversité des données : Variables numériques, catégorielles, dates... Un vrai terrain de jeu pour l'analyse !

3️⃣ Questions passionnantes à explorer :

- L'évolution des genres les plus vendus au fil du temps
- La répartition des genres par console
- Les préférences des éditeurs en termes de genres et d'équipes de développement

🔍 Et ce n'est que la partie émergée de l'iceberg ! On pourra aussi :

- Regrouper par décennies
- Identifier les suites et sagas

Je sais pas vous, mais moi je suis surexcité par les possibilités ! 🚀

J'aimerais avoir votre avis, qu'en pensez-vous ?

- Avez-vous des hypothèses sur ce dataset ?
- Des analyses spécifiques que vous aimeriez voir ?
- Des visualisations particulières qui vous intéresseraient ?

Partagez vos idées en commentaire ! Construisons ensemble cette analyse passionnante ! 💡

#DataScience #JeuxVidéo #AnalyseDeDonnées #Python #MachineLearning

P.S. : Likez et partagez pour que d'autres passionnés de data et de gaming nous rejoignent dans cette aventure ! 🙌

## 24/06/2024

🎮 C'est décidé, cet été, je renoue avec mon premier amour ! 💕

Et VOUS allez m'y aider ! 🚀

J'ai décidé de profiter de mon temps libre pour vous offrir une expérience data unique. Mon défi ? Analyser et documenter en direct le jeu de données "Video Game Sales 2024" de [Kaggle](https://www.kaggle.com/datasets/asaniczka/video-game-sales-2024/data).

📊 Au menu, selon VOS envies :
- Data visualisation époustouflante
- Analyse de l'importance des variables
- Modèles de prédiction
- Techniques de régression
- Et bien plus encore !

🐍 Nouveauté : J'utiliserai Python pour sortir de ma zone de confort R habituelle.

📅 Rendez-vous 1 à 2 fois par semaine pour suivre mon avancée et participer à cette exploration data !

🔥 À vous de jouer ! Que voulez-vous absolument voir dans cette analyse ? 
- Des graphiques spécifiques ?
- Des analyses particulières ?
- Des techniques que vous brûlez d'explorer ?

Partagez vos idées en commentaire ! Ensemble, créons une analyse de données captivante et instructive sur l'univers fascinant des jeux vidéo. 🕹️

#DataScience #Python #VideoGames #DataAnalysis #MachineLearning

P.S. Suivez-moi pour ne rien manquer de cette aventure data !

♻️ Partagez ce post pour agrandir notre communauté d'explorateurs de données ! Merci d'avance !
