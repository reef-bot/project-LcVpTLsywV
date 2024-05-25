# main.py

import discord
from discord.ext import commands

from bot import Bot
from command_system import CommandSystem

# Initialize Discord bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')

# Initialize Bot and Command System
my_bot = Bot(bot)
command_system = CommandSystem(my_bot)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Event: Message received
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

# Command: Help
@bot.command()
async def help(ctx):
    await ctx.send(command_system.get_help_message())

# Command: Add new moderation action
@bot.command()
async def add_moderation(ctx, action, user_id, reason):
    result = command_system.add_moderation_action(action, user_id, reason)
    await ctx.send(result)

# Command: Get user warnings
@bot.command()
async def get_warnings(ctx, user_id):
    warnings = command_system.get_user_warnings(user_id)
    await ctx.send(warnings)

# Command: Ban user
@bot.command()
async def ban_user(ctx, user_id):
    result = command_system.ban_user(user_id)
    await ctx.send(result)

# Command: Unban user
@bot.command()
async def unban_user(ctx, user_id):
    result = command_system.unban_user(user_id)
    await ctx.send(result)

# Run the bot
bot.run('YOUR_DISCORD_BOT_TOKEN')