faturamento = [
    {"dia": "segunda", "valor": 1200},
    {"dia": "terça", "valor": 1500},
    {"dia": "quarta", "valor": 900},
    {"dia": "quinta", "valor": 1800},
    {"dia": "sexta", "valor": 2400},
]

# 1. Calcule o faturamento total da semana.
faturamento_total = 0
for venda in faturamento:
    faturamento_total += venda["valor"]

print(f"1. Faturamento total da semana: R$ {faturamento_total}")

# 1.2. Descubra qual foi o dia de maior faturamento.
dia_maior_faturamento = ""
maior_valor = -1

for venda in faturamento:
    if venda["valor"] > maior_valor:
        maior_valor = venda["valor"]
        dia_maior_faturamento = venda["dia"]

print(f"2. Dia de maior faturamento: {dia_maior_faturamento} (R$ {maior_valor})")

# 1.3. Calcule a média de vendas.
quantidade_dias = len(faturamento)
media_vendas = faturamento_total / quantidade_dias

print(f"3. Média de vendas: R$ {media_vendas:.2f}")

estoque = { # estoques em 3 filiais
    "notebook": [5, 7, 3],
    "mouse": [20, 25, 18],
    "teclado": [12, 14, 9],
}

# Novo dicionário para armazenar os totais
totais_estoque = {}

# 1. Calcule o estoque total de cada produto.
for produto, quantidades in estoque.items():
    estoque_total_produto = sum(quantidades)
    totais_estoque[produto] = estoque_total_produto
    print(f"1. Estoque total de {produto}: {estoque_total_produto}")

# 2. Descubra qual produto tem o menor estoque total.
produto_menor_estoque = ""
menor_estoque = float('inf') # Começa com um valor muito alto

for produto, total in totais_estoque.items():
    if total < menor_estoque:
        menor_estoque = total
        produto_menor_estoque = produto

print(f"2. Produto com menor estoque total: {produto_menor_estoque} ({menor_estoque} unidades)")

# 3. Transforme os totais em um novo dicionário.
# (Já fizemos isso ao calcular o total, é 'totais_estoque')
print(f"3. Dicionário de totais: {totais_estoque}")

funcionarios = [
    {"nome": "Ana", "salario": 4500, "departamento": "RH"},
    {"nome": "Carlos", "salario": 7000, "departamento": "TI"},
    {"nome": "Beatriz", "salario": 5200, "departamento": "Financeiro"},
    {"nome": "João", "salario": 4800, "departamento": "TI"},
]

# 1. Calcule a folha salarial total da empresa.
folha_salarial_total = 0
for func in funcionarios:
    folha_salarial_total += func["salario"]

print(f"1. Folha salarial total: R$ {folha_salarial_total}")

# 2. Descubra qual funcionário ganha mais.
funcionario_maior_salario = ""
maior_salario = -1

for func in funcionarios:
    if func["salario"] > maior_salario:
        maior_salario = func["salario"]
        funcionario_maior_salario = func["nome"]

print(f"2. Funcionário com maior salário: {funcionario_maior_salario} (R$ {maior_salario})")

# 3. Agrupe os salários por departamento em um dicionário.
salarios_por_departamento = {}

for func in funcionarios:
    departamento = func["departamento"]
    salario = func["salario"]
    
    # Se o departamento ainda não está no dicionário, inicializa
    if departamento not in salarios_por_departamento:
        salarios_por_departamento[departamento] = 0
    
    # Adiciona o salário
    salarios_por_departamento[departamento] += salario

print(f"3. Salários totais por departamento: {salarios_por_departamento}")

avaliacoes = {
    "loja A": [8, 9, 7, 10, 6],
    "loja B": [5, 7, 6, 8, 7],
    "loja C": [9, 8, 9, 10, 9],
}

medias_satisfacao = {}

# 1. Calcule a média de satisfação de cada loja.
for loja, notas in avaliacoes.items():
    soma_notas = sum(notas)
    num_avaliacoes = len(notas)
    media = soma_notas / num_avaliacoes
    medias_satisfacao[loja] = media
    print(f"1. Média de satisfação da {loja}: {media:.2f}")

# 2. Descubra qual loja tem a maior média.
loja_maior_media = ""
maior_media = -1

for loja, media in medias_satisfacao.items():
    if media > maior_media:
        maior_media = media
        loja_maior_media = loja

print(f"2. Loja com a maior média de satisfação: {loja_maior_media} ({maior_media:.2f})")

# 3. Gere um dicionário só com as médias.
# (Já fizemos isso, é 'medias_satisfacao')
print(f"3. Dicionário de médias: {medias_satisfacao}")

vendas = [
    {"vendedor": "Marcos", "itens": {"notebook": 2, "mouse": 5}},
    {"vendedor": "Lucia", "itens": {"notebook": 1, "teclado": 3}},
    {"vendedor": "Paula", "itens": {"mouse": 4, "teclado": 2}},
]

