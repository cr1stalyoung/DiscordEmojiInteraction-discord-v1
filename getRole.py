import discord
from discord.ext import commands

# *** List of Intents ***
intents = discord.Intents.default()
intents.members = True
# *** List of Intents ***

client = commands.Bot(
    command_prefix='!',
    help_command=None,
    intents=intents,
)


@client.event
async def on_ready():
    print("BOT STARTED")


@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == id_message: # message id of the message through which the role will be received with the help of emoji
        guild = client.get_guild(payload.guild_id)
        if payload.emoji.name == "name_emoji":
            role = discord.utils.get(guild.roles, name="name_emoji")
            await payload.member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == id_message: # message id of the message through which the roles will be removed with emoji
        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        if payload.emoji.name == "name_emoji":
            role = discord.utils.get(guild.roles, name="name_emoji")
            await member.remove_roles(role)


client.run('TOKEN')
