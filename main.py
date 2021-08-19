import discord
import os 
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

prefix = "f "
client = commands.Bot(prefix, description = "A bot to give you the day's timetable.")

@client.event
async def on_ready():
    print("Bot online")
    await client.change_presence(activity = discord.Game("f help"))

@client.command(name="hello")
async def hello(ctx):
    await ctx.send("Hello " + ctx.message.author.mention)

@client.command(name="class")
async def _class(ctx):
    
    def message_check(m):
        return m.author == ctx.message.author
    
    await ctx.send("Which day's time table do you need? " + ctx.message.author.mention)
    day = await client.wait_for('message',timeout=None,check=message_check)
    
    f = open("timetable.txt","r")
    for i in f:
        if day.content.lower() in i.lower():
            await ctx.send(f.readline())
        else:
            continue
    
    f.close()
    
    # if day.content.lower() == "tuesday":
    #     await ctx.send("Taking user input works")
    # else:
    #     await ctx.send("Not tuesday")

client.run(os.getenv('TOKEN'))