from coins import get_price
import telebot


TOKEN = '575819178:AAEIDmSjlvLw9XINaUcn16iy9EQwj6R48-4'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['price_btc'])
def print_price(message):
    bot.reply_to(message, get_price())

bot.polling(timeout=60)

