
# General Purpose Valorant Bot

This is a Discord bot built using the Discord.py library. The bot fetches and processes data from an API to provide information about Valorant players.

## Table of Contents

- [Overview](#overview)
- [Roadmap and features](#Roadmap/bot-features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Bot](#running-the-bot)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Valorant Discord Bot is a general-purpose bot for Discord designed to provide Valorant-related information and functionalities. This bot utilizes the Valorant API to fetch real-time game data, match statistics, and more. It is built using Python and the `discord.py` library to interface with Discord's API.

### APIs Used

- <a href="https://github.com/Henrik-3/unofficial-valorant-api"> **unofficial valorant api**</a> by <a href="https://github.com/Henrik-3">__Henrik 3__</a>: Provides data related to Valorant matches, player statistics, and other game information.
- <a href="https://valorant-api.com/"> **valorant-api.com**</a> by <a href="https://github.com/NotOfficer">__NotOfficer__</a>: Provides various Valorant in game assets including skins, icons, agents and many more

## Roadmap/bot features

- [x] Player info
- [x] Player statistics
- [x] Player rank information
- [ ] Agent information
- [ ] Weapon stats
- [ ] Map information
- [ ] Patch notes
- [ ] User profiles
- [ ] Info on VCT matches commands
- [ ] Valorant leaderboard features
    - [ ] Premier
    - [ ] Radiant and Immortal leaderboard

## Prerequisites

Before you begin, ensure you have met the following requirements:

- [Python 3.12.2](https://www.python.org/downloads/) or higher is installed on your machine.
- [Visual Studio Code](https://code.visualstudio.com/download) is the recommended IDE for developing the discord bot
- VScode Python and Pylance Extension for the python environment
- [git](https://git-scm.com/downloads) and [Github Desktop](https://github.com/apps/desktop) for version control
- [pip](https://pip.pypa.io/en/stable/installation/) is installed for package management.
- Access to the discord bot application and token (Message harpoonz_ on discord)
- Access to API key (Message harpoonz_ on discord)

## Installation

To set up the project, follow these steps:

1. **Fork the Repository:**
To contribute to this project or modify it for your use, first fork the repository:
- Navigate to the repository on GitHub.
- Click on the `Fork` button at the top right of the page to create a copy of the repository under your own GitHub account.
2. **Clone the repository:** 
```bash
git clone https://github.com/your_username/General-Purpose-Valorant-Bot.git
```
3. **Navigate to the project directory:**
```bash
cd General-Purpose-Valorant-Bot
```
4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Configuration

1. **Create a `.env` File**

   In the root directory of the project, create a `.env` file to store your sensitive information like the Discord bot token and any API keys.

   ```
   DISCORD_TOKEN=your_discord_bot_token_here
   API_KEY=your_api_key_here
   ```

2. **Configure Environment Variables**

   Ensure your `.env` file is correctly formatted and saved in the project’s root directory. The `.env` file should not be included in version control, as it contains sensitive information. Make sure your `.gitignore` file includes:

   ```
   .env
   ```

## Running the Bot

**Run the Bot**

   Start the Discord bot using:

   ```bash
   python discord_bot.py
   ```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.