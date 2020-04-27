import discord
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions
import _asyncio
from datetime import date
import helpers.SteamInfoPuller
import helpers.Flip
from helpers.Flip import rsItem
import helpers.DiscordBotKey

client = discord.Client()
client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(helpers.SteamInfoPuller.SelectRandomGame()))
    print('Bot logging in as {0.user}'.format(client))

# Start of commands

@commands.cooldown(1, 3, commands.BucketType.guild)
@client.command()
async def ping(ctx):
    if ctx.author.id != 267402012742778891:
        await ctx.channel.send("go away idiot (took {}".format(int(client.latency * 1000)) + "ms to flame.)")

@client.command()
async def rsitem(ctx, *item):
    if ctx.author.id != 267402012742778891:
        item = (" ".join(item[:]))
        await ctx.channel.send(rsItem(item))

@client.command()
async def kill(ctx, amt):
    if ctx.author.id == 150009383592525826:
        await ctx.channel.purge(limit=int(amt)+1)
        await ctx.channel.send("Killed {}".format(amt) + " messages.")

@client.command()
async def steam(ctx, arg):
    if ctx.author.id != 267402012742778891:
        await ctx.channel.send(helpers.SteamInfoPuller.SteamGameSearch(arg))

@client.command()
async def hello(ctx):
    await ctx.channel.send('helo dood :D')

# Start of commands

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

    if message.guild.id == 213868052373045248 or message.guild.id == 476472672625098752: # graveyard or bikini bottom
        #if message.content == 'test':
           #await message.channel.send(type(message.author.joined_at))
           #await message.channel.send(type(date.today()))

        if "spopy" in message.content.lower() or "spop" in message.content.lower():            
            await message.add_reaction(emoji='❓')

        if "anime" in message.content.lower():
            await message.add_reaction(emoji='😡')

        if message.author.id == 578771603475791893:
            if "dark souls" in message.content.lower():
                await message.add_reaction(emoji='😔')

    if message.guild.id == 213330594749349888: # ninjacord
        if message.content.startswith("$classhelp"):
            await message.channel.send("Remember to direct all ninja/kuno questions to the channels #ninja-help and #kuno-help!")
        
        if message.content.startswith('!spopy7'):
            await message.channel.send('https://gyazo.com/77a9b9d4cc3890b70eed030fa7d51a87')

        if "spopy" in message.content.lower() or "spop" in message.content.lower():
            await message.add_reaction(emoji='<:What: 271214076728836096 >')   
        

#        if message.guild.id == 213330594749349888:
#            ninjahelp = client.get_channel('213334511805530112')
#            kunohelp = client.get_channel('257393132059099136')
#            question_list = ['what', 'where', 'when', 'how', 'why', 'which', 'can', 'should', 'is']
#           for word in question_list:
#               if message.content.lower().startswith(word):
#                    if 'ninja' in message.content.lower() and 'kuno' in message.content.lower():
#                        await message.channel.send("Remember to direct all ninja/kuno questions to the channels " + ninjahelp.mention + " and " + kunohelp.mention)
#                   elif 'ninja' in message.content.lower():
#                        await message.channel.send("Remember to direct all ninja questions to " + ninjahelp.mention)
#                    elif 'kuno' in message.content.lower():
#                        await message.channel.send("Remember to direct all kuno questions to " + kunohelp.mention)
              
# Changed to a try/catch because people don't read ReadMe usually
try:
  client.run(helpers.DiscordBotKey.private_Key)
except:
  print("You did not provide a Discord Private key (aka. TOKEN in discord dev website under Bot category) as you should have.")