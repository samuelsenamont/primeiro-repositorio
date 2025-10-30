# 1.
frutas = ["maçã", "banana", "uva", "laranja"]
print(f"Lista de frutas criada: {frutas}")

# 2. 
primeiro_elemento = frutas[0]
último_elemento = frutas[3]
print(f"O primeiro elento da lista é: {primeiro_elemento}")
print(f"O último elemento da lista é: {último_elemento}")

# 3, 4, 5.
Nova_lista_de_frutas = ["maçã", "uva", "abacaxi", "manga"]
print(f"Nova lista de frutas: {Nova_lista_de_frutas}")

# 6.
Numeros = list(range(1,11))
print(f"Numeros: {Numeros}")

# 7.
soma_dos_numeros = (1+2+3+4+5+6+7+8+9+10)
print(f"Soma dos nuemros ; {soma_dos_numeros}")

# 8.
maior_numero = max(Numeros)
menor_numero = min(Numeros)
print(f"maior numero: {maior_numero}")
print(f"menor numero: {menor_numero}")

# 9.
numeros_ao_inverso = reversed(Numeros)
print(f"lista reversa: ")

# 10.
cidades = ("São Paulo", "Rio de Janeiro","Belo Horizonte", "Curitiba")
print(f"Cidades: {cidades}")

# 11. 
cidades_em_ordem_alfabetica = sorted(cidades)
print(f"cidades em ordem alfabetica{cidades_em_ordem_alfabetica}")

# 12.
nova_lista_de_cidades = ("São Paulo", "Rio de Janeiro","Belo Horizonte", "Curitiba","Porto Alegre")
print(f"nova lista de cidades: {nova_lista_de_cidades}")

# 13. 
indice_curitiba = cidades.index("Curitiba")
print(f"indice de curitiba é: {indice_curitiba}")

# 14.
Nova_lista_sem_rio_de_janeiro = ("São Paulo","Belo Horizonte", "Curitiba","Porto Alegre")
print(f"Nova lista: {Nova_lista_sem_rio_de_janeiro}")

# 15.
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(f"Lista1: {lista1}")
print(f"Lista2: {lista2}")

# 16, 17.
lista3 = lista1 + lista2
print("A nova lista concatenada é: {lista3}")

# 18. 
animais_domesticos = ("cachorro","gato","coelho")
animais_selvagens = ("leao","tigre","urso")

# 19, 20.
todos_os_animais = animais_domesticos + animais_selvagens
print(f"Lista todos os animais: {todos_os_animais}")    

# 21, 22.
lista_nome = ["ana","pedro","maria","joao"]
print(f"lista nomes: {lista_nome}")
for nome in lista_nome:
    print(lista_nome)

# 23.
nomes_maiusculos = []
for nome in lista_nome:
    nomes_maiusculos.append(nome.upper())
    print(nomes_maiusculos)

# 24.
lista_numeros = list(range(1, 21))
for numero in lista_numeros:
    if numero % 2 == 0:
        print(numero)

# 25.
quadrados = [] 
for numero in lista_numeros:
    quadrados.append(quadrados)
print(quadrados)

# 26.
palavras = ["python", "java", "c", "javascript"]
for palavra in palavras:
    print(f"A palavra '{palavra}' tem {len(palavra)} letras.")

# 27. 
idades = [12, 18, 25, 40, 60]
for idade in idades:
    if idade >= 18:
        print(f"{idade} anos: Maior de idade")
    else:
        print(f"{idade} anos: Menor de idade")

# 28. 
notas = [5.5, 7.0, 8.3, 4.9, 6.2]
aprovados = 0
reprovados = 0
for nota in notas:
    if nota > 7:
        aprovados += 1  
    elif nota < 7:
        reprovados += 1 
print(f"Alunos aprovados: {aprovados}")
print(f"Alunos reprovados: {reprovados}")

# 29.
palavras = ["arara", "banana", "radar", "python"]
print("Verificando palíndromos:")
for palavra in palavras:
    if palavra == palavra[::-1]:
        print(f"- {palavra} é um palíndromo.")

# 30.
compras = ["arroz", "feijão", "batata", "carne"]
for item in compras:
    print(f"Preciso comprar: {item}")



  # 31.
contador = 1
while contador <= 10:
    print(contador)
    contador += 1 
print("Loop finalizado!") 

# 32.
numero = -1 
while numero != 0:
    numero = int(input("Digite um número inteiro (ou 0 para sair): "))
    print(f"Você digitou: {numero}")
print("Programa encerrado porque você digitou 0.")

# 33.
numero_atual = 1
soma_total = 0
while numero_atual <= 100:
    soma_total += numero_atual 
    numero_atual += 1
print(f"A soma de todos os números de 1 a 100 é: {soma_total}")

# 34.
numero_secreto = 7
palpite = 0 
while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número secreto (entre 1 e 10): "))
    if palpite < numero_secreto:
        print("Tente um número maior!")
    elif palpite > numero_secreto:
        print("Tente um número menor!")
print(f"Parabéns! Você acertou! O número secreto era {numero_secreto}.")

# 35.
numero = 2
while numero <= 20:
    print(numero)
    numero += 2 
print("Fim dos números pares.")