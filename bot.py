from vkbottle import *
import requests


bot=Bot('token')

@bot.on.message(text='<name>')
async def wrapper(ans: Message, name):
    response = requests.get("https://isinkin-bot-api.herokuapp.com/1/talk?q="+name.replace(" ","%20")).text[9:-2]
    await ans(f'{response}')

bot.run_polling()
