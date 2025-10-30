# 1 crie variaveis que representem:
# sua idade
idade = 19
# sua altura 
altura = 1,85
# seu nome 
nome = "Samuel"
# se voce é estudante 
eh_estudante = True
# para ver o tipo de variavel 
type(eh_estudante)

# 2 - o usuario digita sua idade
# - Converta essa entrada para numero inteiro 
# - Some +5 anos e mostre resultado 
idade = input("digite sua idade")
idade = int(idade) + 5
print(idade)

# 3 soma de numeros inteiros 
# leia dois numeros ineteiros e exiba a soma deles
# entrada: dois numeros inteiros
# saida: a soma dos dois numeros 
# exemplo: entrada: 3, 5, saida: 8
num1 = input("digite o primeiro numero")
num2 = input("digite o segundo numero")
num1 = int(num1)
num2 = int(num2)
soma = num1 + num2
print(f"A soma é igual a: {soma}")

# 4 Média de três numeros  inteiros 
num1 = input("digite o primeiro numero")
num2 = input("digite o segundo numero")
num3 = input("digite o terceiro numero")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
media = (num1 + num2 + num3)/3
media = float(media)
print("media:" , media)

# 5 Média ponderada (Padrão IBMEC):
num1 = input("digite o primeiro numero")
num2 = input("digite o segundo numero")
num3 = input("digite o terceiro numero")
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)
media = (num1 + num2 + num3)
print("media" , media)

# 6 Manipulação de Strings:
nome = input("digite seu nome")
nome.upper()
nome.split()
len(nome)