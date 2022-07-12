import telebot
from telebot import types
from pyowm import OWM

bot=telebot.TeleBot('key')

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Краснодар")
    btn2 = types.KeyboardButton("Апшеронск")
    btn3 = types.KeyboardButton("Славянск-На-Кубани")
    btn4 = types.KeyboardButton("Абакан")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text="Здравствуйте, товарищ!\n\nРад вас видеть в нашей Сибирской партии!\n\nЯ помогу тебе подобрать одежду по погоде!")
    bot.send_message(message.chat.id, text="Какой город тебя интересует?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def give_weather(message):
    owm = OWM('b8aaeff8eed70574cc24c5180c57a66f')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    t = w.temperature('celsius')
    t1 = t['temp']
    t2 = t['feels_like']
    t3 = t['temp_max']
    t4 = t['temp_min']

    # Скорость ветра
    wi = w.wind()['speed']

    # Влажность
    humi = w.humidity

    answer = f'В г. {message.text} сейчас {t1} C°.\n\nМакс. температура: {t3} C°\n\nМин. темперутара: {t4} C°'

    if int(t1) < 5:
        answer1 = 'Пуховичок, шарф и перчатки - сегодня твои друзья.'
    elif int(t1) < 10:
        answer1 = 'Сегодня стоит одеть пуховик или теплую куртку.'
    elif int(t1) < 15:
        answer1 = 'Рекомендую сегодня одевать легкую куртку или теплую кофту.'
    elif int(t1) < 20:
        answer1 = 'Классная погода для поездок на велике.\n\nОдной кофты сегодя будет достаточно.'
    elif int(t1) < 30:
        answer1 = 'Сегодня отличная погода, футболка с джинсами будет в самый раз.'
    elif int(t1) < 35:
        answer1 = 'Кажется сегодня будет очень жарко, без воды на улице сегодня не обойтись.'
    elif int(t1) > 35:
        answer1 = 'Сегодня будет пекло, на улицу выходить не рекомендуется.'
 
    bot.send_message(message.chat.id, answer)
    bot.send_message(message.chat.id, answer1)

bot.polling(none_stop=True, interval=0)
