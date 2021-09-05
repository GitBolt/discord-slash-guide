"""
To update a slash command, use the same format, only difference being instead of 
`delete` request, use `put` request with the json body of your updated command!

Remember that this is a `put` request which means you would need to
send your entire command with the change again, not only the little change which you wanted.
"""

import os
import requests

TOKEN = os.environ["TOKEN"] or os.getenv["TOKEN"]
HEADERS = {"Authorization": f"Bot {TOKEN}"}


def get_global_command(application_id: int, command_id: int) -> str:
    """
    https://discord.com/developers/docs/interactions/application-commands#get-global-application-command
    Get a globally registered slash command.
    Takes the application(bot) ID as a single arguments.
    """

    url = f"https://discord.com/api/v9/applications/{application_id}/commands/{command_id}"
    res = requests.get(url, headers=HEADERS)

    return (
        f"Response code: {res.status_code}\n"
        f"JSON text: {res.json()}\n"
    )


def get_guild_command(
                    application_id: int,
                    guild_id: int,
                    command_id: int
                    ) -> str:
    """
    https://discord.com/developers/docs/interactions/application-commands#get-guild-application-command
    Get a guild specfic registered slash command.
    Takes the application (bot) ID and guild ID respectively as arguments.
    """

    url = (
        "https://discord.com/api/v9/applications/"
        f"{application_id}/guilds/{guild_id}/commands/{command_id}"
        )
    res = requests.get(url, headers=HEADERS)

    return (
        f"Response code: {res.status_code}\n"
        f"JSON text: {res.json()}\n"
    )


# print(get_global_command(884099662653562961, 1))
# print(get_guild_command(884099662653562961, 845726630231932980, 1))