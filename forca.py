def run():
    print("************************************")
    print("***     Welcome to the Game !    ***")
    print("************************************")

    palavra_secreta = "pele".upper()
    letras_acertadas = ["_", "_", "_", "_"]

    perdeu = False
    ganhou = False
    erros = 0

    print(letras_acertadas)

    while(not perdeu and not ganhou):
        chute = input("Digite uma Letra:  \n").upper().strip()
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros = erros + 1

        perdeu = erros == 6
        ganhou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (ganhou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
run()



