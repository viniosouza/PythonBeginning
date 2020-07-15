from random import randint

print('********************************')
print('*      Jogo da adivinhação      *')
print('********************************')

numero_secreto = randint(0,10)

chute = int(input('Digite o seu número: '))
print('Você digitou ', chute)

if(numero_secreto == chute):
    print('Você acertou!')
else:
    print('Você errou! O número correto é o {}'.format(numero_secreto))