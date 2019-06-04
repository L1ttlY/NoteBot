import telebot

bot_token = '764198186:AAGPu1-Bc8gVQDmL1ZO0sTgHkV8bLmjv2DU'

bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome!')


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'To use this bot, send it a username')


@bot.message_handler(commands=['features'])
def send_welcome(message):
    bot.reply_to(message, 'In the future i would be able to send notes')

bot.polling()
