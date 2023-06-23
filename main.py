import telebot
import time
from telebot import types
from db import db_table_val, db_comment_save

bot = telebot.TeleBot('YOU TOKEN')


@bot.message_handler(commands=['start'])
def start(message):
    us = message.from_user.id
    name = message.from_user.first_name
    fam = message.from_user.last_name
    nik = message.from_user.username
    db_table_val(us, name, fam, nik)

    video = open('video/video1.MOV', 'rb')
    bot.send_video(message.chat.id, video)

    text = f'''
<b>Я могу быть вам полезна:</b>
⠀
✔️если вам необходима услуга комплексного ведения аккаунта (SMM)
⠀
✔️ если вам нужна консультация по блогу.
Вы не понимаете почему нет продаж и блог не растет. Помогу разобраться именно с вашей ситуацией, выстроить стратегию развития и роста аккаунта.
Отвечу на все ваши вопросы.
⠀
✔️ так же если вы новичок в Instagram, но хотите тут зарабатывать. Вы можете прийти ко мне в личную работу или на курс «Smm с 0».'''
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
    data_user = (
        f'ID нашего пользователя->:{message.from_user.id}, Имя нашего пользователя->:{message.from_user.first_name}, фамилия->:{message.from_user.last_name}, Ник нейм->:{message.from_user.username}')
    db_comment_save(message.from_user.id, message.text)
    c = [7777777777]
    for i in c:
        bot.send_message(i, f'У нас новый отзыв, нам написал: <b>{data_user}</b>, и вот что он пишет: <b>{message.text}</b>', parse_mode='HTML')
    text1 = ('Спасибо вам за ваш отзыв!')
    bot.send_message(message.chat.id, text1, parse_mode='HTML')


@bot.message_handler()
def get_user_text(message):
    if message.text == 'SMM 👩🏻‍💻':
        text1 = ('''<b>Комплексное ведение аккаунта, SMM</b>

        <b>Для кого данная услуга?</b>

        ✔ У вас нет времени на создание контента и ведение социальных сетей,
        ✔ У вас нет/мало навыков работы в инстаграм, но понимаете что вести его необходимо,
        ✔ Хотите увеличить прибыль, привлекать клиентов онлайн
        ✔ Хотите, что бы у вас было больше свободного времени на себя и свою семью, а не на создание сторис, рилс и написание постов

        <b>Что входит в услугу?</b>

        - изучение вашей ниши
        - подробный анализ и сегментирование целевой аудитории
        - анализ конкурентов
        - стратегия продвижения
        - продающая визуальная упаковка профиля наполненная смыслами, которые будут откликаться вашей ЦА: оформление шапки профиля, наполнение контентом вечных сторис, оформление заставок, создание визуала
        - контент-план на 12 публикаций в месяц (пост/Reels)
        - копирайтинг: написание постов или редактирование ваших(12 шт. в месяц)
        - контент-план для сторис (на месяц)
        - оформление сторис 6шт в день
        - подбор идей для Reels и монтаж, подбор идей для фото
        - подбор блогеров для рекламы, написание для них ТЗ (до 3 в месяц)
        - подбор целевых хештегов
        - одноразовое создание чек-листа / гайда для вашей аудитории(приветственное письмо)''')
        text2 = ('''

        <b>Что вы получите:</b>

        - клиентов и прибыль
        - отстройку от конкурентов и узнаваемость вашего бренда
        - продвижение ваших продуктов / услуг
        - свободное время для более важных вещей, вам не придется ломать голову что сегодня выложить и где взять контент
        - ведение аккаунта без простоев и задержек с контентом
        - ответственного smm-специалиста, ответственного и заинтересованного в продвижении вашего бизнеса
        ___________________________________
        <b>Стоимость пакета: 25 000 р/месяц
        Съемка контента оплачивается отдельно - 2 500р/час</b>''')

        bot.send_message(message.chat.id, text1 + text2, parse_mode='HTML')
    if message.text == 'Консультация 📝':
        text = '''<b>Консультация по блогу</b>

        <b>Кому нужна консультация?</b>

        ✔ для тех, кто самостоятельно ведет свой коммерческий / экспертный аккаунт, реализует в нем продукты / услуги
        ✔ вы не понимаете почему на вас плохо подписываются и нет продаж
        ✔ вам не понятно, как оформить блог и какие ошибки / пробелы есть в вашем аккаунте
        ✔ не понимаете, как двигаться дальше, не можете определиться с позиционированием, как определить свою ЦА, какой контент нужен для вас и вашей аудитории и какие смыслы в него закладывать
        ✔ как вести блог не выгорая и находить идеи для контента

        <b>Что необходимо для консультации?</b>

        - ответить подробно на все вопросы в брифе(высылаю по запросу)

        <b>Что входит в услугу?</b>

        - анализ вашего профиля на текущий момент, анализ вашего запроса / цели
        - составление четкой стратегии работы в блоге, исходя из ваших целей, весь материал оформляется в презентацию и остается у вас навсегда.
        - консультация 1,5 - 2 часа онлайн / офлайн 
        - сопровождение в течении 14 дней после консультации, где вы можете задать мне все возникающие вопросы
        - дополнительные материалы по запросу выборочно (инструкции, видео-уроки, скрипты и тд.)


        ___________________________________
        <b>Стоимость 7 000р 
        Сроки выполнения подготовки к консультации до 7 дней.</b>'''
        bot.send_message(message.chat.id, text, parse_mode='HTML')

    if message.text == 'Обучение SMM с нуля':
        text = '''Программа обучения:
⠀
        1. Вводная лекция.
        1.1 Безопасность.
        1.2 Целевая аудитоия и брифинг.
        ⠀
        2. Оформление шапки профиля.
        2.1. Позиционирование и УТП.
        ⠀
        3. Визуальное оформление ленты.
        3.1 Базовые правила съемки и компановки ленты.
        ⠀
        4. Виды текстового контента.
        4.1 Учимся писать текст.
        ⠀
        5. Сторис. Вовлечение. Работа со статистикой.
        ⠀
        6. Продвижение блога.
        6.1 Бесплатные методы.
        6.2 Продвижение с помощью Reels.
        6.3 Реклама у блогеров.
        ⠀
        7. Оформление кейса. Рекомендации по поиску клиентов.
        7.1 Лайфхаки в работе.
⠀
        Бонус: обучающие уроки по ВК в записи.'''
        bot.send_message(message.chat.id, text, parse_mode='HTML')

    if message.text == 'Начать все сначала 🔄':
        start(message)

    if message.text == 'Оставить коментарий 💭':
        comment(message)

    if message.text == 'Написать в Direct 📨':
        z = types.InlineKeyboardMarkup()
        z.add(types.InlineKeyboardButton('Перейти в Instagram',
                                         url='https://instagram.com/konovalenko.marya?igshid=YmMyMTA2M2Y='))
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
        c = [77777777777]
        for i in c:
            bot.send_message(i, 'ТелеграмБОТ **** скоро упадет')