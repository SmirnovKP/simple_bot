import logging # мпортируем стандартную библиотеку logging
import settings # Подключаем файл с токеном
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', #Выводит время, имя, и само сообщение об ошибке
					level=logging.INFO,
					filename='bot.log' # записывает это все в данный фаул
					)

def start_bot(update: Updater, context: CallbackContext):
	mytext = """Hello {}

	I have only /start command!""".format(update.message.chat.first_name) #тройные ковычки нужны для возможности перенома строки
	update.message.reply_text(mytext) # Этой командой мы выводим нашу переменую т.е. наш текст

def chat(update: Updater, context: CallbackContext):
	text = update.message.text #Бот отвечает тем же текстом что мы ввели
	logging.info(text) #пишет в лог, что мы писали в чате

	update.message.reply_text(text)

def main():
	updtr = Updater(settings.TOKEN_TELEGRAMM)

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
	updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

	updtr.start_polling()
	updtr.idle()

if __name__ == "__main__":
	logging.info('Bot started!')
	main()