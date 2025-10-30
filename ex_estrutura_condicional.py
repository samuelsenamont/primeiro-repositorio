# 1. Par ou Ímpar
num1 = 10
if num1 % 2 == 0:
    print("O numero é par")
else:
    print("O numero é ímpar")

# 2. Aprovado ou Reprovado
ap1 = float(input("Digite a nota da ap1"))
ap2 = float(input("Digite a nota da ap2"))
ac = float(input("Digite a nota de ac"))
media = 0.4 * ap1 + 0.4 * ap2 + 0.2 * ac
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

# 3. Cálculo de Desconto
valor = float(input("Digite o valor da sua compra"))
if valor > 100:
    desconto = valor * 0.1
    valor_desconto = valor - desconto
    print("O valor com desconto é", valor_desconto)
else:
    print("valor sem desconto:", valor )

    # 4. Conversão de temperatura
    # Leia a temnperatura em celsius e converta para Fahrenreit usando a formula: F = (C x 9/5) + 32.
celsius = float(input("Digite a temperatura em graus celsius"))
fahrenreit = (celsius * 9/5) + 32
print("Fahrenreit" , fahrenreit)

# 5. Maior numero (Dois valores)
# Leia dois numeros inteiros e informe
# Qual deles é o maior
# Ou se são iguais
num1 = int(input("Digite o primeiro numero"))
num2 = int(input("Digite o segundo numero inteiro"))
if num1 > num2:
    print("O maior numero é", num1)
if num2 > num1:
    print("O maior numero é", num2)
else: 
    print("Os dois numeros são iguais")

# 6. Maior numero tres valores
num1 = int(input("Digite o primeiro numero"))
num2 = int(input("Digite o segundo numero"))
num3 = int(input("Digite o terceiro numero"))
if num1 > num2 > num3:
    print("O maior numero é", num1)
elif num2 > num3 > num1:
    print("O maior numero é", num2)
elif num3 > num2 > num1:
    print("O maior numero é", num3)
    
# 7. Calculadora simples
num1 = float(input("Digite o primeiro numero"))
operacao = input("Digite a operacao(+, - , *, /)").strip()
print(f"o resultado {num1} + {num2} é: {resultado}")
num2 = float(input("Digite o segundo numero"))

# 9. Ano bissexto 
ano = int(input("Digite um ano"))
if (ano % 4 == 0, ano % 100 != 0) or (ano % 400 ==0):
    print("Bissexto")
else:
    print("Não bissexto")

# 10. Intervalo de Idade
idade = int(input("Digite sua idade"))
if idade >= 18 and idade <= 65:
    print("Dentro da Faixa etaria permitida")
else:
    print("Fora da faixa etaria permitida")

    # 11. Acesso ao sistema
    usuario = input("Digite o usuario")
    senha = input("Digite a senha")
    if usuario == "admin" and Senha == "1234":
        print("Acesso permitido")
    else:
        print("Acesso negado")

    # 12. Voto Obrigatorio
    idade = int(input("Digite a sua idade"))
    if idade < 16:
        print("Nao vota")
    elif idade >= 16 and idade< 18 or idade >=70:
        print("Voto facultativo")
    elif idade >=18 or idade >=70:
        print("Voto obrigatorio")

    # 13. Numero fora de intervalo
    numero = int(input("Digite o numero"))
    if numero >=10 and numero <=50:
        print("Dentro do intervalo")
    else:
        print("Fora de intervalo")

    # 14. Aluno aprovado com recuperacao
    media = float(input("Digite a media final"))
    if media >= 7:
        print("Aprovado")
    elif media >= 5 and media < 7:
        print("Recuperacao")
    else:
        print("Reprovado")






    



