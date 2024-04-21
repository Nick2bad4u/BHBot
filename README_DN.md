# BHBot 

Gold/XP farming bot for Brawlhalla 

Stærkt inspireret af [BrawlhallaEZ](https://github.com/jamunano/BrawlhallaEZ-) 

### -------------------------------------------------- ----------- 

### BOT ER TILBAGE TIL AT VÆRE AKTIVT VEDLIGEHOLDELSE! 
###### Tilmeld dig [Discord](https://discord.gg/2HDmuqqq9p "Discord") for at hjælpe med at vedligeholde botten eller tilføje nye funktioner! 

### ----------------------------------------------- -------------------- 

**ADVARSEL:** Softwaren blev oprindeligt udviklet til privat brug. 
Selvom det ikke er designet til, kan det potentielt føre til uforudsete resultater, herunder udførelse af transaktioner i Mallhalla ved hjælp af in-game valutaer. 

**Udviklerne fraskriver sig ethvert ansvar for eventuelle skader, der måtte opstå som følge af brugen af ​​denne software. Det tilrådes at fortsætte med forsigtighed og bruge softwaren efter eget skøn.** 

(Botten er blevet testet af flere personer i over 3.000 timer uden problemer pr. 18.4.2024) 

# Installation 
Seneste udgivelse kan altid downloades [her ](https://github.com/Nick2bad4u/BHBot/releases) 

# Funktioner 

- Fungerer fuldstændig i baggrunden 
- Sender input direkte til Brawlhalla for ikke at forstyrre dig 
- Starter spillet automatisk 
- Opretter/opretter automatisk lobby 
- Vælger/ændrer automatisk karakter og spilvarighed 
- Registrerer og nulstiller automatisk xp-grænsen 
- Understøtter brugerdefinerede tilstande 
- Understøtter brugerdefinerede sprog 
- Understøtter endda brugerdefinerede skrifttyper 
- ~~Bryger kaffe til dig~~ (kun te understøttes indtil videre) 

# Brug 
- Processen er designet til at være intuitiv. Vælg blot de nødvendige indstillinger ved at klikke på knappen "Indstillinger" 
- Når indstillingerne er gemt, start programmet ved at klikke på knappen "Start" 

# Begrænsninger 
- Bot kræver, at "Skjul krydsovergange" er indstillet til Ja. Hvis du mener, at det automatisk skal indstille det til at være det, bedes du [åbn et problem](https://github.com/nick2bad4u/bhbot/issues) 
- Bot kræver, at ingame-sproget er indstillet til engelsk. Hvis du mener, at det automatisk skal indstille det til at være det, bedes du [åbn et problem](https://github.com/nick2bad4u/bhbot/issues) 

# Teknisk oversigt 
- Den underliggende kode er altid tilgængelig for gennemgang af alle. 
- Botten anvender i bund og grund Windows SendMessage API til at overføre input direkte til Brawlhalla-vinduet. Den bruger pixeldetektion til at skelne tilstande og bestemme den passende handling på ethvert givet tidspunkt.

- BrawlhallaBot-klassen kan bruges direkte, eller du kan udvikle en brugerdefineret indpakning til den. Den er designet til at fungere uafhængigt, hvor gui.py kun tjener som en grafisk indpakning ved hjælp af PySimpleGUI.
