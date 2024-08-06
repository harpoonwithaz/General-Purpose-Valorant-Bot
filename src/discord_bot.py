import os
from dotenv import load_dotenv

# Discord bot imports
import discord
from discord import app_commands
from discord.ext import commands

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
    
    # Creates the discord embed
    embed = discord.Embed(
        description=f"⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n**Player Info:**\nUsername: {username}\n\nTagline: #{tagline}\n\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n**Player stats:**\nLevel: player level here\n\nWins: wins here\n\nLosses: losses here\n\nWin Rate: win rate here\n\nGames Played: games played here\n\nPeak Rating: peak rating here\n\nCurrent Rank: current rank here\n\nLast Game Result: last game here\n\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\n\n> Episode 9 Act 1",
        colour=0x00b0f4
    )

    # User's peak rating and badge will be displayed
    embed.set_author(name="Peaking rating: *peak rating here*",
                 icon_url="https://media.valorant-api.com/competitivetiers/564d8e28-c226-3180-6285-e48a390db8b1/19/smallicon.png")
    
    # User's banner wide at the bottom
    embed.set_image(url="https://media.valorant-api.com/playercards/c7e58b09-4b1f-ca2a-5ab6-daa6cab2fa6c/wideart.png")

    # Displays user's current rank as icon
    embed.set_thumbnail(url="https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/16/smallicon.png")

    # Displays user's username and tagline at the bottom with small icon of banner
    embed.set_footer(text="H00DBYAIR#BMWM5",
                    icon_url="https://media.valorant-api.com/playercards/c7e58b09-4b1f-ca2a-5ab6-daa6cab2fa6c/smallart.png")

    await interaction.response.send_message(embed=embed)

# Runs bot with token from .env file
bot.run(bot_token)