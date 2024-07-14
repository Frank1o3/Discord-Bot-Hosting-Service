from json import load,JSONDecodeError
from discord import app_commands
import discord

try:
    file = open("Clients/example1/Config.json","r")
    data = load(file)
    print(data["Token"])
except JSONDecodeError as e:
    raise e
finally:
    file.close()

Intents = discord.Intents().all()
Intents.message_content = True
Intents.guild_reactions = True
Intents.guild_typing = True
Intents.guilds = True

Client = discord.Client(intents=Intents)
Tree = app_commands.CommandTree(Client)


@Client.event
async def on_ready():
    print(f"{Client.user.name} Is Running...\n")
    async for guild in Client.fetch_guilds(limit=150):
        Tree.sync(guild=guild)

@Tree.command(name="ping",description="Reply's with Pong!")
async def ping(interaction:discord.Interaction):
    await interaction.response.send_message("Pong!")

Client.run()