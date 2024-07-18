#Telegram Bot
#
#pip install pyTelegramBotAPI


import telebot
from telebot import types
import webbrowser

bot = telebot.TeleBot("Token Bot")


@bot.message_handler(content_types=["audio", "video", "photo"])
def get_avp(message):
    file = open("./pasxalka.jpg", "rb")
    bot.reply_to(message, f"Поздравляю {message.from_user.first_name}, это пасхалка с фото, видео и музыкой")
    bot.send_photo(message.chat.id, file)


@bot.message_handler(commands=["google"])
def site(message):
    webbrowser.open("https://www.google.ru/")
    bot.send_message(message.chat.id, "https://www.google.ru/")


@bot.message_handler(commands=["start"])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Открыть Google в браузере", url="https://www.google.ru/")
    ya_eda = types.InlineKeyboardButton("Открыть Яндекс Еду в браузере", url="https://eda.yandex.ru/")
    markup.row(btn1, ya_eda)
    btn2 = types.InlineKeyboardButton("Открыть Яндекс в браузере", url="https://ya.ru/")
    btn3 = types.InlineKeyboardButton("Открыть Bing в браузере", url="https://www.bing.com/")
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name} это бот на Python cписок команд /help", reply_markup=markup)


@bot.message_handler(commands=["bing"])
def main(message):
    webbrowser.open("https://www.bing.com/")
    bot.send_message(message.chat.id, "https://www.bing.com/")

@bot.message_handler(commands=["yandex", "ya"])
def main(message):
    webbrowser.open("https://ya.ru/")
    bot.send_message(message.chat.id, "https://ya.ru/")


@bot.message_handler(commands=["eda", "yaeda"])
def main(message):
    webbrowser.open("https://eda.yandex.ru/")
    bot.send_message(message.chat.id, "https://eda.yandex.ru/")


@bot.message_handler(commands=["help"])
def main(message):
    bot.send_message(message.chat.id, f"Команды /google - Открыть Google в браузере /create - Разработчик бота /help - Список команд /yandex - Открыть Яндекс в браузере /bing - Открыть Bing в браузере /eda - Открыть Яндекс Еда")



@bot.message_handler(commands=["create"])
def main(message):
    bot.send_message(message.chat.id, f"{message.from_user.first_name}, разработчик Discord qopq1366")



@bot.message_handler()
def info(message):
    if message.text.lower() == "пасхалка":
        file = open("./pasxalka.jpg", "rb")
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, ты нашел пасхалку")
        bot.send_photo(message.chat.id, file)
    
    elif message.text.lower() == "id":
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, твой id:{message.from_user.id} и это мини пасхалка")

    elif message.text.lower() == "гугл":
        webbrowser.open("https://www.google.ru/")
        bot.send_message(message.chat.id, "https://www.google.ru/")
    elif message.text.lower() == "google":
        webbrowser.open("https://www.google.ru/")
        bot.send_message(message.chat.id, "https://www.google.ru/")
    elif message.text.lower() == "яндекс":
        webbrowser.open("https://ya.ru/")
        bot.send_message(message.chat.id, "https://ya.ru/")
    elif message.text.lower() == "yandex":
        webbrowser.open("https://ya.ru/")
        bot.send_message(message.chat.id, "https://ya.ru/")
    elif message.text.lower() == "ya":
        webbrowser.open("https://ya.ru/")
        bot.send_message(message.chat.id, "https://ya.ru/")
        

bot.infinity_polling()