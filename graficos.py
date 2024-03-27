import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import yaml

# Carregar dados YAML para um DataFrame do Pandas
with open("empresa.yaml", "r") as file:
    dados = yaml.safe_load(file)

# Converter seção 'vendas' para DataFrame
vendas_df = pd.DataFrame(dados['vendas'])

# Converter a coluna 'data' para o tipo datetime
vendas_df['data'] = pd.to_datetime(vendas_df['data'])

# Extrair o mês e o ano da data
vendas_df['ano_mes'] = vendas_df['data'].dt.to_period('M')

# Contagem de vendas por mês e ano
vendas_por_ano_mes = vendas_df.groupby('ano_mes').size()

# Calcular estatísticas descritivas básicas para as colunas numéricas
estatisticas_descritivas = vendas_df.describe()

# Identificar os produtos mais vendidos
desempenho_df = pd.DataFrame(dados['desempenho_do_produto'])
desempenho_df.set_index('produto', inplace=True)
produtos_mais_vendidos = desempenho_df['vendas_totais'].copy()  # Inicializar a variável

# Combinação de dados com o método combine_first()
produtos_mais_vendidos = produtos_mais_vendidos.combine_first(desempenho_df['vendas_totais'])

# Calcular a receita total gerada por cada produto
vendas_df['receita'] = vendas_df['quantidade'] * vendas_df['preco_unitario']
receita_por_produto = vendas_df.groupby('produto')['receita'].sum()

# Criar função para plotar os gráficos dentro das abas
def plotar_graficos():
    # Criar janela principal
    root = tk.Tk()
    root.title("Análise de Vendas")

    # Criar abas
    abas = ttk.Notebook(root)

    # Aba para a contagem de vendas por mês
    aba_vendas_por_mes = ttk.Frame(abas)
    abas.add(aba_vendas_por_mes, text='Vendas por Mês')

    # Gráfico de barras para contagem de vendas por mês
    fig1 = plt.figure(figsize=(8, 6))
    vendas_por_ano_mes.plot(kind='bar', color='skyblue')
    plt.title('Contagem de Vendas por Mês')
    plt.xlabel('Mês e Ano')
    plt.ylabel('Número de Vendas')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    canvas1 = FigureCanvasTkAgg(fig1, master=aba_vendas_por_mes)
    canvas1.draw()
    canvas1.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Aba para as estatísticas descritivas
    aba_estatisticas = ttk.Frame(abas)
    abas.add(aba_estatisticas, text='Estatísticas Descritivas')

    # Exibir as estatísticas descritivas em uma caixa de texto
    txt_estatisticas = tk.Text(aba_estatisticas)
    txt_estatisticas.insert(tk.END, estatisticas_descritivas)
    txt_estatisticas.config(state='disabled')
    txt_estatisticas.pack(fill=tk.BOTH, expand=True)

    # Aba para os produtos mais vendidos
    aba_produtos_mais_vendidos = ttk.Frame(abas)
    abas.add(aba_produtos_mais_vendidos, text='Produtos Mais Vendidos')

    # Gráfico de barras para produtos mais vendidos
    fig2 = plt.figure(figsize=(8, 6))
    produtos_mais_vendidos.plot(kind='bar', color='skyblue')
    plt.title('Produtos Mais Vendidos')
    plt.xlabel('Produto')
    plt.ylabel('Quantidade Vendida')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.yticks(range(0, produtos_mais_vendidos.max() + 5, 5))  # Definindo os limites do eixo y com incrementos de 5
    canvas2 = FigureCanvasTkAgg(fig2, master=aba_produtos_mais_vendidos)
    canvas2.draw()
    canvas2.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Aba para a distribuição da receita por produto
    aba_distribuicao_receita = ttk.Frame(abas)
    abas.add(aba_distribuicao_receita, text='Distribuição da Receita')

    # Gráfico de pizza para distribuição da receita
    fig3 = plt.figure(figsize=(8, 8))
    plt.pie(receita_por_produto, labels=receita_por_produto.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
    plt.title('Distribuição da Receita por Produto')
    plt.axis('equal')
    canvas3 = FigureCanvasTkAgg(fig3, master=aba_distribuicao_receita)
    canvas3.draw()
    canvas3.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # aba para analise temporal
    aba_analise_temporal = ttk.Frame(abas)
    abas.add(aba_analise_temporal, text='Evolução das Vendas')

    # Gráfico de linha para evolução das vendas ao longo do tempo
    fig4 = plt.figure(figsize=(8, 6))
    plt.plot(vendas_por_ano_mes.index.to_timestamp(), vendas_por_ano_mes.values, color='green')
    plt.title('Evolução das Vendas ao Longo do Tempo')
    plt.xlabel('Data')
    plt.ylabel('Número de Vendas')
    plt.grid(True)
    canvas4 = FigureCanvasTkAgg(fig4, master=aba_analise_temporal)
    canvas4.draw()
    canvas4.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Adicionar abas à janela principal
    abas.pack(fill=tk.BOTH, expand=True)

    # Iniciar loop principal da interface gráfica
    root.mainloop()

# Chamar a função para plotar os gráficos dentro das abas
plotar_graficos()