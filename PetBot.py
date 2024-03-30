import discord
from discord.ext import commands
from pet_logic import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
    bot.loop.create_task(decrease_happiness())
    bot.loop.create_task(decrease_hunger())

@bot.command()
async def adopt(ctx, pet_name=None, species="Köpek"):
    if not pet_name:
        pet_name = get_random_pet_name()
    await ctx.send(adopt_pet(pet_name, species))

@bot.command()
async def feed(ctx):
    await ctx.send(feed_pet())

@bot.command()
async def play(ctx):
    await ctx.send(play_with_pet())

@bot.command()
async def info(ctx):
    await ctx.send(get_pet_info())

@bot.command()
async def change_pet(ctx, pet_name=None, species="Köpek"):
    global server_pet
    if server_pet is not None:
        server_pet = None 
    await ctx.send(adopt_pet(pet_name, species))


bot.run(Token_Here)
