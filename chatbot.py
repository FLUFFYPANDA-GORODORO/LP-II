from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Customer Bot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
response = chatbot.get_response('What is your Number')
print(response)|
response = chatbot.get_response('Who are you?')
print(response)


#Make sure to use
#pip install chatterbot
#pip install chatterbot-corpus
