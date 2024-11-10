import textwrap
import discord
from datetime import date
from discord import Embed

from contracts.constants import Constants

def raids_serializer(raids):
    embed = Embed(title="Raids de guilde", color=0xEA9999)

    for raid in raids:
        boss_name = raid.get('label', 'Inconnu')
        boss_loots = raid.get('loots', 'Inconnu')

        embed.add_field(name="Boss", value=boss_name, inline=False)

        for loot in boss_loots:
            loot_label = loot.get('label', 'Inconnu')
            loot_type = loot.get('loot_type', 'Inconnu')
            loot_type_label = loot_type.get('label', 'Inconnu')

            embed.add_field(name=loot_label, value=loot_type_label, inline=True)

    embed.set_footer(text=Constants.EMBED_FOOTER)

    return embed

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

def boss_sondage_serializer(raid):
    print(raid)
    boss_name = raid.get('label', 'Inconnu')

    return boss_name
