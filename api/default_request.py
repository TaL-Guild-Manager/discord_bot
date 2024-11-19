import os
import discord

from services.send_message import send_message

_HOST = os.getenv('HOST')
_HEADERS = {'Host': _HOST}

async def default_request(url, session, destination, serializer, error_message, api_error_message):
    async with session.get(url, headers=_HEADERS) as resp:
        data = await resp.json()
        code = data.get('code', 500)
        if code == 200:
            content = data.get('data', [])
            if content:
                serialized_data = serializer(content)
                
                if isinstance(serialized_data, discord.Embed):
                    await send_message(destination, embed=serialized_data)
                elif isinstance(serialized_data, str):
                    for chunk in [serialized_data[i:i+1999] for i in range(0, len(serialized_data), 1999)]:
                        await send_message(destination, content=chunk)
                else:
                    await send_message(destination, content="An error occurred while processing the data.")
            else:
                await send_message(destination, content=error_message)
        elif code == 404:
            await send_message(destination, content=f"{api_error_message} Ce que vous recherchiez n'a pas été trouvé.")
        else:
            content = data.get('data', [])
            await send_message(destination, content=f"{api_error_message}\nCode obtenu : {code}\nMessage de l'API: {content.get('error', None)}")

async def loop_message(url, session, destination, serializer, error_message, api_error_message):
    async with session.get(url, headers=_HEADERS) as resp:
        data = await resp.json()
        code = data.get('code', 500)
        if code == 200:
            content = data.get('data', [])
            if content:
                for item in content:
                    serialized_data = serializer(item)
                    
                    if isinstance(serialized_data, discord.Embed):
                        await send_message(destination, embed=serialized_data, reaction='👍')
                    elif isinstance(serialized_data, str):
                        for chunk in [serialized_data[i:i+1999] for i in range(0, len(serialized_data), 1999)]:
                            await send_message(destination, content=chunk, reaction='👍')
                    else:
                        await send_message(destination, content="An error occurred while processing the data.")
            else:
                await send_message(destination, content=error_message)
        elif code == 404:
            await send_message(destination, content=f"{api_error_message} Ce que vous recherchiez n'a pas été trouvé.")
        else:
            content = data.get('data', [])
            await send_message(destination, content=f"{api_error_message}\nCode obtenu : {code}\nMessage de l'API: {content.get('error', None)}")
