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

print("Changing One one of the bots tokens")

name = input("Name For You'r App: ")
Token = input("Token of you'r Discord Bot: ")

while True:
    offset = random.randint(1, 546523)
    Encrypted_Token = shift_encrypt(Token, offset)
    if Token != Encrypted_Token:
        break

config_file = {"Token": Encrypted_Token, "ID": offset}

Path = __file__
Path = Path.replace("Python/Scripts/Encrypt_Token.py", f"Clients/{name}/Config.json")
Path = Path.replace("./Python/Encrypt_Token.py", f"Clients/{name}/Config.json")

print(Path)

if os.path.exists(Path.removesuffix(f"Clients/{name}/Config.json")):
    if Path == __file__:
        exit(0)
    pass
else:
    print("Bot does not exists")
    exit(0)


with open(Path, "w") as file:
    file.write(json.dumps(config_file))
    file.close()
