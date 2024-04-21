
# BHBot 

[Этот файл доступен на Русском языке](README_RU.md) 

Gold/XP farming bot for Brawlhalla 

Sterkt inspirert av [BrawlhallaEZ](https://github.com/jamunano/BrawlhallaEZ-) 

# ----## -------------------------------------------------- ----------- 

### BOT ER TILBAKE TIL Å BLI AKTIVT VEDLIKEHOLDT! 
###### Bli med i [Discord](https://discord.gg/2HDmuqqq9p "Discord") for å vedlikeholde boten eller legge til nye funksjoner! 

### ----------------------------------------------- -------------------- 

**ADVARSEL:** Programvaren ble opprinnelig utviklet for privat bruk. 
Selv om det ikke er designet for, kan det potensielt føre til uforutsette utfall, inkludert utførelse av transaksjoner i Mallhalla ved å bruke valutaer i spillet. 

**Utviklerne fraskriver seg alt ansvar for eventuelle skader som kan oppstå ved bruk av denne programvaren. Det anbefales å fortsette med forsiktighet og bruke programvaren etter eget skjønn.** 

(Botten har blitt testet av flere personer i over 3000 timer uten problemer per 18.4.2024) 

# Installasjon 
Siste utgivelse kan alltid lastes ned [her](https://github.com/Nick2bad4u/BHBot/releases) 

# Funksjoner 

- Fungerer helt i bakgrunnen 
- Sender innspill direkte til Brawlhalla for ikke å forstyrre deg 
- Starter spillet automatisk 
- Oppretter/sett opp lobbyen 
- Velger/endres automatisk karakter og spillvarighet 
- Oppdager og tilbakestiller automatisk xp-grense 
- Støtter egendefinerte moduser 
- Støtter tilpassede språk 
- Støtter til og med egendefinerte fonter 
- ~~Bryger deg kaffe~~ (bare te støttes foreløpig) 

# Bruk 
- Prosessen er designet for å være intuitiv. Bare velg de nødvendige innstillingene ved å klikke på "Innstillinger"-knappen 
- Når innstillingene er lagret, start programmet ved å klikke på "Start"-knappen 

# Begrensninger 
- Bot krever at "Skjul crossovers" er satt til Ja. Hvis du tror den automatisk skal sette den til å være slik, vennligst [åpne et problem](https://github.com/nick2bad4u/bhbot/issues) 
- Bot krever at ingame-språket er satt til engelsk. Hvis du tror at det automatisk skal sette det slik, vennligst [åpne et problem](https://github.com/nick2bad4u/bhbot/issues) 

# Teknisk oversikt 
- Den underliggende koden er alltid tilgjengelig for vurdering av alle. 
- Boten bruker i hovedsak Windows SendMessage API for å overføre innganger direkte til Brawlhalla-vinduet. Den bruker pikseldeteksjon for å skjelne tilstander og bestemme passende handling til enhver tid.

- BrawlhallaBot-klassen kan brukes direkte, eller du kan utvikle en tilpasset innpakning for den. Den er designet for å fungere uavhengig, med gui.py som kun fungerer som en grafisk innpakning ved hjelp av PySimpleGUI.
