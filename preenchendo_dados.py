import yaml
import numpy as np

# Carregar o arquivo YAML
with open('empresa.yaml', 'r') as file:
    dados = yaml.safe_load(file)

# Função para calcular o valor_gasto_total e preencher os campos faltantes
def calcular_valor_gasto_total(cliente_id):
    for cliente in dados['comportamento_do_cliente']:
        if cliente['id'] == cliente_id:
            valor_gasto_total = sum([venda['quantidade'] * venda['preco_unitario'] for venda in dados['vendas'] if venda['cliente_id'] == cliente_id])
            cliente['valor_gasto_total'] = valor_gasto_total

# Preencher os campos faltantes de valor_gasto_total
for venda in dados['vendas']:
    if 'cliente_id' in venda:
        calcular_valor_gasto_total(venda['cliente_id'])

# Função para calcular as vendas_totais e receita_total por produto
def calcular_desempenho_produto(produto):
    vendas_totais = sum([venda['quantidade'] for venda in dados['vendas'] if venda['produto'] == produto])
    receita_total = sum([venda['quantidade'] * venda['preco_unitario'] for venda in dados['vendas'] if venda['produto'] == produto])
    return vendas_totais, receita_total

# Preencher os campos faltantes de vendas_totais e receita_total
for produto_info in dados['desempenho_do_produto']:
    vendas_totais, receita_total = calcular_desempenho_produto(produto_info['produto'])
    produto_info['vendas_totais'] = vendas_totais
    produto_info['receita_total'] = receita_total

# Salvar as alterações de volta no arquivo YAML
with open('empresa.yaml', 'w') as file:
    yaml.dump(dados, file)