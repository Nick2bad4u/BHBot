[![Lint Code Base](https://github.com/Nick2bad4u/BHBot/actions/workflows/super-linter.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/super-linter.yml)
[![Bandit](https://github.com/Nick2bad4u/BHBot/actions/workflows/bandit.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/bandit.yml)
[![CodeQL](https://github.com/Nick2bad4u/BHBot/actions/workflows/codeql.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/codeql.yml)
[![Dependabot Updates](https://github.com/Nick2bad4u/BHBot/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/dependabot/dependabot-updates)
[![Dependency review](https://github.com/Nick2bad4u/BHBot/actions/workflows/dependency-review.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/dependency-review.yml)
[![DevSkim](https://github.com/Nick2bad4u/BHBot/actions/workflows/devskim.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/devskim.yml)
[![Generate xml sitemap](https://github.com/Nick2bad4u/BHBot/actions/workflows/sitemap.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/sitemap.yml)
[![Greetings](https://github.com/Nick2bad4u/BHBot/actions/workflows/greetings.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/greetings.yml)
[![Mark stale issues and pull requests](https://github.com/Nick2bad4u/BHBot/actions/workflows/stale.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/stale.yml)
[![Microsoft Defender For Devops](https://github.com/Nick2bad4u/BHBot/actions/workflows/defender-for-devops.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/defender-for-devops.yml)
[![OSSAR](https://github.com/Nick2bad4u/BHBot/actions/workflows/ossar.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/ossar.yml)
[![pages-build-deployment](https://github.com/Nick2bad4u/BHBot/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/pages/pages-build-deployment)
[![Pylint](https://github.com/Nick2bad4u/BHBot/actions/workflows/pylint.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/pylint.yml)
[![Python application](https://github.com/Nick2bad4u/BHBot/actions/workflows/python-app.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/python-app.yml)
[![Python Package using Conda](https://github.com/Nick2bad4u/BHBot/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/python-package-conda.yml)
[![Scorecard supply-chain security](https://github.com/Nick2bad4u/BHBot/actions/workflows/scorecard.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/scorecard.yml)
[![Semgrep](https://github.com/Nick2bad4u/BHBot/actions/workflows/semgrep.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/semgrep.yml)
[![Sobelow](https://github.com/Nick2bad4u/BHBot/actions/workflows/sobelow.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/sobelow.yml)
[![Upload Python Package](https://github.com/Nick2bad4u/BHBot/actions/workflows/python-publish.yml/badge.svg)](https://github.com/Nick2bad4u/BHBot/actions/workflows/python-publish.yml)

# BHBot

[Этот файл доступен на Русском языке](README_RU.md)

Gold/XP farming bot for Brawlhalla

Heavily inspired by [BrawlhallaEZ](https://github.com/jamunano/BrawlhallaEZ)

### -------------------------------------------------------------------

### BOT IS BACK TO BEING ACTIVELY MAINTAINED!
###### Join [Discord](https://discord.gg/2HDmuqqq9p "Discord") to help maintain the bot or add new features!

### -------------------------------------------------------------------

**WARNING:** The software was originally developed for private utilization. 
While it is not designed to, it may potentially lead to unforeseen outcomes, including the execution of transactions within Mallhalla using in-game currencies. 

**The developers disclaims all liability for any damages that may arise from the use of this software. It is advised to proceed with caution and utilize the software at your own discretion.**

(Bot has been tested by multiple people for over 3,000 hours without issue as of 4/18/2024)

# Installation
Latest release can always be downloaded [here](https://github.com/Nick2bad4u/BHBot/releases)

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
- The process is designed to be intuitive. Simply choose the required settings by clicking the "Settings" button
- Once settings are saved, start the program by clicking on "Start" button

# Limitations
- Bot requires "Collapse crossovers" to be set to Yes. If you think it should automatically set it to be so, please [open an issue](https://github.com/nick2bad4u/bhbot/issues)
- Bot requires ingame language to be set to English. If you think it should automatically set it to be so, please [open an issue](https://github.com/nick2bad4u/bhbot/issues)

# Technical Overview
- The underlying code is always available for review by anyone.
- Essentially, the bot employs the Windows SendMessage API to transmit inputs directly to the Brawlhalla window. It utilizes pixel detection to discern states and determine the appropriate action at any given moment.

- The BrawlhallaBot class can be utilized directly or you may develop a custom wrapper for it. It is designed to operate independently, with gui.py serving merely as a graphical wrapper using PySimpleGUI<img src="https://www.google-analytics.com/collect?v=2&tid=G-6RR5ZF4BJV&cid=555&t=event&en=eventName">
