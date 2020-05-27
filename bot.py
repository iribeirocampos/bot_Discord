import discord
import settings

LIST = {}

client = discord.Client()


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith("/add"):
        if message.content[4:] in LIST:
            await message.channel.send("Choose another one, that is already been taken")
        else:
            await message.channel.send(
                "Planet {} has been added to the list".format(message.content[4:])
            )
            LIST.update({message.content[4:]: message.author.name})

    if message.content.startswith("/remove"):
        if message.content[7:] in LIST:
            await message.channel.send(
                "Planeta {} has been removed from the list".format(message.content[7:])
            )
            LIST.pop(message.content[7:])
        else:
            await message.channel.send("Planet has not been choosen, you can add it.")

    if message.content.startswith("/list"):
        if len(LIST) == 0:
            await message.channel.send("There are no claims.")
        else:
            reply = ""
            for plan, user in LIST.items():
                reply += "Planet {} has been claimed by {}\n".format(plan, user)
            await message.channel.send(reply)

    if message.content.startswith("/help"):
        await message.channel.send(
            "It's simple,\n '/add' followed by planet's coords to add claim. \n '/remove' followed by planet's coords to remove claim. \n '/list' to list all made claims."
        )


client.run(settings.DISCORD_TOKEN)
