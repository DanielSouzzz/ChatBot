import telebot

CHAVE_API = "6221818830:AAEpSJ4tfSFiHW1nHYB4r6wmKNd-FBpwFEk"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["op1"])
def op1(mensagem):
    bot.send_message(mensagem.chat.id, "texto para op1")

@bot.message_handler(commands=["op2"])
def op2(mensagem):
    bot.send_message(mensagem.chat.id, "text op2")

@bot.message_handler(commands=["op3"])
def op3(mensagem):
    bot.send_message(mensagem.chat.id, "voltar")

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    print(mensagem)
    nome_usuario = mensagem.from_user.username
    '''resposta_opcao1 = """
    Olá {}.Gostaria de agendar qual de nossos serviços? (Clique em uma opção)
    /Corte de cabelo
    /Corte+barba
    /outros""".format(nome_usuario)'''
    resposta_opcao1 = f"Opção 1 selecionada por {nome_usuario}."
    bot.send_message(mensagem.chat.id, resposta_opcao1)#envia a veriavel mensagem para o end do .chat.id

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Cancelado")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "link") # exibe uma string 


# verifica se tem mensagens, se tiver entao exibe o menu principal
def verificar(mensagem):
    return True

# menu principal
@bot.message_handler(func=verificar)
def responder(mensagem):
    #print(mensagem)
    menu = """
    Escolha uma opção para continuar (Clique no item):
     /opcao1 agendar um serviço
     /opcao2 cancelar um agendamento
     /opcao3 quem nós somos
    """
    bot.reply_to(mensagem, menu)
    #processar_opcao1(mensagem)
    #print(mensagem.id()) #Exibe o log da conversa

bot.polling()