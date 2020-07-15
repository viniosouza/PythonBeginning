from random import randint

numero = randint(0, 100)
chute = int(input('Insira um número de 0-100: '))

acertou = chute == numero
maior = chute > numero
menor = chute < numero

if chute == numero:
    print('Você	acertou')
elif(maior):
    print('Você errou! O seu chute foi maior que o número secreto, o número correto é o {}'.format(numero))
elif(menor):
    print('Você errou! O seu chute foi menor que o número secreto, o número correto é o {}'.format(numero))

# Primeiro código

# else:
#     print('Você	errou')
