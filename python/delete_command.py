import os
import requests

TOKEN = os.environ["TOKEN"] or os.getenv["TOKEN"]
HEADERS = {"Authorization": f"Bot {TOKEN}"}


def delete_global_command(application_id: int, command_id: int) -> str:
    """
    https://discord.com/developers/docs/interactions/application-commands#delete-global-application-command
    Delete a globally registered slash command.
    Takes the application(bot) ID as a single arguments.
    """

    url = (
        "https://discord.com/api/v9/applications/"
        f"{application_id}/commands/{command_id}"
            )
            
    res = requests.delete(url, headers=HEADERS)

    return (
        f"Response code: {res.status_code}\n"
        f"JSON text: {res.json()}\n"
    )


def delete_guild_command(
                        application_id: int, 
                        guild_id: int, 
                        command_id: int
                        ) -> str:
    """
    https://discord.com/developers/docs/interactions/application-commands#delete-guild-application-command
    Delete a guild specfic registered slash command.
    Takes the application (bot) ID and guild ID respectively as arguments.
    """

    url = (
        "https://discord.com/api/v9/applications/"
        f"{application_id}/guilds/{guild_id}/commands/{command_id}"
            )

    res = requests.delete(url, headers=HEADERS)

    return (
        f"Response code: {res.status_code}\n"
        f"JSON text: {res.json()}\n"
    )


# print(delete_global_command(884099662653562961, 1))
# print(delete_guild_command(884099662653562961, 845726630231932980, 1))
