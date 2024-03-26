import yaml
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados do arquivo YAML
with open('empresa.yaml', 'r') as file:
    dados = yaml.safe_load(file)

# Criar DataFrames a partir dos dados
vendas_df = pd.DataFrame(dados['vendas'])
cliente_df = pd.DataFrame(dados['comportamento_do_cliente'])
produto_df = pd.DataFrame(dados['desempenho_do_produto'])

# Juntar os DataFrames de vendas e clientes
vendas_completo_df = vendas_df.merge(cliente_df, left_on='cliente_id', right_on='id')

# Criar gráfico de dispersão da idade dos clientes versus o valor gasto total
sns.scatterplot(data=vendas_completo_df, x='idade', y='valor_gasto_total', hue='sexo')
plt.title('Idade dos Clientes vs Valor Gasto Total')
plt.xlabel('Idade')
plt.ylabel('Valor Gasto Total')
plt.show()

# Criar gráfico de barras da receita total por produto
sns.barplot(data=produto_df, x='produto', y='receita_total')
plt.title('Receita Total por Produto')
plt.xlabel('Produto')
plt.ylabel('Receita Total')
plt.xticks(rotation=45)
plt.show()

# Criar gráfico de correlação entre idade do cliente e valor gasto total
sns.jointplot(data=vendas_completo_df, x='idade', y='valor_gasto_total', kind='reg')
plt.title('Correlação entre Idade e Valor Gasto Total')
plt.xlabel('Idade')
plt.ylabel('Valor Gasto Total')
plt.show()
