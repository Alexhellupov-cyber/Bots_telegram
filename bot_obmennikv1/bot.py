import telebot
from telebot import types

# Замените 'YOUR_API_KEY' на ваш API ключ от BotFather
bot = telebot.TeleBot('7298626795:AAHSg1ICslDatqnQfHAVZyc5TlRrxMhpzos')


user_states = {}

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
    bot.send_message(message.chat.id, """🔄 Курс обмена: 5572455.00 РУБ → 1 BTC
💵 Минимальная сумма: 0.00049 BTC
💵 Максимальная сумма: 15.14530008 BTC

Введите сумму в рублях для покупки BTC:""")
    user_states[message.chat.id] = 'buy_btc'

@bot.message_handler(func=lambda message: message.text == 'Купить ETH')
def buy_eth(message):
    bot.send_message(message.chat.id, """🔄 Курс обмена: 243516.00 РУБ → 1 ETH
💵 Минимальная сумма: 0.01125 ETH
💵 Максимальная сумма: 217.54699897 ETH

Введите сумму в рублях для покупки ETH:""")
    user_states[message.chat.id] = 'buy_eth'

@bot.message_handler(func=lambda message: message.text == 'Купить LTC')
def buy_ltc(message):
    bot.send_message(message.chat.id, """🔄 Курс обмена: 6091.05 РУБ → 1 LTC
💵 Минимальная сумма: 0.44975 LTC
💵 Максимальная сумма: 1629.63282 LTC

Введите сумму в рублях для покупки LTC:""")
    user_states[message.chat.id] = 'buy_ltc'

