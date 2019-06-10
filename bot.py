import telebot
import emoji
from telebot import types


bot_token = '764198186:AAGPu1-Bc8gVQDmL1ZO0sTgHkV8bLmjv2DU'

bot = telebot.TeleBot(token=bot_token)


# COMMANDS


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hi! I am NoteBot - telegram bot that can send notes for musical instruments =)')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, 'All commands:'
                                      '/features, /start, /help, /songs_harmonica, /songs_piano and /songs_guitar')


@bot.message_handler(commands=['features'])
def send_features(message):
    bot.send_message(message.chat.id, 'I can send musical notes,'
                                      'but their number is limited because I do not use API at the moment.')


@bot.message_handler(commands=['harmonica'])
def send_note_harmonica(message):
    bot.send_message(message.chat.id, 'At the moment,'
                                      ' sheet music is only available for the following musical compositions:\n'
                                      'Godfather, March of Mendelssohn, Dancing in the Dark,'
                                      'Imperial march and Dancing in the dark.\n'
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


def send_all_2_photos(message, url_id, photo_id, photo_id_2):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Go to website with notes",
                                            url=url_id)
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Hello! You can see the notes by clicking on the button below =)",
                     reply_markup=keyboard)
    bot.send_photo(chat_id=message.chat.id,
                   photo=photo_id)
    bot.send_photo(chat_id=message.chat.id,
                   photo=photo_id_2)


# TEXT FEATURES


@bot.message_handler(commands=['songs_harmonica'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Godfather', 'Imperial march')
    markup.row('March of Mendelssohn', 'Dancing in the dark')
    bot.send_message(message.chat.id, "Choose one song:", reply_markup=markup)


@bot.message_handler(commands=['songs_piano'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row(emoji.emojize('Godfather :musical_keyboard:'),
               emoji.emojize('Chopin - Prelude in E minor Op.28 No.4 :musical_keyboard:'))
    bot.send_message(message.chat.id, "Choose one song:", reply_markup=markup)


@bot.message_handler(commands=['songs_guitar'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row(emoji.emojize('Godfather :guitar:'), emoji.emojize('Aladdin - A Whole New World :guitar:'))
    bot.send_message(message.chat.id, "Choose one song:", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Hello my friend!')
    elif message.text.lower() == 'bye':
        bot.send_message(message.chat.id, 'Bye! Hope to see you soon again =)')
    elif message.text.lower() == 'i love you':
        bot.send_sticker(message.chat.id, 'CAADAgADewEAAk-cEwKCccJvIsWEBwI')
    elif message.text.lower() == 'hse':
        bot.send_sticker(message.chat.id, 'CAADAgADVwEAAk-cEwKdCE6LUElPhAI')
    elif message.text.lower() == 'godfather':
        data = send_all(message, "https://www.harmonica.com/the-godfather-by-nino-rota-1822.html",
                        'https://pp.userapi.com/c855016/v855016562/65c9f/40Nph1jK3UI.jpg')
    elif message.text.lower() == 'imperial march':
        data = send_all(message, "https://www.harmonica.com/darth-vader-imperial-march-by-john-williams-1788.html",
                        'https://pp.userapi.com/c855016/v855016562/65c7c/Ptv2M44sAXE.jpg')
    elif message.text.lower() == 'march of mendelssohn':
        data = send_all(message, "https://antropinum.ru/tabs/12678",
                        'https://pp.userapi.com/c855016/v855016562/65c8a/dzXxnAyQ054.jpg')
    elif message.text.lower() == 'dancing in the dark':
        data = send_all(message, "https://www.harmonica.com/dancing-in-the-dark-by-bruce-springsteen-2559.html",
                        'https://pp.userapi.com/c855016/v855016562/65c56/ZFSjdEnIiEg.jpg')
    elif message.text.lower() == emoji.emojize('godfather :musical_keyboard:'):
        data = send_all(message, "https://musescore.com/user/9265496/scores/2049321",
                        'https://pp.userapi.com/c856032/v856032448/6567c/VgRmqqvAxdE.jpg')
    elif message.text.lower() == emoji.emojize('chopin - prelude in e minor op.28 no.4 :musical_keyboard:'):
        data = send_all_2_photos(message, "https://www.8notes.com/scores/9765.asp",
                                 'https://pp.userapi.com/c849128/v849128883/1ae7ba/ybJz0QyhPkI.jpg',
                                 'https://pp.userapi.com/c849128/v849128883/1ae7c2/NLK3jqJlT5U.jpg')
    elif message.text.lower() == emoji.emojize('godfather :guitar:'):
        data = send_all(message, "https://tabs.ultimate-guitar.com/tab/nino_rota/godfather_tabs_334933",
                        'https://pp.userapi.com/c849128/v849128448/1afa7b/B-xtBwHf29M.jpg')
    elif message.text.lower() == emoji.emojize('aladdin - a whole new world :guitar:'):
        data = send_all_2_photos(message, "https://tabs.ultimate-guitar.com/tab/misc_cartoons/"
                                          "aladdin_-_a_whole_new_world_tabs_342734",
                                 'https://pp.userapi.com/c849128/v849128883/1ae75f/oTGYubndX-Y.jpg',
                                 'https://pp.userapi.com/c849128/v849128883/1ae766/eU9PDwMkRS4.jpg')


bot.polling()
