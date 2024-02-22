# EXERCÍCIOS DO SENAI - CURSO EM PROGRAMAÇÃO EM PYTHON

#1
#Concatene uma cidade e um adjetivo para ela
cidade = input("escolha uma cidade:")
adjetivo = input("Digite um ajetivo:")
print('{} é {}' .format(cidade , adjetivo))
#2
#concatene uma viagem e quem vai participar dela
name = input("quem irá viajar? ")
lugar = input("Onde? ")
print('{} irá viajar para {}' .format(viagem , lugar))

#3
#concatene função programador seu nome ou nome do usuário
funcao = input("Digite sua função:")
nome = input("Selecione seu nome de usuário: ")
print('{}{}' .format(funcao , nome))

#1
numero = int(input("Escolha um número:"))
resultado = numero **2
print("O resultado do quadrado desse {} é {}" .format(numero, resultado))

#2
nome = input("Digite seu nome:")
obrenome = input("Digite seu sobrenome:")
print("Seu nome completo é {} {}" .format(nome,sobrenome))

#3
n1 = input("Escolha o primeiro número:")
n2 = input("Escolha o segundo número:")
print("O primeiro número escolhido foi o {} e o segundo o {}" .format(n1, n2))

##4
palavra = "Python"
numero = 5
print("{}{}" .format(palavra, numero))

#5
frase = "Mas que linda vista desse"
palavra = input("Escolha uma palavra para completar a frase: Mas que linda vista desse ")
print("{} {}" .format(frase,palavra))

# Calculadora

numero1 = float(input("Escolha o primeiro número:"))
numero2 = float(input("Escolha o segundo número:"))

print("Soma:" ,numero1 + numero2)
print("Subtração:" , numero1 - numero2)
print("Divisão:", numero1 /numero2)
print("Multiplicação:" , numero1 * numero2)
print("Exponenciação" , numero1 ** numero2)
print("Divisão Inteira:" , numero1 // numero2)
