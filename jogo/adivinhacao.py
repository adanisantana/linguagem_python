import random

def jogar():
   print("Bem vindo ao jogo de adivinhação")

   numero_secreto= random.randrange(1,101)
   total_tentativas = 0
   pontos = 1000
   print("Qual nível de dificuldade?")
   print("(1) Fácil  (2) Médio  (3)Difícil")

   nivel= int(input("Defina o nível: "))

   if (nivel==1):
      total_tentativas = 20
   elif (nivel==2):
      total_tentativas = 10
   else:
      total_tentativas = 5


   for rodada in range(1, total_tentativas):
      print("Tentativa {} de {}".format(rodada, total_tentativas))
      chute_str = input("Digite um número entre 1 a 100: ")
      print("Você digitou:", chute_str)
      chute = int(chute_str)

      if (chute <1 or chute>100):
         print("Valor inválido")
         continue
       
      acertou = numero_secreto == chute
      maior = chute > numero_secreto
      menor = chute < numero_secreto

      if acertou:
         print("Você acertou e fez {} pontos".format(pontos))
         break
    
      else:
         if (maior):
            print("Você errou! O seu chute foi maior que o número secreto")
         elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto")
         pontos_perdidos = abs(numero_secreto - chute)
         pontos = pontos - pontos_perdidos
      
   print("Fim do Jogo!")

if(__name__=="__main__"):
   jogar()

