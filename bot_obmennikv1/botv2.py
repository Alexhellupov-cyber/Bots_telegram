import telebot
import datetime
import os

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types

# Замените 'YOUR_API_KEY' на ваш API ключ от BotFather
bot = telebot.TeleBot('7298626795:AAHSg1ICslDatqnQfHAVZyc5TlRrxMhpzos')

user_states = {}

# Курс обмена
exchange_btc_rate = 5577915.00
exchange_eth_rate = 243251.40
exchange_ltc_rate = 6083.70
exchange_usdt_rate = 94.38 
exchange_usdc_rate = 94.38 

# Минимальная длина адреса для каждой криптовалюты
address_lengths = {
    "BTC": 34,
    "ETH": 42,
    "LTC": 34,
    "USDT TRC-20": 34,
    "USDT ERC-20": 42,
    "USDT BEP20": 34,
    "USDT Solana": 44,
    "USDT Arbitrum": 42,
    "USDC TRC-20": 34,
    "USDC ERC-20": 42,
    "USDC BEP20": 34,
    "USDC Solana": 44,
    "USDC Arbitrum": 42
}

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
⬆️ Продажа: 1 USDT TRC20 → 89.89 ₽

⬇️ Покупка: 1 USDC TRC20 → 94.38 ₽
⬆️ Продажа: 1 USDC TRC20 → 89.89 ₽""", reply_markup=markup)

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

@bot.message_handler(func=lambda message: message.text == 'Купить USDT')
def buy_usdt(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("USDT TRC-20", callback_data="usdt_trc20"))
    markup.add(InlineKeyboardButton("USDT ERC-20", callback_data="usdt_erc20"))
    markup.add(InlineKeyboardButton("USDT BEP20", callback_data="usdt_bep20"))
    markup.add(InlineKeyboardButton("USDT Solana", callback_data="usdt_solana"))
    markup.add(InlineKeyboardButton("USDT Arbitrum", callback_data="usdt_arbitrum"))
    
    bot.send_message(message.chat.id, "Выберите сеть обмена:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Купить USDC')
def buy_usdc(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("USDC TRC-20", callback_data="usdc_trc20"))
    markup.add(InlineKeyboardButton("USDC ERC-20", callback_data="usdc_erc20"))
    markup.add(InlineKeyboardButton("USDC BEP20", callback_data="usdc_bep20"))
    markup.add(InlineKeyboardButton("USDC Solana", callback_data="usdc_solana"))
    markup.add(InlineKeyboardButton("USDC Arbitrum", callback_data="usdc_arbitrum"))
    
    bot.send_message(message.chat.id, "Выберите сеть обмена:", reply_markup=markup)

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
    elif call.data == "usdt_trc20":
        bot.send_message(call.message.chat.id, "Вы выбрали сеть USDT TRC-20.")
        msg = bot.send_message(call.message.chat.id, "Введите количество рублей для обмена USDT TRC-20:")
        bot.register_next_step_handler(msg, process_rub_amount_usdt_trc20)
    elif call.data == "usdt_erc20":
        bot.send_message(call.message.chat.id, "Вы выбрали сеть USDT ERC-20.")
        msg = bot.send_message(call.message.chat.id, "Введите количество рублей для обмена USDT ERC-20:")
        bot.register_next_step_handler(msg, process_rub_amount_usdt_erc20)
    elif call.data == "usdt_bep20":
        bot.send_message(call.message.chat.id, "Вы выбрали сеть USDT BEP20.")
        msg = bot.send_message(call.message.chat.id, "Введите количество рублей для обмена USDT BEP20:")
        bot.register_next_step_handler(msg, process_rub_amount_usdt_bep20)
    elif call.data == "usdt_solana":
        bot.send_message(call.message.chat.id, "Вы выбрали сеть USDT Solana.")
        msg = bot.send_message(call.message.chat.id, "Введите количество рублей для обмена USDT Solana:")
        bot.register_next_step_handler(msg, process_rub_amount_usdt_solana)
    elif call.data == "usdt_arbitrum":
        bot.send_message(call.message.chat.id, "Вы выбрали сеть USDT Arbitrum.")
        msg = bot.send_message(call.message.chat.id, "Введите количество рублей для обмена USDT Arbitrum:")
        bot.register_next_step_handler(msg, process_rub_amount_usdt_arbitrum)
    elif call.data == "usdc_trc20":
        bot.send_message(call.message.chat.id, "Вы выбрали сеть USDC TRC-20.")
        msg = bot.send_message(call.message.chat.id, "Введите количество рублей для обмена USDC TRC-20:")
        bot.register_next_step_handler(msg, process_rub_amount_usdc_trc20)
    elif call.data == "usdc_erc20":
        bot.send_message(call.message.chat.id, "Вы выбрали сеть USDC ERC-20.")
        msg = bot.send_message(call.message.chat.id, "Введите количество рублей для обмена USDC ERC-20:")
        bot.register_next_step_handler(msg, process_rub_amount_usdc_erc20)
    elif call.data == "usdc_bep20":
        bot.send_message(call.message.chat.id, "Вы выбрали сеть USDC BEP20.")
        msg = bot.send_message(call.message.chat.id, "Введите количество рублей для обмена USDC BEP20:")
        bot.register_next_step_handler(msg, process_rub_amount_usdc_bep20)
    elif call.data == "usdc_solana":
        bot.send_message(call.message.chat.id, "Вы выбрали сеть USDC Solana.")
        msg = bot.send_message(call.message.chat.id, "Введите количество рублей для обмена USDC Solana:")
        bot.register_next_step_handler(msg, process_rub_amount_usdc_solana)
    elif call.data == "usdc_arbitrum":
        bot.send_message(call.message.chat.id, "Вы выбрали сеть USDC Arbitrum.")
        msg = bot.send_message(call.message.chat.id, "Введите количество рублей для обмена USDC Arbitrum:")
        bot.register_next_step_handler(msg, process_rub_amount_usdc_arbitrum)

# Обработка ввода суммы в рублях для BTC
def process_rub_amount_btc(message):
    try:
        rub_amount = float(message.text)
        btc_amount = rub_amount / exchange_btc_rate
        bot.send_message(message.chat.id, f"За {rub_amount} рублей вы получите {btc_amount:.8f} BTC.")
        request_crypto_address(message, "BTC")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

# Обработка ввода суммы в BTC
def process_btc_amount(message):
    try:
        btc_amount = float(message.text)
        rub_amount = btc_amount * exchange_btc_rate
        bot.send_message(message.chat.id, f"За {btc_amount} BTC вам нужно заплатить {rub_amount:.2f} рублей.")
        request_crypto_address(message, "BTC")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

# Обработка ввода суммы в рублях для ETH
def process_rub_amount_eth(message):
    try:
        rub_amount = float(message.text)
        eth_amount = rub_amount / exchange_eth_rate
        bot.send_message(message.chat.id, f"За {rub_amount} рублей вы получите {eth_amount:.8f} ETH.")
        request_crypto_address(message, "ETH")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

# Обработка ввода суммы в ETH
def process_eth_amount(message):
    try:
        eth_amount = float(message.text)
        rub_amount = eth_amount * exchange_eth_rate
        bot.send_message(message.chat.id, f"За {eth_amount} ETH вам нужно заплатить {rub_amount:.2f} рублей.")
        request_crypto_address(message, "ETH")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

# Обработка ввода суммы в рублях для LTC
def process_rub_amount_ltc(message):
    try:
        rub_amount = float(message.text)
        ltc_amount = rub_amount / exchange_ltc_rate
        bot.send_message(message.chat.id, f"За {rub_amount} рублей вы получите {ltc_amount:.8f} LTC.")
        request_crypto_address(message, "LTC")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

# Обработка ввода суммы в LTC
def process_ltc_amount(message):
    try:
        ltc_amount = float(message.text)
        rub_amount = ltc_amount * exchange_ltc_rate
        bot.send_message(message.chat.id, f"За {ltc_amount} LTC вам нужно заплатить {rub_amount:.2f} рублей.")
        request_crypto_address(message, "LTC")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

# Обработка ввода суммы в рублях для USDC BEP20
def process_rub_amount_usdc_bep20(message):
    try:
        rub_amount = float(message.text)
        usdc_amount = rub_amount / exchange_usdc_rate
        bot.send_message(message.chat.id, f"За {rub_amount} рублей вы получите {usdc_amount:.8f} USDC BEP20.")
        request_crypto_address(message, "USDC BEP20")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

# Обработка ввода суммы в рублях для USDC Solana
def process_rub_amount_usdc_solana(message):
    try:
        rub_amount = float(message.text)
        usdc_amount = rub_amount / exchange_usdc_rate
        bot.send_message(message.chat.id, f"За {rub_amount} рублей вы получите {usdc_amount:.8f} USDC Solana.")
        request_crypto_address(message, "USDC Solana")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

# Обработка ввода суммы в рублях для USDC Arbitrum
def process_rub_amount_usdc_arbitrum(message):
    try:
        rub_amount = float(message.text)
        usdc_amount = rub_amount / exchange_usdc_rate
        bot.send_message(message.chat.id, f"За {rub_amount} рублей вы получите {usdc_amount:.8f} USDC Arbitrum.")
        request_crypto_address(message, "USDC Arbitrum")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

def request_crypto_address(message, crypto_name):
    msg = bot.send_message(message.chat.id, f"💬 Укажите Ваш адрес {crypto_name} для зачисления:")
    bot.register_next_step_handler(msg, process_crypto_address, crypto_name)

def process_crypto_address(message, crypto_name):
    address = message.text
    if len(address) == address_lengths[crypto_name]:
        bot.send_message(message.chat.id, f"Ваш адрес для зачисления {crypto_name}: {address}")
    else:
        bot.send_message(message.chat.id, f"Ошибка: адрес {crypto_name} должен содержать {address_lengths[crypto_name]} символов. Пожалуйста, введите корректный адрес.")
        request_crypto_address(message, crypto_name)

@bot.message_handler(func=lambda message: message.text == 'Назад')
def back_to_main_menu(message):
    send_welcome(message)


def create_exchange_request(username, user_id, amount, crypto_address):
    try:
        # Получаем текущее время
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Создаем уникальный номер заказа
        order_id = f"order_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # Формируем содержимое файла
        content = (
            f"Время создания заявки: {current_time}\n"
            f"Имя пользователя: {username}\n"
            f"ID пользователя: {user_id}\n"
            f"Сумма/количество криптовалюты: {amount}\n"
            f"Адрес кошелька: {crypto_address}\n"
        )
        
        # Определяем абсолютный путь для файла
        file_path = os.path.join(os.getcwd(), f"{order_id}.txt")
        
        # Создаем файл с уникальным именем
        with open(file_path, "w") as file:
            file.write(content)
        
        print(f"Заявка {order_id} успешно создана! Файл сохранен по пути: {file_path}")
    
    except Exception as e:
        print(f"Произошла ошибка при создании файла: {e}")

# Пример использования функции
create_exchange_request("Ivan", 123456, "0.5 BTC", "3Mfz7JdiPxTrA8HbMhQiKKfqkYrHbxkWPM")

print("Bot is running...")
# Запуск бота
bot.polling()
print("Bot is LAUNCHED")
