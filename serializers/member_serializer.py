import textwrap
from datetime import date
from discord import Embed

from contracts.constants import Constants

def members_serializer(members):
    members_list = []

    for member in members:
        member_name = member.get('username', 'Inconnu')
        member_grade = member.get('grade', 'Inconnu')
        member_weapon = member.get('weapon', 'Inconnu')
        member_combat_type = member.get('combat_type', 'Inconnu')
        member_info = textwrap.dedent(f"""\
            # {member_name}
            ├⎯ **Grade** : {member_grade.get('label', 'Inconnu')}
            ├⎯ **Armes** : {member_weapon.get('label', 'Inconnu')}
            ├⎯ **Style de combat** : {Constants.COMBAT_TYPE_ICONS.get(member_combat_type.get('id', None), '')} {member_combat_type.get('label', 'Inconnu')}
        """)

        members_list.append(member_info.strip())

    return '\n'.join(members_list)

def member_serializer(member):
    member_name = member.get('username', 'Inconnu')
    member_grade = member.get('grade', 'Inconnu')
    member_weapon = member.get('weapon', 'Inconnu')
    member_combat_type = member.get('combat_type', 'Inconnu')
    grade = member_grade.get('label', 'Inconnu')
    weapons = member_weapon.get('label', 'Inconnues')
    combat_type = f"{Constants.COMBAT_TYPE_ICONS.get(member_combat_type.get('id', None), '')} {member_combat_type.get('label', 'Inconnu')}"
    is_pvp = Constants.BOOL_TRANSLATION.get(member.get('is_pvp', 'false'), 'Non')
    on_discord = Constants.BOOL_TRANSLATION.get(member.get('is_on_discord', 'false'), 'Non')
    is_active = Constants.BOOL_TRANSLATION.get(member.get('is_active', 'false'), 'Non')
    date_in = member.get('added_at', 'Inconnue')

    embed = Embed(title=member_name, color=0xbcdab1)

    embed.add_field(name="**Grade**", value=grade, inline=True)
    embed.add_field(name="**Armes**", value=weapons, inline=True)
    embed.add_field(name="**Style de combat**", value=combat_type, inline=True)
    embed.add_field(name="**Intéressé par le PvP ?**", value=is_pvp, inline=True)
    embed.add_field(name="**Membre actif dans la guide ?**", value=is_active, inline=True)
    embed.add_field(name="**Présent sur le discord ?**", value=on_discord, inline=True)
    embed.add_field(name="**Date d'entrée dans la guilde**", value=date_in, inline=True)
    embed.set_footer(text=Constants.EMBED_FOOTER)

    return embed