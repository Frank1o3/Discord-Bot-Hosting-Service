# What Is This Repo?
Well this repo was made to make it eazy to host multiple discord bots at the same time.

# What is the Builder script?
The script will ask you for a name and your discord bot token then it will make a dir and two files.
The Main.py contains some base code so you can make application commands and have them sync on the bots start. You can check a example [Here](https://github.com/Frank1o3/Discord-Bot-Hosting-Service/blob/main/Clients/example/Main.py).

After Running the Builder script the result will be like [this](https://github.com/Frank1o3/Discord-Bot-Hosting-Service/tree/main/Clients/Test), and you can look at the Main.py and Config.json to get and idea of what the end result will be.

# Requirements
For you use the scripts in this repo i would recommend making a python Virtual Envirement you can do that by running `python3 -m venv venv`
then you need to activate the venv by running this command:

# Making the Virtual Envirement & Activating it
For Windows:
    `./venv/bin/activate`

For Linux & Mac:
    `source venv/bin/activate`

# Installing the Lib needed
Run:
    `pip install -r requirements.txt`

after you do all that
you can run `./Python/Builder.py` if you want to add a other discord bot or you can run `./Python/Main.py` to run all the discord bots you currently have.