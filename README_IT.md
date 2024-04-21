# BHBot 

Bot agricolo Gold/XP per Brawlhalla 

Fortemente ispirato da [BrawlhallaEZ](https://github.com/jamunano/BrawlhallaEZ) 

### ------ -------------------------------------------------- ----------- 

### IL BOT TORNA A ESSERE MANTENUTO ATTIVAMENTE! 
###### Unisciti a [Discord](https://discord.gg/2HDmuqqq9p "Discord") per aiutare a mantenere il bot o aggiungere nuove funzionalità! 

### ----------------------------------------------- -------------------- 

**ATTENZIONE:** Il software è stato originariamente sviluppato per uso privato. 
Anche se non è progettato per questo, potrebbe potenzialmente portare a risultati imprevisti, inclusa l'esecuzione di transazioni all'interno di Mallhalla utilizzando le valute di gioco. 

**Gli sviluppatori declinano ogni responsabilità per eventuali danni che potrebbero derivare dall'uso di questo software. Si consiglia di procedere con cautela e utilizzare il software a propria discrezione.** 

(Il bot è stato testato da più persone per oltre 3.000 ore senza problemi al 18/4/2024) 

# Installazione 
L'ultima versione può sempre essere scaricata [qui ](https://github.com/Nick2bad4u/BHBot/releases) 

# Funzionalità 

- Funziona completamente in background 
- Invia input direttamente a Brawlhalla per non disturbarti 
- Avvia automaticamente il gioco 
- Crea/imposta automaticamente la lobby 
- Seleziona/modifica automaticamente personaggio e durata del gioco 
- Rileva e reimposta automaticamente il limite XP 
- Supporta modalità personalizzate 
- Supporta lingue personalizzate 
- Supporta anche caratteri personalizzati 
- ~~Prepara il caffè~~ (per ora è supportato solo il tè) 

# Utilizzo 
- Il processo è progettato per essere intuitivo. Scegli semplicemente le impostazioni richieste facendo clic sul pulsante "Impostazioni" 
- Una volta salvate le impostazioni, avvia il programma facendo clic sul pulsante "Avvia" 

# Limitazioni 
- Il bot richiede che "Comprimi crossover" sia impostato su Sì. Se ritieni che dovrebbe essere impostato automaticamente in questo modo, per favore [apri un problema](https://github.com/nick2bad4u/bhbot/issues) 
- Il bot richiede che la lingua di gioco sia impostata sull'inglese. Se ritieni che dovrebbe essere impostato automaticamente in questo modo, per favore [apri un problema](https://github.com/nick2bad4u/bhbot/issues) 

# Panoramica tecnica 
: il codice sottostante è sempre disponibile per la revisione da parte di chiunque. 
- Essenzialmente, il bot utilizza l'API SendMessage di Windows per trasmettere input direttamente alla finestra Brawlhalla. Utilizza il rilevamento dei pixel per discernere gli stati e determinare l'azione appropriata in un dato momento.

- La classe BrawlhallaBot può essere utilizzata direttamente oppure è possibile sviluppare un wrapper personalizzato per essa. È progettato per funzionare in modo indipendente, con gui.py che funge semplicemente da wrapper grafico utilizzando PySimpleGUI.