@bot.message_handler(func=lambda message: message.text == 'Купить USDC')
def buy_usdc(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton('USDC TRC20')
    btn_2 = types.KeyboardButton('USDC ERC20')
    btn_3 = types.KeyboardButton('USDC BEP20')
    btn_4 = types.KeyboardButton('USDC Solana')
    btn_5 = types.KeyboardButton('USDC Arbitrum')
    btn_back = types.KeyboardButton('Назад')
    markup.add(btn_1, btn_2, btn_3, btn_4, btn_5, btn_back)
    bot.send_message(message.chat.id, "Выберите сеть отправки:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Купить USDT')
def buy_usdt(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton('USDT TRC20')
    btn_2 = types.KeyboardButton('USDT ERC20')
    btn_3 = types.KeyboardButton('USDT BEP20')
    btn_4 = types.KeyboardButton('USDT Solana')
    btn_5 = types.KeyboardButton('USDT Arbitrum')
    btn_back = types.KeyboardButton('Назад')
    markup.add(btn_1, btn_2, btn_3, btn_4, btn_5, btn_back)
    bot.send_message(message.chat.id, "Выберите сеть отправки:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.isdigit())
def handle_amount(message):
    amount_rub = float(message.text)
    state = user_states.get(message.chat.id)

    if state == 'buy_btc':
        exchange_rate = 5572455.00
        amount_btc = amount_rub / exchange_rate
        bot.send_message(message.chat.id, f"Вы получите {amount_btc:.8f} BTC за {amount_rub} RUB")
    elif state == 'buy_eth':
        exchange_rate = 243251.40
        amount_eth = amount_rub / exchange_rate
        bot.send_message(message.chat.id, f"Вы получите {amount_eth:.8f} ETH за {amount_rub} RUB")
    elif state == 'buy_ltc':
        exchange_rate = 6091.05
        amount_ltc = amount_rub / exchange_rate
        bot.send_message(message.chat.id, f"Вы получите {amount_ltc:.8f} LTC за {amount_rub} RUB")






@bot.message_handler(func=lambda message: message.text == 'USDT Arbitrum')
def buy_usdt_arbitrum(message):
    bot.send_message(message.chat.id, """
🔄 Курс обмена: 94.38 РУБ → 1 USDT Arbitrum
💵 Минимальная сумма: 29.0 USDT Arbitrum
💵 Максимальная сумма: 127416.8 USDT Arbitrum

Введите сумму в рублях для покупки USDT Arbitrum:""")
    user_states[message.chat.id] = 'buy_usdt_arbitrum'
    print(f"User state set to 'buy_usdt_arbitrum' for user {message.chat.id}")

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'buy_usdt_arbitrum')
def calculate_usdt_arbitrum(message):
    print(f"calculate_usdt_arbitrum called for user {message.chat.id} with message: {message.text}")
    try:
        rub_amount = float(message.text)
        print(f"rub_amount: {rub_amount}")
        usdt_amount = rub_amount / 94.38
        print(f"usdt_amount: {usdt_amount}")
        bot.send_message(message.chat.id, f"Вы получите {usdt_amount:.2f} USDT Arbitrum. Пожалуйста, введите адрес вашего кошелька:")
        user_states[message.chat.id] = 'enter_wallet_address'
        print(f"User state set to 'enter_wallet_address' for user {message.chat.id}")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректную сумму в рублях.")
        print(f"Invalid amount entered by user {message.chat.id}")

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'enter_wallet_address')
def get_wallet_address(message):
    print(f"get_wallet_address called for user {message.chat.id} with message: {message.text}")
    wallet_address = message.text
    # Здесь можно добавить логику для обработки адреса кошелька
    bot.send_message(message.chat.id, f"Ваш адрес кошелька: {wallet_address}. Спасибо за использование нашего сервиса!")
    user_states[message.chat.id] = None
    print(f"Wallet address received from user {message.chat.id}: {wallet_address}")

print("Bot is running...")
bot.polling()
print("Polling started...")













@bot.message_handler(func=lambda message: message.text == 'USDT Solana')
def buy_usdt_solana(message):
    bot.send_message(message.chat.id, """
🔄 Курс обмена: 94.38 РУБ → 1 USDT Solana
💵 Минимальная сумма: 29.0 USDT Solana
💵 Максимальная сумма: 127416.8 USDT Solana

Введите сумму в рублях для покупки USDT Solana:""")
    user_states[message.chat.id] = 'buy_usdt_solana'

@bot.message_handler(func=lambda message: message.text == 'USDT TRC20')
def buy_usdt_trc20(message):
    bot.send_message(message.chat.id, """
🔄 Курс обмена: 94.38 РУБ → 1 USDT TRC-20
💵 Минимальная сумма: 29.0 USDT TRC-20
💵 Максимальная сумма: 127416.8 USDT TRC-20

Введите сумму в рублях для покупки USDT TRC20:""")
    user_states[message.chat.id] = 'buy_usdt_trc20'

@bot.message_handler(func=lambda message: message.text.isdigit())
def handle_usdt_amount(message):
    amount_rub = float(message.text)
    exchange_rate = 94.38  # Пример курса обмена
    state = user_states.get(message.chat.id)

    if state == 'buy_usdt_arbitrum':
        amount_usdt = amount_rub / exchange_rate
        bot.send_message(message.chat.id, f"Вы получите {amount_usdt:.8f} USDT Arbitrum за {amount_rub} RUB")
    elif state == 'buy_usdt_solana':
        amount_usdt = amount_rub / exchange_rate
        bot.send_message(message.chat.id, f"Вы получите {amount_usdt:.8f} USDT Solana за {amount_rub} RUB")
    elif state == 'buy_usdt_trc20':
        amount_usdt = amount_rub / exchange_rate
        bot.send_message(message.chat.id, f"Вы получите {amount_usdt:.8f} USDT TRC20 за {amount_rub} RUB")



@bot.message_handler(func=lambda message: message.text == 'USDC Arbitrum')
def buy_usdc_arbitrum(message):
    bot.send_message(message.chat.id, """
🔄 Курс обмена: 94.38 РУБ → 1 USDC Arbitrum
💵 Минимальная сумма: 29.0 USDC Arbitrum
💵 Максимальная сумма: 127416.8 USDC Arbitrum

Введите сумму в рублях для покупки USDC Arbitrum:""")
    user_states[message.chat.id] = 'buy_usdc_arbitrum'

@bot.message_handler(func=lambda message: message.text == 'USDC Solana')
def buy_usdc_solana(message):
    bot.send_message(message.chat.id, """
🔄 Курс обмена: 94.38 РУБ → 1 USDC Solana
💵 Минимальная сумма: 29.0 USDC Solana
💵 Максимальная сумма: 127416.8 USDC Solana

Введите сумму в рублях для покупки USDC Solana:""")
    user_states[message.chat.id] = 'buy_usdc_solana'

@bot.message_handler(func=lambda message: message.text == 'USDC TRC20')
def buy_usdc_trc20(message):
    bot.send_message(message.chat.id, """
🔄 Курс обмена: 94.38 РУБ → 1 USDC TRC-20
💵 Минимальная сумма: 29.0 USDC TRC-20
💵 Максимальная сумма: 127416.8 USDC TRC-20

Введите сумму в рублях для покупки USDC TRC20:""")
    user_states[message.chat.id] = 'buy_usdc_trc20'

@bot.message_handler(func=lambda message: message.text == 'USDC ERC20')
def buy_usdc_erc20(message):
    bot.send_message(message.chat.id, """
🔄 Курс обмена: 94.38 РУБ → 1 USDC ERC-20
💵 Минимальная сумма: 29.0 USDC ERC-20
💵 Максимальная сумма: 127416.8 USDC ERC-20

Введите сумму в рублях для покупки USDC ERC-20:""")
    user_states[message.chat.id] = 'buy_usdc_erc20'

@bot.message_handler(func=lambda message: message.text == 'USDC BEP20')
def buy_usdc_bep20(message):
    bot.send_message(message.chat.id, """
🔄 Курс обмена: 94.38 РУБ → 1 USDC BEP-20
💵 Минимальная сумма: 29.0 USDC BEP-20
💵 Максимальная сумма: 127416.8 USDC BEP-20

Введите сумму в рублях для покупки USDC BEP-20:""")
    user_states[message.chat.id] = 'buy_usdc_bep20'

@bot.message_handler(func=lambda message: message.text.isdigit())
def handle_amount(message):
    amount_rub = float(message.text)
    exchange_rate = 94.38  # Пример курса обмена
    state = user_states.get(message.chat.id)

    if state == 'buy_usdc_arbitrum':
        amount_usdc = amount_rub / exchange_rate
        bot.send_message(message.chat.id, f"Вы получите {amount_usdc:.8f} USDC Arbitrum за {amount_rub} RUB")
    elif state == 'buy_usdc_solana':
        amount_usdc = amount_rub / exchange_rate
        bot.send_message(message.chat.id, f"Вы получите {amount_usdc:.8f} USDC Solana за {amount_rub} RUB")
    elif state == 'buy_usdc_trc20':
        amount_usdc = amount_rub / exchange_rate
        bot.send_message(message.chat.id, f"Вы получите {amount_usdc:.8f} USDC TRC20 за {amount_rub} RUB")
    elif state == 'buy_usdc_erc20':
        amount_usdc = amount_rub / exchange_rate
        bot.send_message(message.chat.id, f"Вы получите {amount_usdc:.8f} USDC ERC20 за {amount_rub} RUB")
    elif state == 'buy_usdc_bep20':
        amount_usdc = amount_rub / exchange_rate
        bot.send_message(message.chat.id, f"Вы получите {amount_usdc:.8f} USDC BEP20 за {amount_rub} RUB")

@bot.message_handler(func=lambda message: message.text == 'Назад')
def back_to_main_menu(message):
    send_welcome(message)



# Запуск бота
bot.polling()
