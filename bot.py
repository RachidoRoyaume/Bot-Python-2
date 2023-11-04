import discord
from discord.ext import commands

intents = discord.Intents.default()
# Activer les intents appropriés en fonction de vos besoins
intents.guilds = True  # Pour accéder aux informations sur les serveurs
intents.guild_messages = True  # Pour recevoir des messages de serveur
intents.message_content = True  # Pour lire le contenu des messages
intents.guilds = True
intents.members = True

TOKEN = 'MTEzNzQ4NjM5NTk1MTI4NDM0Ng.Gp2Jwe.BaRCSRe5jw-JoPEeL9GePoKZseFTlDezES5xOQ'

bot = commands.Bot(command_prefix='!', intents=intents)

# Fonction pour supprimer des salons par ID
async def delete_channels(ctx, *channel_ids):
    for channel_id in channel_ids:
        try:
            channel = ctx.guild.get_channel(int(channel_id))
            if channel:
                await channel.delete()
                await ctx.send(f"Salon {channel.name} supprimé avec succès.")
            else:
                await ctx.send(f"Salon avec l'ID {channel_id} non trouvé.")
        except Exception as e:
            await ctx.send(f"Une erreur s'est produite lors de la suppression du salon {channel_id}: {e}")

# Commande !channel pour supprimer des salons par ID
@bot.command()
async def channel(ctx, *channel_ids):
    if not channel_ids:
        await ctx.send("Utilisation : !channel <ID1> <ID2> ...")
    else:
        await delete_channels(ctx, *channel_ids)

# Démarrage du bot avec votre jeton Discord

async def delete_roles(ctx, *role_ids):
    for role_id in role_ids:
        try:
            role = ctx.guild.get_role(int(role_id))
            if role:
                await role.delete()
                await ctx.send(f"Rôle {role.name} supprimé avec succès.")
            else:
                await ctx.send(f"Rôle avec l'ID {role_id} non trouvé.")
        except Exception as e:
            await ctx.send(f"Une erreur s'est produite lors de la suppression du rôle {role_id}: {e}")

# Commande !role pour supprimer des rôles par ID
@bot.command()
async def role(ctx, *role_ids):
    if not role_ids:
        await ctx.send("Utilisation : !role <ID1> <ID2> ...")
    else:
        await delete_roles(ctx, *role_ids)

async def clear_category(ctx, category_id):
    try:
        category = ctx.guild.get_channel(int(category_id))
        if category and isinstance(category, discord.CategoryChannel):
            for channel in category.channels:
                await channel.delete()
            await ctx.send(f"Tous les canaux de la catégorie {category.name} ont été supprimés avec succès.")
        else:
            await ctx.send(f"Catégorie avec l'ID {category_id} non trouvée.")
    except Exception as e:
        await ctx.send(f"Une erreur s'est produite lors de la suppression de la catégorie {category_id}: {e}")

# Commande !clearcategorie pour supprimer tous les canaux d'une catégorie par son ID
@bot.command()
async def clearcategorie(ctx, category_id):
    if not category_id:
        await ctx.send("Utilisation : !clearcategorie <ID de la catégorie>")
    else:
        await clear_category(ctx, category_id)

message = "Venez sur discord.gg/royaume @everyone"

@bot.command()
async def pub(ctx, nombre_messages: int, *, message: str):
    if nombre_messages < 1 or nombre_messages > 1000000:
        await ctx.send("Le nombre de messages doit être compris entre 1 et 10.")
    elif not message:
        await ctx.send("Veuillez spécifier le message que vous souhaitez envoyer.")
    else:
        await ctx.send(f"Envoi de {nombre_messages} messages :")

        for i in range(nombre_messages):
            await ctx.send(f"{i + 1}. {message}")

@bot.command()
async def unbanall(ctx):
    banned_users = await ctx.guild.bans()  # Obtient la liste des bannis sur le serveur
    
    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban(user)
    
    await ctx.send("Tous les bannissements ont été révoqués.")


# Commande !dmall pour envoyer un message DM à tous les membres avec un rôle spécifique
@bot.command()
async def dmall(ctx, *, message):
    for member in ctx.guild.members:
        try:
            await member.send(message)
            await ctx.send(f"Message envoyé à {member.display_name}.")
        except discord.Forbidden:
            await ctx.send(f"Impossible d'envoyer un message à {member.display_name} (les DMs sont désactivés ou le membre a bloqué les DMs).")
        except Exception as e:
            await ctx.send(f"Une erreur s'est produite lors de l'envoi du message à {member.display_name}: {e}")







bot.run(TOKEN)
