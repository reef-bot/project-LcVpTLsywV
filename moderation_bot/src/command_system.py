# command_system.py

import discord

class CommandSystem:
    def __init__(self, client):
        self.client = client
        self.commands = {}

    def add_command(self, command_name, callback):
        self.commands[command_name] = callback

    async def handle_command(self, message):
        if message.content.startswith('!'):
            command = message.content.split(' ')[0][1:]
            if command in self.commands:
                await self.commands[command](message)

# Dependencies: This file depends on the discord.py library for interacting with the Discord API. It also relies on the main bot.py file to instantiate the client and connect to the Discord server. This file is responsible for handling and executing commands sent by users in Discord channels. It defines a CommandSystem class that allows for registering and executing custom commands defined by the server admins.