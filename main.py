

# import discord
# import os
# from discord import Intents
# from dotenv import load_dotenv
# import requests
# import json
# import random

# sad_words = set([
#     'sad', 'unhappy', 'miserable', 'depressed', 'down', 'sorrow', 'grief',
#     'heartbroken', 'lonely', 'dejected', 'despair', 'melancholy', 'blue',
#     'gloomy', 'woeful', 'downhearted', 'troubled', 'distressed', 'upset',
#     'disheartened', 'forlorn', 'tearful', 'despondent', 'desolate', 'pensive',
#     'discouraged', 'anguished', 'empty', 'painful', 'hurt', 'agonized',
#     'regretful', 'melancholic', 'brokenhearted', 'isolated', 'numb',
#     'unfulfilled', 'despairing', 'low', 'sorrowful', 'broken', 'abandoned'
# ])

# encouragements = [
#     "You’re doing your best, and that’s more than enough. Keep moving forward!",
#     "Remember, every challenge is an opportunity to grow. You’ve got this!",
#     "It’s okay to feel down sometimes. You have the strength to get through this.",
#     "Believe in yourself. You have overcome so much already and can handle this too.",
#     "Don’t forget to take care of yourself. You’re important and your well-being matters.",
#     "Even small steps forward are progress. Keep going, and you’ll make it through.",
#     "You are stronger than you realize, and you’re capable of amazing things.",
#     "It’s normal to have tough days, but remember, brighter days are ahead.",
#     "Every effort you make is a step towards something great. Keep up the good work!",
#     "You are not alone in this. Reach out if you need support; people care about you.",
#     "Your feelings are valid, and it’s okay to take things one day at a time.",
#     "Success is built on perseverance. Stay positive and keep striving toward your goals.",
#     "Even on difficult days, remember that you’re making progress. Keep going!",
#     "You’ve faced challenges before and emerged stronger. You can do it again.",
#     "It’s okay to take a break. You’re doing great, and rest is part of the journey."
# ]


# def get_quote():
#   response = requests.get("https://zenquotes.io/api/random")
#   json_data = json.loads(response.text)
#   quote = json_data[0]['q'] + " -" + json_data[0]['a']
#   return quote


# def Get_Joke():
#   response = requests.get('https://official-joke-api.appspot.com/jokes/random')
#   joke = json.loads(response.text)
#   joke_final = joke['setup'] + "\n" + joke['punchline']
#   return joke_final


# def get_fact():
#   api_url = 'https://api.api-ninjas.com/v1/facts'
#   response = requests.get(api_url, headers={'X-Api-Key': '/HvL2UMcWwwzAjsMWWK59A==Qc5yQuq0dM6kmdRE'})
 
#   fact = json.loads(response.text)
#   final = fact[0]['fact']
#   return final
  
#   # response = requests.get(
#   #     "https://api.api-ninjas.com/v1/facts")
#   # fact = json.loads(response.text)
#   # return str(fact)


# # Load environment variables from .env file
# load_dotenv()

# intents = Intents.default()
# intents.message_content = True
# client = discord.Client(intents=intents)


# @client.event
# async def on_ready():
#   print(f'We have logged in as {client.user}')


# @client.event
# async def on_message(message):
#   if message.author == client.user:
#     return
#   if message.content.startswith('$hello'):
#     await message.channel.send(
#         'Hello! BATMAN IS HERE 🚀\n'
#         'I’m here to inspire you, share random facts, and crack some jokes. Just use one of these commands:\n'
#         '- `$BatmanPleaseInspireMe` for inspiration\n'
#         '- `$BatmanTellMeAJoke` for a joke\n'
#         '- `$BatmanEnlightenMe` for a random fact\n'
#         'What can I do for you today?')

#   if message.content.startswith(
#       '$BatmanPleaseInspireMe') or message.content.startswith(
#           '$batmanpleaseinspireme'):
#     quote = get_quote()
#     await message.channel.send(
#         "No worries!!! Batman is here to inspire you. \n " + quote)
#   if message.content.startswith(
#       '$BatmanTellMeAJoke') or message.content.startswith(
#           '$batmantellmeajoke'):
#     joke = Get_Joke()
#     await message.channel.send("Batman is here to lighten your mood. \n " +
#                                joke + "\n Wasn't that hilarious !!!")

#   if message.content.startswith(
#       '$BatmanEnlightenMe') or message.content.startswith(
#           '$batmanenlightenme'):
#     fact = get_fact()
#     await message.channel.send(
#         "No worries!!! Batman is here with something interesting: \n " + fact)

#   if any(word in message.content.lower() for word in sad_words):
#     await message.channel.send(random.choice(encouragements))


