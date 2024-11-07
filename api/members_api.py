import os
import aiohttp

from serializers.member_serializer import members_serializer, member_serializer
from .default_request import default_request

_DJANGO_API_URL = os.getenv('DJANGO_API_URL')

async def members(message):
    async with aiohttp.ClientSession() as session:
        try:
            url = f"{_DJANGO_API_URL}/member"
            response_message = "Voici la liste des membres de Kumiho\n\n"
            error_message = "Aucun membre trouvé."
            api_error_message = "Erreur lors de la récupération des membres de la guilde. L'API a retouné l'erreur suivante:"

            await default_request(url, session, message, members_serializer, response_message, error_message, api_error_message)
        except aiohttp.ClientError as e:
            await message.channel.send(f"Une erreur de client est survenue: {str(e)}")
        except Exception as e:
            await message.channel.send(f"Une erreur est survenue: {str(e)}")

async def member(message):
    member = message.content.split(' ')[1]

    async with aiohttp.ClientSession() as session:
        try:
            url = f"{_DJANGO_API_URL}/member/find?username={member}"
            response_message = "Voici les informations concernant le membre recherché\n\n"
            error_message = "Aucun membre trouvé avec ce pseudo."
            api_error_message = "Erreur lors de la récupération du membre de la guilde. L'API a retouné l'erreur suivante:"

            await default_request(url, session, message, member_serializer, response_message, error_message, api_error_message)
        except aiohttp.ClientError as e:
            await message.channel.send(f"Une erreur de client est survenue: {str(e)}")
        except Exception as e:
            await message.channel.send(f"Une erreur est survenue: {str(e)}")
    