import telebot, emoji
from telebot import types


bot_token = '764198186:AAGPu1-Bc8gVQDmL1ZO0sTgHkV8bLmjv2DU'

bot = telebot.TeleBot(token=bot_token)


# COMMANDS


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     emoji.emojize('Hi! I am NoteBot :musical_note: '
                                   '- Telegram Bot that can send notes for musical instruments \n'
                                   'Type /features to see what i can do\n'
                                   'If you have found any bugs:'
                                   ' please contact us at notebotproject@gmail.com'))


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, 'All available commands:'
                                      '/start - introduction\n'
                                      '/features - things that i can do\n'
                                      '/songs_harmonica, /songs_piano, /songs_guitar - songs\n'
                                      '/learn_harmonica, /learn_piano, /learn_guitar - playlists on YT for beginners\n'
                                      '"hello", "bye", "i love you", "hse" - messages that you can use to '
                                      'interact with me(the last one is an easter egg for HSE students (: )\n'
                                      '/future_work - priorities for us to make NoteBot more useful to you')


@bot.message_handler(commands=['future_work'])
def send_features(message):
    bot.send_message(message.chat.id, 'Our plans for future are:\n'
                                      '- Use API\n'
                                      '- Add more songs\n'
                                      '- Add more useful and interesting features')


@bot.message_handler(commands=['features'])
def send_features(message):
    bot.send_message(message.chat.id, 'I can send musical notes for Harmonica, Piano and Guitar,'
                                      ' but their number is limited '
                                      'because I do not use API at the moment.\n'
                                      'To see songs for these instruments, please use commands:\n'
                                      '/songs_harmonica for Harmonica songs\n'
                                      '/songs_piano for Piano songs\n'
                                      '/songs_guitar for Guitar songs\n'
                                      'You can learn the basics of these musical instruments by using '
                                      'commands: /learn_harmonica, /learn_piano and /learn_guitar.\n'
                                      'You can see all available commands by using /help.')


@bot.message_handler(commands=['songs_harmonica'])  # harmonica
def handle_start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Godfather', 'Imperial march')
    markup.row('March of Mendelssohn', 'Dancing in the dark')
    markup.row('Jingle Bells', 'Twinkle Twinkle Little Star')
    markup.row('I Believe I Can Fly', 'Smells Like Teen Spirit')
    markup.row('Nothing Else Matters', 'What a Wonderful World')
    bot.send_message(message.chat.id, "Choose one song:", reply_markup=markup)


@bot.message_handler(commands=['songs_piano'])  # piano
def handle_start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row(emoji.emojize('Godfather :musical_keyboard:'),
               emoji.emojize('Chopin - Prelude in E minor Op.28 No.4 :musical_keyboard:'))
    markup.row(emoji.emojize('The Entertainer :musical_keyboard:'),
               emoji.emojize('Greensleeves :musical_keyboard:'))
    markup.row(emoji.emojize('Fur Elise :musical_keyboard:'),
               emoji.emojize('Por Una Cabeza :musical_keyboard:'))
    markup.row(emoji.emojize('Waltz from Sleeping Beauty :musical_keyboard:'),
               emoji.emojize('Eine Kleine Nachtmusik :musical_keyboard:'))
    markup.row(emoji.emojize('O Holy Night :musical_keyboard:'),
               emoji.emojize('Ode to Joy :musical_keyboard:'))
    bot.send_message(message.chat.id, "Choose one song:", reply_markup=markup)


@bot.message_handler(commands=['songs_guitar'])  # guitar
def handle_start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row(emoji.emojize('Godfather :guitar:'),
               emoji.emojize('Aladdin - A Whole New World :guitar:'))
    markup.row(emoji.emojize('Jingle Bells :guitar:'),
               emoji.emojize('Happy Birthday :guitar:'))
    markup.row(emoji.emojize('Old MacDonald Had a Farm :guitar:'),
               emoji.emojize('Prelude in D :guitar:'))
    markup.row(emoji.emojize('Lullaby (Wiegenlied) :guitar:'),
               emoji.emojize('Country Dance :guitar:'))
    markup.row(emoji.emojize('Bolero :guitar:'),
               emoji.emojize('Turkish March :guitar:'))
    bot.send_message(message.chat.id, "Choose one song:", reply_markup=markup)


# FUNCTIONS


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


def learn(message, url_id):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Start learning",
                                            url=url_id)
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Hey! You can learn basics of this musical instrument"
                                      " by clicking on the button below",
                     reply_markup=keyboard)

# LEARNING


@bot.message_handler(commands=['learn_guitar'])
def send_learning(message):
    send_link = learn(message, "https://www.youtube.com/playlist?list=PL-RYb_OMw7GfqsbipaR65GDDzA1rP5deq")


@bot.message_handler(commands=['learn_piano'])
def send_learning(message):
    send_link = learn(message, "https://www.youtube.com/playlist?list=PLP9cbwDiLzdL6IS4-rmzR42ghq3T56XnK")


