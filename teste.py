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

import seaborn as sns
import matplotlib.pyplot as plt

# Heatmap de Correlação entre Variáveis
correlation_matrix = vendas_completo_df[['idade', 'quantidade', 'valor_gasto_total']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap de Correlação entre Variáveis')
plt.show()

# Distribuição de Idade dos Clientes por Cidade
plt.figure(figsize=(10, 6))
sns.violinplot(data=vendas_completo_df, x='cidade', y='idade')
plt.title('Distribuição de Idade dos Clientes por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Idade')
plt.xticks(rotation=45)
plt.show()

# Valor Gasto Total por Produto
plt.figure(figsize=(10, 6))
sns.barplot(data=produto_df, x='produto', y='receita_total')
plt.title('Valor Gasto Total por Produto')
plt.xlabel('Produto')
plt.ylabel('Valor Gasto Total')
plt.xticks(rotation=45)
plt.show()

# Distribuição de Valor Gasto Total por Sexo do Cliente
plt.figure(figsize=(10, 6))
sns.barplot(data=vendas_completo_df, x='sexo', y='valor_gasto_total', estimator=sum)
plt.title('Valor Gasto Total por Sexo do Cliente')
plt.xlabel('Sexo')
plt.ylabel('Valor Gasto Total')
plt.show()
