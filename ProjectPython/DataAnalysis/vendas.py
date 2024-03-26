import yaml
import pandas as pd
import matplotlib.pyplot as plt

#Carregando os dados do YAML
with open('/home/alberto-linux/RepositoriosGitHub/Banheiras/ProjectPython/DataAnalysis/company.yaml', 'r') as file:
    data = yaml.safe_load(file)

#Convertendo os dados de vendas para um DataFrame
vendas_df = pd.DataFrame(data['vendas'])

# Convertendo a coluna 'data' para datetime 
vendas_df['data'] = pd.to_datetime(vendas_df['data'])

# Garantir que a quantidade é do tipo int
vendas_df['quantidade'] = vendas_df['quantidade'].astype(int)

# mês e produto/e somar as quantidades
vendas_por_mes_e_produto = vendas_df.groupby([pd.Grouper(key='data', freq='M'), 'produto']).agg({'quantidade': 'sum'}).reset_index()

# ter produtos como colunas e datas como linhas
vendas_pivot = vendas_por_mes_e_produto.pivot(index='data', columns='produto', values='quantidade').fillna(0)

#  gráfico
vendas_pivot.plot(kind='bar', figsize=(10, 6))
plt.title('Quantidade de Vendas por Produto e Mês')
plt.xlabel('Mês')
plt.ylabel('Quantidade de Vendas')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend(title='Produto')
plt.tight_layout()
plt.show()
