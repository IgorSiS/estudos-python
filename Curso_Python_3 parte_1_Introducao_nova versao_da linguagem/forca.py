def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    print("Fim do jogo")

if(__name__ == "__main__"): # Se o arquivo for importado, ele não chama aqui direto. 
    jogar()


# Precisamos dar um jeito para que, quando executarmos o jogo de adivinhação diretamente, 
# a função jogar() deve ser chamada, mas quando só o importamos, não queremos que a função seja chamada.

# Essa variável é a __name__, e ela é preenchida com o valor __main__ caso o arquivo seja executado diretamente.
# Se ele não não tiver preenchida, então o arquivo só foi importado. 
 #Na hora de importar um arquivo, ele lê o código da função, mas não o executa, pois ele não é o arquivo principal
#  Vamos então fazer if para verificar se ela está preenchida ou não:
