import telebot
from telebot import types


bot_token = '764198186:AAGPu1-Bc8gVQDmL1ZO0sTgHkV8bLmjv2DU'

bot = telebot.TeleBot(token=bot_token)


# COMMANDS


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hi! I am NoteBot - telegram bot that can send notes for musical instruments =)')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, 'All commands: /features, /start, /help, /harmonica')


@bot.message_handler(commands=['features'])
def send_features(message):
    bot.send_message(message.chat.id, 'In the future i would be able to send notes')


@bot.message_handler(commands=['test'])
def test_send_photo(message):
    bot.send_photo(chat_id=message.chat.id,
                   photo='https://images.unsplash.com/photo-1531804055935-76f44d7c3621?ixlib=rb-1.2.1&ixid''='
                         'eyJhcHBfaWQiOjEyMDd9&w=1000&q=80')


@bot.message_handler(commands=['harmonica'])
def send_note_harmonica(message):
    bot.send_message(message.chat.id, 'At the moment,'
                                      ' sheet music is only available for the following musical compositions:\n'
                                      '/Godfather /March_of_Mendelssohn and /Imperial_march.\n'
                                      'Please press'
                                      ' the name of the musical composition of the note you would like to know.\n'
                                      'Soon we will use API and there will be much more sheet music available.')


# SONGS


@bot.message_handler(commands=['Godfather'])
def send_link(message):
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Go to website with notes", url="https://antropinum.ru/tabs/13430")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Hello! You can see the notes by clicking on the button below =)",
                         reply_markup=keyboard,)
        bot.send_photo(chat_id=message.chat.id,
                       photo='http://www.moosevilleusa.com/uploads/6/7/5/9/6759109/5958355_orig.jpg')
        # test photo, tabs are different


@bot.message_handler(commands=['Imperial_march'])
def send_link(message):
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Go to website with notes", url="https://antropinum.ru/tabs/12574")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Hello! You can see the notes by clicking on the button below =)",
                         reply_markup=keyboard)


@bot.message_handler(commands=['March_of_Mendelssohn'])
def send_link(message):
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Go to website with notes", url="https://antropinum.ru/tabs/12678")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Hello! You can see the notes by clicking on the button below =)",
                         reply_markup=keyboard)

# TEXT FEATURES


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Hello my friend!')
    elif message.text.lower() == 'bye':
        bot.send_message(message.chat.id, 'Bye! Hope to see you soon again =)')
    elif message.text.lower() == 'i love you':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')


bot.polling()
