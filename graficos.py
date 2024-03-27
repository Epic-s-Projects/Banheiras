from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import yaml
import seaborn as sns

# Carregar dados do arquivo YAML
with open('empresa.yaml', 'r') as file:
    dados_empresa = yaml.safe_load(file)

# Converter para DataFrame
df_vendas = pd.DataFrame(dados_empresa['vendas'])

# Converter a coluna 'data' para o tipo datetime
df_vendas['data'] = pd.to_datetime(df_vendas['data'])

# Extrair o mês de cada venda
df_vendas['mes'] = df_vendas['data'].dt.month

# Calcular a soma das quantidades vendidas por mês
total_vendas_por_mes = df_vendas.groupby('mes')['quantidade'].sum()

# Criar lista com os meses de janeiro a dezembro
meses = range(1, 13)

# Preencher com zeros os meses sem vendas
total_vendas_por_mes = total_vendas_por_mes.reindex(meses, fill_value=0)

# Identificar os três maiores valores
top3_indices = total_vendas_por_mes.sort_values(ascending=False).index[:3]

# Verificar se há empate entre os três maiores valores
if len(set(total_vendas_por_mes[top3_indices])) == 1:
    top3_indices = total_vendas_por_mes.index[:3]

# Plotar o gráfico de barras mostrando o total de vendas por mês
def plot_total_vendas():
    cores = ['red' if v < total_vendas_por_mes.median() else 'yellow' if i in top3_indices else 'green' for i, v in enumerate(total_vendas_por_mes.values)]
    plt.bar(total_vendas_por_mes.index, total_vendas_por_mes.values, color=cores, edgecolor='black')
    plt.title('Total de Vendas por Mês')
    plt.xlabel('Mês')
    plt.ylabel('Total de Vendas')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

# Calcular estatísticas descritivas básicas
estatisticas_descritivas = df_vendas.describe()

# Verificar valores ausentes no conjunto de dados
valores_ausentes = df_vendas.isnull().sum()

print(estatisticas_descritivas)
print(valores_ausentes)

# Dados sobre o desempenho dos produtos
desempenho_produto = """
desempenho_do_produto:
  - produto: Banheira
    vendas_totais: 32
    receita_total: 80000.0
  - produto: Ofuro
    vendas_totais: 41
    receita_total: 123000.0
  - produto: Spa
    vendas_totais: 37
    receita_total: 185000.0
"""

# Carregar dados sobre o desempenho dos produtos do YAML
dados_desempenho_produto = yaml.safe_load(desempenho_produto)

# Extrair informações sobre os produtos
produtos = [produto['produto'] for produto in dados_desempenho_produto['desempenho_do_produto']]
vendas_totais = [produto['vendas_totais'] for produto in dados_desempenho_produto['desempenho_do_produto']]
receita_total = [produto['receita_total'] for produto in dados_desempenho_produto['desempenho_do_produto']]

# Identificar os produtos mais vendidos
produto_mais_vendido = produtos[vendas_totais.index(max(vendas_totais))]

# Plotar um gráfico de barras mostrando os produtos mais vendidos
def plot_produtos_mais_vendidos():
    plt.bar(produtos, vendas_totais, color='skyblue')
    plt.title('Produtos Mais Vendidos')
    plt.xlabel('Produto')
    plt.ylabel('Vendas Totais')
    plt.xticks(rotation=45)
    plt.tight_layout()

