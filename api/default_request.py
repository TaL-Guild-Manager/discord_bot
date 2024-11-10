import os
import discord

_HOST = os.getenv('HOST')
_HEADERS = {'Host': _HOST}

async def default_request(url, session, message, serializer, error_message, api_error_message):
    async with session.get(url, headers=_HEADERS) as resp:
        data = await resp.json()
        code = data.get('code', 500)
        if code == 200:
            content = data.get('data', [])
            if content:
                serialized_data = serializer(content)
                
                if isinstance(serialized_data, discord.Embed):
                    await message.channel.send(embed=serialized_data)
                elif isinstance(serialized_data, str):
                    for chunk in [serialized_data[i:i+1999] for i in range(0, len(serialized_data), 1999)]:
                        await message.channel.send(chunk)
                else:
                    await message.channel.send("An error occurred while processing the data.")
            else:
                await message.channel.send(error_message)
        elif code == 404:
            await message.channel.send(f"{api_error_message} Ce que vous recherchiez n'a pas été trouvé.")
        else:
            content = data.get('data', [])
            await message.channel.send(f"{api_error_message}\nCode obtenu : {code}\nMessage de l'API: {content.get('error', None)}")

async def loop_message(url, session, message, serializer, error_message, api_error_message):
    async with session.get(url, headers=_HEADERS) as resp:
        data = await resp.json()
        code = data.get('code', 500)
        if code == 200:
            content = data.get('data', [])
            if content:
                for item in content:
                    print(item)
                    serialized_data = serializer(item)
                
                    if isinstance(serialized_data, discord.Embed):
                        msg = await message.channel.send(embed=serialized_data)
                        await msg.add_reaction('👍')
                    elif isinstance(serialized_data, str):
                        for chunk in [serialized_data[i:i+1999] for i in range(0, len(serialized_data), 1999)]:
                            msg = await message.channel.send(chunk)
                            await msg.add_reaction('👍')
                    else:
                        await message.channel.send("An error occurred while processing the data.")
            else:
                await message.channel.send(error_message)
        elif code == 404:
            await message.channel.send(f"{api_error_message} Ce que vous recherchiez n'a pas été trouvé.")
        else:
            content = data.get('data', [])
            await message.channel.send(f"{api_error_message}\nCode obtenu : {code}\nMessage de l'API: {content.get('error', None)}")
