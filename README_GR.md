# BHBot 

Gold/XP-Farming-Bot für Brawlhalla 

Stark inspiriert von [BrawlhallaEZ](https://github.com/jamunano/BrawlhallaEZ) 

### ------ -------------------------------------------------- ----------- 

### BOT WIRD WIEDER AKTIV GEWARTET! 
###### Treten Sie [Discord](https://discord.gg/2HDmuqqq9p) bei, um bei der Wartung des Bots zu helfen oder neue Funktionen hinzuzufügen! 

### ----------------------------------------------- -------------------- 

**WARNUNG:** Die Software wurde ursprünglich für den privaten Gebrauch entwickelt. 
Obwohl dies nicht beabsichtigt ist, kann es möglicherweise zu unvorhergesehenen Ergebnissen führen, einschließlich der Ausführung von Transaktionen innerhalb von Mallhalla unter Verwendung von Spielwährungen. 

**Die Entwickler lehnen jegliche Haftung für Schäden ab, die durch die Verwendung dieser Software entstehen könnten. Es wird empfohlen, mit Vorsicht vorzugehen und die Software nach eigenem Ermessen zu verwenden.** 

(Der Bot wurde am 18.04.2024 über 3.000 Stunden lang von mehreren Personen ohne Probleme getestet.) 

# Installation 
Die neueste Version kann immer [hier](https://github.com/Nick2bad4u/BHBot/releases) heruntergeladen werden 

# Funktionen 

– Funktioniert vollständig im Hintergrund 
– Sendet Eingaben direkt an Brawlhalla, um Sie nicht zu stören 
– Startet das Spiel automatisch 
– Erstellt/richtet automatisch eine Lobby ein 
– Wählt/Änderungen automatisch aus Charakter und Spieldauer 
– Erkennt das XP-Limit automatisch und setzt es zurück 
– Unterstützt benutzerdefinierte Modi 
– Unterstützt benutzerdefinierte Sprachen 
– Unterstützt sogar benutzerdefinierte Schriftarten 
– ~~Brüht Ihnen Kaffee~~ (derzeit wird nur Tee unterstützt) 

# Verwendung 
– Der Prozess ist so konzipiert, dass er intuitiv ist. Wählen Sie einfach die erforderlichen Einstellungen aus, indem Sie auf die Schaltfläche „Einstellungen“ klicken. 
- Sobald die Einstellungen gespeichert sind, starten Sie das Programm, indem Sie auf die Schaltfläche „Start“ klicken. 

# Einschränkungen 
– Für den Bot muss „Crossovers reduzieren“ auf „Ja“ eingestellt sein. Wenn Sie der Meinung sind, dass dies automatisch so eingestellt werden sollte, [öffnen Sie bitte ein Problem](https://github.com/nick2bad4u/bhbot/issues) 

– Der Bot erfordert, dass die Ingame-Sprache auf Englisch eingestellt ist. Wenn Sie der Meinung sind, dass dies automatisch so eingestellt werden sollte, [öffnen Sie bitte ein Problem](https://github.com/nick2bad4u/bhbot/issues) 

# Technischer Überblick 
– Der zugrunde liegende Code steht jederzeit zur Überprüfung durch jedermann zur Verfügung. 
– Im Wesentlichen nutzt der Bot die Windows SendMessage API, um Eingaben direkt an das Brawlhalla-Fenster zu übermitteln. Es nutzt die Pixelerkennung, um Zustände zu erkennen und zu jedem Zeitpunkt die richtige Aktion zu bestimmen.

- Die BrawlhallaBot-Klasse kann direkt verwendet werden oder Sie können einen benutzerdefinierten Wrapper dafür entwickeln. Es ist für den unabhängigen Betrieb konzipiert, wobei gui.py lediglich als grafischer Wrapper mit PySimpleGUI dient.
