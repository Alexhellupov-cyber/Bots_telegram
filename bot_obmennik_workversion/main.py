# -*- coding: utf-8 -*-
import telebot
import requests
import json
import random
import config
import merchant
import time
import threading
import schedule
from telebot import types

bot = telebot.TeleBot(config.token)

otdaet = ''
poluchaet = ''
summ = ''
rekvezit = ''
user_language = {}  # Словарь для хранения языка пользователя

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def start_language_selection(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button1 = types.KeyboardButton('Русский')
    button2 = types.KeyboardButton('English')
    markup.add(button1, button2)
    msg = bot.send_message(message.chat.id, "🗣 Выберите язык / Choose a language:", reply_markup=markup)
    bot.register_next_step_handler(msg, set_language)

@bot.message_handler(commands=['start'])
def set_language(message):
    global user_language
    if message.text == 'Русский':
        user_language[message.from_user.id] = 'ru'
        language_prefix = "Русский"
    elif message.text == 'English':
        user_language[message.from_user.id] = 'en'
        language_prefix = "English"
    else:
        bot.send_message(message.chat.id, "❌ Пожалуйста, выберите язык из предложенных вариантов.")
        return start_language_selection(message)
    
    # Отправляем приветственное сообщение
    welcome_message = (
        f"✌️ Приветствуем Вас, {message.from_user.first_name} 🟩.\n"
        "Changer - это моментальный бот обмена криптовалют.\n"
        "Приступим к обменам!" if user_language[message.from_user.id] == 'ru' else
        f"✌️ Welcome, {message.from_user.first_name} 🟩.\n"
        "Changer is an instant cryptocurrency exchange bot.\n"
        "To start exchanging, send me /exchange"
    )
    bot.send_message(message.chat.id, welcome_message)
    
    # Запускаем выбор валюты
    start_exchange(message)

# Функция для начала обмена
def start_exchange(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button1 = types.KeyboardButton('BTC')
    button2 = types.KeyboardButton('USDT')
    button3 = types.KeyboardButton('ETH')
    button4 = types.KeyboardButton('NEO')
    button6 = types.KeyboardButton('DOGE')
    button7 = types.KeyboardButton('LTC')
    button13 = types.KeyboardButton('Поддержка/Support')
    markup.add(button1, button2, button3, button4, button6, button7, button13)
    msg = bot.send_message(message.chat.id, get_text(message.from_user.id, 
        "💸 Укажите валюту, которую хотите ПРОДАТЬ:", 
        "💸 Specify the currency you want to SELL:"), 
        reply_markup=markup
    )
    bot.register_next_step_handler(msg, order_2)

def get_text(user_id, ru_text, en_text):
    lang = user_language.get(user_id, 'ru')
    return ru_text if lang == 'ru' else en_text

def order_2(message):
    global otdaet
    otdaet = message.text
    if message.text == 'Поддержка':
        bot.send_message(message.chat.id, get_text(message.from_user.id, "📞 Обратитесь к менеджеру @elison_smm", "📞 Contact the manager @elison_smm"))
        return

    markup1 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button1 = types.KeyboardButton('USD')
    button2 = types.KeyboardButton('EUR')
    button3 = types.KeyboardButton('RUB')
    button4 = types.KeyboardButton('KZT')
    button6 = types.KeyboardButton('AED')
    button7 = types.KeyboardButton('CHA')
    button13 = types.KeyboardButton('Поддержка/Support')
    markup1.add(button1, button2, button3, button4, button6, button7, button13)
    msg = bot.send_message(message.chat.id, get_text(message.from_user.id, "🤑 Теперь выберите валюту ПОЛУЧИТЬ:", "🤑 Now select the currency to RECEIVE:"), reply_markup=markup1)
    bot.register_next_step_handler(msg, order_3)

def order_3(message):
    global poluchaet
    poluchaet = message.text
    url = f"https://min-api.cryptocompare.com/data/price?fsym={otdaet}&tsyms={poluchaet}"
    try:
        j = requests.get(url)
        data = json.loads(j.text)
        price = data[poluchaet]
        
        # Применение комиссии
        token_comission = float(merchant.comission[otdaet])
        adjusted_price = price * (1 + token_comission / 100)
        
        coin_limit = merchant.limits[otdaet]
        bot.send_message(message.chat.id, get_text(message.from_user.id, 
            f'📥 Обмен: {otdaet} на {poluchaet}\n📈 Курс обмена: 1 {otdaet} = {adjusted_price} {poluchaet}\n👇 {coin_limit}:\n', 
            f'📥 Exchange: {otdaet} to {poluchaet}\n📈 Exchange rate: 1 {otdaet} = {adjusted_price} {poluchaet}\n👇 {coin_limit}:\n'), parse_mode="Html")
        bot.register_next_step_handler(message, order_4)
    except Exception as e:
        bot.send_message(message.chat.id, get_text(message.from_user.id, f'❌ Ошибка при получении данных: {str(e)}', f'❌ Error retrieving data: {str(e)}'))

def order_4(message):
    global summ
    if isfloat(message.text):
        summ = float(message.text)
        bot.send_message(message.chat.id, get_text(message.from_user.id, '👇 Укажите реквизиты получаемой валюты:', '👇 Provide receiving currency details:'), parse_mode="Html")
        bot.register_next_step_handler(message, order_5)
    else:
        bot.send_message(message.chat.id, get_text(message.from_user.id, '❌ Пожалуйста, введите корректное число.', '❌ Please enter a valid number.'))
        bot.register_next_step_handler(message, order_4)

def order_5(message):
    global rekvezit
    rekvezit = message.text
    url = f"https://min-api.cryptocompare.com/data/price?fsym={otdaet}&tsyms={poluchaet}"
    try:
        j = requests.get(url)
        data = json.loads(j.text)
        price = data[poluchaet]
        
        # Применение комиссии
        token_comission = float(merchant.comission[otdaet])
        adjusted_price = price * (1 + token_comission / 100)
        
        podshet = summ * adjusted_price
        token_discount = float(merchant.discount[poluchaet])
        calculate1 = (podshet * token_discount) / 100
        calculate2 = podshet - calculate1
        calculate3 = calculate2 + token_comission
        token_coin = merchant.pay[otdaet]
        
        user_lang = user_language.get(message.from_user.id, 'ru')
        language_prefix = "Русский" if user_lang == 'ru' else "English"
        
        confirmation_message = (
            f'📥 Обмен: {otdaet} на {poluchaet}\n'
            f'📥 Отдаете: {summ} {otdaet}, получаете: {calculate3} {poluchaet}\n'
            f'💳 Реквизиты для получения (номер кошелька): {rekvezit}\n'
            f'📈 Курс обмена: 1 {otdaet} = {adjusted_price} {poluchaet}\n'
            f'Переведите на этот счёт {summ} {otdaet}\n'
            f'{token_coin}\n'
            f'🔄 Ожидайте подтверждения обмена' if user_lang == 'ru' else
            f'📥 Exchange: {otdaet} to {poluchaet}\n'
            f'📥 You send: {summ} {otdaet}, you receive: {calculate3} {poluchaet}\n'
            f'💳 Receiving details (wallet number): {rekvezit}\n'
            f'📈 Exchange rate: 1 {otdaet} = {adjusted_price} {poluchaet}\n'
            f'Transfer {summ} {otdaet} to this account\n'
            f'{token_coin}\n'
            f'🔄 Awaiting exchange confirmation'
        )
        
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text=get_text(message.from_user.id, "✅ Оплатил", "✅ Paid"), callback_data="accept")
        button2 = types.InlineKeyboardButton(text=get_text(message.from_user.id, "❌ Отказаться", "❌ Cancel"), callback_data="cancel")
        keyboard.add(button1, button2)
        
        bot.send_message(message.chat.id, confirmation_message, reply_markup=keyboard, parse_mode="Html")
        
        # Сообщение для администраторов
        admin_message = (
            f'💵 Пользователь {message.from_user.username} ({message.from_user.id}) \n подтвердил выбор языка: {language_prefix}\n'
            f'📥 Обмен: {otdaet} на {poluchaet}\n'
            f'📥 Отдаете: {summ} {otdaet}, получаете: {calculate3} {poluchaet}\n'
            f'💳 Реквизиты для получения (номер кошелька): {rekvezit}\n'
            f'📈 Курс обмена: 1 {otdaet} = {adjusted_price} {poluchaet}\n'
            f'Переведит на этот счёт {summ} {otdaet}\n'
            f'{token_coin}\n'
        )
        
        for user_number in range(len(config.adminid)):
            chat_id = config.adminid[user_number]
            if chat_id:
                bot.send_message(chat_id=chat_id, text=admin_message)
            else:
                print("Ошибка: chat_id не найден")
    except Exception as e:
        bot.send_message(message.chat.id, get_text(message.from_user.id, f'❌ Ошибка при обработке запроса: {str(e)}', f'❌ Error processing request: {str(e)}'))

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    message = call.message
    user_name = call.from_user.first_name  # Получение имени пользователя
    if call.message:
        if call.data == "accept":
            bot.send_message(message.chat.id, get_text(call.from_user.id, "✅ Вы подтвердили оплату.\n Денежные средства зачислятся в течении 5 - 15 минут, в зависимости от загруженности сайта.\n Что-бы сделать ещё один обмен введите /exchange", "✅ You confirmed the payment.\n Funds will be credited within 5 - 15 minutes, depending on website load.\n To make another exchange, type /exchange"))
            notify_admins_payment_accepted(user_name, message.chat.id)
        elif call.data == "cancel":
            bot.send_message(message.chat.id, get_text(call.from_user.id, "❌ Вы отменили оплату.\n Что-бы сделать ещё один обмен введите /exchange", "❌ You canceled the payment.\n To make another exchange, type /exchange"))
            notify_admins_payment_canceled(user_name, message.chat.id)

def notify_admins_payment_accepted(user_name, user_chat_id):
    for admin_id in config.adminid:
        bot.send_message(chat_id=admin_id, text=f'💵 Пользователь {user_name} ({user_chat_id}) подтвердил оплату. Ждите зачисления средств.')

def notify_admins_payment_canceled(user_name, user_chat_id):
    for admin_id in config.adminid:
        bot.send_message(chat_id=admin_id, text=f'❌ Пользователь {user_name} ({user_chat_id}) отменил оплату.')

def notify_admins_bot_started():
    for admin_id in config.adminid:
        bot.send_message(chat_id=admin_id, text="🚀 Бот успешно запущен и работает!")
        	
def notify_admins_restart_in_5_minutes():
    for admin_id in config.adminid:
        bot.send_message(chat_id=admin_id, text="Бот работает")

def run_scheduled_tasks():
    schedule.every().hour.at(":00").do(notify_admins_restart_in_5_minutes)
    while True:
        schedule.run_pending()
        time.sleep(1)

def run_bot():
    print('10%')
    time.sleep(0.3)
    print('20%')
    time.sleep(0.3)
    print('30%')
    time.sleep(0.3)
    print('40%')
    time.sleep(0.3)
    print('50%')
    time.sleep(0.3)
    print('60%')
    time.sleep(0.3)
    print('70%')
    time.sleep(0.3)
    print('80%')
    time.sleep(0.3)
    print('90%')
    time.sleep(0.3)
    print('100%')
    time.sleep(0.3)
    print('BOT START WORK')
    notify_admins_bot_started()
    bot.polling(none_stop=True)

if __name__ == "__main__":
    threading.Thread(target=run_scheduled_tasks, daemon=True).start()
    run_bot()
