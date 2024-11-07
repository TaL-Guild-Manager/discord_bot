class Constants:
    BOT_PREFIX = "9"

    EMBED_FOOTER = "九尾狐 - 맹독이 최고야!"
  
    BOOL_TRANSLATION = {
        0: 'Non',
        1: 'Oui',
    }

    COMBAT_TYPE_ICONS = {
        1: '🗡️',
        2: '🛡️',
        3: '💚',
    } 

    COMMANDS = [
        "## DISCLAIMER",
        "Les données sont entrées manuellement et peuvent donc variées ou être inexactes. Veuillez contacter **Maengdok** si vous pensez qu'il y a une erreur.",
        f"- ✅ **{BOT_PREFIX}help** : Permet d'obtenir la liste des commandes disponibles",
        f"- ✅ **{BOT_PREFIX}membres** : Permet d'obtenir la liste des membres de la guilde",
        f"- ✅ **{BOT_PREFIX}membre** *<Nom du membre>* : Permet d'obtenir les informations concernant un membre",
        f"- ❌ **{BOT_PREFIX}roadsters** : Permet d'obtenir la liste des roadsters de la guilde",
        f"- ✅ **{BOT_PREFIX}raids** : Permet d'obtenir la liste des raids de guilde disponibles",
        f"- ✅ **{BOT_PREFIX}raid** *<Nom du boss>* : Permet d'obtenir les informations concernant un boss de raid",
        f"- ❌ **{BOT_PREFIX}bis** : Permet d'obtenir la liste des utilisateurs ayant partagé leur BiS",
        f"- ❌ **{BOT_PREFIX}bis_membre** *<Nom du membre>* : Permet d'obtenir les informations concernant le BiS d'un membre",
        f"- ❌ **{BOT_PREFIX}items** : Permet d'obtenir la liste des items pouvant être obtenu sur les différents raids",
        f"- ❌ **{BOT_PREFIX}distribution** *<Nom anglais de l'item>*: Permet d'obtenir la distribution d'un item aux différents membres ayant l'item pour BiS",
        f"- ❌ **{BOT_PREFIX}contributions** : Permet d'obtenir la liste des membres et leur contribution respective sur la semaine actuelle (du jour du reset hebdo soit mercredi à la veille du reset hebdo soit mardi)",
        f"- ❌ **{BOT_PREFIX}contribution** *<Nom du membre>* : Permet d'obtenir la contribution d'un membre sur la semaine actuell (du jour du reset hebdo soit mercredi à la veille du reset hebdo soit mardi)",
        f"- ❌ **{BOT_PREFIX}surveillance** : Permet d'obtenir la liste des membres qui risquent le kick pour inactivité",
        "✅ : Commande fonctionnelle\n⚠️ : Commande en construction\n❌ : Commande non fonctionnelle ou en prévision",
    ]