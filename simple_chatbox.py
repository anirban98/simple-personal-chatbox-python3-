from chatterbot import ChatBot
bot = ChatBot('john')

import logging
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

#TRAINING THE INTERNET

from chatterbot.trainers import ChatterBotCorpusTrainer
trainer = ChatterBotCorpustrainer(bot)
trainer.train("chatterbot.corpus.english")

#sending the message

while True:
    message = input('you: ')
    print(message)
    if(message.strip()!='Bye'):
        reply = bot.get_response(message)
        print('john:',reply)
    else:
        print('john:bye')
        break
