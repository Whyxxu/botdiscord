import discord,sys
from discord.ext import commands

bot = commands.Bot(command_prefix="%")



@bot.event
async def on_ready():
    print("Le bot est prêt !")





@bot.command(name="parle")
async def on_message(contexte,message:str):
    if contexte.author.id == bot.user.id:
        pass
    else:
        rechercheMsg = contexte.message.content
        if "ta gueule" in rechercheMsg:
            await contexte.channel.send("le language svp")
        print(contexte.guild, ":", contexte.channel, ":", contexte.author, ":", contexte.message.content)
        if message == "test":
            await contexte.channel.send("test fonctionnel")



if __name__=="__main__":
    bot.run(sys.argv[1])