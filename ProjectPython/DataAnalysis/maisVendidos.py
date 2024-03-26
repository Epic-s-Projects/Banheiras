import pandas as pd
import yaml
import matplotlib.pyplot as plt

# Carregando os dados do arquivo YAML
with open('/home/alberto-linux/RepositoriosGitHub/Banheiras/ProjectPython/DataAnalysis/company.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Criando DataFrame a partir da seção 'vendas'
vendas_df = pd.DataFrame(data['vendas'])

# Calculando a quantidade vendida por produto
produtos_quantidade = vendas_df.groupby('produto')['quantidade'].sum().sort_values(ascending=False)

# Calculando a receita por produto
vendas_df['receita'] = vendas_df['quantidade'] * vendas_df['preco_unitario']
receita_produto = vendas_df.groupby('produto')['receita'].sum().sort_values(ascending=False)

receita_por_produto = vendas_df.groupby('produto')['receita'].sum()

# Plotando gráfico de pizza para a distribuição da receita entre os produtos
receita_por_produto.plot(kind='pie', figsize=(10, 8), autopct='%1.1f%%', startangle=90)
plt.title('Distribuição da Receita por Produto')

# Ajustando a legenda para incluir os valores de receita
plt.legend(labels=[f'{produto}: ${valor:,.2f}' for produto, valor in receita_por_produto.items()], loc='upper left', bbox_to_anchor=(1, 1))

plt.ylabel('')  


# Plotando gráfico de barras para os produtos mais vendidos
plt.title('Produtos Mais Vendidos')
plt.xlabel('Produto')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45)
plt.show()
