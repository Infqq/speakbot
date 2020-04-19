from vkbottle import *
import requests


bot=Bot('token')

speak = 1

@bot.on.message(text='<name>')
async def wrapper(ans: Message, name):
    if speak == 1:
        response = requests.get("https://isinkin-bot-api.herokuapp.com/1/talk?q="+name.replace(" ","%20")).text[9:-2]
        await ans(f'{response}')
    else:
        await ans('Команда не найдена.')

bot.run_polling()
