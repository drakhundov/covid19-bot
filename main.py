import os

import telebot

from WebParser import WebParser

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
webparser = WebParser(os.getenv("API_URL"), args_lst=["q"])


@bot.message_handler(commands=["start"])
def start(message):
    first_message = "<b> Hi!\nEnter country, please. </b>"
    bot.send_message(message.chat.id, first_message, parse_mode="html")


@bot.message_handler(content_types=["text"])
def send_info(message):
    user_message = message.text.strip().lower()
    if user_message == "hello" or user_message == "hi":
        start(message)
    else:
        data = webparser.parse(args={"q": user_message})
        info_message = f"<u><b> Information in {data['region']['name']} </b></u>\n"
        info_message += f"""
            <i> New Confirmed: {data['confirmed_diff']} </i>
            <i> Total Confirmed: {data['confirmed']} </i>

            <i> New Deaths: {data['deaths_diff']} </i>
            <i> Total Deaths: {data['deaths']} </i>
        
            <i> New Recovered: {data['recovered_diff']} </i>
            <i> Total Recovered: {data['recovered']} </i>
        """
        bot.send_message(message.chat.id, info_message, parse_mode="html")


bot.polling(none_stop=True)
