# 1.
aluno = {
    'name' : 'Eduardo',
    'idade' : 19,
    'curso' : 'administração'
}
print(f"nome: {aluno['name']}")
print(f"idade: {aluno['idade']}")
print(f"curso:{aluno['curso']}")

# 2.
produto = {
    "nome": "Teclado Mecânico",
    "preco": 350.00,
    "estoque": 10
}
produto['marca'] = 'Redragon'
produto['preco'] = 320
produto['estoque'] -= 2
del produto['estoque']
print(f"Dicionario final do produto")
print(produto)

# 3.
notas = {
    "Alice": 8.5,
    "Bruno": 7.0,
    "Carla": 9.2,
    "Daniel": 6.8
}
print("Notas dos alunos:")
for aluno, nota in notas.items():
    print(f"- {aluno}: {nota}")
    soma_das_notas = sum(notas.values())
    quantidade_de_alunos = len(notas)
    media = soma_das_notas / quantidade_de_alunos
    print(f"A media da turma é: {media: .2f}")

# 4.
numeros = {'a': '10', 'b': '20', 'c': '30'}
soma_total = 0
for valor_texto in numeros.values():
    soma_total += int(valor_texto)
print(f"Saída esperada: {soma_total}")

# 5.
lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
frequencia = {}
for fruta in lista:
    if fruta in frequencia:
        frequencia[fruta] += 1
    else:
        frequencia[fruta] = 1
print(f"Saída esperada: {frequencia}")

# 6.
produtos = {
    "caneta": 10,
    "mochila": 80,
    "caderno": 45,
    "notebook": 3000
}
produtos_filtrados = {}
for produto, preco in produtos.items():
    if preco > 50:
        produtos_filtrados[produto] = preco
print("Saída esperada:", produtos_filtrados)

# 7.
tradutor = {
    "cat": "gato",
    "dog": "cachorro",
    "house": "casa",
    "python": "píton"
}
palavra_ingles = input("Digite uma palavra em inglês para traduzir: ")
if palavra_ingles in tradutor:
    traducao = tradutor[palavra_ingles]
    print(f"A tradução de '{palavra_ingles}' é '{traducao}'.")
else:
    print("Palavra não encontrada.")

    # 8. 
lista_de_compras = {}
while True:
    print("\n--- Menu Lista de Compras ---")
    print("1: Adicionar produto")
    print("2: Atualizar quantidade")
    print("3: Remover produto")
    print("4: Ver lista")
    print("5: Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        produto = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        lista_de_compras[produto] = quantidade
        print(f"'{produto}' adicionado com sucesso!")

    elif escolha == '2':
        produto = input("Qual produto deseja atualizar? ")
        if produto in lista_de_compras:
            nova_quantidade = int(input(f"Nova quantidade para '{produto}': "))
            lista_de_compras[produto] = nova_quantidade
            print(f"'{produto}' atualizado com sucesso!")
        else:
            print("Produto não encontrado na lista.")

    elif escolha == '3':
        produto = input("Qual produto deseja remover? ")
        if produto in lista_de_compras:
            del lista_de_compras[produto]
            print(f"'{produto}' removido com sucesso!")
        else:
            print("Produto não encontrado na lista.")

    elif escolha == '4':
        print("\n--- Sua Lista de Compras ---")
        if not lista_de_compras:
            print("A lista está vazia.")
        else:
            for produto, quantidade in lista_de_compras.items():
                print(f"- {produto}: {quantidade}")
        print("--------------------------")


    elif escolha == '5':
        print("Encerrando o programa. Boas compras!")
        break

    else:
        print("Opção inválida. Tente novamente.")

    #9.
turma = {
    "Ana": {"idade": 17, "notas": [8, 9, 7]},
    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]}
}
print("\n--- Passo 1: Adicionando novo aluno ---")
turma["Lucas"] = {"idade": 18, "notas": [7, 8, 9]}
print("Aluno 'Lucas' adicionado. Turma atualizada:")
print(turma)
print("\n--- Passo 2: Calculando as médias ---")
for nome, dados in turma.items():
    lista_de_notas = dados["notas"]
    media = sum(lista_de_notas) / len(lista_de_notas)
    print(f"{nome}: Média {media:.1f}")
print("\n--- Passo 3: Encontrando a maior média ---")
maior_media = -1 
aluno_com_maior_media = ""

for nome, dados in turma.items():
    lista_de_notas = dados["notas"]
    media_atual = sum(lista_de_notas) / len(lista_de_notas)
    if media_atual > maior_media:
        maior_media = media_atual          
        aluno_com_maior_media = nome       

print(f"O aluno com a maior média é: {aluno_com_maior_media} (Média: {maior_media:.1f})")

# 10.
funcionarios = {}

while True:
    print("\n--- Sistema de Cadastro ---")
    print("1: Adicionar funcionário")
    print("2: Consultar funcionário")
    print("3: Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        nome = input("Digite o nome do funcionário: ")
        cargo = input("Digite o cargo: ")
        salario = float(input("Digite o salário: "))
        funcionarios[nome] = {
            "cargo": cargo,
            "salario": salario
        }
        print(f"Funcionário '{nome}' cadastrado com sucesso!")

    elif escolha == '2':
        nome_consulta = input("Digite o nome do funcionário para consultar: ")

        if nome_consulta in funcionarios:
            dados_funcionario = funcionarios[nome_consulta]
            
            print("\n--- Ficha do Funcionário ---")
            print(f"Nome: {nome_consulta}")
            print(f"Cargo: {dados_funcionario['cargo']}")
            print(f"Salário: R$ {dados_funcionario['salario']:.2f}")
            print("--------------------------")
        else:
            print("Funcionário não encontrado no sistema.")

    elif escolha == '3':
        print("Encerrando o sistema.")
        break
    
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")