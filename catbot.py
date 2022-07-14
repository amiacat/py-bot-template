import discord
from discord.user import Profile

name_owner = 'set your name here'
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('c!hello'):
        await message.channel.send(f'Hello! **{message.author}**!')
    if message.content.startswith('c!about'):
        await message.channel.send(f'Hello, I\'m a bot! I was created by **{name_owner}**')
    if message.content.startswith('c!staff'):
        if discord.user.Profile.staff == True:
            await message.channel.send(f'{message.author.name} is a Staff Member! ')
        else:
            await message.channel.send(f'{message.author.name} isn\'t a Staff Member!')
            
        
client.run('Set your token here/Coloque seu token aqui')
