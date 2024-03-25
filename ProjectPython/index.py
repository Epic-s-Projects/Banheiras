import tkinter as tk
from tkinter import ttk
from turtle import title
from matplotlib.figure import Figure
import pandas as pd
import matplotlib.pyplot as plt
import yaml


#installing PyYAML


app = tk.Tk()
app.title('Análise de dados')
app.geometry('900x900') #largura - altura

nb = ttk.Notebook(app)

nb.place(x=0,y=0, width= 900, height=900)

tab1 = ttk.Frame(nb)
nb.add(tab1, text="Cursos")

tab2 = ttk.Frame(nb)
nb.add(tab2, text="Cursos 2")


lb1 = ttk.Label(tab1, text="a")
lb1.pack()
app.mainloop()

def mostrar_venda_mes():
    with open('/home/alberto-linux/RepositoriosGitHub/Banheiras/ProjectPython/DataAnalysis/company.yaml', 'r') as file:
        # Carrega os dados do arquivo
        dataCompany = yaml.safe_load(file)

    # Cria o DataFrame
    vendas_df = pd.DataFrame(dataCompany['vendas'])
    vendas_df['data'] = pd.to_datetime(vendas_df['data'])
    vendas_df['quantidade'] = vendas_df['quantidade'].astype(int)
    
    # Processamento dos dados
    vendas_por_mes_e_produtos = vendas_df.groupby([pd.Grouper(key='data', freq='M'), 'produto']).agg({'quantidade': 'sum'}).reset_index()
    vendas_pivot = vendas_por_mes_e_produtos.pivot(index='data', columns='produto', values='quantidade').fillna(0)
    
    # Cria a figura do gráfico
    fig = Figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    vendas_pivot.plot(kind='bar', ax=ax)
    ax.set_title('Vendas por Mês')
    ax.set_xlabel('Mês')
    ax.set_ylabel('Vendas do mês')
    ax.legend(title='Produto')
    ax.grid(True)
    
    # Retorna a figura
    return fig


def calcular_media():
        with open('/home/alberto-linux/RepositoriosGitHub/Banheiras/ProjectPython/DataAnalysis/company.yaml', 'r') as file:
            data = yaml.safe_load(file)

            vendas_df = pd.DataFrame(data['vendas'])
            estatisticas = vendas_df.describe()
            print(estatisticas)
            valores_ausentes = vendas_df.isnull().sum()
            print(valores_ausentes)
            #calculando médias da idade
            idade_media = vendas_df['idade'].mean()
            idade_mediana = vendas_df['idade'].median()
            idade_minima = vendas_df['idade'].min()
            idade_maxima = vendas_df['idade'].max()
            #calculando média de valores gastos
            valor_gast_media = vendas_df['valor_gasto_total'].mean()
            valor_gast_media = vendas_df['valor_gasto_total'].median()
            valor_gast_media = vendas_df['valor_gasto_total'].min()
            valor_gast_media = vendas_df['valor_gasto_total'].max()

def remover_valores_nulos():
     with open('/home/alberto-linux/RepositoriosGitHub/Banheiras/ProjectPython/DataAnalysis/company.yaml', 'r') as file:
            data = yaml.safe_load(file)

            vendas_df = pd.DataFrame(data['vendas'])
     for coluna in vendas_df.select_dtypes(include=['float', 'int']).columns:
        vendas_df[coluna].fillna(vendas_df[coluna].mean(), inplace=True)
