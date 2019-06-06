import telebot, requests
from telebot import types



bot_token = '764198186:AAGPu1-Bc8gVQDmL1ZO0sTgHkV8bLmjv2DU'

bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hi! I am NoteBot - telegram bot that can send notes for musical instruments =)')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'All commands: /features, /start, /help, /harmonica')


@bot.message_handler(commands=['features'])
def send_features(message):
    bot.reply_to(message, 'In the future i would be able to send notes')


@bot.message_handler(commands=['harmonica'])
def send_note_harmonica(message):
    bot.reply_to(message, 'At the moment, sheet music is only available for the following musical compositions: /Godfather, /March_of_Mendelssohn and /Imperial_march. Please press the name of the musical composition of the note you would like to know. Soon we will use API and there will be much more sheet music availible.')


@bot.message_handler(commands=['Godfather'])
def send_link(message):
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти на сайт с нотами", url="https://antropinum.ru/tabs/13430")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди на сайт с нотами.", reply_markup=keyboard)
@bot.message_handler(commands=['Imperial_march'])
def send_link(message):
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти на сайт с нотами", url="https://antropinum.ru/tabs/12574")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди на сайт с нотами.", reply_markup=keyboard)
@bot.message_handler(commands=['March_of_Mendelssohn'])
def send_link(message):
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти на сайт с нотами", url="https://antropinum.ru/tabs/12678")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди на сайт с нотами.", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Hello world!')
    elif message.text.lower() == 'buy':
        bot.send_message(message.chat.id, 'Buy')
    elif message.text.lower() == 'i love you':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    #elif message.text.lower() == 'godfather':   #я хочу что бы "godfather" вводилась как обычное сообщение а не команда, но в этом виде оно не работает
     #   def send_link(message):
      #      keyboard = types.InlineKeyboardMarkup()
       #     url_button = types.InlineKeyboardButton(text="Перейти на сайт с нотами", url="https://antropinum.ru/tabs/13430")
        #    keyboard.add(url_button)
         #   bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди на сайт с нотами.", reply_markup=keyboard)










bot.polling()