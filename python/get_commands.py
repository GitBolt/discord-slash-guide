"""
This is to get all commands, not to be confused with `get_command.py` 
which returns details of a particular command.
"""

import os
import requests

TOKEN = os.environ["TOKEN"] or os.getenv["TOKEN"]
HEADERS = {"Authorization": f"Bot {TOKEN}"}


def get_global_commands(application_id: int) -> str:
    """
    https://discord.com/developers/docs/interactions/application-commands#get-global-application-commands
    Get globally registered slash commands.
    Takes the application(bot) ID as a single arguments.
    """

    url = f"https://discord.com/api/v9/applications/{application_id}/commands"
    res = requests.get(url, headers=HEADERS)

    return (
        f"Response code: {res.status_code}\n"
        f"Total commands: {len(res.json())}\n"
        f"JSON text: {res.json()}\n"
    )


def get_guild_commands(application_id: int, guild_id: int) -> str:
    """
    https://discord.com/developers/docs/interactions/application-commands#get-guild-application-commands
    Get guild specfic registered slash commands.
    Takes the application (bot) ID and guild ID respectively as arguments.
    """

    url = f"https://discord.com/api/v9/applications/{application_id}/guilds/{guild_id}/commands"
    res = requests.get(url, headers=HEADERS)

    return (
        f"Response code: {res.status_code}\n"
        f"Total commands: {len(res.json())}\n"
        f"JSON text: {res.json()}\n"
    )


# print(get_global_commands(884099662653562961))
# print(get_guild_commands(884099662653562961, 845726630231932980))
