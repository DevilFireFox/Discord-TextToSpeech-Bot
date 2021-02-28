import discord
from discord.ext import commands
from gtts import gTTS

setLanguage = True

setPrefix = True

setToken = True

while setToken: 
    print("")
    print("╔======================╗")
    print("║ Input token your bot ║")
    print("╚======================╝")
    print("")
    token = input("Input: ")
    w = True
    
    setVar = True
    while setVar:
        print("Your bot token: " + str(token))
        print("Are you sure that your token is correct?")
        var = input("Y/N: ")
        a = True
        if var.lower() != "y" and var.lower() != "n":
            print('The request  "' + var + '" is not correct!')
            a = False
        if a == True:
            if var.lower() == "y":
                w = True
            if var.lower() == "n":
                w = False
            setVar = False
    
    if w == False:
        setToken = True
    if w == True:
        setToken = False

while setPrefix: 
    print("")
    print("╔=========================╗")
    print("║ Set prefix for your bot ║")
    print("╚=========================╝")
    print("")
    prefix = input("Set: ")
    w = True
    
    setVar = True
    while setVar:
        print("Your bot pefix: " + str(prefix))
        print("Do you confirm the choice?")
        var = input("Y/N: ")
        a = True
        if var.lower() != "y" and var.lower() != "n":
            print('The request  "' + var + '" is not correct!')
            a = False
        if a == True:
            if var.lower() == "y":
                w = True
            if var.lower() == "n":
                w = False
            setVar = False
    
    if w == False:
        setPrefix = True
    if w == True:
        setPrefix = False

while setLanguage: 
    print("")
    print("╔==================================╗")
    print("║ Select language for TextToSpeech ║")
    print("╠==================================╣")
    print("║           1 - English            ║")
    print("║           2 - Russian            ║")
    print("╚==================================╝")
    print("")
    lang = input("Select: ")
    w = True
    if lang != "1" and lang != "2":
        print('The request  "' + lang + '" is not correct!')
        setLanguage = True
        w = False
    if w == True:
        if lang == "1":
            lang = "en"
        if lang == "2":
            lang = "ru"
        setLanguage = False

client = commands.Bot(command_prefix = prefix)

@client.event
async def on_ready():
    print("")
    print('We have logged in as {0.user}'.format(client))
    print("TextToSpeech Bot started!")
    print("")
    print("Link to invite the bot: https://discordapp.com/oauth2/authorize?&client_id=" + str(client.user.id) + "&scope=bot&permissions=8")
    print("Your bot's name: " + str(client.user.name))
    print("")
    print("I start listening to the chat!")
    
@client.event
async def on_message(message):
    nickname = message.author.name
    channel = message.channel
    msg = message.content
    guild = message.guild.name
    print(f"| {guild} | {channel} | {nickname}: {msg}")

    if msg.startswith('.tts'):
        words = msg.split(' ')
        fragment = '.tts'
        new_words = []
        for word in words:
            if fragment not in word:
                new_words.append(word)
        
        mess = ' '.join(new_words)
        
        myobj = gTTS(text=mess, lang=lang, slow=False)
        myobj.save("TextToSpeech.mp3")
        await message.channel.send(file = discord.File(fp = "TextToSpeech.mp3"))
        await message.delete()

client.run(token)