import telebot
import random 
from env import TOKEN
bot = telebot.TeleBot(TOKEN)
keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('Да')
button2 = telebot.types.KeyboardButton('Нет')
keyboard.add(button1,button2)

@bot.message_handler(commands=['start','Салам пополам'])
def start_function(message):
    msg=bot.send_message(message.chat.id,f'Салам Алейкум {message.chat.first_name} начнем игру?', reply_markup=keyboard)
    bot.register_next_step_handler(msg,answer_chek)
    
    # bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAJKMmOhPXjh0zP1Hf-1DWwpYsR4wHwsAAIdBAACR_sJDBtEhnEa_TLcLAQ')
    # bot.send_photo(message.chat.id,'https://gamerwall.pro/uploads/posts/2022-05/1651636791_23-gamerwall-pro-p-zevs-bog-krasivo-oboi-33.jpg')

def answer_chek(msg):
    if msg.text=='Да':
        bot.send_message(msg.chat.id,'У тебя есть 3 попытки угадать число от 1 до 10!')
        random_number=random.randint(1,10)
        p = 3
        start_game(msg,random_number,p)

    else:
        bot.send_message(msg.chat.id,'Ну и ладно')

def start_game(msg,random_number,p):
    msg=bot.send_message(msg.chat.id,'Введи число от 1 до 10: ')
    bot.register_next_step_handler(msg,check_func,random_number,p - 1)

def check_func(msg,random_number,p):
    if msg.text==str(random_number):
        bot.send_message(msg.chat.id,'Ты победиииииил Братааан!')
    elif p==0:
        bot.send_message(msg.chat.id, f'Ты проиграл братиш! Число было - {random_number}')
    else:
        bot.send_message(msg.chat.id, f'Попробуй еще раз братиш , у тебя еще есть {p} попыток')
        start_game(msg,random_number,p)

# @bot.message_handler()
# def echo_all(message):
#     bot.send_message(message.chat.id,message.text)

bot.polling()
