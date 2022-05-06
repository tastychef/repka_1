import telebot
bot = telebot.TeleBot('5393953243:AAEgydRql-P3YNYHY7uBLIxUIXqC3BBsIrQ')

@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
