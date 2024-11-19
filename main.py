import os
import discord
import logging

from discord import app_commands
from contracts.constants import Constants
from api.members_api import members, member
from api.raids_api import raids, boss, boss_sondage
from api.bis_api import bis
from services.discord_thread import DiscordThread
from services.discord_poll import DiscordPoll

logging.basicConfig(level=logging.ERROR)
_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
_ID = int(os.getenv('DISCORD_ID'))
_CHAN_ID = int(os.getenv('EVENT_CHANNEL_ID'))
INTENTS = discord.Intents.default()
INTENTS.message_content = True

BOT = discord.Client(intents=INTENTS)
TREE = app_commands.CommandTree(BOT)

@BOT.event
async def on_ready():
    try:
        guild = discord.Object(id=_ID)
        await TREE.sync(guild=guild)
        print(f'Synced commands for guild {guild.id}')
    except Exception as e:
        print(f'Error syncing commands: {e}')
    
    print(f'Logged in as {BOT.user}')  


@BOT.event
async def on_error(event_method, *args, **kwargs):
    logging.exception(f'Error in {event_method}')

@BOT.event
async def on_message(message):
    pass

@TREE.command(name='ping', description="A simple ping command")
async def ping(interaction: discord.Interaction):
    print(f"/ping command invoked by {interaction.user}")
    await interaction.response.send_message('Pong!')

@TREE.command(name='membres', description="Permet d'obtenir la liste des membres de la guilde")
async def member_list(interaction: discord.Interaction):
    print("J'ai recu une commande sur membres")   
    await members(interaction)  

@TREE.command(name='membre', description="Permet d'obtenir les informations concernant un membre")
@app_commands.describe(
    pseudo="Pseudo du membre dont tu veux obtenir les informations.",
)
async def member_details(interaction: discord.Interaction, pseudo: str): 
    await member(interaction, pseudo)

@TREE.command(name='raids', description="Permet d'obtenir la liste des raids de guilde disponibles")
async def raid_list(interaction: discord.Interaction):   
    await raids(interaction)

@TREE.command(name='raid', description="Permet d'obtenir les informations concernant un boss de raid")
@app_commands.describe(
    boss="Nom du boss dont tu veux obtenir les informations.",
)
async def raid_details(interaction: discord.Interaction, boss: str): 
    await boss(interaction, boss)

@TREE.command(name='bis', description="Permet d'obtenir la liste des utilisateurs ayant partagé leur BiS")
async def members_with_bis(interaction: discord.Interaction):   
    await members(interaction, "bis=true")

@TREE.command(name='no_bis', description="Permet d'obtenir la liste des utilisateurs n'ayant pas partagé leur BiS")
async def members_without_bis(interaction: discord.Interaction):   
    await members(interaction, "bis=false")

@TREE.command(name='stuff', description="Permet d'obtenir les informations concernant le BiS d'un membre")
@app_commands.describe(
    pseudo="Pseudo du membre dont tu veux obtenir les informations.",
)
async def member_bis(interaction: discord.Interaction, pseudo: str):   
    await bis(interaction, pseudo)

@TREE.command(name='sb', description="Permet d'obtenir la liste des boss de raid avec un emoji pour faciliter les votes")
async def boss_sondage_creation(interaction: discord.Interaction):   
    await boss_sondage(interaction)

@TREE.command(name='rt', description="Permet de créer un thread sur le canal #évènements")
@app_commands.describe(
    name="Nom du thread",
    message="Message initial du thread",
    duration="Durée de l'auto-archive (1H: 1 heure, 24H: 24 heures, 3J: 3 jours, 1S: 1 semaine)",
    tags="Tags à ajouter séparés à l'aide d'une virgule (Dungeon, Raid, PvP, Event)"
)     
async def create_thread(
    interaction: discord.Interaction,
    name: str,
    message: str,
    duration: str = "1W",
    tags: str = "Raid"
):
    try:
        discord_thread = DiscordThread(BOT)
        thread = await discord_thread.create_thread(
            channel_id=_CHAN_ID,
            thread_name=name,
            message_content=message,
            auto_archive_duration=duration,
            applied_tags=tags
        )
        
        await interaction.response.send_message(f"Thread created: {thread.mention}")
    except Exception as e:
        await interaction.followup.send(f"Error creating Thread: {e}")

@TREE.command(name='poll', description="Permet de créer un sondage")
@app_commands.describe(
    channel="Id du canal où envoyer le sondage",
    question="Question (jusqu'à 300 caractères)",
    answers="Réponses séparées par des virgules (2 à 20 réponses de 55 caractères chacune)",
    duration="Durée du sondage (1H: 1 heure, 24H: 24 heures, 3J: 3 jours, 1S: 1 semaine)",
    multiple="Est-ce un QCM ? (True/False)",
)
async def create_poll(
    interaction: discord.Interaction,
    channel: int,
    question: str,
    answers: str,
    duration: int,
    multiple: bool = False,
):
    await interaction.response.defer()
    answers_list = [answer.strip() for answer in answers.split(',') if answer.strip()]
    try:
        poll = DiscordPoll(BOT)
        poll_message = await poll.create_poll(
            channel_id=channel,
            question=question,
            answers=answers_list,
            duration=duration,
            multiple=multiple,
        )
        await interaction.followup.send(f"Poll created in channel {poll_message.channel.mention}.")
    except Exception as e:
        await interaction.followup.send(f"Error creating Poll: {e}")

BOT.run(_TOKEN)
