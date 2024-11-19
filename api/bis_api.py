import os
import aiohttp
import discord

from serializers.bis_serializer import bis_serializer
from .default_request import default_request
from services.send_message import send_message


_DJANGO_API_URL = os.getenv('DJANGO_API_URL')

async def bis(interaction: discord.Interaction, pseudo: str):
    async with aiohttp.ClientSession() as session:
        try:
            url = f"{_DJANGO_API_URL}/bis/find?username={pseudo}"
            error_message = "Aucun BiS trouvé avec ce pseudo."
            api_error_message = "Erreur lors de la récupération du BiS de la guilde."

            await default_request(url, session, interaction, bis_serializer, error_message, api_error_message)
        except aiohttp.ClientError as e:
            await send_message(interaction, content=f"Une erreur de client est survenue: {str(e)}")