@bot.message_handler(commands=['learn_harmonica'])
def send_learning(message):
    send_link = learn(message, "https://www.youtube.com/playlist?list=PLKONji9dlomQtLpyMM4vT9K1mx_jUNxLp")


# TEXT FEATURES


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

    # HARMONICA SONGS

    elif message.text.lower() == 'godfather':
        data = send_all(message, "https://www.harmonica.com/the-godfather-by-nino-rota-1822.html",
                        'https://pp.userapi.com/c855016/v855016562/65c9f/40Nph1jK3UI.jpg')
    elif message.text.lower() == 'jingle bells':
        data = send_all(message, "https://www.harmonica.com/jingle-bells-by-unknown-2014.html",
                        "https://pp.userapi.com/c855020/v855020705/646ce/ans525gkw9Y.jpg")
    elif message.text.lower() == 'twinkle twinkle little star':
        data = send_all(message, 'https://www.harmonica.com/'
                                 'free-harmonica-tabs-for-twinkle-twinkle-little-star-by-unknown-2668.html',
                        'https://pp.userapi.com/c855020/v855020705/6471f/IUJbtHUhsLQ.jpg')
    elif message.text.lower() == 'i believe i can fly':
        data = send_all_2_photos(message, "https://www.harmonica.com/i-believe-i-can-fly-by-r-kelly-2519.html",
                                 "https://pp.userapi.com/c855020/v855020705/647bd/LHSUBcErS48.jpg",
                                 "https://pp.userapi.com/c855020/v855020705/647c4/MP5H6pr9qD4.jpg")
    elif message.text.lower() == 'smells like teen spirit':
        data = send_all_2_photos(message, "https://www.harmonica.com/smells-like-teen-spirit-by-nirvana-1654.html",
                                 "https://pp.userapi.com/c855020/v855020705/647e7/B0OxD97lpK4.jpg",
                                 "https://pp.userapi.com/c855020/v855020705/647ee/jCFkL41HF5k.jpg")
    elif message.text.lower() == 'nothing else matters':
        data = send_all_2_photos(message, "https://www.harmonica.com/nothing-else-matters-by-metallica-2234.html",
                                 "https://pp.userapi.com/c855020/v855020705/647ff/WZ3SWdIVHDw.jpg",
                                 "https://pp.userapi.com/c855020/v855020705/64807/jbetMMai3Bk.jpg")
    elif message.text.lower() == 'what a wonderful world':
        data = send_all_2_photos(message, "https://www.harmonica.com/"
                                          "what-a-wonderful-world-by-louis-armstrong-1660.html",
                                 "https://pp.userapi.com/c855020/v855020965/68290/yX3T5B5hrUQ.jpg",
                                 "https://pp.userapi.com/c855020/v855020965/68298/v4tcQppfE3g.jpg")
    elif message.text.lower() == 'imperial march':
        data = send_all(message, "https://www.harmonica.com/darth-vader-imperial-march-by-john-williams-1788.html",
                        'https://pp.userapi.com/c855016/v855016562/65c7c/Ptv2M44sAXE.jpg')
    elif message.text.lower() == 'march of mendelssohn':
        data = send_all(message, "https://antropinum.ru/tabs/12678",
                        'https://pp.userapi.com/c855016/v855016562/65c8a/dzXxnAyQ054.jpg')
    elif message.text.lower() == 'dancing in the dark':
        data = send_all(message, "https://www.harmonica.com/dancing-in-the-dark-by-bruce-springsteen-2559.html",
                        'https://pp.userapi.com/c855016/v855016562/65c56/ZFSjdEnIiEg.jpg')

    # PIANO SONGS

    elif message.text.lower() == emoji.emojize('godfather :musical_keyboard:'):
        data = send_all(message, "https://musescore.com/user/9265496/scores/2049321",
                        'https://pp.userapi.com/c856032/v856032448/6567c/VgRmqqvAxdE.jpg')
    elif message.text.lower() == emoji.emojize('chopin - prelude in e minor op.28 no.4 :musical_keyboard:'):
        data = send_all_2_photos(message, "https://www.8notes.com/scores/9765.asp",
                                 'https://pp.userapi.com/c849128/v849128883/1ae7ba/ybJz0QyhPkI.jpg',
                                 'https://pp.userapi.com/c849128/v849128883/1ae7c2/NLK3jqJlT5U.jpg')
    elif message.text.lower() == emoji.emojize('the entertainer :musical_keyboard:'):
        data = send_all(message, "https://www.8notes.com/scores/13178.asp",
                        'https://pp.userapi.com/c855016/v855016676/67f99/q7O2R9p_0QE.jpg')
    elif message.text.lower() == emoji.emojize('greensleeves :musical_keyboard:'):
        data = send_all(message, "https://www.8notes.com/scores/12179.asp",
                        'https://pp.userapi.com/c855016/v855016676/67fd2/fSkZHXx4Bm0.jpg')
    elif message.text.lower() == emoji.emojize('fur elise :musical_keyboard:'):
        data = send_all_2_photos(message, "https://www.8notes.com/scores/457.asp",
                                 'https://pp.userapi.com/c855016/v855016676/67fda/51NKeBRAfe4.jpg',
                                 'https://pp.userapi.com/c855016/v855016676/67fe2/7ycehEkbaj0.jpg')
    elif message.text.lower() == emoji.emojize('por una cabeza :musical_keyboard:'):
        data = send_all_2_photos(message, "https://www.8notes.com/scores/18093.asp",
                                 'https://pp.userapi.com/c855016/v855016046/6814b/BNBvI6jIDgA.jpg',
                                 'https://pp.userapi.com/c855016/v855016046/68143/O04hvB7UFyQ.jpg')
    elif message.text.lower() == emoji.emojize('waltz from sleeping beauty :musical_keyboard:'):
        data = send_all(message, "https://www.8notes.com/scores/13169.asp",
                                 'https://pp.userapi.com/c851028/v851028394/1411a8/f6KalVJTVX0.jpg')
    elif message.text.lower() == emoji.emojize('eine kleine nachtmusik :musical_keyboard:'):
        data = send_all_2_photos(message, "https://www.8notes.com/scores/418.asp",
                                 'https://pp.userapi.com/c851028/v851028394/1411ba/FB6D7nCRnTs.jpg',
                                 'https://pp.userapi.com/c851028/v851028394/1411c2/QwdsEHYnK3A.jpg')
    elif message.text.lower() == emoji.emojize('o holy night :musical_keyboard:'):
        data = send_all_2_photos(message, "https://www.8notes.com/scores/13800.asp",
                                 'https://pp.userapi.com/c851028/v851028394/1411ee/hRKHueqJ_lY.jpg',
                                 'https://pp.userapi.com/c851028/v851028394/1411f7/QdiZRkauIXU.jpg')
    elif message.text.lower() == emoji.emojize('ode to joy :musical_keyboard:'):
        data = send_all(message, "https://www.8notes.com/scores/12180.asp",
                        'https://pp.userapi.com/c850628/v850628717/140545/IoZim1zBanc.jpg')

    # GUITAR SONGS

    elif message.text.lower() == emoji.emojize('godfather :guitar:'):
        data = send_all(message, "https://tabs.ultimate-guitar.com/tab/nino_rota/godfather_tabs_334933",
                        'https://pp.userapi.com/c849128/v849128448/1afa7b/B-xtBwHf29M.jpg')
    elif message.text.lower() == emoji.emojize('aladdin - a whole new world :guitar:'):
        data = send_all_2_photos(message, "https://tabs.ultimate-guitar.com/tab/misc_cartoons/"
                                          "aladdin_-_a_whole_new_world_tabs_342734",
                                 'https://pp.userapi.com/c849128/v849128883/1ae75f/oTGYubndX-Y.jpg',
                                 'https://pp.userapi.com/c849128/v849128883/1ae766/eU9PDwMkRS4.jpg')
    elif message.text.lower() == emoji.emojize('jingle bells :guitar:'):
        data = send_all(message, "https://www.8notes.com/scores/11624.asp",
                        'https://pp.userapi.com/c855620/v855620241/6a160/GeZxKqoC90E.jpg')
    elif message.text.lower() == emoji.emojize('happy birthday :guitar:'):
        data = send_all(message, "https://www.8notes.com/scores/15676.asp",
                        'https://pp.userapi.com/c855620/v855620241/6a171/9RDpd25jW-c.jpg')
    elif message.text.lower() == emoji.emojize('lullaby (wiegenlied) :guitar:'):
        data = send_all(message, "https://www.8notes.com/scores/17659.asp",
                        'https://pp.userapi.com/c855620/v855620241/6a179/RnngwLuEdqs.jpg')
    elif message.text.lower() == emoji.emojize('country dance :guitar:'):
        data = send_all_2_photos(message, "https://www.8notes.com/scores/16780.asp",
                                 'https://pp.userapi.com/c855620/v855620241/6a18b/eP-HDpG3mhQ.jpg',
                                 'https://pp.userapi.com/c855620/v855620241/6a19b/RwOhE5eFYxg.jpg')
    elif message.text.lower() == emoji.emojize('old macdonald had a farm :guitar:'):
        data = send_all(message, "https://www.8notes.com/scores/15036.asp",
                        'https://pp.userapi.com/c855620/v855620241/6a1c1/UV9H0v0M5fo.jpg')
    elif message.text.lower() == emoji.emojize('prelude in d :guitar:'):
        data = send_all(message, "https://www.8notes.com/scores/23526.asp",
                        'https://pp.userapi.com/c855620/v855620241/6a1dc/omCFll-G3qk.jpg')
    elif message.text.lower() == emoji.emojize('bolero :guitar:'):
        data = send_all(message, "https://www.8notes.com/scores/17231.asp",
                        'https://pp.userapi.com/c855620/v855620241/6a1e4/noZOaxZyURw.jpg')
    elif message.text.lower() == emoji.emojize('turkish march :guitar:'):
        data = send_all(message, "https://www.8notes.com/scores/29551.asp",
                        'https://pp.userapi.com/c855620/v855620241/6a209/CU-ujaemvDU.jpg')


bot.polling()
