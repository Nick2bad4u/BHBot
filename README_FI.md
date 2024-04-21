# BHBot 

[Этот файл доступен на Русском языке](README_RU.md) 

Kulta-/XP-viljelybotti Brawlhallalle. 

Vahvasti inspiroitunut [BrawlhallaEZ](https://github.com/jamunano/BrawlhallaEZ)

# --------------------------------------------------- ----------- 

### BOTI ON TAAS AKTIIVISESTI YLLÄPISTETTY! 
###### Liity [Discordiin](https://discord.gg/2HDmuqqq9p "Discord") auttaaksesi ylläpitämään bottia tai lisäämään uusia ominaisuuksia! 

### ------------------------------------------------- -------------------- 

**VAROITUS:** Ohjelmisto on alun perin kehitetty yksityiskäyttöön. 
Vaikka sitä ei ole suunniteltu niin, se voi mahdollisesti johtaa odottamattomiin tuloksiin, mukaan lukien tapahtumien suorittamiseen Mallhallassa käyttämällä pelin sisäisiä valuuttoja. 

**Kehittäjä ei ota vastuuta kaikista tämän ohjelmiston käytöstä mahdollisesti aiheutuvista vahingoista. On suositeltavaa toimia varoen ja käyttää ohjelmistoa oman harkintasi mukaan.** 

(Monet ihmiset ovat testaaneet Botia yli 3 000 tuntia ilman ongelmia 18.4.2024) 

# Asennus 
Uusin versio on aina ladattavissa [täältä ](https://github.com/Nick2bad4u/BHBot/releases) 

# Ominaisuudet 

- Toimii täysin taustalla 
- Lähettää syötteet suoraan Brawlhallalle, jotta se ei häiritse sinua 
- Käynnistää pelin automaattisesti 
- Luo/määrittää aulan automaattisesti 
- Poimii/muuttaa automaattisesti hahmo ja pelin kesto 
- Tunnistaa ja nollaa xp limitin automaattisesti 
- Tukee mukautettuja tiloja 
- Tukee mukautettuja kieliä 
- Tukee jopa mukautettuja fontteja 
- ~~Hauduttaa kahvia~~ (toistaiseksi tuettu vain teetä) 

# Käyttö 
- Prosessi on suunniteltu intuitiiviseksi. Valitse vain tarvittavat asetukset napsauttamalla "Asetukset" -painiketta 
- Kun asetukset on tallennettu, käynnistä ohjelma napsauttamalla "Käynnistä"-painiketta. 

# Rajoitukset 
- Bot vaatii "Collapse crossovers" -asetukseksi Kyllä. Jos uskot, että sen pitäisi asettaa se automaattisesti niin, [avaa ongelma](https://github.com/nick2bad4u/bhbot/issues) 
– Bot vaatii, että pelin kieleksi on asetettava englanti. Jos uskot, että sen pitäisi asettaa se automaattisesti niin, [avaa ongelma](https://github.com/nick2bad4u/bhbot/issues) 

# Tekninen yleiskatsaus 
– taustalla oleva koodi on aina kenen tahansa tarkastettavissa. 
- Pohjimmiltaan botti käyttää Windows SendMessage API:ta syötteiden välittämiseen suoraan Brawlhalla-ikkunaan. Se käyttää pikselien havaitsemista tilojen erottamiseen ja sopivan toiminnan määrittämiseen kulloinkin.

- BrawlhallaBot-luokkaa voi käyttää suoraan tai voit kehittää sille mukautetun kääreen. Se on suunniteltu toimimaan itsenäisesti, ja gui.py toimii vain graafisena kääreenä PySimpleGUI:n avulla.
