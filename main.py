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
            
            tt = f.readline()
            lst = tt.split(',')
            
            ttformatted = ""
            
            for j in lst:
                ttformatted += j + '\n'                 #Each course in seperate lines
            
            embed = discord.Embed(title = day.content.upper(), description = ttformatted, color = discord.Color.gold())
            embed.set_author(name = ctx.author.display_name, icon_url = ctx.author.avatar_url)
            embed.set_footer(text = "Regular class timetable")      
            await ctx.send(embed = embed)

        else:
            continue
    
    f.close()

client.run(os.getenv('TOKEN'))