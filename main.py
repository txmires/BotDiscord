from concurrent.futures import process
import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix="!", case_insensitive=True)


@client.event
async def on_ready():
    print('Entramos como {0.user}' .format(client))


@client.command()
async def ola(ctx):
    await ctx.send(f'Olá, {ctx.author.name}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "palavrão" in message.content:
        await message.channel.send(f"Favor não xingar ai rapazeada!!")

        await message.delete()

    await client.process_commands(message)


@client.command()
async def dado(ctx, numero):
    variavel = random.randint(1, int(numero))
    await ctx.send(f'O número que saiu no dado é {variavel}')


@client.command()
async def calcular(ctx, expression):
    response = eval(expression)
    await ctx.send("A resposta é " + str(response))


@client.command()
async def segredo(ctx):
    await ctx.author.send("curioso...")

with open("token.0.txt", "r", encoding="utf-8") as f:
    bottoken = f.read()

client.run(bottoken)
