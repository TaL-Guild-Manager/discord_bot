import os
import discord

_HOST = os.getenv('HOST')
_HEADERS = {'Host': _HOST}

async def default_request(url, session, message, serializer, response_message, error_message, api_error_message):
    async with session.get(url, headers=_HEADERS) as resp:
        if resp.status == 200:
            data = await resp.json()
            content = data.get('data', [])
            if content:
                serialized_data = serializer(content)
                
                await message.channel.send(response_message)
                
                if isinstance(serialized_data, discord.Embed):
                    await message.channel.send(embed=serialized_data)
                elif isinstance(serialized_data, str):
                    for chunk in [serialized_data[i:i+1999] for i in range(0, len(serialized_data), 1999)]:
                        await message.channel.send(chunk)
                else:
                    await message.channel.send("An error occurred while processing the data.")
            else:
                await message.channel.send(error_message)
        else:
            await message.channel.send(f"{api_error_message} {resp.status}")
