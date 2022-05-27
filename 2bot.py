import telebot
bot = telebot.TeleBot("5393953243:AAEgydRql-P3YNYHY7uBLIxUIXqC3BBsIrQ")

@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}"
    bot.send_message(message.chat.id, mess, parse_mode="html")

bot.polling(none_stop = True)

