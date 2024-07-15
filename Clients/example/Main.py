from json import load, JSONDecodeError
from discord import app_commands
import discord
import os


def shift_decrypt(text, offset):
    result = ""
    for char in text:
        # Decrypt all characters, wrapping within the ASCII range
        result += chr((ord(char) - offset) % 256)
    return result


# Load and decrypt the token from the JSON file
Path = __file__
Name = os.path.basename(__file__)

Path = Path.replace(Name, "Config.json")

try:
    with open(Path, "r") as file:
        data = load(file)
        Token = shift_decrypt(data["Token"], data["ID"])
        print(Token)
except JSONDecodeError as e:
    raise e

# Set up the intents
intents = discord.Intents.default()
intents.message_content = True
intents.guild_reactions = True
intents.guild_typing = True
intents.guilds = True

# Initialize the client and command tree
Client = discord.Client(intents=intents)
tree = app_commands.CommandTree(Client)


@Client.event
async def on_ready():
    print(f"{Client.user.name} is running...\n")
    async for guild in Client.fetch_guilds(limit=150):
        tree.copy_global_to(guild=discord.Object(id=guild.id))
        synced = await tree.sync(guild=discord.Object(id=guild.id))
        if synced:
            for command in synced:
                print(f"Synced command: {command.name} for this server: {guild.name}")


@tree.command(name="greet", description="Say hi to you")
async def greet(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Hi {interaction.user.mention}!",
        ephemeral=True,  # This makes the message visible only to the user
    )


@tree.command(name="ping", description="Say pong to you")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!", ephemeral=True)


# Run the client
Client.run(Token)
