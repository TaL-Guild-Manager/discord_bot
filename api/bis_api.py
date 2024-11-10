import os
import aiohttp

from serializers.bis_serializer import bis_serializer
from .default_request import default_request

_DJANGO_API_URL = os.getenv('DJANGO_API_URL')

async def bis(message):
    member = message.content.split(' ')[1]

    async with aiohttp.ClientSession() as session:
        try:
            url = f"{_DJANGO_API_URL}/bis/find?username={member}"
            error_message = "Aucun BiS trouvé avec ce pseudo."
            api_error_message = "Erreur lors de la récupération du BiS de la guilde."

            await default_request(url, session, message, bis_serializer, error_message, api_error_message)
        except aiohttp.ClientError as e:
            await message.channel.send(f"Une erreur de client est survenue: {str(e)}")
        # except Exception as e:
        #     await message.channel.send(f"Une erreur est survenue: {str(e)}")
    