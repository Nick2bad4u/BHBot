# BHBot

[Этот файл доступен на Русском языке](README_RU.md)

Gold/XP farming bot for Brawlhalla

Heavily inspired by [BrawlhallaEZ](https://github.com/jamunano/BrawlhallaEZ)

**WARNING:** Bot was initially made for personal use. It should not, but still can cause some unexpected consequences, including making purchases from mallhalla (with in-game currencies). Developer is
not responsible for any harm the program may case. Use at your own risk

[Virus Total Scan](https://www.virustotal.com/gui/file/af110c1886ba1a24c1122cfc527d0183a4650bb933a35d44c2389ed1d585b489?nocache=1)
![Results](https://github.com/Nick2bad4u/BHBot/assets/20943337/92bb7f30-e7ae-4e85-a13b-95a6530eeaf9)

[Submitted to Microsoft as a False Positive for Windows Defender, coming back clean as of 3-12-24.](https://www.microsoft.com/en-us/wdsi/submission/e9889ce6-6dc9-44bc-b7ba-c5759544b2a4)
![Windows Defender Results](https://i.gyazo.com/acbabb1aa492c86852e5ca2027044992.png)

(it should work fine tho, I tested it for >600 hours at this point)

# Installation
Latest release can always be downloaded [here](https://sovamor.co/bhbot)

Bot _should_ auto-update as soon as any updates are released according to selected branch in settings

# Features

- Works completely in background
- Sends inputs directly to Brawlhalla to not disturb you
- Automatically launches the game
- Automatically creates/sets up lobby
- Automatically picks/changes character and game duration
- Automatically detects and resets xp limit
- Supports custom modes
- Supports custom languages
- Even supports custom fonts
- ~~Brews you coffee~~ (only tea supported for now)

# Usage
Should be pretty straightforward. Just select needed settings and click "Start" :)

# Limitations
- Bot requires "Collapse crossovers" to be set to Yes. If you think it should automatically set it to be so, please [open an issue](https://github.com/sovamorco/bhbot/issues)
- Bot requires ingame language to be set to English. If you think it should automatically set it to be so, please [open an issue](https://github.com/sovamorco/bhbot/issues)

# Internal stuff
You can always check the code, but basically bot uses windows SendMessage API to send inputs directly to Brawlhalla window and pixel detection to detect states and
decide what to do at any given point

You can use BrawlhallaBot class directly or write your own wrapper for it. It should be completely independent and gui.py is just a PySimpleGUI graphical wrapper
