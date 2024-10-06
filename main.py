import os
import telebot
from telebot.types import BotCommand

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

commands = [
    BotCommand(command="restart", description="Restart the current game"),
    BotCommand(command="statistics", description="See statistics"),
    BotCommand(command="about", description="About the bot")
]

@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    bot.reply_to(message, "Hi!")

@bot.message_handler(commands=['statistics'])
def send_welcome_message(message):
    bot.reply_to(message, "Hi!")

@bot.message_handler(commands=['about'])
def send_welcome_message(message):
    bot.reply_to(message, "Hi!")


bot.set_my_commands(commands)
bot.infinity_polling()