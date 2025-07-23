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
        " \n "
        print("Pão de queijo mineiro: \n "
            " \n "
            "Ingredientes: \n "
            "2 xícaras de polvilho doce \n "
            "1 xícara de leite \n "
            "½ xícara de óleo \n "
            "1 colher de chá de sal \n "
            "1 ½ xícara de queijo ralado (meia cura ou parmesão) \n "
            "2 ovos"
            " \n "
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

def final():
    print("Espero que você tenha gostado. Obrigado por usar o ChatBot!")


chatbot()
escolha()
final()