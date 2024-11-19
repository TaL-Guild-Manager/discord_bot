import discord
from discord.ext import commands

async def send_message(destination, content=None, embed=None, reaction=None):
    msg = None
    if isinstance(destination, discord.Interaction):
        if not destination.response.is_done():
            await destination.response.send_message(content=content, embed=embed)
            msg = await destination.original_response()
        else:
            msg = await destination.followup.send(content=content, embed=embed)
    elif isinstance(destination, commands.Context):
        msg = await destination.send(content=content, embed=embed)
    else:
        raise TypeError("destination must be an Interaction or Context")

    if reaction and msg:
        try:
            await msg.add_reaction(reaction)
        except Exception as e:
            print(f"Failed to add reaction: {e}")

    return msg
