import telebot as t
from telebot import types

bot = t.TeleBot('5520821655:AAEZfkhXuy1r9Cj3EX2pLYv64LzqD6UEvoc')

@bot.message_handler(commands=['start', 'help'], content_types=['text'])
def help_message(message):
    bot.reply_to(message, f"Hello {message.from_user.username}.Welcome to the page about Joji")
    mane = types.ReplyKeyboardMarkup()
    profile = types.KeyboardButton('Contact us')
    about = types.KeyboardButton('About us')
    music = types.KeyboardButton('Listen')
    restart = types.KeyboardButton('Restart bot')
    mane.row(profile, about)
    mane.row(music)
    mane.row(restart)
    bot.send_sticker(message.chat.id,'CAACAgQAAxkBAAEFM3lixKzMwUHJRh5lzQ_QEwhi0ahyKAACNw0AAnSLSFJNd2kbEg1ziykE', reply_markup=mane)



@bot.message_handler(content_types=['text'])
def navigation(message):
    if message.text == 'Contact us':
        keyboard = types.InlineKeyboardMarkup()
        inst_button = types.InlineKeyboardButton(text="Instgram", url='https://www.instagram.com/sushitrash/')
        tw_button = types.InlineKeyboardButton(text="Twitter", url='https://twitter.com/sushitrash')
        yt_button = types.InlineKeyboardButton(text="YouTube", url='https://www.youtube.com/channel/UCFl7yKfcRcFmIUbKeCA-SJQ')
        keyboard.add(inst_button)
        keyboard.add(tw_button)
        keyboard.add(yt_button)
        bot.send_message(message.chat.id, 'Contact us', reply_markup=keyboard)

    elif message.text == 'About us':
        keyboard_about = types.InlineKeyboardMarkup()
        git_button = types.InlineKeyboardButton(text='About Joji',
                                                url='https://jojimusic.com/')
        keyboard_about.add(git_button)
        bot.send_message(message.chat.id,
                         ("This bot was written\n"
                           "in Python 3.10.5 \n"
                          "\n"
                          "This bot was created using\n"
                           "telebot library\n"
                          "\n"
                          "Thanks for using the bot!"), reply_markup=keyboard_about)

    elif message.text == 'Listen':
        k_music = types.InlineKeyboardMarkup()
        music_button2 = types.InlineKeyboardButton('Deezeer',url='https://www.deezer.com/us/artist/5078097?autoplay=true')
        music_button3 = types.InlineKeyboardButton('Spotify', url='https://open.spotify.com/artist/3MZsBdqDrRTJihTHQrO6Dq')
        k_music.add(music_button2,music_button3,)
        k_test = types.ReplyKeyboardMarkup()
        main_menu_b = types.KeyboardButton('Main menu')
        k_test.row(main_menu_b)
        bot.send_message(message.chat.id, ('''
        All tracks you can listen on such music platforms as spotify,dezeer'''), reply_markup=k_music)
        bot.send_message(message.chat.id, text="[downside menu updated]", reply_markup=k_test)
    elif message.text == 'Restart bot':
        bot.send_message(message.chat.id, 'To restart the bot click this button(/start)')
    elif message.text == 'Main menu':
        bot.send_message(message.chat.id, 'To access the main menu of the bot click on this button (/start)')


@bot.message_handler(content_types=['sticker', 'photo'])
def sticker_id(message):
    print(message)


bot.polling()