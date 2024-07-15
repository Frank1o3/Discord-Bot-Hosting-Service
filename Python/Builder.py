#!/usr/bin/env python3

import random
import json
import os


def shift_encrypt(text: str, offset: int):
    result = ""

    for char in text:
        # Encrypt all characters, wrapping within the ASCII range
        result += chr((ord(char) + offset) % 256)

    return result

name = input("Name For You'r App: ")
Token = input("Token of you'r Discord Bot: ")

while True:
    offset = random.randint(1, 546523)
    Encrypted_Token = shift_encrypt(Token, offset)
    if Token != Encrypted_Token:
        break

config_file = {"Token": Encrypted_Token, "ID": offset}

Path = __file__
Path = Path.replace("Python/Scripts/Builder.py", f"Clients/{name}/")
Path = Path.replace("./Python/Builder.py", f"Clients/{name}/")

print(Path)

if os.path.exists(Path):
    print("Project already Exists..")
    exit(0)

os.makedirs(Path,exist_ok=True)

with open(f"{Path}Config.json","w") as file:
    file.write(json.dumps(config_file))
    file.close()

with open(f"{Path}Main.py","w") as file:
    file.write(
        """from json import load, JSONDecodeError
from discord import app_commands
import discord
import os\n\n
def shift_decrypt(text, offset):
    result = ""
    for char in text:
        # Decrypt all characters, wrapping within the ASCII range
        result += chr((ord(char) - offset) % 256)
    return result\n\n
# Load and decrypt the token from the JSON file
Path = __file__
Name = os.path.basename(__file__)\n
Path = Path.replace(Name, "Config.json")\n
try:
    with open(Path, "r") as file:
        data = load(file)
        Token = shift_decrypt(data["Token"], data["ID"])
except JSONDecodeError as e:
    raise e\n
# Set up the intents
intents = discord.Intents.default()
intents.message_content = True
intents.guild_reactions = True
intents.guild_typing = True
intents.guilds = True\n
# Initialize the client and command tree
Client = discord.Client(intents=intents)
tree = app_commands.CommandTree(Client)\n\n
@Client.event
async def on_ready():
    print(f"{Client.user.name} is running...\\n")
    async for guild in Client.fetch_guilds(limit=150):
        tree.copy_global_to(guild=discord.Object(id=guild.id))
        synced = await tree.sync(guild=discord.Object(id=guild.id))
        if synced:
            for command in synced:
                print(f"Synced command: {command.name} for this server: {guild.name}")\n
# Put You'r Code the Bot Code here you can change the top code if you like but dont change the os json and the reading file code\n
Client.run(Token)
"""
    )
