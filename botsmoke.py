import discord
import os
import asyncio
from dotenv import load_dotenv
from discord.utils import get
from discord.ext import commands

client = commands.Bot(command_prefix = '!')


load_dotenv()

TOKEN=os.getenv('TOKEN')

@client.command()
async def ghostping(ctx, member: discord.User):
    await ctx.message.delete()
    a = 0
    number = int('3')
    while a < number :
        await ctx.send(f"{member.mention}", delete_after=0)
        a=a+1


@client.command()
async def ghostpingbzr(ctx, member: discord.User):
        await ctx.message.delete()
        channel = client.get_channel(789459187591413780)
        await channel.send(f"{member.mention}", delete_after=0)
        channel = client.get_channel(789156154084163594)
        await channel.send(f"{member.mention}", delete_after=0)
        channel = client.get_channel(790528092485189633)
        await channel.send(f"{member.mention}", delete_after=0)
        channel = client.get_channel(809173996515360808)
        await channel.send(f"{member.mention}", delete_after=0)
        channel = client.get_channel(822950516459962449)
        await channel.send(f"{member.mention}", delete_after=0)
        channel = client.get_channel(854022417365336075)
        await channel.send(f"{member.mention}", delete_after=0)

@client.event
async def on_connect():
    print("Woooooo")
    channel = client.get_channel(854002292469268555)
    #await channel.send("Woooooooo's back baby", delete_after=4)

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.UserNotFound):
        await ctx.message.delete()
        await ctx.send("User pas spécifié ou pas sur le serveur, wooooo",delete_after=7)
    elif isinstance(error,commands.MissingRequiredArgument):
        await ctx.message.delete()
        await ctx.send("Il manque le nom de l'utilisateur, wooooo",delete_after=7)
    else:
        raise error



client.run(TOKEN)