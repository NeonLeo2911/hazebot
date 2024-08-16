import discord
from discord.ext import commands
import datetime
import os
from dotenv import load_dotenv

load_dotenv()



intents = discord.Intents.default()
intents.message_content = True
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)
client = commands.Bot(command_prefix = 'h!', intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(
        type= discord.ActivityType.playing, name=f"h! and {len(client.guilds)} server"
    ))
    print("The bot is now rady to use!")


@client.command()
@commands.has_permissions(moderate_members=True,ban_members=True)
async def mute(ctx, member:discord.Member,timelimit,reason=None):
    if "s" in timelimit:
        gettime = timelimit.strip("s")
        if int(gettime) > 2419000:
            await ctx.send("The mute time amount cannot be bigger than 28 days")
        else:
            newtime = datetime.timedelta(seconds=int(gettime))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
            embed = discord.Embed(title="Muted", description=f"{member} has been muted in {timelimit}\nReason: {reason}")
            embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)
    elif "m" in timelimit:
        gettime = timelimit.strip("m")
        if int(gettime) > 40320:
                await ctx.send("The mute time amount cannot be bigger than 28 days")
        else:
            newtime = datetime.timedelta(minutes=int(gettime))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
            embed = discord.Embed(title="Muted", description=f"{member} has been muted in {timelimit}\nReason: {reason}")
            embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)
    elif "h" in timelimit:
        gettime = timelimit.strip("h")
        if int(gettime) > 672:
            await ctx.send("The mute time amount cannot be bigger than 28 days")
        else:
            newtime = datetime.timedelta(hours=int(gettime))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
            embed = discord.Embed(title="Muted", description=f"{member} has been muted in {timelimit}\nReason: {reason}")
            embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)
    elif "d" in timelimit:
        gettime = timelimit.strip("d")
        if int(gettime) > 28:
            await ctx.send("The mute time amount cannot be bigger than 28 days")
        else:
            newtime = datetime.timedelta(days=int(gettime))
            await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
            embed = discord.Embed(title="Muted", description=f"{member} has been muted in {timelimit}\nReason: {reason}")
            embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)
        

@client.command()
@commands.has_permissions(moderate_members=True,ban_members=True)
async def ban(ctx, member:discord.Member,reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(title="Banned", description=f"{member} has been banned\nReason: {reason}")
    embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.display_avatar)
    await ctx.send(embed=embed)

bad_words = ["a", "b", "c", "d", "e"]

@client.event
async def on_message(msg):
  for bad_word in bad_words:
    if bad_word in msg.content.lower().split(" "):
      await msg.delete()
      bad_word_embed = discord.Embed(title = "Bad Word", description=f"{msg.author.mention}, please do not say any bad words", color = discord.Color.green())
      await msg.channel.send(embed=bad_word_embed, delete_after=5.0)


client.run(TOKEN)