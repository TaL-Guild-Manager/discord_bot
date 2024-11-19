import os
import aiohttp
import discord

from serializers.raids_serializer import raids_serializer, boss_serializer, boss_sondage_serializer
from .default_request import default_request, loop_message
from services.send_message import send_message

_DJANGO_API_URL = os.getenv('DJANGO_API_URL')

async def raids(ctx):
    async with aiohttp.ClientSession() as session:
        try:
            url = f"{_DJANGO_API_URL}/boss"
            error_message = "Aucun raid trouvé."
            api_error_message = "Erreur lors de la récupération des raids de guilde. L'API a retouné l'erreur suivante:"

            await default_request(url, session, ctx, raids_serializer, error_message, api_error_message)
        except aiohttp.ClientError as e:
            await send_message(ctx, content=f"Une erreur de client est survenue: {str(e)}")
        except Exception as e:
            await send_message(ctx, content=f"Une erreur est survenue: {str(e)}")

async def boss(interaction: discord.Interaction, boss: str):
    async with aiohttp.ClientSession() as session:
        try:
            url = f"{_DJANGO_API_URL}/boss/find?label={boss}"
            error_message = "Aucun raid trouvé avec ce nom."
            api_error_message = "Erreur lors de la récupération du raid de guilde. L'API a retouné l'erreur suivante:"

            await default_request(url, session, interaction, boss_serializer, error_message, api_error_message)
        except aiohttp.ClientError as e:
            await send_message(interaction, content=f"Une erreur de client est survenue: {str(e)}")
        except Exception as e:
            await send_message(interaction, content=f"Une erreur est survenue: {str(e)}")

async def boss_sondage(ctx):
    async with aiohttp.ClientSession() as session:
        try:
            url = f"{_DJANGO_API_URL}/boss"
            error_message = "Aucun raid trouvé."
            api_error_message = "Erreur lors de la récupération des raids de guilde. L'API a retouné l'erreur suivante:"

            await loop_message(url, session, ctx, boss_sondage_serializer, error_message, api_error_message)
        except aiohttp.ClientError as e:
            await send_message(ctx, content=f"Une erreur de client est survenue: {str(e)}")
        except Exception as e:
            await send_message(ctx, content=f"Une erreur est survenue: {str(e)}")
    