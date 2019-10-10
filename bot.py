import telebot

import urls
from menu import markup
from parse import parse_rss


TOKEN = 'your_token'
bot = telebot.TeleBot(TOKEN)

TEXT_GREETINGS = '{}\n{}'.format(
    'Hi!', 'Now you can read the latest IT, Tech news and about another interesting things.')

TEXT_WARNING = 'Please, use the menu.'


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, TEXT_GREETINGS,
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text_handler(call):
    text = call.text
    if text == 'IT news':
        parse_rss(bot, call, urls.it)
    elif text == 'Technologies':
        parse_rss(bot, call, urls.tech)
    elif text == 'Lifehacks':
        parse_rss(bot, call, urls.lifehacks)
    elif text == 'Fun':
        parse_rss(bot, call, urls.fun)
    else:
        bot.send_message(call.chat.id, TEXT_WARNING)


if __name__ == '__main__':
    bot.polling(none_stop=True)
