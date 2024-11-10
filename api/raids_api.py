import os
import aiohttp

from serializers.raids_serializer import raids_serializer, boss_serializer, boss_sondage_serializer
from .default_request import default_request, loop_message

_DJANGO_API_URL = os.getenv('DJANGO_API_URL')

async def raids(message):
    async with aiohttp.ClientSession() as session:
        try:
            url = f"{_DJANGO_API_URL}/boss"
            error_message = "Aucun raid trouvé."
            api_error_message = "Erreur lors de la récupération des raids de guilde. L'API a retouné l'erreur suivante:"

            await default_request(url, session, message, raids_serializer, error_message, api_error_message)
        except aiohttp.ClientError as e:
            await message.channel.send(f"Une erreur de client est survenue: {str(e)}")
        except Exception as e:
            await message.channel.send(f"Une erreur est survenue: {str(e)}")

async def boss(message):
    boss = message.content.split(' ')[1]

    async with aiohttp.ClientSession() as session:
        try:
            url = f"{_DJANGO_API_URL}/boss/find?label={boss}"
            error_message = "Aucun raid trouvé avec ce nom."
            api_error_message = "Erreur lors de la récupération du raid de guilde. L'API a retouné l'erreur suivante:"

            await default_request(url, session, message, boss_serializer, error_message, api_error_message)
        except aiohttp.ClientError as e:
            await message.channel.send(f"Une erreur de client est survenue: {str(e)}")
        except Exception as e:
            await message.channel.send(f"Une erreur est survenue: {str(e)}")

async def boss_sondage(message):
    async with aiohttp.ClientSession() as session:
        try:
            url = f"{_DJANGO_API_URL}/boss"
            error_message = "Aucun raid trouvé."
            api_error_message = "Erreur lors de la récupération des raids de guilde. L'API a retouné l'erreur suivante:"

            await loop_message(url, session, message, boss_sondage_serializer, error_message, api_error_message)
        except aiohttp.ClientError as e:
            await message.channel.send(f"Une erreur de client est survenue: {str(e)}")
        except Exception as e:
            await message.channel.send(f"Une erreur est survenue: {str(e)}")
    