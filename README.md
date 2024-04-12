# **BHBot**
#### **Gold/XP farming bot for Brawlhalla**

[![Semgrep](https://github.com/Nick2bad4u/BHBot/actions/workflows/semgrep.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/semgrep.yml)
[![Upload Python Package](https://github.com/Nick2bad4u/BHBot/actions/workflows/python-publish.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/python-publish.yml)
[![Python Package using Conda](https://github.com/Nick2bad4u/BHBot/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/python-package-conda.yml)
[![CodeQL](https://github.com/Nick2bad4u/BHBot/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/github-code-scanning/codeql)
[![Bandit](https://github.com/Nick2bad4u/BHBot/actions/workflows/bandit.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/bandit.yml)
[![Dependency review](https://github.com/Nick2bad4u/BHBot/actions/workflows/dependency-review.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/dependency-review.yml)
[![DevSkim](https://github.com/Nick2bad4u/BHBot/actions/workflows/devskim.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/devskim.yml)
[![Greetings](https://github.com/Nick2bad4u/BHBot/actions/workflows/greetings.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/greetings.yml)
[![Mark stale issues and pull requests](https://github.com/Nick2bad4u/BHBot/actions/workflows/stale.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/stale.yml)
[![Microsoft Defender For Devops](https://github.com/Nick2bad4u/BHBot/actions/workflows/defender-for-devops.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/defender-for-devops.yml)
[![OSSAR](https://github.com/Nick2bad4u/BHBot/actions/workflows/ossar.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/ossar.yml)
[![Python application](https://github.com/Nick2bad4u/BHBot/actions/workflows/python-app.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/python-app.yml)
[![Scorecard supply-chain security](https://github.com/Nick2bad4u/BHBot/actions/workflows/scorecard.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/scorecard.yml)
[![Sobelow](https://github.com/Nick2bad4u/BHBot/actions/workflows/sobelow.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/sobelow.yml)
[![Lint Code Base](https://github.com/Nick2bad4u/BHBot/actions/workflows/super-linter.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/super-linter.yml)

- **[Latest Release](https://github.com/Nick2bad4u/BHBot/releases)** - Download Python (Source Code) or Compiled EXE version for Windows here. 
###### (Looking for a Mac user to compile it into a .DMG file, if you know any or would be willing to do this, let me know.)

**USA** users that want to use stealth mode, please do the following: (otherwise everytime the *"earn free rewards"* pops up it will stop the bot until cleared)
- You need to go into the bot settings and unselect "mute" if you are using stealth mode in the USA.
- Manually mute the bot via Windows Volume Mixer

[Этот файл доступен на Русском языке](README_RU.md)

Heavily inspired by [BrawlhallaEZ](https://github.com/jamunano/BrawlhallaEZ)

- **WARNING:** Bot was initially made for personal use. It should not, but still can cause some unexpected consequences, including making purchases from mallhalla (with in-game currencies). Developer is not responsible for any harm the program may case.
- **Use at your own risk**
- ###### (It should work fine, I tested it for >2000 hours at this point along with a variety of other people)

# Installation

Latest release can always be downloaded [here](https://github.com/Nick2bad4u/BHBot/releases/)

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

- Should be pretty straightforward. Just select needed settings and click "Start" :)

# Limitations

- Bot requires "Collapse crossovers" to be set to Yes.
- Bot requires ingame language to be set to English.

# Internal stuff

- You can always check the code, but basically the bot uses Windows SendMessage API to send inputs directly to a Brawlhalla window with pixel detection to detect states of the game and then decide what to do at any given point - depending on mode selected

- You can use BrawlhallaBot class directly or write your own wrapper for it. 
- It is completely independent and gui.py is just a PySimpleGUI graphical wrapper
