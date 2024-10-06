import os
import telebot
from telebot.types import BotCommand

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

commands = [
    BotCommand(command="start", description="Start Telegram Bot")
]

@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    bot.reply_to(message, "Hi!")

bot.set_my_commands(commands)
bot.infinity_polling()