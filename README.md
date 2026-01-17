> ⚠️ **Project Closed - Move to PRAWL! — Please Read**
>
> This repository is no longer the active.
> Active development on another BHBOT type program continues at **https://github.com/phruut/prawl**.  
> Please update your bookmarks and submit issues or PRs there instead.
> Do NOT pay for any Brawlhalla bots as they are most likely scams.
>
> ⚠️ **Project Closed - Move to PRAWL! — Please Read**

# BHBot

[Этот файл доступен на Русском языке](README_RU.md)

Gold/XP farming bot for Brawlhalla

Heavily inspired by [BrawlhallaEZ](https://github.com/jamunano/BrawlhallaEZ)

### **WARNING:** The software only works on Windows 64 bit versions. No other Operating Systems are supported.

### -------------------------------------------------------------------

### BOT IS BACK TO BEING ACTIVELY MAINTAINED!
###### Join [Discord](https://discord.gg/2HDmuqqq9p "Discord") to help maintain the bot or add new features!

### -------------------------------------------------------------------

**WARNING:** The software was originally developed for private utilization. 
While it is not designed to, it may potentially lead to unforeseen outcomes, including the execution of transactions within Mallhalla using in-game currencies. 

**The developers disclaims all liability for any damages that may arise from the use of this software. It is advised to proceed with caution and utilize the software at your own discretion.**

(Bot has been tested by multiple people for over 3,000 hours without issue as of 4/18/2024)

# Installation
- Latest release can always be downloaded [here](https://github.com/Nick2bad4u/BHBot/releases) I recommend using the .exe version if you are not experienced with Python.
- If you have issues running the .exe version, try to download the [source code directly](https://github.com/Nick2bad4u/BHBot/archive/refs/tags/BHBOT.zip) then run gui.pyw or gui.py.
- If you double click and nothing happens, try to open PowerShell or Command Prompt and navigate to the source code folder you downloaded and run it:
	- You can use the following command to change directories in Command Prompt or PowerShell:
		- ``cd C:\your\sourcecode\folder\here``
	- Then type``gui.pyw`` or ``gui.py``
- If you still cannot get the bot started or running, make sure you have python installed. I recommend [Python 3.11.8](https://www.python.org/downloads/release/python-3118/), but [any version after](https://www.python.org/downloads/) should work.
- If the bot is still not working, open Windows Powershell or Command Prompt and change directory to the source code folder you downloaded (You need to unzip it). 
	- You can use the following command to change directories in Command Prompt or PowerShell:
		- ``cd C:\your\sourcecode\folder\here``
	- Once you are in the proper directory, type the following:
		- ``pip install -r requirements.txt``
			- This will install the proper dependencies for the bot to run. 
			- This isn't needed in most cases but I've seen a few users who need to do this in order to get the bot running. *Not sure why as of now. :|*

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

- The BrawlhallaBot class can be utilized directly or you may develop a custom wrapper for it. It is designed to operate independently, with gui.py serving merely as a graphical wrapper using PySimpleGUI.
