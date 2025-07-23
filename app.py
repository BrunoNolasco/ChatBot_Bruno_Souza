import os
from datetime import datetime

def chatbot():
    nome = input("Olá! Qual o seu nome? ")
    print(f"Prazer em te conhecer, {nome}!")

    humor = input("Como você está hoje? (bem/mal) ").strip().lower()
    if humor == "bem":
        print("Que ótimo! Espero que continue assim!")
    elif humor == "mal":
        print("Sinto muito, Espero que o seu dia melhore!")
    else:
        print("Não entendi, mas espero que esteja tudo bem!")
        
    idade = int(input("Quantos anos você tem? "))
    print("Muito bem!, tenho certeza que já é muito responsável pra sua idade!")
    return idade
        
def escolha():
    escolhas = input("Você gastaria de jogar um jogo ou receber uma receita? (jogo/receita): ")
    if escolhas == "jogo":
        print("Ótimo, vamos jogar ""quem sou eu"".")
    elif escolhas == "receita":
        print("Ótimo, deixa eu te passar uma receita que eu adoro!")
    else:
        print("Não entendi, vamos tentar de novo? ")
        
def jogo(escolha = "jogo"):
    print("escreva 'desisto' se desejar saber a resposta")
    escolha = input("Na água nasci, na água me criei, mas se me jogarem na água, na água morrerei. Quem sou eu?").strip().lower()
    if escolha == "sal" or "o sal" or "O sal" or "O Sal" or "Sal" or "o Sal":
        print("Parabéns, você ganhou o jogo!")
    elif escolha == "desisto" or "Desisto":
        print("Ohh, não tem problema, essa era difícil mesmo, a resposta é 'O sal'. ")
    else:
        print("Não é isso, tente de novo! ")
        
chatbot()
escolha()
jogo(escolha)









































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