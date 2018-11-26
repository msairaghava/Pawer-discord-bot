"""
Extra test cogs
"""

import requests
from modules.config import CONFIG
from modules.helpers import is_channel
from discord.ext import commands



class Extra:
    """Usefull cogs not Bismuth specific"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test', brief="test", pass_context=True)
    @is_channel(CONFIG['bot_channel'])
    async def test(self, ctx):
        # print(ctx.message.content)
        await self.bot.say('test')


    @commands.command()
    @is_channel(CONFIG['bot_channel'])
    async def ping(self):
        await self.bot.say('Pong')

    @commands.command(name='bitcoin', brief="Shows bitcoin price")
    @is_channel(CONFIG['bot_channel'])
    async def bitcoin(self, pass_context=True):
        # TODO: cache
        url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
        response = requests.get(url)
        value = response.json()['bpi']['USD']['rate']
        # await client.send_message(discord.Object(id='502494064420061184'), "Bitcoin price is: " + value)
        await self.bot.say("Bitcoin price is {:0.2f} USD".format(value))