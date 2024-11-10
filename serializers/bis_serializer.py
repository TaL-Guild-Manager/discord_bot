import textwrap
from datetime import date
from discord import Embed

from contracts.constants import Constants

def bis_serializer(bis):
    bis_member = bis.get('member', 'Inconnu')
    bis_stuffs = bis.get('stuffs', 'Inconnu')
    member_name = bis_member.get('username', 'Inconnu')
    member_weapon = bis_member.get('weapon', 'Inconnu')
    member_combat_type = bis_member.get('combat_type', 'Inconnu')
    weapons = member_weapon.get('label', 'Inconnues')
    combat_type = f"{Constants.COMBAT_TYPE_ICONS.get(member_combat_type.get('id', None), '')} {member_combat_type.get('label', 'Inconnu')}"

    embed = Embed(title=member_name, color=0xbcdab1)
    embed.add_field(name="**Armes**", value=weapons, inline=False)
    embed.add_field(name="**Style de combat**", value=combat_type, inline=False)

    for stuff in bis_stuffs:
        stuff_name = stuff.get('label', 'Inconnu')
        raid_loot = stuff.get('is_raid_loot', False)
        stuff_type = stuff.get('loot_type', 'Inconnu')
        type_label = stuff_type.get('label', 'Inconnu')
        
        embed.add_field(name=stuff_name, value=type_label, inline=True)

        if raid_loot:
            stuff_boss = stuff.get('boss', 'Inconnu')
            boss_name = stuff_boss.get('label', 'Inconnu')

            embed.add_field(name="Loot de", value=boss_name, inline=True)

    embed.set_footer(text=Constants.EMBED_FOOTER)

    return embed