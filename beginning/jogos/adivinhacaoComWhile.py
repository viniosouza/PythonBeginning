from random import randint

print('********************************')
print('*      Jogo da adivinhação      *')
print('********************************')

numero_secreto = 42
total_de_tentativas = 3
chute = int(input('Insira um número de 0-100: '))

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

while (total_de_tentativas > 0):

    if chute == numero_secreto:
        print('Você	acertou')
    elif(maior):
        print('Você errou! O seu chute foi maior que o número secreto, o número correto é o {}'.format(
            numero_secreto))
    elif(menor):
        print('Você errou! O seu chute foi menor que o número secreto, o número correto é o {}'.format(
            numero_secreto))
total_de_tentativas = total_de_tentativas - 1
