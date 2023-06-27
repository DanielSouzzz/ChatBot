import telebot

CHAVE_API = "6221818830:AAEpSJ4tfSFiHW1nHYB4r6wmKNd-FBpwFEk"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["opcao01"])
def opcao01(mensagem):
    resposta_opcao11 = f"""
    Hoários disponíveis para 03/07/2023:
    /opcao1: 15h00
    /opcao2: 16h00
    /opcao3: 19h00
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
    #print(mensagem)
    #nome_usuario = mensagem.from_user.first_name
    resposta_opcao1 = f"""
    Qual serviço você deseja agendar? (Clique no item)
    /opcao01: corte de cabelo
    /opcao2: corte + barba
    /opcao3: voltar"""
    #resposta_opcao1 = f"Opção 1 selecionada por {nome_usuario}."
    bot.send_message(mensagem.chat.id, resposta_opcao1)#envia a veriavel mensagem para o end do .chat.id
    #bot.reply_to(mensagem, opcao01)
    
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
    nome_usuario1 = mensagem.from_user.first_name
    menu = f"""
    Olá, {nome_usuario1}. Bem vindo(a) a barberia Souza&Souza!
    Escolha uma opção para continuar
    (Clique no item):
    /opcao1: Agendar um de nossos serviços
    /opcao2: Cancelar um agendamento
    /opcao3: Falar com um atendente
    """
    bot.reply_to(mensagem, menu)
    #processar_opcao1(mensagem)
    #print(mensagem.id()) #Exibe o log da conversa

bot.polling()