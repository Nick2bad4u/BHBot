# BHBot 

[Этот файл доступен на Русском языке](README_RU.md) 

Gold/XP farming bot för Brawlhalla 

Starkt inspirerad av [BrawlhallaEZ](https://github.com/jamunano/BrawlhallaEZ-) 

# ----## -------------------------------------------------- ----------- 

### BOT ÄR TILLBAKA TILL ATT BLI AKTIVT UNDERHÅLLS! 
###### Gå med i [Discord](https://discord.gg/2HDmuqqq9p "Discord") för att hjälpa till att underhålla boten eller lägga till nya funktioner! 

### ---------------------------------------------------- -------------------- 

**VARNING:** Programvaran utvecklades ursprungligen för privat användning. 
Även om det inte är designat för det kan det potentiellt leda till oförutsedda resultat, inklusive genomförande av transaktioner inom Mallhalla med valutor i spelet. 

**Utvecklarna frånsäger sig allt ansvar för eventuella skador som kan uppstå från användningen av denna programvara. Det rekommenderas att fortsätta med försiktighet och använda programvaran efter eget gottfinnande.** 

(Botten har testats av flera personer i över 3 000 timmar utan problem den 18/4/2024) 

# Installation 
Senaste versionen kan alltid laddas ner [här ](https://github.com/Nick2bad4u/BHBot/releases) 

# Funktioner 

- Fungerar helt i bakgrunden 
- Skickar ingångar direkt till Brawlhalla för att inte störa dig 
- Startar spelet automatiskt 
- Skapar/ställer in lobbyn 
- Väljer/ändrar automatiskt karaktär och spellängd 
- Upptäcker och återställer automatiskt xp limit 
- Stöder anpassade lägen 
- Stöder anpassade språk 
- Stöder även anpassade typsnitt 
- ~~Bryggar kaffe~~ (endast te stöds för närvarande) 

# Användning 
- Processen är designad för att vara intuitiv. Välj helt enkelt de nödvändiga inställningarna genom att klicka på knappen "Inställningar" 
- När inställningarna har sparats, starta programmet genom att klicka på "Start"-knappen 

# Begränsningar 
- Bot kräver att "Komprimera korsningar" är inställd på Ja. Om du tror att det automatiskt ska ställa in det så, vänligen [öppna ett problem](https://github.com/nick2bad4u/bhbot/issues) 
- Bot kräver att spelspråket är inställt på engelska. Om du tror att det automatiskt ska ställa in det så, vänligen [öppna ett problem](https://github.com/nick2bad4u/bhbot/issues) 

# Teknisk översikt 
- Den underliggande koden är alltid tillgänglig för granskning av vem som helst. 
- Boten använder sig av Windows SendMessage API för att överföra indata direkt till Brawlhalla-fönstret. Den använder pixeldetektion för att urskilja tillstånd och bestämma lämplig åtgärd vid varje givet ögonblick.

- Klassen BrawlhallaBot kan användas direkt eller så kan du utveckla en anpassad omslag för den. Den är designad för att fungera självständigt, med gui.py som endast fungerar som ett grafiskt omslag med PySimpleGUI.
