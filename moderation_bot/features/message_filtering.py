# message_filtering.py

import discord
from discord.ext import commands

class MessageFiltering(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # Implement message filtering logic here
        if "bad_word" in message.content:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please refrain from using inappropriate language.")

def setup(bot):
    bot.add_cog(MessageFiltering(bot))