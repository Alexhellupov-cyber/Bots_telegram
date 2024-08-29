import telebot
from telebot import types

# Замените 'YOUR_API_TOKEN' на ваш реальный API токен
bot = telebot.TeleBot('7296845868:AAFWvXxzvSeFvN4DEekD9FJDKIZWd_LDoFE')


# Множество для хранения ID пользователей
user_ids = {542079843, 7429348425, 527084141}
user_states = {}
# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Добавляем ID пользователя в множество, если его там еще нет
    user_ids.add(message.chat.id)
    
    # Создаем клавиатуру с кнопкой запроса трансляции геолокации
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_alarm = types.KeyboardButton(text="Транслировать геопозицию", request_location=True)
    keyboard.add(button_alarm)
    
    bot.send_message(message.chat.id, "Нажми 'Транслировать геопозицию' для трансляции геопозиции", reply_markup=keyboard)

# Обработчик получения геолокации
@bot.message_handler(content_types=['location'])
def location(message):
    if message.location:
        latitude = message.location.latitude
        longitude = message.location.longitude
        user_name = message.from_user.first_name
        print(f"Received location from {user_name}: {latitude}, {longitude}")  # Debug print
        
        # Отправляем сообщение всем пользователям из множества
        for user_id in user_ids:
            bot.send_message(user_id, f"Пользователь {user_name} нажал на тревожную кнопку по координатам - широта {latitude}, долгота {longitude}")
            bot.forward_message(user_id, message.chat.id, message.message_id)
            print(f"Forwarded message to {user_id}")  # Debug print

@bot.message_handler(func=lambda message: message.text.lower() == 'admin')
def handle_admin_message(message):
    user_states[message.chat.id] = 'awaiting_password'
    bot.reply_to(message, "введи пас")

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'awaiting_password')
def check_password(message):
    if message.text == '123':
        user_states[message.chat.id] = 'authenticated'
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn1 = types.KeyboardButton('Отправить сообщение всем')
        btn2 = types.KeyboardButton('Назад')
        markup.add(btn1,btn2)
        bot.reply_to(message, "Привет, администратор!", reply_markup=markup)
    else:
        bot.reply_to(message, "Пароль неверный. Попробуйте снова.")

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'authenticated' and message.text == 'Отправить сообщение всем')
def request_broadcast_message(message):
    user_states[message.chat.id] = 'awaiting_broadcast_message'
    bot.reply_to(message, "Введите сообщение, которое хотите отправить всем пользователям.")

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'awaiting_broadcast_message')
def broadcast_message(message):
    if message.text == 'Назад':
        user_states[message.chat.id] = 'authenticated'
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn1 = types.KeyboardButton('Отправить сообщение всем')
        btn2 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2)
        bot.reply_to(message, "Вы вернулись назад.", reply_markup=markup)
    else:
        for user_id in user_ids:
            if user_id != message.chat.id:  # Не отправлять сообщение самому себе
                bot.send_message(user_id, message.text)
        bot.reply_to(message, "Сообщение отправлено всем пользователям.")
        user_states[message.chat.id] = 'authenticated'  # Возвращаем состояние в 'authenticated'

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'awaiting_broadcast_message')
def broadcast_message(message):
    if message.text == 'Назад':
        user_states[message.chat.id] = 'authenticated'
        send_welcome(message)  # Возвращаемся к команде /start
    else:
        for user_id in user_ids:
            if user_id != message.chat.id:  # Не отправлять сообщение самому себе
                bot.send_message(user_id, message.text)
        bot.reply_to(message, "Сообщение отправлено всем пользователям.")
        user_states[message.chat.id] = 'authenticated'  # Возвращаем состояние в 'authenticated'



# Запуск бота
bot.polling(none_stop=True)