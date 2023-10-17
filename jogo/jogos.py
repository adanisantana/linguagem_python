import forca
import adivinhacao

def escolhe_jogo():
    print("**************Menu*******************")
    print("--------Escolha o seu jogo---------")

    print("(1)Forca (2)Adivinhação")
    jogo = int(input("Qual o jogo? "))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()
    else:
        print("Opção inválida!")
           
      
print("Fim do Jogo!")

if(__name__=="__main__"):
    escolhe_jogo()

