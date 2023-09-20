import telebot
from config import keys, TOKEN
from extensions import APIException, CurrConverter


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help_answ(message: telebot.types.Message):
    text='Чтобы начать работу введите команду боту в следующем формате:\n <имя валюты> ' \
         '<в какую валюту перевести> <количество переводимой валюты>\n\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values_answ(message: telebot.types.Message):
    text='Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.lower().split(' ')

        if len(values) != 3:
            raise APIException('введите команду боту в следующем формате:\n <имя валюты> ' \
         '<в какую валюту перевести> <количество переводимой валюты>')

        curr_from, curr_to, amount = values
        price=CurrConverter.get_price(curr_from, curr_to, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text= f'{abs(float(amount))} {keys[curr_from]} = {price * abs(float(amount))} {keys[curr_to]}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)