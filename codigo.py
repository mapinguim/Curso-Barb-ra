
from datetime import datetime

estoque = {}
historico_vendas = []

def consultar_estoque(produto):
    if produto in estoque:
      return True
    else:
      return False

repita = True
menu = ["cadastro", "consulta", "exibir estoque", "venda"]

while repita:
  print("\n Menu:")
  for i in menu:
    print(i)
  processo = input("Digite uma das opções ou 'fim' para encerrar: ")
  if processo.lower() == "cadastro":
    cadastro = True
    while cadastro:
      nome_prod = input("\n Digite o nome do produto ou 'finalizar' para encerrar o cadastro: ")
      if nome_prod.lower() == 'finalizar':
        cadastro = False
      elif consultar_estoque(nome_prod):
        print("\n Produto já cadastrado.")
      else:
        preco_prod = float(input("Digite o preço do produto: "))
        estoque_prod = int(input("Digite a quantidade em estoque do produto: "))
        estoque[nome_prod] = [preco_prod, estoque_prod]
        print("\n Produto cadastrado.")
  elif processo.lower() == "consulta":
    consulta = True
    while consulta:
      consulta_prod = input("Digite o produto para consulta ou 'fim': ")
      if consulta_prod.lower() == "fim":
        consulta = False
      else:
        if consulta_prod(nome_prod):
          print (f"\n {consulta_prod} - Preço: R${estoque[consulta_prod][0]} - Qtd: {estoque[consulta_prod][1]}")
        else:
          print("\n Produto não encontrado.")
  elif processo.lower() == "venda":
    venda = True
    total_venda = 0
    venda_atual = {} # acumula os dados "total", "produtos" ([nome,quantidade]) e "data" de cada venda iniciada
    produtos_venda_atual = [] #acumula os dados "nome" e "quantidade" de cada produto adicionado à venda
    while venda:
      nome_prod = input("\n Digite o nome do produto ou 'finalizar' para encerrar a venda: ")
      if nome_prod.lower() == 'finalizar':
        venda = False
      elif consultar_estoque(nome_prod):
        qtd_venda = int(input("Digite a quantidade desejada do produto: "))
        if qtd_venda > estoque[nome_prod][1]:
          print(f"Erro - quantidade disponível {estoque[nome_prod][1]}")
        else:
          valor_venda = qtd_venda * estoque[nome_prod][0]
          estoque[nome_prod][1] = estoque[nome_prod][1] - qtd_venda
          total_venda = total_venda + valor_venda #soma o valor total da venda com o valor do produto específico
          print(f"Total = R$ {total_venda:}")
          produtos_venda_atual.append([nome_prod, qtd_venda])
      else:
        print("Produto indisponível.")
    venda_atual["data"] = datetime.now().strftime("%B %d, %Y - %H:%M")
    venda_atual["total"] = total_venda
    venda_atual["produtos"] = produtos_venda_atual
    historico_vendas.append(venda_atual)
  elif processo.lower() == "exibir estoque":
    print("\n Estoque:")
    for produto in estoque:
      print(f"{produto} - Preço: {estoque[produto][0]} - Qtd: {estoque[produto][1]}")
  elif processo.lower() == 'fim':
    print("\n Processo encerrado.")
    repita = False

for i in historico_vendas:
  print(i)
