# Video Games Sales Data Analysis

> Ce dépôt retrace l'analyse du jeux de données Video Games Sales 2024 disponible sur Kaggle dans le cadre d'une
> campagne de communication LinkedIn.
>
> Je retracerais dans ce README les différents posts de la campagne.
>
> Si vous souhaitez en savoir plus, clicker sur le
> logo [<img src="https://static-00.iconduck.com/assets.00/linkedin-original-icon-512x512-myo6evy9.png" width="24">](https://www.linkedin.com/in/martin-jeremy/recent-activity/all/)

---

## 12/08/2024

🚀 Nous voilà partis pour le cinquième et dernier jour de notre aventure data dans l'univers des jeux vidéo ! 

🎮📊Aujourd'hui, on clôture cette campagne avec des insights passionnants et quelques nouveautés dans notre boîte à outils !

1️⃣ 𝗦𝘄𝗶𝘁𝗰𝗵 𝘃𝗲𝗿𝘀 𝗗𝘂𝗰𝗸𝗗𝗕 : En plein cœur de ma formation data-upskilling, j'ai décidé de passer à DuckDB pour mettre en pratique les conseils de Benjamin Dubreu. Je trouve le requêtage SQL beaucoup plus clair et lisible. Un vrai game-changer pour mes analyses !

2️⃣ 𝗩𝗶𝘀𝘂𝗮𝗹𝗶𝘀𝗮𝘁𝗶𝗼𝗻 𝗮𝘃𝗲𝗰 𝗣𝗹𝗼𝘁𝗻𝗶𝗻𝗲 : Pour ceux qui, comme moi, viennent de R et adorent ggplot, Plotnine est une alternative fantastique à Matplotlib. La syntaxe est fidèle à la Grammar of Graphics et permet de créer des visualisations élégantes sans effort.

3️⃣ 𝗔𝗻𝗮𝗹𝘆𝘀𝗲 𝗱𝗲𝘀 𝗦𝗲́𝗿𝗶𝗲𝘀 𝗱𝗲 𝗝𝗲𝘂𝘅 : J'ai décidé de faire un focus sur les séries de jeux. Résultat ? Call of Duty est la série la plus vendue ! Je garde les fonctions de Pandas dans ma boîte à outils : la fonction cumsum() m'évite de me replonger dans les CTE et les Window Functions en SQL (en vrai, c'est au programme, mais je n'ai pas encore abordé cette partie 🤫🙈).

4️⃣ 𝗩𝗶𝘀𝘂𝗮𝗹𝗶𝘀𝗮𝘁𝗶𝗼𝗻 𝗱𝗲𝘀 𝗩𝗲𝗻𝘁𝗲𝘀 𝗽𝗮𝗿 𝗖𝗼𝗻𝘀𝗼𝗹𝗲 : En appliquant la même logique aux consoles, les courbes en cloche révèlent la durée de vie typique de 5 à 8 ans par console. Fascinant de voir comment les tendances évoluent !

Cette campagne a été une véritable plongée dans l'analyse de données et le monde des jeux vidéo. Avec les bons outils et un peu de curiosité, on peut extraire des informations précieuses d'un simple jeu de données !

Dans le cadre d'un projet data, il est important de considérer la composante métier ou le niveau de connaissance du domaine d'étude. Elle n'est 𝗽𝗮𝘀 𝗶𝗻𝗱𝗶𝘀𝗽𝗲𝗻𝘀𝗮𝗯𝗹𝗲 pour réaliser l'analyse, mais elle permet d'être bien plus 𝗮𝘂𝘁𝗼𝗻𝗼𝗺𝗲 sur son interprétation et facilite la prise de recul. Au cours de cette étude, j'ai relevé certains points qui m'interpellent, comme :

1️⃣ GuitarHero et Madden NFL dans le Top 10 des séries de jeux vidéo les plus vendues, mais pas Pokémon ?
2️⃣ SEGA qui cumule plus de ventes que Nintendo ?
3️⃣ Les jeux de stratégie surreprésentés sur les supports PC, mais pas les jeux d'aventure à l'ancienne (Monkey Island, Carmen Sandiego, Syberia, ...) 

En l'état, je me questionne sur la bonne qualité de mon JDD et je serais curieux de confirmer ces résultats avec d'autres sources.

Je n'ai malheureusement pas réussi à maintenir le rythme d'un post par semaine sur ce projet, mais je suis très content d'avoir pu appliquer à cette étude les premiers conseils acquis de ma formation.

Et vous, qu'avez-vous appris ? Des surprises ou des confirmations ? Partagez vos réflexions en commentaire !

hashtag#DataAnalyse hashtag#JeuxVidéo hashtag#DuckDB hashtag#Plotnine hashtag#DataViz

P.S. : Pour les curieux, le code complet de cette analyse est disponible sur GitHub ! 👉 https://lnkd.in/dfi3mzqN

## 25/07/2024

🚀 C'est parti pour le J4 de notre aventure data dans l'univers des jeux vidéo ! 🎮📊

Aujourd'hui, on plonge dans l'encodage et la visualisation des corrélations. Préparez-vous, ça va secouer !

1️⃣ 𝗟𝗮𝗯𝗲𝗹 𝗘𝗻𝗰𝗼𝗱𝗶𝗻𝗴 𝘃𝘀 𝗢𝗻𝗲 𝗛𝗼𝘁 𝗘𝗻𝗰𝗼𝗱𝗶𝗻𝗴 : 𝗹𝗲 𝗺𝗮𝘁𝗰𝗵 𝗱𝘂 𝘀𝗶𝗲̀𝗰𝗹𝗲 !

- 𝗟𝗮𝗯𝗲𝗹 𝗘𝗻𝗰𝗼𝗱𝗶𝗻𝗴 : Simple et rapide. On transforme "Mario" en 1, "Zelda" en 2... Pratique, mais attention aux fausses
  hiérarchies !
- 𝗢𝗻𝗲-𝗛𝗼𝘁 𝗘𝗻𝗰𝗼𝗱𝗶𝗻𝗴 : Plus lourd, mais plus précis. Chaque catégorie devient sa propre colonne. Bye bye, hiérarchies non
  désirées !

𝗠𝗼𝗻 𝗮𝘃𝗶𝘀 ? One-Hot gagne pour la précision, mais Label reste utile pour les datasets XXL !

2️⃣ 𝗖𝗼𝗿𝗿𝗲́𝗹𝗮𝘁𝗶𝗼𝗻 : 𝗹𝗲 𝗱𝗲́𝘁𝗲𝗰𝘁𝗶𝘃𝗲 𝗱𝗲 𝗻𝗼𝘀 𝗱𝗼𝗻𝗻𝗲́𝗲𝘀 !
On a utilisé la méthode de Pearson pour débusquer les liens cachés entre nos variables. Mais attention ! Corrélation
n'est pas causalité. On reste vigilants, et on pense à s'assurer de la significativité de nos approches ! 🕵️‍♂️

3️⃣ 𝗨𝗻𝗲 𝗮𝗹𝘁𝗲𝗿𝗻𝗮𝘁𝗶𝘃𝗲 𝗿𝗮𝗽𝗶𝗱𝗲 : 𝗹𝗲 𝗰𝗿𝗼𝘀𝘀𝘁𝗮𝗯
Pour une vision d'ensemble rapide des relations entre deux variables catégorielles, le crosstab (ou tableau de
contingence) est une excellente alternative. Moins gourmand en ressources et plus rapide, il permet de visualiser les
fréquences et pourcentages des catégories croisées. Idéal pour des analyses exploratoires, à condition de savoir quoi
chercher !

