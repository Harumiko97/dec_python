import telebot

SECRET_TOKEN = '6742420165:AAHeJnbcCGMNMbiM8wK2PaMIYk1UHFpdUbE'

bot = telebot.TeleBot(SECRET_TOKEN)


@bot.message_handler(commands=['start', ])
def handle_start(message):
    bot.reply_to(message, 'Hello from Prog Academy')


if __name__ == "__main__":
    bot.polling()