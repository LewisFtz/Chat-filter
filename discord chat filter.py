import discord
import asyncio
client = discord.Client()




chat_filter = []
WordsFile = open("bannedwordsfile.txt", "r")
for Word in WordsFile:
    chat_filter.append(Word.strip().upper())
WordsFile.close()   
    
#print (chat_filter)

@client.event

async def on_ready():
    print("Logging in as:")
    print(client.user.name)
    print("ID:")
    print(client.user.id)
    print("Ready to use!")
    

@client.event
async def on_message(message):
    userID = message.author.id
    contents = message.content.split(" ")
    
    if message.content.upper().startswith('!PING'):        
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))


    for word in contents:
        if word.upper() in chat_filter:
            if not "#roleid" in [role.id for role in message.author.roles]:
                try: 
                    await client.delete_message(message)
                    await client.send_message(message.channel, "<@%s> **Hey** Swearing is not allowed." % (userID))
                except discord.errors.NotFound:
                    return 
                                
###client.runID
