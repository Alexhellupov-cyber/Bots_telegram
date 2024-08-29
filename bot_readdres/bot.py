import telebot

# Замените 'YOUR_API_KEY' на ваш API ключ от BotFather
bot = telebot.TeleBot('7075938431:AAFT-n2dC0BSpn1Keqp4EfuIS_f-QHM9G7o')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! вот ссылка на группу https://t.me/order_armv")

# Запуск бота
bot.polling()
