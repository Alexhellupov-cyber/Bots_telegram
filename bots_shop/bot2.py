import telebot
from telebot import types

# Замените 'YOUR_API_TOKEN' на ваш реальный API токен
bot = telebot.TeleBot('7438062994:AAGZtpLpUeT23cnRn9wVaAs8TWWkm6GujQY')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Услуги')
    btn2 = types.KeyboardButton('Как заказать?')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Привет! Выберите один из вариантов:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Услуги')
def services_menu(message):
    with open('C:/Users/380674914614/Desktop/bot/photo/услуги.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Рассылка')
    btn2 = types.KeyboardButton('Реклама')
    btn_back = types.KeyboardButton('Назад')
    markup.add(btn1, btn2,btn_back)
    bot.send_message(message.chat.id, "Выберите услугу:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Рассылка')
def software(message):
    with open('C:/Users/380674914614/Desktop/bot/photo/рассылка.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Комбайн')
    btn2 = types.KeyboardButton('Рассылка в лс')
    btn3 = types.KeyboardButton('Рассылка по чатам')
    btn_back = types.KeyboardButton('Назад')
    markup.add(btn1,btn2,btn3, btn_back)
    bot.send_message(message.chat.id, "Отправляет ваш текст с фото и видео в личку\чатам.", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Комбайн')
def software(message):
    with open('C:/Users/380674914614/Desktop/bot/photo/Комбайн.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Заказать')
    btn_back = types.KeyboardButton('Назад')
    markup.add(btn1, btn_back)
    bot.send_message(message.chat.id, "Комбайн - в нем сразу содержится пару услуг: парсер, инвайтер, спаммер классик, автоподписка на каналы. Цена: 70$", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Рассылка в лс')
def software(message):
    with open('C:/Users/380674914614/Desktop/bot/photo/рассылкавлс.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Заказать')
    btn_back = types.KeyboardButton('Назад')
    markup.add(btn1, btn_back)
    bot.send_message(message.chat.id, "Отправляет ваш текст с фото и видео в лс. Цена: 60$", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Рассылка по чатам')
def software(message):
    with open('C:/Users/380674914614/Desktop/bot/photo/рассылкапочатам.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Заказать')
    btn_back = types.KeyboardButton('Назад')
    markup.add(btn1, btn_back)
    bot.send_message(message.chat.id, "Отправляет ваш текст с фото и видео в чатам. Цена: 50$", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Заказать')
def order_service(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('Назад')
    markup.add(btn_back)
    bot.send_message(message.chat.id, "Заказать вы можете у администратора @elison_smm", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Реклама')
def advertisement(message):
    with open('C:/Users/380674914614/Desktop/bot/photo/фото.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Заказать')
    btn_back = types.KeyboardButton('Назад')
    markup.add(btn1, btn_back)
    bot.send_message(message.chat.id, """Рекламируем:

Работа/Фриланс 
Биржа каналов
Бизнес
Инвестиции 
Коучинг
Банки/Кредиты
Криптовалюта
Майнинг
МЛМ
Экзотерика
Теневая тематика
Психология 
Cтaвки/Kaзино
Авто 
Aрбитрaж 
Beйп/Табaк 
Маркетплейсы

а так же любое другое""", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Как заказать?')
def how_to_order(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Заказать')
    btn_back = types.KeyboardButton('Назад')
    markup.add(btn1, btn_back)
    bot.send_message(message.chat.id, "Заказать вы можете у администратора @elison_smm", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Назад')
def back_to_main_menu(message):
    send_welcome(message)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Комбайн':
        bot.reply_to(message, "Комбайн - в нем сразу содержится пару услуг: парсер, инвайтер, спаммер классик, автоподписка на каналы. Цена: 70$")
    elif message.text == 'Рассылка в ЛС':
        bot.reply_to(message, "Рассылка в ЛС - отправляет ваш текст с фото и видео в личку. Цена: 50$")
    elif message.text == 'Автоподписка на каналы':
        bot.reply_to(message, "Автоподписка на каналы. Цена: 35$")
    elif message.text == 'Правила сайта':
        bot.reply_to(message, "https://vm.tiktok.com/ZMrxhH1C6")
    elif message.text == 'Создатель':
        bot.reply_to(message, "@alexhellupov")
    elif message.text == 'Пасхалка':
        bot.reply_to(message, "1488")
    else:
        bot.reply_to(message, "Извините, я не понимаю эту команду.")

if __name__ == '__main__':
    bot.infinity_polling()









user_states = {}

# Курс обмена
exchange_btc_rate = 5577915.00
exchange_eth_rate = 243251.40
exchange_ltc_rate = 6083.70
exchange_usdt_rate = 94.38 
exchange_usdc_rate = 94.38 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('Купить')
    btn2 = types.KeyboardButton('Продать')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, """⭕️ Добро пожаловать в автоматический обменный пункт BitCash!

🔄 Курсы обмена:

⬇️ Покупка: 1 BTC → 5577915.00 ₽
⬆️ Продажа: 1 BTC → 5312300.00 ₽

⬇️ Покупка: 1 ETH → 243251.40 ₽
⬆️ Продажа: 1 ETH → 231668.00 ₽

⬇️ Покупка: 1 LTC → 6083.70 ₽
⬆️ Продажа: 1 LTC → 5794.00 ₽

⬇️ Покупка: 1 USDT TRC20 → 94.38 ₽
⬆️ Продажа: 1 USDT TRC20 → 89.89 ₽""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Купить')
def services_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_btc = types.KeyboardButton('Купить BTC')
    btn_eth = types.KeyboardButton('Купить ETH')
    btn_usdt = types.KeyboardButton('Купить USDT')
    btn_usdc = types.KeyboardButton('Купить USDC')
    btn_ltc = types.KeyboardButton('Купить LTC')
    btn_back = types.KeyboardButton('Назад')
    markup.add(btn_btc, btn_eth, btn_usdt, btn_usdc, btn_ltc, btn_back)
    bot.send_message(message.chat.id, "Выберите услугу:", reply_markup=markup)   

@bot.message_handler(func=lambda message: message.text == 'Купить BTC')
def buy_btc(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Ввести сумму в рублях", callback_data="rub_btc"))
    markup.add(InlineKeyboardButton("Ввести количество BTC", callback_data="btc"))
    
    bot.send_message(message.chat.id, 
                     "Курс обмена: 5609310.00 РУБ - 1 BTC\nМинимальная сумма: 0.00049 BTC\nМаксимальная сумма: 15.05999401 BTC", 
                     reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Купить ETH')
def buy_eth(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Ввести сумму в рублях", callback_data="rub_eth"))
    markup.add(InlineKeyboardButton("Ввести количество ETH", callback_data="eth"))
    
    bot.send_message(message.chat.id, 
                     "Курс обмена: 243251.40 РУБ - 1 ETH\nМинимальная сумма: 0.01 ETH\nМаксимальная сумма: 1000 ETH", 
                     reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Купить LTC')
def buy_ltc(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Ввести сумму в рублях", callback_data="rub_ltc"))
    markup.add(InlineKeyboardButton("Ввести количество LTC", callback_data="ltc"))
    
    bot.send_message(message.chat.id, 
                     "Курс обмена: 6083.70 РУБ - 1 LTC\nМинимальная сумма: 0.1 LTC\nМаксимальная сумма: 1000 LTC", 
                     reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "rub_btc":
        msg = bot.send_message(call.message.chat.id, "Введите количество рублей для обмена:")
        bot.register_next_step_handler(msg, process_rub_amount_btc)
    elif call.data == "btc":
        msg = bot.send_message(call.message.chat.id, "Введите количество BTC для обмена:")
        bot.register_next_step_handler(msg, process_btc_amount)
    elif call.data == "rub_eth":
        msg = bot.send_message(call.message.chat.id, "Введите количество рублей для обмена:")
        bot.register_next_step_handler(msg, process_rub_amount_eth)
    elif call.data == "eth":
        msg = bot.send_message(call.message.chat.id, "Введите количество ETH для обмена:")
        bot.register_next_step_handler(msg, process_eth_amount)
    elif call.data == "rub_ltc":
        msg = bot.send_message(call.message.chat.id, "Введите количество рублей для обмена:")
        bot.register_next_step_handler(msg, process_rub_amount_ltc)
    elif call.data == "ltc":
        msg = bot.send_message(call.message.chat.id, "Введите количество LTC для обмена:")
        bot.register_next_step_handler(msg, process_ltc_amount)

# Обработка ввода суммы в рублях для BTC
def process_rub_amount_btc(message):
    try:
        rub_amount = float(message.text)
        btc_amount = rub_amount / exchange_btc_rate
        bot.send_message(message.chat.id, f"За {rub_amount} рублей вы получите {btc_amount:.8f} BTC.")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

# Обработка ввода суммы в BTC
def process_btc_amount(message):
    try:
        btc_amount = float(message.text)
        rub_amount = btc_amount * exchange_btc_rate
        bot.send_message(message.chat.id, f"За {btc_amount} BTC вам нужно заплатить {rub_amount:.2f} рублей.")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

# Обработка ввода суммы в рублях для ETH
def process_rub_amount_eth(message):
    try:
        rub_amount = float(message.text)
        eth_amount = rub_amount / exchange_eth_rate
        bot.send_message(message.chat.id, f"За {rub_amount} рублей вы получите {eth_amount:.8f} ETH.")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

# Обработка ввода суммы в ETH
def process_eth_amount(message):
    try:
        eth_amount = float(message.text)
        rub_amount = eth_amount * exchange_eth_rate
        bot.send_message(message.chat.id, f"За {eth_amount} ETH вам нужно заплатить {rub_amount:.2f} рублей.")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

# Обработка ввода суммы в рублях для LTC
def process_rub_amount_ltc(message):
    try:
        rub_amount = float(message.text)
        ltc_amount = rub_amount / exchange_ltc_rate
        bot.send_message(message.chat.id, f"За {rub_amount} рублей вы получите {ltc_amount:.8f} LTC.")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

# Обработка ввода суммы в LTC
def process_ltc_amount(message):
    try:
        ltc_amount = float(message.text)
        rub_amount = ltc_amount * exchange_ltc_rate
        bot.send_message(message.chat.id, f"За {ltc_amount} LTC вам нужно заплатить {rub_amount:.2f} рублей.")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")
