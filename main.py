import discord,sys

client = discord.Client()



@client.event
async def on_ready():
    print("Le bot est prêt !")





@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        pass
    else:
        rechercheMsg = message.content
        if "ta gueule" in rechercheMsg:
            await message.channel.send("le language svp")
        print(message.guild, ":", message.channel, ":",  message.author, ":", message.content)
        if message.content == "test":
            await ("test fonctionnel")



if __name__=="__main__":
    client.run(sys.argv[1])