4️⃣ 𝗟𝗮 𝗰𝗲𝗿𝗶𝘀𝗲 𝘀𝘂𝗿 𝗹𝗲 𝗴𝗮̂𝘁𝗲𝗮𝘂 : 𝗹𝗲 𝗭-𝗦𝗰𝗼𝗿𝗲 !

Le Z-score permet de comparer des données de manière équitable en les normalisant. Imagine que tu compares des pommes et
des oranges, mais grâce au Z-score, tu les transformes toutes en fruits de taille comparable ! 🍎🍊

En pratique, le Z-score indique combien une donnée est éloignée de la moyenne en termes d'écarts-types. Cela permet de
voir facilement si une donnée est au-dessus ou en dessous de la moyenne et de combien. Que ce soit des notes, des
tailles, ou n'importe quelles mesures, tout devient comparable sur une même échelle grâce au Z-score.

🤔 𝗣𝗼𝘂𝗿𝗾𝘂𝗼𝗶 𝘁𝗼𝘂𝘁 𝗰𝗲 𝗰𝗶𝗿𝗾𝘂𝗲 ?
Pour révéler les patterns cachés dans nos données
Pour éviter les biais dus aux différences d'échelle
Pour préparer le terrain à des analyses plus poussées

Le grand enseignement du jour : la corrélation, c'est comme un indice dans une enquête. Intéressant, mais à confirmer !
Toujours croiser avec des tests de significativité pour ne pas tomber dans le piège des fausses pistes.

Alors, qu'en pensez-vous ? Avez-vous déjà utilisé ces techniques ? Partagez vos expériences en commentaire !

#DataAnalyse #JeuxVidéo #Encoding #Corrélation

P.S. : Curieux de voir les coulisses ? Le code est toujours dispo sur GitHub ! 👉 https://lnkd.in/dfi3mzqN

## 11/07/2024

🎮 Jour 3 de notre aventure data dans l'univers des jeux vidéo ! 📊

Aujourd'hui, focus sur les valeurs manquantes ! Elles nous embêtent, mais on va peut-être les transformer en opportunité. 

En creusant dans le dataset VGSales 2024, j'ai découvert que de nombreuses entrées ont toutes (ou presque) leurs colonnes à NULL. Certaines catégories sont même entièrement vides ! Par exemple, les entrées pour les consoles "Séries" (comme "Call of Duty", "Pokemon", "Legend of Zelda") sont toutes à NULL. 

Je vais me faire une copie de cette sous-partie, je suis sûr que ça nous servira plus tard. Pour la suite, on va nettoyer une bonne partie en supprimant les entrées ayant "total_sales" à NULL. Enfin, hypothèse 100% biaisée : les jeux avec "last_update" à NULL n'ont jamais eu de mise à jour... le jeux vidéo avant l'existence du "Patch Day One", toute une époque, n'est-ce pas ?!

J'ai mis en place une fonction pour voir le Top N par catégorie, et c'est plutôt informatif. On y voit un manque de diversité dans les jeux les plus vendus (et ils ne sont même pas à mon goût 😑). On apprend que les branches d'EA sont particulièrement prolifiques, tandis que Nintendo se retrouve en 10e place ! Pour vous donner une idée, sur Kaggle et les datasets d'avant 2016, ils étaient en première position ! La fin de la Wii a-t-elle enterrée Nintendo ?

La prochaine fois, on va creuser un peu plus : OneHot encoding, corrélation, etc.. J'ai trop hâte ! Et vous ?

🤔 Pourquoi Nintendo a-t-il chuté sur cette première moitié de la décennie ? Un indice 🔎, ça a plus à voir avec le jeux de données qu'avec la R&D de Nintendo. 💡 Partagez vos idées en commentaire !

#DataScience #JeuxVidéo #AnalyseDeDonnées #Python #DataViz

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
