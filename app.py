from config import *
from extensions import *

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    bot.send_message(message.chat.id,f"Отправьте сообщение боту в виде <имя валюты, цену которой хотите узнать>"
                                     f" <имя валюты, в которой надо узнать цену первой валюты>"
                                     f" <количество первой валюты> и бот посчитает ее по текущему курсу за вас! \n"
                                     f"Указывайте название валюты в единственном числе!\n"
                                     f"Чтобы увидеть список доступных валют: /values")

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    bot.send_message(message.chat.id,"Здесь будет список валют")

@bot.message_handler(content_types = ['text'])
def say_rate(message: telebot.types.Message):
    a = message.text.lower()
    a = a.split()
    try:
        if len(a) != 3: raise Smthn_wrong('Упс.. Вы отправили не то, что мы ожидали. Пожалуйста прочитайте инструкцию /help')
    except Smthn_wrong as e:
        bot.reply_to(message, e)
    else:
        try:
            b = try_.convert(a[0],a[1],a[2])
        except Smthn_wrong as e:
            bot.reply_to(message,e)
        else:
            bot.reply_to(message,f'Цена {a[2]} {a[0]} в {a[1]} = {str(get_price(symbols_now[a[0]], symbols_now[a[1]], int(a[2])))}' )



@bot.message_handler(content_types = ["audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
                 "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
                 "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                 "migrate_from_chat_id", "pinned_message"])
def say_errow(message: telebot.types.Message):
    try:
        raise Smthn_wrong('Упс.. Вы отправили не то, что мы ожидали. Пожалуйста прочитайте инструкцию /help')
    except Smthn_wrong as e:
        bot.send_message(message.chat.id,e)

bot.polling(none_stop=True)