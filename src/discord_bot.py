import os
from dotenv import load_dotenv

# Discord bot imports
import discord
from discord import app_commands
from discord.ext import commands

from data_formatter import get_player_info

# load token from safe file
load_dotenv()
bot_token = os.getenv('DISCORD_TOKEN')

# Loads bot with intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '%', intents = discord.Intents.default())

# Attempts to sync commands on start
@bot.event
async def on_ready():
    print(f'{bot.user} is now running')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

# Get player info command
@bot.tree.command(name='embed')
@app_commands.describe(username = 'Player username?') # Prompt to ask for player username
@app_commands.describe(tagline = 'Player tagline?') # Prompt to ask for player tagline
async def embed(interaction: discord.Interaction, username : str, tagline : str):
    # Check to see if user included hashtag, and parses it from the tagline
    if tagline[0] == '#':
        tagline = tagline[1:]
    
    player_data = get_player_info(username.lower(), tagline.lower())

    # Creates the discord embed
    embed = discord.Embed(
        description=f"⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n**Player Info:**\nUsername: {player_data['username']}\n\nTagline: #{player_data['tagline']}\n\nRegion: {(player_data['region']).upper()}\n\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n**Player stats:**\nLevel: {player_data['level']}\n\nWins: {player_data['all_time_ranked_wins']}\n\nLosses: {player_data['all_time_ranked_loses']}\n\nWin Rate: {player_data['all_time_winrate']}%\n\nGames Played: {player_data['all_time_ranked_games']}\n\nPeak Rating: {player_data['peak_rank']}\n\nCurrent Rank: {player_data['current_rank']}\n\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n> Episode 9 Act 1",
        colour=0x00b0f4
    )

    # User's peak rating and badge will be displayed
    embed.set_author(name=f"Peaking rating: {player_data['peak_rank']}",
                 icon_url="https://media.valorant-api.com/competitivetiers/564d8e28-c226-3180-6285-e48a390db8b1/19/smallicon.png")
    
    # User's banner wide at the bottom
    embed.set_image(url=f"{player_data['banner_wide']}")

    # Displays user's current rank as icon
    embed.set_thumbnail(url=f"{player_data['current_rank_icons']['small']}")

    # Displays user's username and tagline at the bottom with small icon of banner
    embed.set_footer(text=f"{player_data['username']}#{player_data['tagline']}",
                    icon_url=f"{player_data['banner_small']}")

    await interaction.response.send_message(embed=embed)

# Runs bot with token from .env file
bot.run(bot_token)