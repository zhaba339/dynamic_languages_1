import telebot
from telebot import types
import random

secret_number = 0
bot = telebot.TeleBot('6403710737:AAFPbfAZYotE5hMdec_7TLJRkj4xYu2bMr0')
@bot.message_handler(content_types=['text'])


def get_text_messages(message):
    global secret_number

    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Привет, давай сыграем в игру \"Угадай число\".\nЯ загадываю число от 1 до 10, а ты должен его угадать.\nНапиши свой ответ.')
        secret_number = random.randint(1, 10)
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши \"/start\"')
    else:
        # Проверяем, начата ли игра
        if secret_number != 0:
            game_start(message)
        else:
            bot.send_message(message.from_user.id, 'Я тебя не понимаю, напиши /help')

def game_start(message):
    if message.text.isdigit():
        user_guess = int(message.text)
        if user_guess == secret_number:
            bot.send_message(message.from_user.id, 'Поздравляю! Ты угадал число!')
        else:
            bot.send_message(message.from_user.id, 'Не угадал. Попробуй еще раз.')

bot.polling(none_stop=True, interval=0)

