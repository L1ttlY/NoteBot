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
    bot.send_message(message.chat.id, 'All commands: /features, /start, /help, /harmonica, /songs')


@bot.message_handler(commands=['features'])
def send_features(message):
    bot.send_message(message.chat.id, 'I can send musical notes, but their number is limited because I do not use API at the moment.')


@bot.message_handler(commands=['harmonica'])
def send_note_harmonica(message):
    bot.send_message(message.chat.id, 'At the moment,'
                                      ' sheet music is only available for the following musical compositions:\n'
                                      'Godfather, March of Mendelssohn, Dancing in the Dark, Imperial march and Dancing in the dark.\n'
                                      'Please press'
                                      ' the name of the musical composition of the note you would like to know.\n'
                                      'Soon we will use API and there will be much more sheet music available.')





# SONGS





def send_all(message, url_id, photo_id):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Go to website with notes",
                                            url=url_id)
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Hello! You can see the notes by clicking on the button below =)",
                     reply_markup=keyboard)
    bot.send_photo(chat_id=message.chat.id,
                   photo=photo_id)







# TEXT FEATURES
@bot.message_handler(commands=['songs'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Godfather', 'Imperial march')
    markup.row('March of Mendelssohn', 'Dancing in the dark')
    bot.send_message(message.chat.id, "Choose one song:", reply_markup=markup)





@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Hello my friend!')
    elif message.text.lower() == 'bye':
        bot.send_message(message.chat.id, 'Bye! Hope to see you soon again =)')
    elif message.text.lower() == 'i love you':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif message.text.lower() == 'godfather':
        data = send_all(message, "https://www.harmonica.com/the-godfather-by-nino-rota-1822.html", 'https://pp.userapi.com/c855016/v855016562/65c9f/40Nph1jK3UI.jpg')
    elif message.text.lower() == 'imperial march':
        data = send_all(message, "https://www.harmonica.com/darth-vader-imperial-march-by-john-williams-1788.html", 'https://pp.userapi.com/c855016/v855016562/65c7c/Ptv2M44sAXE.jpg')
    elif message.text.lower() == 'march of mendelssohn':
        data = send_all(message, "https://antropinum.ru/tabs/12678", 'https://pp.userapi.com/c855016/v855016562/65c8a/dzXxnAyQ054.jpg')
    elif message.text.lower() == 'dancing in the dark':
        data = send_all(message, "https://www.harmonica.com/dancing-in-the-dark-by-bruce-springsteen-2559.html", 'https://pp.userapi.com/c855016/v855016562/65c56/ZFSjdEnIiEg.jpg')




bot.polling()