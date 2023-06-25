import telebot
import time
from telebot import types
from db import db_table_val, db_comment_save
from options import *

bot = telebot.TeleBot(CODE)


@bot.message_handler(commands=['start'])
def start(message):
    us = message.from_user.id
    name = message.from_user.first_name
    fam = message.from_user.last_name
    nik = message.from_user.username
    db_table_val(us, name, fam, nik)

    video = open('video/video1.MOV', 'rb')
    bot.send_video(message.chat.id, video)
    time.sleep(15)
    bot.send_message(message.chat.id, text, parse_mode='HTML')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('SMM 👩🏻‍💻')
    btn2 = types.KeyboardButton('Консультация 📝')
    btn3 = types.KeyboardButton('Написать в Direct 📨')
    btn4 = types.KeyboardButton('Написать в WhatsApp 💚')
    btn5 = types.KeyboardButton('Обучение SMM с нуля')
    btn6 = types.KeyboardButton('Начать все сначала 🔄')
    btn7 = types.KeyboardButton('Оставить коментарий 💭')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    bot.send_message(message.chat.id, 'Узнать подробную информацию и цены ↓', reply_markup=markup)


@bot.message_handler(commands=['comment'])
def comment(message):
    mess1 = bot.reply_to(message, 'Пожалуйста, оставьте ваш отзыв!')
    bot.register_next_step_handler(mess1, comment_action)


def comment_action(message):
    data_user = (f'ID нашего пользователя->:{message.from_user.id}, Имя нашего пользователя->:{message.from_user.first_name}, фамилия->:{message.from_user.last_name}, Ник нейм->:{message.from_user.username}')
    db_comment_save(message.from_user.id, message.text)
    c = [7777777777]
    for i in c:
        bot.send_message(i, f'У нас новый отзыв, нам написал: <b>{data_user}</b>, и вот что он пишет: <b>{message.text}</b>', parse_mode='HTML')
    text1 = ('Спасибо вам за ваш отзыв!')
    bot.send_message(message.chat.id, text1, parse_mode='HTML')


@bot.message_handler()
def get_user_text(message):
    if message.text == 'SMM 👩🏻‍💻':
        bot.send_message(message.chat.id, text2, parse_mode='HTML')
    if message.text == 'Консультация 📝':
        bot.send_message(message.chat.id, text3, parse_mode='HTML')

    if message.text == 'Обучение SMM с нуля':
        bot.send_message(message.chat.id, text4, parse_mode='HTML')

    if message.text == 'Начать все сначала 🔄':
        start(message)

    if message.text == 'Оставить коментарий 💭':
        comment(message)

    if message.text == 'Написать в Direct 📨':
        z = types.InlineKeyboardMarkup()
        z.add(types.InlineKeyboardButton('Перейти в Instagram', url='https://instagram.com/konovalenko.marya?igshid=YmMyMTA2M2Y='))
        bot.send_message(message.chat.id, 'Instagram 📲', reply_markup=z)

    if message.text == 'Написать в WhatsApp 💚':
        q = types.InlineKeyboardMarkup()
        q.add(types.InlineKeyboardButton('Перейти в WhatsApp', url='https://wa.me/79292970175'))
        bot.send_message(message.chat.id, 'WhatsApp 📲', reply_markup=q)


if __name__ == "__main__":

    try:
        bot.polling(none_stop=True)
    except TimeoutError:
        print('Ошибка которую мы пытаемся поймать')
    finally:
        print('Сработал finally')
        time.sleep(15)
        bot.polling(none_stop=True)
        c = [7777777777]
        for i in c:
            bot.send_message(i, 'Телеграм БОТ ***** скоро упадет')