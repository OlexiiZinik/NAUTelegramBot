import telebot
from telebot import types
from loguru import logger

import settings
from Bot.UserManager import UserManager

@logger.catch
def Bot():
    UM = UserManager()

    @bot.message_handler(commands = ['start'])
    def start_func(message):
        logger.debug(f'{message.from_user.id} {message.from_user.first_name} started the bot')
        UM.AddUser(message.from_user.id, message.from_user.username,  message.from_user.first_name, message.from_user.last_name)
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}, i am NAUBOT')
    
    @bot.message_handler(content_types = ['text'])
    def echo(message):
        logger.debug(f'{message.from_user.id} {message.from_user.first_name} {message.text}')
        res = int(message.text)
        bot.send_message(message.chat.id, f'{res**2}')        

if __name__ == '__main__':
    bot = telebot.TeleBot(settings.BOT_TOKEN)
    #створюється папка з логами(внесена в .gitignore)
    logger.add('logs/debug.log', format = '{time} {level} {message}', rotation = '100 KB', compression = 'zip')
    Bot()
    bot.polling(True)
    
