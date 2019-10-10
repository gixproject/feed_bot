from telebot.types import KeyboardButton, ReplyKeyboardMarkup


markup = ReplyKeyboardMarkup(resize_keyboard=True)
btnMainItem1 = KeyboardButton('IT news')
btnMainItem2 = KeyboardButton('Technologies')
btnMainItem3 = KeyboardButton('Lifehacks')
btnMainItem4 = KeyboardButton('Fun')
markup.row(btnMainItem1, btnMainItem2)
markup.row(btnMainItem3, btnMainItem4)
