import telebot

bot = telebot.TeleBot('5393953243:AAEgydRql-P3YNYHY7uBLIxUIXqC3BBsIrQ')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Проголодался, Толстячелллло!? Ща сообразим')
@bot.message_handler(content_types=['text', 'document', 'audio'])
def handle_text(message):
    bot.send_message(message.chat.id, "Понедельник\nБудешь рыбу или мясо?")

    if message.text == "Рыбу" or "Рыба":
        bot.send_message(message.from_user.id, "Припущенный сибас с сезонными овощами подойдет?")
        if message.text == "да":
            print("ШИК! Крис приготовит")
        else:
            print("как насчет Дорадо напару?")
            if message.text == "да":
                print("отлично. я рад, что попал!")
    elif message.text == "Мясо" or "мясо":
        bot.send_message(message.from_user.id, "Рульку давай!")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)