# 1. Calcule quantos notebooks foram vendidos no total.
total_notebooks = 0
for venda in vendas:
    # Usa .get() com valor padrão 0 caso o item não esteja na venda
    total_notebooks += venda["itens"].get("notebook", 0)

print(f"1. Total de notebooks vendidos: {total_notebooks}")

# 2. Descubra qual vendedor vendeu mais itens no mês.
vendedor_mais_vendas = ""
max_itens_vendidos = -1

for venda in vendas:
    total_itens_vendedor = sum(venda["itens"].values())
    
    if total_itens_vendedor > max_itens_vendidos:
        max_itens_vendidos = total_itens_vendedor
        vendedor_mais_vendas = venda["vendedor"]

print(f"2. Vendedor que vendeu mais itens: {vendedor_mais_vendas} ({max_itens_vendidos} itens)")

# 3. Monte um dicionário consolidando o total de cada produto.
total_vendas_por_produto = {}

for venda in vendas:
    for produto, quantidade in venda["itens"].items():
        # Adiciona a quantidade ao total existente ou inicializa
        if produto not in total_vendas_por_produto:
            total_vendas_por_produto[produto] = 0
        
        total_vendas_por_produto[produto] += quantidade

print(f"3. Total de vendas por produto: {total_vendas_por_produto}")

produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Mouse", "preco": 80},
    {"nome": "Teclado", "preco": 150},
    {"nome": "Cadeira", "preco": 900},
]

classificacoes_precos = {}

for produto in produtos:
    nome = produto["nome"]
    preco = produto["preco"]
    
    if preco <= 100:
        classificacao = 'barato'
    elif 101 <= preco <= 1000:
        classificacao = 'médio'
    else: # preco > 1000
        classificacao = 'caro'
    
    classificacoes_precos[nome] = classificacao

print(f"Classificação de produtos por preço: {classificacoes_precos}")

funcionarios = [
    {"nome": "Ana", "nota": 9},
    {"nome": "Carlos", "nota": 6},
    {"nome": "Beatriz", "nota": 4}, 
    {"nome": "João", "nota": 7},
]

classificacoes_desempenho = {}

for func in funcionarios:
    nome = func["nome"]
    nota = func["nota"]
    
    if nota >= 8:
        classificacao = 'Excelente'
    elif 5 <= nota <= 7:
        classificacao = 'Regular'
    else: # nota < 5
        classificacao = 'Precisa melhorar'
        
    classificacoes_desempenho[nome] = classificacao

print(f"Classificação de desempenho dos funcionários: {classificacoes_desempenho}")

estoque = {
    "notebook": 3,
    "mouse": 25,
    "teclado": 8,
    "monitor": 2
}

print("--- Alerta de Estoque ---")

for produto, quantidade in estoque.items():
    if quantidade < 5:
        alerta = 'Estoque crítico'
    elif 5 <= quantidade < 10:
        alerta = 'Estoque baixo'
    else: # quantidade >= 10
        alerta = 'Estoque adequado'
    
    print(f"{produto}: {quantidade} unidades. Situação: **{alerta}**")

    vendas = [
    {"regiao": "Sul", "valor": 12000},
    {"regiao": "Norte", "valor": 8000},
    {"regiao": "Sudeste", "valor": 20000},
    {"regiao": "Centro-Oeste", "valor": 5000},
]

analise_vendas_regiao = []
meta = 10000

for venda in vendas:
    regiao = venda["regiao"]
    valor = venda["valor"]
    
    if valor >= meta:
        situacao = 'Meta atingida'
    else:
        situacao = 'Meta não atingida'
        
    # Cria o dicionário para a lista de resultado
    resultado = {
        "regiao": regiao,
        "situacao": situacao
    }
    
    analise_vendas_regiao.append(resultado)

print(f"Análise de vendas por região: {analise_vendas_regiao}")

compras = [
    {"cliente": "Maria", "valor": 450},
    {"cliente": "José", "valor": 1200},
    {"cliente": "Clara", "valor": 3000},
]

registro_compras_final = {}

for compra in compras:
    cliente = compra["cliente"]
    valor_original = compra["valor"]
    
    if valor_original < 500:
        taxa_desconto = 0.05  # 5%
    elif 500 <= valor_original < 2000:
        taxa_desconto = 0.10  # 10%
    else: # valor_original >= 2000
        taxa_desconto = 0.15  # 15%
        
    desconto = valor_original * taxa_desconto
    valor_final = valor_original - desconto
    
    registro_compras_final[cliente] = {
        "valor_original": valor_original,
        "desconto": round(desconto, 2), # Arredonda o desconto
        "valor_final": round(valor_final, 2) # Arredonda o valor final
    }

print(f"Registro de compras com descontos: {registro_compras_final}")

