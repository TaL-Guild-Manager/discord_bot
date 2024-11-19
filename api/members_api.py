import os
import aiohttp
import discord

from serializers.member_serializer import members_serializer, member_serializer
from .default_request import default_request
from services.send_message import send_message

_DJANGO_API_URL = os.getenv('DJANGO_API_URL')

async def members(ctx, filter=None):
    async with aiohttp.ClientSession() as session:
        try:
            if filter:
                url = f"{_DJANGO_API_URL}/member?{filter}"
            else:
                url = f"{_DJANGO_API_URL}/member"
            error_message = "Aucun membre trouvé."
            api_error_message = "Erreur lors de la récupération des membres de la guilde. L'API a retouné l'erreur suivante:"

            await default_request(url, session, ctx, members_serializer, error_message, api_error_message)
        except aiohttp.ClientError as e:
            await send_message(ctx, content=f"Une erreur de client est survenue: {str(e)}")
        except Exception as e:
            await send_message(ctx, content=f"Une erreur est survenue: {str(e)}")

async def member(interaction: discord.Interaction, pseudo: str):
    await interaction.response.defer(thinking=True)

    async with aiohttp.ClientSession() as session:
        try:
            url = f"{_DJANGO_API_URL}/member/find?username={pseudo}"
            error_message = "Aucun membre trouvé avec ce pseudo."
            api_error_message = "Erreur lors de la récupération du membre de la guilde. L'API a retouné l'erreur suivante:"

            await default_request(url, session, interaction, member_serializer, error_message, api_error_message)
        except aiohttp.ClientError as e:
            await send_message(interaction, content=f"Une erreur de client est survenue: {str(e)}")
        except Exception as e:
            await send_message(interaction, content=f"Une erreur est survenue: {str(e)}")
    