# # Get the bot token from the environment variable
# token = os.getenv('TOKEN')

# # Print the token to verify it is being retrieved correctly (remove this in production)
# print(f'Token: {token}')

# if token:
#   client.run(token)
# else:
#   print("Error: No TOKEN found in environment variables.")


from replit import db
from replit import db
import discord
import os
from discord import Intents
from dotenv import load_dotenv
import requests
import json
import random

sad_words = set([
    'sad', 'unhappy', 'miserable', 'depressed', 'down', 'sorrow', 'grief',
    'heartbroken', 'lonely', 'dejected', 'despair', 'melancholy', 'blue',
    'gloomy', 'woeful', 'downhearted', 'troubled', 'distressed', 'upset',
    'disheartened', 'forlorn', 'tearful', 'despondent', 'desolate', 'pensive',
    'discouraged', 'anguished', 'empty', 'painful', 'hurt', 'agonized',
    'regretful', 'melancholic', 'brokenhearted', 'isolated', 'numb',
    'unfulfilled', 'despairing', 'low', 'sorrowful', 'broken', 'abandoned'
])

encouragements = [
    "You’re doing your best, and that’s more than enough. Keep moving forward!",
    "Remember, every challenge is an opportunity to grow. You’ve got this!",
    "It’s okay to feel down sometimes. You have the strength to get through this.",
    "Believe in yourself. You have overcome so much already and can handle this too.",
    "Don’t forget to take care of yourself. You’re important and your well-being matters.",
    "Even small steps forward are progress. Keep going, and you’ll make it through.",
    "You are stronger than you realize, and you’re capable of amazing things.",
    "It’s normal to have tough days, but remember, brighter days are ahead.",
    "Every effort you make is a step towards something great. Keep up the good work!",
    "You are not alone in this. Reach out if you need support; people care about you.",
    "Your feelings are valid, and it’s okay to take things one day at a time.",
    "Success is built on perseverance. Stay positive and keep striving toward your goals.",
    "Even on difficult days, remember that you’re making progress. Keep going!",
    "You’ve faced challenges before and emerged stronger. You can do it again.",
    "It’s okay to take a break. You’re doing great, and rest is part of the journey."
]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

def Get_Joke():
    response = requests.get('https://official-joke-api.appspot.com/jokes/random')
    joke = json.loads(response.text)
    joke_final = joke['setup'] + "\n" + joke['punchline']
    return joke_final

def get_fact():
    api_url = 'https://api.api-ninjas.com/v1/facts'
    response = requests.get(api_url, headers={'X-Api-Key': '/HvL2UMcWwwzAjsMWWK59A==Qc5yQuq0dM6kmdRE'})
    fact = json.loads(response.text)
    final = fact[0]['fact']
    return final

# Load environment variables from .env file
load_dotenv()

intents = Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(
            'Hello! BATMAN IS HERE 🚀\n'
            'I’m here to inspire you, share random facts, and crack some jokes. Just use one of these commands:\n'
            '- `$BatmanPleaseInspireMe` for inspiration\n'
            '- `$BatmanTellMeAJoke` for a joke\n'
            '- `$BatmanEnlightenMe` for a random fact\n'
            '- `$new <your encouragement>` to add a new encouragement quote\n'
            'What can I do for you today?')

    if message.content.startswith('$BatmanPleaseInspireMe') or message.content.startswith('$batmanpleaseinspireme'):
        quote = get_quote()
        await message.channel.send("No worries!!! Batman is here to inspire you. \n " + quote)

    if message.content.startswith('$BatmanTellMeAJoke') or message.content.startswith('$batmantellmeajoke'):
        joke = Get_Joke()
        await message.channel.send("Batman is here to lighten your mood. \n " + joke + "\n Wasn't that hilarious !!!")

    if message.content.startswith('$BatmanEnlightenMe') or message.content.startswith('$batmanenlightenme'):
        fact = get_fact()
        await message.channel.send("No worries!!! Batman is here with something interesting: \n " + fact)

    if any(word in message.content.lower() for word in sad_words):
        all_encouragements = list(db.get('encouragements', [])) + encouragements
        await message.channel.send(random.choice(all_encouragements))

    if message.content.startswith('$new '):
        new_quote = message.content[len('$new '):].strip()
        existing_encouragements = db.get('encouragements', [])
        if new_quote not in existing_encouragements:
            existing_encouragements.append(new_quote)
            db['encouragements'] = existing_encouragements
            await message.channel.send("Thanks for contributing! The new encouragement has been added.")
        else:
            await message.channel.send("This encouragement is already in the database.")

# Get the bot token from the environment variable
token = os.getenv('TOKEN')

if token:
    client.run(token)
else:
    print("Error: No TOKEN found in environment variables.")
