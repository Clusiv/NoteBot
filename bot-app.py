import telebot
from NB import NoteBook
from telebot import types

# Здесь указать токен, который прислал BotFather.
# Не забудьте ковычки!
bot = telebot.TeleBot("1543078251:AAHCkuKqo_0cjDUJe-AxS5mK7ViTukwCeLY") 

markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
markup.add('Создать заметку', 'Поиск по слову', 'Выдать по ID')

statuses = ['Создать заметку', 'Поиск по слову', 'Выдать по ID']
current_status = ''

notebook = NoteBook()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Этот бот умеет хранить заметки.", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in statuses)
def get_status(message):
    global notebook, current_status, statuses

    current_status = message.text

    if current_status == 'Создать заметку':
        bot.send_message(message.chat.id, 'Напишите заметку')
    elif current_status == 'Поиск по слову':
        bot.send_message(message.chat.id, 'Ожидаю слово')
    elif current_status == 'Выдать по ID':
        bot.send_message(message.chat.id, 'Напишите номер заметки')

@bot.message_handler(func=lambda message: True)
def send_note(message):
    global notebook, current_status, statuses
    
    if current_status == 'Создать заметку':
        txt = 'Записал под идентификатором #' + str(notebook.create_note(message.text))
    elif current_status == 'Поиск по слову':
        txt = notebook.find_note(message.text)
    elif current_status == 'Выдать по ID':
        txt = notebook.get_note(int(message.text))

    txt = 'Выберите команду'
    bot.send_message(message.chat.id, txt, reply_markup=markup)
    current_status = ''
bot.polling()