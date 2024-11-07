import textwrap
import discord
from datetime import date
from discord import Embed

from contracts.constants import Constants

def raids_serializer(raids):
    raids_list = []

    for raid in raids:
        raid_name = f" - **{raid.get('label', 'Inconnu')}**"

        raids_list.append(raid_name.strip())

    return '\n'.join(raids_list)

def boss_serializer(raid):
    raid_name = raid.get('label', 'Inconnu')
    raid_loots = raid.get('loots', 'Inconnu')

    embed = Embed(title=raid_name, color=0xEA9999)

    loot_n = 0
    for raid_loot in raid_loots:
        loot_n += 1
        loot_label = raid_loot.get('label', 'Inconnu')
        loot_type = raid_loot.get('loot_type', {})
        loot_type_label = loot_type.get('label', 'Inconnu')

        field_name = f"**Loot {loot_n}**: {loot_label}"
        field_value = f"{loot_type_label}"
        embed.add_field(name=field_name, value=field_value, inline=False)

    embed.set_footer(text=Constants.EMBED_FOOTER)

    return embed