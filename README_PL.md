# BHBot 

Bot rolniczy Gold/XP dla Brawlhalla 

Mocno inspirowany [BrawlhallaEZ](https://github.com/jamunano/BrawlhallaEZ) 

### ------ -------------------------------------------------- ----------- 

### BOT POWRACA DO AKTYWNIE UTRZYMANEGO! 
###### Dołącz do [Discord](https://discord.gg/2HDmuqqq9p), aby pomóc w utrzymaniu bota lub dodaniu nowych funkcji! 

### -------------------------------------------------------------- -------------------- 

**OSTRZEŻENIE:** Oprogramowanie zostało pierwotnie opracowane do użytku prywatnego. 
Chociaż nie jest to przeznaczone, może potencjalnie prowadzić do nieprzewidzianych skutków, w tym do realizacji transakcji w ramach Mallhalla przy użyciu walut w grze. 

** Twórcy zrzekają się wszelkiej odpowiedzialności za jakiekolwiek szkody, które mogą wyniknąć z korzystania z tego oprogramowania. Zaleca się zachowanie ostrożności i korzystanie z oprogramowania według własnego uznania.** 

(Bot był testowany przez wiele osób przez ponad 3000 godzin bez żadnych problemów na dzień 18.04.2024 r.) 

# Instalacja 
Zawsze można pobrać najnowszą wersję [tutaj ](https://github.com/Nick2bad4u/BHBot/releases) 

# Funkcje 

- Działa całkowicie w tle 
- Wysyła dane wejściowe bezpośrednio do Brawlhalla, aby ci nie przeszkadzać 
- Automatycznie uruchamia grę 
- Automatycznie tworzy/konfiguruje lobby 
- Automatycznie wybiera/zmienia postać i czas trwania gry 
- Automatycznie wykrywa i resetuje limit XP 
- Obsługuje niestandardowe tryby 
- Obsługuje niestandardowe języki 
- Obsługuje nawet niestandardowe czcionki 
- ~~Parzy kawę~~ (na razie obsługiwana jest tylko herbata) 

# Użycie 
- Proces został zaprojektowany tak, aby był intuicyjny. Po prostu wybierz żądane ustawienia, klikając przycisk „Ustawienia”. 
- Po zapisaniu ustawień uruchom program, klikając przycisk „Start”. 

# Ograniczenia 
- Bot wymaga ustawienia opcji „Zwiń skrzyżowania” na Tak. Jeśli uważasz, że powinno to zostać ustawione automatycznie, [otwórz problem](https://github.com/nick2bad4u/bhbot/issues)

- Bot wymaga ustawienia języka gry na angielski. Jeśli uważasz, że powinno to zostać automatycznie ustawione, aby tak było, [otwórz problem](https://github.com/nick2bad4u/bhbot/issues) 

# Przegląd techniczny 
- kod źródłowy jest zawsze dostępny do przeglądu dla każdego. 
- Zasadniczo bot wykorzystuje interfejs API Windows SendMessage do przesyłania danych wejściowych bezpośrednio do okna Brawlhalla. Wykorzystuje detekcję pikseli do rozpoznawania stanów i określania odpowiednich działań w danym momencie.

- Klasę BrawlhallaBot można wykorzystać bezpośrednio lub możesz opracować dla niej niestandardowe opakowanie. Został zaprojektowany do niezależnego działania, a gui.py służy jedynie jako opakowanie graficzne korzystające z PySimpleGUI.
