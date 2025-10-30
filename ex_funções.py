# 1.
x_quadrado = lambda x: x**2
resultado = x_quadrado(4)
print(resultado)

# 2.
f1 = lambda x: 5*x -3
print(f1(2))

# 3.
f2 = lambda x: x**2 + 2*x +1
print("Se x = -1, o resultado é",f2(-1))
print("Se x = 0, o resultado é",f2(0))
print("Se x = 1, o resultado é",f2(1))

# 4.
f3 = lambda x, y: x**2 + 2*x*y + y**2
print(f3(2, 4))

# 5.
f4 = lambda x, y, z: x**y + z
print(f4(3, 2, 10))

# 6.
def lucro(receita, custo):
    return receita - custo
receita1 = 10000
custo1 = 7500
lucrocalculado = lucro(receita1, custo1)
print(lucrocalculado)

# 7.
def margem_lucro(receita, custo):
    lucro = receita - custo
    margem = (lucro / receita) *100
    return margem
receita2 = 20000
custo2 = 15000
margem_calculada = margem_lucro(receita2, receita1)
print(margem_calculada / 2,"%")

# 8.
def ponto_equilibrio(custo_fixo, preco, custo_variavel):
  margem_contribuicao = preco - custo_variavel
  if margem_contribuicao <= 0:
    return "Não é possível atingir o ponto de equilíbrio com esses valores."
  quantidade_equilibrio = custo_fixo / margem_contribuicao
  return quantidade_equilibrio
cf_teste = 5000
preco_teste = 50
cv_teste = 30
qe_calculado = ponto_equilibrio(cf_teste, preco_teste, cv_teste)
print(f"A quantidade de equilíbrio é: {qe_calculado} unidades")

# 9.
def folha(funcionarios):
  total_salarios = 0
  for funcionario in funcionarios:
    total_salarios += funcionario['salario']
  return total_salarios
lista_funcionarios = [
    {'nome': 'Ana', 'salario': 3000},
    {'nome': 'Carlos', 'salario': 4500}
]
total_folha = folha(lista_funcionarios)
print(f"O total da folha salarial é: R$ {total_folha}")

# 10. 
def juros_compostos(capital, taxa, tempo):
  montante = capital * (1 + taxa) ** tempo
  return montante
capital_teste = 1000
taxa_teste = 0.02
tempo_teste = 12
montante_calculado = juros_compostos(capital_teste, taxa_teste, tempo_teste)
print(f"O montante após {tempo_teste} períodos será de: R$ {montante_calculado:.2f}")
