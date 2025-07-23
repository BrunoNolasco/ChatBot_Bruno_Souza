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
            receita()
            break
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

def receita():
    resposta = input("Você que aprender a fazer pão de queijo ou bolo de cenoura?").strip().lower()
    if resposta == "pão de queijo":
        " \n \n "
        print("Pão de queijo mineiro: \n "
            " \n \n "
            "Ingredientes: \n "
            "2 xícaras de polvilho doce \n "
            "1 xícara de leite \n "
            "½ xícara de óleo \n "
            "1 colher de chá de sal \n "
            "1 ½ xícara de queijo ralado (meia cura ou parmesão) \n "
            "2 ovos"
            " \n \n "
            "Modo de Preparo: \n "
            "Aqueça o leite, o óleo e o sal até começar a ferver. \n "
            "Despeje essa mistura quente sobre o polvilho e mexa bem até formar uma massa. \n "
            "Deixe esfriar um pouco, junte os ovos e o queijo. \n "
            "Misture bem com a mão até a massa ficar homogênea. \n "
            "Modele bolinhas e coloque numa forma untada ou com papel manteiga. \n "
            "Leve ao forno pré-aquecido a 180°C por 25-30 min, até dourar.) \n ")
        
    elif resposta == "bolo de cenoura":
        " \n "
        print("Bolo de cenoura com cobertura de chocolate: \n "
            " \n "
            "Ingredientes da massa: \n "
            "3 cenouras médias (descascadas e picadas) \n "
            "3 ovos \n "
            "1 xícara de óleo \n "
            "2 xícaras de açúcar \n "
            "2 ½ xícaras de farinha de trigo \n "
            "1 colher de sopa de fermento em pó \n "
            " \n "
            "Modo de Preparo da massa: \n "
            "Bata no liquidificador: cenoura, ovos e óleo até ficar liso. \n "
            "Transfira para uma tigela e misture o açúcar e a farinha. \n "
            "Adicione o fermento por último, mexendo levemente. \n "
            "Coloque numa forma untada e enfarinhada. \n "
            "Asse em forno pré-aquecido a 180°C por 40-45 min. \n "
            " \n "
            "Cobertura de chocolate: \n "
            "4 colheres de sopa de açúcar \n "
            "2 colheres de sopa de chocolate em pó \n "
            "2 colheres de sopa de manteiga \n "
            "2 colheres de sopa de leite \n "
            "Modo de Preparo da cobertura: \n "
            "Misture tudo em uma panela e leve ao fogo baixo. \n "
            "Mexa até engrossar um pouco (cerca de 5 min). \n "
            "Jogue por cima do bolo ainda quente.")
    else:
        print("Não conheço essa receita. Tente de novo!")


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