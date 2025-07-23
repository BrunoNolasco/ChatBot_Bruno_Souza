def chatbot():
    nome = input("Olá! Qual o seu nome? ")
    print(f"Prazer em te conhecer, {nome}!")

    humor = input("Como você está hoje? (bem/mal) ").strip().lower()
    if humor == "bem":
        print("Que ótimo! Espero que continue assim!")
    elif humor == "mal":
        print("Sinto muito. Espero que o seu dia melhore!")
    else:
        print("Não entendi, mas espero que esteja tudo bem!")

    idade = input("Quantos anos você tem? ")
    print("Muito bem! Tenho certeza que já é muito responsável pra sua idade!")
    return idade

def escolha():
    while True:
        escolha_usuario = input("Você gostaria de jogar um jogo ou receber uma receita? (jogo/receita): ").strip().lower()
        if escolha_usuario == "jogo":
            print("Ótimo, vamos jogar 'Quem sou eu?'.")
            jogo()
            break
            
        elif escolha_usuario == "receita":
            print("Ótimo! Deixa eu te passar uma receita que eu adoro:")
            
        else:
            print("Não entendi. Vamos tentar de novo?")

def jogo():
    print("Escreva 'desisto' se desejar saber a resposta.")
    
    while True:
        resposta = input("Na água nasci, na água me criei, mas se me jogarem na água, na água morrerei. Quem sou eu? ").strip().lower()

        if resposta in ["sal", "o sal"]:
            print("Parabéns, você ganhou o jogo!")
            break
        elif resposta == "desisto":
            print("Ohh, não tem problema, essa era difícil mesmo. A resposta é 'o sal'.")
            break
        else:
            print("Não é isso. Tente de novo!")

chatbot()
escolha()










































#def obter_resposta(texto: str) -> str:
#    comando: str = texto.lower()
#
#                #if comando in ('olá', 'boa tarde', 'bom dia'):
#                #    return 'Olá tudo bem!'
#                #if comando == 'como estás':
#                #    return 'Estou bem, obrigado!'
#                #if comando == 'como te chamas?':
#                #    return 'O meu nome é: Bot :)'
#                #if comando == 'tempo':
#                #    return 'Está um dia de sol!'
#                #if comando in ('bye', 'adeus', 'tchau'):
#                #    return 'Gostei de falar contigo! Até breve...'
#                #if 'horas' in comando:
#                #    return f'São: {datetime.now():%H:%M} horas'
#                #if 'data' in comando:
#                #    return f'Hoje é dia: {datetime.now():%d-%m-%Y}'
#           
#                #return f'Desculpa, não entendi a questão! {texto}'
#
#    respostas = {
#        ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
#        'como estás': 'Estou bem, obrigado!',
#        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',}
#    for chave, resposta in respostas.items():
#        if isinstance(chave, tuple):
#            if comando in chave:
#                return resposta
#        elif chave in comando:
#            return resposta
#        return f'Desculpa, não entendi a questão! {texto}'
#
#
#def chat() -> None:
#    print('Bem-vindo ao ChatBot!')
#    print('Escreva "bye" para sair do chat')
#    name: str = input('Bot: Como te chamas? ')
#    print(f'Bot: Olá, {name}! \n Como te posso ajudar?')
#
#    while True:
#        user_input: str = input('Tu: ')
#
#        if resposta == 'Gostei de falar contigo! Até breve...':
#            break
#
#    print('Chat acabou')
#    print()
#
#
#def main() -> None:
#    os.system('cls' if os.name == 'nt' else 'clear')
#    chat()
#
#
#if __name__ == '__main__':
#    main()