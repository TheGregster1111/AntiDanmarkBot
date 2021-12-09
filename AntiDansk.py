import discord
import discord.member
import discord.channel
import discord.message
import discord.voice_client
from discord.ext import commands, tasks
import os
import requests
import time
import importlib

class MainCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener() #y = any(x in String for x in List)
    async def on_message(self, message):
        if "🇩🇰" in message.content:
            try:
                await message.delete()
            except:
                await message.reply('No danish "people" allowed here')

        elif 'https://' in message.content:
            if any(x in message.content.lower() for x in ['danmark', 'dansk', 'denmark', 'dansih']):
                try:
                    await message.delete()
                except:
                    await message.reply('No danish "people" allowed here')

    

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == '🇩🇰':
            try:
                await reaction.clear()
            except:
                return

    

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if "🇩🇰" in after.content:
            try:
                await after.delete()
            except:
                await after.reply('No danish "people" allowed here')

def setup(bot):
    bot.add_cog(MainCog(bot))
