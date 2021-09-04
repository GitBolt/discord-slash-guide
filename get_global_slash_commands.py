"""
To get global slash commands registered in your bot, simply make a GET request to
https://discord.com/api/v9//applications/{application.id}/commands with your bot token
prefixed by 'Bot' in Authorization header.
"""
import os
import requests


URL = "https://discord.com/api/v9/applications/792731230360961035/commands"
HEADERS = {"Authorization": f"Bot {os.environ['TOKEN']}"}

res = requests.get(URL, headers=HEADERS)

print(
    f"Response code: {res.status_code}\n"
    f"Total commands: {len(res.json())}\n"
    f"JSON text: {res.json()}"
)