# Plotar um gráfico de pizza mostrando a distribuição da receita entre os produtos
def plot_distribuicao_receita():
    plt.pie(receita_total, labels=produtos, autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue', 'lightgreen'])
    plt.title('Distribuição da Receita por Produto')
    plt.axis('equal')
    plt.tight_layout()

# Extrair o ano de cada venda
df_vendas['ano'] = df_vendas['data'].dt.year

# Extrair informações sobre o comportamento do cliente
gastos_totais = [cliente['valor_gasto_total'] for cliente in dados_empresa['comportamento_do_cliente']]

# Calcular os intervalos para o histograma
intervalos = np.arange(0, max(gastos_totais) + 10000, 10000)

# Plotar o histograma dos gastos dos clientes
def plot_histograma_gastos():
    plt.hist(gastos_totais, bins=intervalos, edgecolor='black', color='skyblue')
    plt.title('Histograma dos Gastos dos Clientes')
    plt.xlabel('Valor Gasto Total (R$)')
    plt.ylabel('Número de Clientes')
    plt.xticks(intervalos)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

# Processar dados das vendas para calcular valor total gasto e frequência de compras por cliente
total_gasto_por_cliente = {}
frequencia_de_compras = {}

for venda in dados_empresa['vendas']:
    cliente_id = venda['cliente_id']
    preco_total = venda['quantidade'] * venda['preco_unitario']
    
    total_gasto_por_cliente[cliente_id] = total_gasto_por_cliente.get(cliente_id, 0) + preco_total
    frequencia_de_compras[cliente_id] = frequencia_de_compras.get(cliente_id, 0) + 1

# Ordenar clientes por valor total gasto
clientes_ordenados = sorted(total_gasto_por_cliente.items(), key=lambda x: x[1], reverse=True)[:5]

# Obter os nomes dos clientes
nomes_clientes = [dados_empresa['comportamento_do_cliente'][cliente_id - 101]['nome'] for cliente_id, _ in clientes_ordenados]

# Preparar dados para o gráfico de dispersão
valores_gastos = [total_gasto for cliente_id, total_gasto in clientes_ordenados]
frequencia_compras = [frequencia_de_compras[cliente_id] for cliente_id, _ in clientes_ordenados]

# Plotar o gráfico de dispersão
def plot_dispersao_fieis():
    plt.scatter(valores_gastos, frequencia_compras, color='blue', alpha=0.7)

    # Adicionar os nomes dos clientes ao gráfico
    for nome, valor_gasto, frequencia in zip(nomes_clientes, valores_gastos, frequencia_compras):
        plt.text(valor_gasto, frequencia, nome, fontsize=9)

    plt.title('Valor Total Gasto vs Frequência de Compras dos 5 Clientes Mais Fiéis')
    plt.xlabel('Valor Total Gasto (R$)')
    plt.ylabel('Frequência de Compras')
    plt.grid(True)
    plt.tight_layout()

# Dicionário para armazenar preços por produto
precos_por_produto = {}

# Organizar os preços por produto
for venda in dados_empresa['vendas']:
    produto = venda['produto']
    preco = venda['preco_unitario']
    # Ajustar nome do produto para considerar caracteres especiais
    produto = produto.lower().capitalize()
    if produto not in precos_por_produto:
        precos_por_produto[produto] = [preco]
    else:
        precos_por_produto[produto].append(preco)

# Lista de preços para cada produto
precos_banheira = precos_por_produto['Banheira']
precos_ofuro = precos_por_produto['Ofuro']
precos_spa = precos_por_produto['Spa']

# Unir todos os preços em uma lista para calcular a média
todos_os_precos = precos_banheira + precos_ofuro + precos_spa

# Calcular preço médio
preco_medio = sum(todos_os_precos) / len(todos_os_precos)

def distribuicao_precos():
    # plt.figure(figsize=(10, 6))
    boxprops = dict(facecolor='lightblue', color='blue')
    medianprops = dict(color='red')
    meanprops = dict(marker='o', markerfacecolor='yellow', markeredgecolor='black', markersize=10)
    plt.boxplot([precos_banheira, precos_ofuro, precos_spa], labels=['Banheira', 'Ofuro', 'Spa'], patch_artist=True, showmeans=True, meanline=True, boxprops=boxprops, medianprops=medianprops, meanprops=meanprops)
    plt.text(2, preco_medio, f'Média Geral: R${preco_medio:.2f}', fontsize=10, ha='center', va='bottom', color='blue')
    plt.title('Distribuição de Preços dos Produtos', fontsize=16)
    plt.xlabel('Produto', fontsize=14)
    plt.ylabel('Preço (R$)', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()


# Processar os dados para calcular as vendas mensais
vendas_mensais = {}
for venda in dados_empresa['vendas']:
    data_venda = datetime.strptime(venda['data'], '%Y-%m-%d')
    mes_venda = data_venda.strftime('%Y-%m')
    quantidade = venda['quantidade']
    if mes_venda in vendas_mensais:
        vendas_mensais[mes_venda] += quantidade
    else:
        vendas_mensais[mes_venda] = quantidade

# Ordenar as vendas mensais por data
vendas_mensais = dict(sorted(vendas_mensais.items()))

# Extrair as datas e quantidades para plotagem
datas = list(vendas_mensais.keys())
quantidades = list(vendas_mensais.values())

def evolucao_vendas():
    plt.plot(datas, quantidades, marker='o', color='b', linestyle='-')
    plt.title('Evolução das Vendas Mensais')
    plt.xlabel('Mês')
    plt.ylabel('Quantidade Vendida')
    plt.xticks(rotation=45)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()


# gráficos mais avançados
# Criar DataFrames a partir dos dados
vendas_df = pd.DataFrame(dados_empresa['vendas'])
cliente_df = pd.DataFrame(dados_empresa['comportamento_do_cliente'])
produto_df = pd.DataFrame(dados_empresa['desempenho_do_produto'])

# Juntar os DataFrames de vendas e clientes
vendas_completo_df = vendas_df.merge(cliente_df, left_on='cliente_id', right_on='id')

def grafico_avancado():
    # Criar gráfico de dispersão da idade dos clientes versus o valor gasto total
    sns.scatterplot(data=vendas_completo_df, x='idade', y='valor_gasto_total', hue='sexo')
    plt.title('Idade dos Clientes vs Valor Gasto Total')
    plt.xlabel('Idade')
    plt.ylabel('Valor Gasto Total')
    plt.tight_layout()

# Criação da interface gráfica com Tkinter
root = tk.Tk()
root.title("Gráficos da Empresa")

# Criar e posicionar os botões das abas
aba_frame = tk.Frame(root)
aba_frame.pack(side="top", fill="x")

# Dicionário com os gráficos
graficos = {
    "Total de Vendas por Mês": plot_total_vendas,
    "Produtos Mais Vendidos": plot_produtos_mais_vendidos,
    "Distribuição da Receita por Produto": plot_distribuicao_receita,
     "Evolução das Vendas": evolucao_vendas,
    "Histograma dos Gastos dos Clientes": plot_histograma_gastos,
    "5 Clientes Mais Fiéis": plot_dispersao_fieis,
    "Distribuicao de preço": distribuicao_precos,
    "Gráfico Avançado": grafico_avancado
}


for nome_grafico in graficos:
    button = tk.Button(aba_frame, text=nome_grafico, command=lambda g=nome_grafico: mostrar_grafico(g))
    button.pack(side="left")

# Container para os gráficos
container = tk.Frame(root)
container.pack(side="top", fill="both", expand=True)

# Função para mostrar o gráfico selecionado
def mostrar_grafico(grafico):
    plt.clf()
    graficos[grafico]()
    canvas.draw()

# Criação do plot inicial
fig, ax = plt.subplots()
graficos_iniciais = plot_total_vendas()

# Integração do plot inicial na interface Tkinter
canvas = FigureCanvasTkAgg(fig, master=container)
canvas.draw()
canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

root.mainloop()
