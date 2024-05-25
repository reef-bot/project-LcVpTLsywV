# bot.py

import discord
from discord.ext import commands
from features import message_filtering, user_warnings, ban_management, spam_detection
from logs import reports
from data_storage import mongodb
from notifications import webhook_system

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name='filter_messages')
async def filter_messages(ctx):
    await message_filtering.filter_messages(ctx)

@bot.command(name='warn_user')
async def warn_user(ctx, user: discord.User, reason: str):
    await user_warnings.warn_user(ctx, user, reason)

@bot.command(name='manage_ban')
async def manage_ban(ctx, user: discord.User, action: str):
    await ban_management.manage_ban(ctx, user, action)

@bot.command(name='detect_spam')
async def detect_spam(ctx):
    await spam_detection.detect_spam(ctx)

@bot.command(name='generate_report')
async def generate_report(ctx):
    await reports.generate_report(ctx)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

@bot.event
async def on_member_ban(guild, user):
    await mongodb.save_ban_data(guild, user)

@bot.event
async def on_member_warn(guild, user, reason):
    await mongodb.save_warning_data(guild, user, reason)

@bot.event
async def on_spam_detection_trigger(ctx):
    await webhook_system.notify_admins(ctx)

bot.run('your_bot_token')