import pandas as pd
import yaml
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

# Carregar dados do arquivo YAML
with open('empresa.yaml') as file:
    dados_yaml = yaml.safe_load(file)

# Converter para DataFrame
df = pd.DataFrame(dados_yaml['vendas'])
# Converter a coluna 'data' para o tipo datetime
df['data'] = pd.to_datetime(df['data'])
# Exatrair mês e ano da data
df['ano_mes'] = df['data'].dt.to_period('M')

vendas_por_ano_mes = df.groupby('ano_mes').size()

# Criando um janela
janela = tk.Tk()
janela.title("Teste Abas")

def grafico_evolucao_temporal():
    # Criando o frame para o gráfico
    frame_grafico = tk.Frame(abas)

    # Criando o gráfico
    fig = plt.Figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.plot(vendas_por_ano_mes.index.to_timestamp(), vendas_por_ano_mes.values, color='green')
    ax.set_title("Evolução de vendas")
    ax.set_xlabel('Data')
    ax.set_ylabel('Número de Vendas')

    # Colocando o gráfico no frame
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    return frame_grafico

# Notebook é utilizado como controle entre as abas
abas = ttk.Notebook(janela)
    
# Criando abas (podendo ter o controle delas)
tab1 = ttk.Frame(abas)
tab2 = ttk.Frame(abas)
tab3 = ttk.Frame(abas)

abas.add(tab1, text='Venda Mensal')
abas.add(tab2, text='Estatísticas Descritivas')
abas.add(tab3, text='Produtos mais Vendidos')

# Adicionando o frame retornado pela função grafico_evolucao_temporal como conteúdo da aba
abas.add(grafico_evolucao_temporal(), text='Analise Temporal das Vendas')

# Adiciona widgets às abas
label1 = tk.Label(tab1, text="Conteúdo da Tab 1")
label1.pack(padx=10, pady=10)

label2 = tk.Label(tab2, text="Conteúdo da Tab 2")
label2.pack(padx=10, pady=10)

label3 = tk.Label(tab3, text="Conteúdo da Tab 3")
label3.pack(padx=10, pady=10)

# Exibe o controle de abas
abas.pack(expand=1, fill="both")

janela.mainloop()
