"""
JSON body format
{
    "type": 1
    "name": "",
    "description": "",
    "options": [
        {
            "type": 1
            "name": "",
            "description: "",
            "required": False,
            "choices": [
                "name": "",
                "value": ""
            ],
            "options": [same format here]

        }
    ],
    "default_permission": True,
}

'type' (only in base command), 'default_permission', 'required' and 'options' 
fields are optional and have the default values as shown in the example.
'options' field can be used to create sub commands which isn't mandatory and 'type'
inside options is required to define what kind of option is it (usually a subcommand with value 1)

There are 3 'types' for the actual base command: 
https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-types

and 10 'types' for the options:
https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-type

"""

import os
import requests

TOKEN = os.environ["TOKEN"] or os.getenv["TOKEN"]
HEADERS = {"Authorization": f"Bot {TOKEN}"}

# No fields with default values are used
EXAMPLE_COMMAND = {
    "name": "pyfact",
    "description": "Shows a random Python fact!",
}


def register_global_command(application_id: int) -> str:
    """
    https://discord.com/developers/docs/interactions/application-commands#create-global-application-command
    Register slash commands globally.
    Takes the application(bot) ID as a single arguments.
    """

    url = f"https://discord.com/api/v9/applications/{application_id}/commands"
    res = requests.post(url, headers=HEADERS, json=EXAMPLE_COMMAND)

    return (
        f"Response code: {res.status_code}\n"
        f"Total commands: {len(res.json())}\n"
        f"JSON text: {res.json()}\n"
    )


def register_guild_command(application_id: int, guild_id: int) -> str:
    """
    https://discord.com/developers/docs/interactions/application-commands#create-global-application-command
    Register slash commands to specific guilds.
    Takes the application (bot) ID and guild ID respectively as arguments.
    """

    url = f"https://discord.com/api/v9/applications/{application_id}/guilds/{guild_id}/commands"
    res = requests.post(url, headers=HEADERS, json=EXAMPLE_COMMAND)

    return (
        f"Response code: {res.status_code}\n"
        f"Total commands: {len(res.json())}\n"
        f"JSON text: {res.json()}\n"
    )


# print(register_global_command(884099662653562961))
# print(register_guild_command(884099662653562961, 845726630231932980))