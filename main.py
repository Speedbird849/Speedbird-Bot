#Import Libraries
import discord
import os
from discord.ext import commands
import requests
import json

#Bot prefix
bot = commands.Bot(command_prefix="-")

#Success message when running code
@bot.event
async def on_ready():
  print('Login successful. {0.user} is now online and active!'.format(bot))


#Script to fetch quote from ZenQuotes server
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
  
@bot.command()
async def quote(ctx):
  quote = get_quote()
  await ctx.channel.send(quote)

#Autoresponder commands
@bot.command()
async def say(ctx, *args):
	response = ""

	for arg in args:
		response = response + " " + arg

	await ctx.channel.send(response)

@bot.command()
async def bump(ctx):
  await ctx.channel.send("!d bump")

#DM command
@bot.command()
async def dm(ctx, user: discord.User, *, message=None):
  await user.send(message)
  await ctx.send('DM Sent!')

#Kick command
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
  await user.send("You've been kicked from Speedbird's top secret lair. Forget it ever existed. (unless Speedbird invites you back)")
  await ctx.send("Alright, ciao!")
  await user.kick()

#Ban command
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member):
  await user.send("You've been banned from Speedbird's top secret lair. Forget it ever existed.")
  await ctx.send("Alright, ciao!")
  await user.ban()

#Trigger commands
async def on_message(message):
  if message.author == bot.user:
    return

  msg = message.content
  if msg.startswith('owo'):
    await message.channel.send('uwu')

#Bot token
bot.run("ODY4NDk2MTc3MjEyMDMxMDQ4.YPwgGA.Cvu_YawCxh8nZgBAcTdOORSQ5ho")