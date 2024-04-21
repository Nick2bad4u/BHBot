# BHBot 

Bot agricole Gold/XP pour Brawlhalla 

Fortement inspiré de [BrawlhallaEZ](https://github.com/jamunano/BrawlhallaEZ) 

### ------ -------------------------------------------------- ----------- 

### LE BOT EST DE RETOUR À ÊTRE ACTIVEMENT MAINTENU ! 
###### Rejoignez [Discord](https://discord.gg/2HDmuqqq9p "Discord") pour aider à maintenir le bot ou ajouter de nouvelles fonctionnalités ! 

### ----------------------------------------------- -------------------- 

**AVERTISSEMENT :** Le logiciel a été initialement développé pour un usage privé. 
Bien que cela ne soit pas conçu pour cela, cela peut potentiellement conduire à des résultats imprévus, notamment l'exécution de transactions au sein de Mallhalla en utilisant les devises du jeu. 

**Les développeurs déclinent toute responsabilité pour les dommages pouvant résulter de l'utilisation de ce logiciel. Il est conseillé de procéder avec prudence et d'utiliser le logiciel à votre propre discrétion.** 

(Le robot a été testé par plusieurs personnes pendant plus de 3 000 heures sans problème au 18/04/2024) 

# Installation 
La dernière version peut toujours être téléchargée [ici](https://github.com/Nick2bad4u/BHBot/releases) 

# Fonctionnalités 

- Fonctionne entièrement en arrière-plan 
- Envoie les entrées directement à Brawlhalla pour ne pas vous déranger 
- Lance automatiquement le jeu 
- Crée/configure automatiquement le lobby 
- Sélectionne/modifie automatiquement durée du personnage et du jeu 
- Détecte et réinitialise automatiquement la limite XP 
- Prend en charge les modes personnalisés 
- Prend en charge les langues personnalisées 
- Prend même en charge les polices personnalisées 
- ~~ Vous prépare du café ~~ (uniquement le thé pris en charge pour l'instant) 

# Utilisation 
- Le processus est conçu pour être intuitif. Choisissez simplement les paramètres requis en cliquant sur le bouton "Paramètres" 
- Une fois les paramètres enregistrés, démarrez le programme en cliquant sur le bouton "Démarrer" 

# Limitations 
- Le robot nécessite que "Réduire les croisements" soit défini sur Oui. Si vous pensez qu'il devrait le définir automatiquement, veuillez [ouvrir un problème](https://github.com/nick2bad4u/bhbot/issues) 
- Le robot nécessite que la langue du jeu soit définie sur l'anglais. Si vous pensez qu'il devrait automatiquement le définir ainsi, veuillez [ouvrir un problème](https://github.com/nick2bad4u/bhbot/issues) 

# Présentation technique 
- Le code sous-jacent est toujours disponible pour examen par n'importe qui. 
- Essentiellement, le bot utilise l'API Windows SendMessage pour transmettre les entrées directement à la fenêtre Brawlhalla. Il utilise la détection de pixels pour discerner les états et déterminer l'action appropriée à un moment donné.

- La classe BrawlhallaBot peut être utilisée directement ou vous pouvez développer un wrapper personnalisé pour celle-ci. Il est conçu pour fonctionner indépendamment, gui.py servant simplement de wrapper graphique utilisant PySimpleGUI.
