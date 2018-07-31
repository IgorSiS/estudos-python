import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101) #arredonda o número para inteiro. Gera um numero entre o valor do primeiro parametro até o último -1
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: ")) #Função inout só retorna string

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10 #
    else:
        total_de_tentativas = 5
    # step 2... Fica 1 3 5 7 9 -> for rodada in range(1,10,2):
    # ou for rodada in [1,2,3,4,5]:
    #range -> se o final for 20, só vai até o 19
    for rodada in range(1, total_de_tentativas + 1): #range = alcane.... Um for normal. Rodada é a variavel que recebe o estado atual do loop
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue #iteração atual acaba e vai para a próxima
        
        #Deixando mais semântico.
        acertou = chute == numero_secreto #Recebe um boolean
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos)) #  interpolação de strings pesquisar na documentação
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor): #igual ao else mas com confição de entrada.
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute) # abs numero absoluto
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
