# And Then
import discord #import discord libarires

client = discord.Client() #discord client

#client event on message
@client.event 
async def on_message(message): # when client types a message
  if message:
         text = "And Then ..." # define text
         await message.channel.send(text) # discord sends data back

  if message.content.startswith('And Then'):
         text = "And Then, And Then, And Then!" # define text
         await message.channel.send(text) # discord sends data back

client.run() # discord run client
