import telebot
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


CHAVE_API = "6221818830:AAEpSJ4tfSFiHW1nHYB4r6wmKNd-FBpwFEk"
bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["opcao01"])
def opcao01(mensagem):
    date01 = "06/10/2023 ás 16:00" # introduzir uma função para consultar horários disponíveis via API
    date02 = "06/10/2023 ás 17:00"
    date03 = "07/10/2023 ás 11:00"
    resposta_opcao11 = f"""
    Datas disponíveis:
    /opcao1: {date01}
    /opcao2: {date02}
    /opcao3: {date03}
    """
    
    bot.send_message(mensagem.chat.id, resposta_opcao11)

@bot.message_handler(commands=["op2"])
def op2(mensagem):
    bot.send_message(mensagem.chat.id, "text op2")

@bot.message_handler(commands=["op3"])
def op3(mensagem):
    bot.send_message(mensagem.chat.id, "voltar")

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    servico01 = "CORTE DE CABELO" # Preencher com nome do serviço
    servico02 = "CORTE E BARBA"
    resposta_opcao1 = f"""
    Qual serviço você deseja agendar? (Clique no item)
    /opcao01: {servico01}
    /opcao2: {servico02}
    /opcao3: voltar
    """
    bot.send_message(mensagem.chat.id, resposta_opcao1)

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Cancelado")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Agendadado!")
    

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    nome_usuario = mensagem.from_user.first_name
    menu = f"""
    Olá, {nome_usuario}. Bem-vindo(a) à barbearia Souza&Souza!
    Escolha uma opção para continuar (Clique no item):
    /opcao1: Agendar um serviço
    /opcao2: Cancelar um agendamento
    /opcao3: Falar com um atendente
    """
    bot.send_message(mensagem.chat.id, menu)

bot.polling()