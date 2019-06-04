import telebot

bot_token = '764198186:AAGPu1-Bc8gVQDmL1ZO0sTgHkV8bLmjv2DU'

bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hi! I am NoteBot - telegram bot that can send notes for musical instruments =)')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'All commands: /features, /start, /help')


@bot.message_handler(commands=['features'])
def send_features(message):
    bot.reply_to(message, 'In the future i would be able to send notes')

bot.polling()
