import discord
import discord.member
import discord.channel
import discord.message
import discord.voice_client
from discord.ext import commands
import re

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

        elif re.search(r'https://(.*?)(danmark|dansk|denmark|danish|danske|pølse|dane|danes|dansken|densk)', message.content):
            try:
                await message.delete()
            except:
                await message.reply('No danish "people" allowed here')

        #elif len(message.attachments) > 0:

    

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

        elif re.search(r'https://(.*?)(danmark|dansk|denmark|danish|danske|pølse|dane|danes|dansken|densk)', after.content):
            try:
                await after.delete()
            except:
                await after.reply('No danish "people" allowed here')

def setup(bot):
    bot.add_cog(MainCog(bot))
