import pandas as pd
import yaml
import matplotlib.pyplot as plt

# Carregando dados do arquivo YAML
with open('/home/alberto-linux/RepositoriosGitHub/Banheiras/ProjectPython/DataAnalysis/company.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Criando DataFrame a partir da seção 'vendas'
vendas_df = pd.DataFrame(data['vendas'])

# Convertendo a coluna 'data' para o formato de data
vendas_df['data'] = pd.to_datetime(vendas_df['data'])

# Calculando a coluna 'receita'
vendas_df['receita'] = vendas_df['quantidade'] * vendas_df['preco_unitario']

# Calculando a receita total por data
receita_por_data = vendas_df.groupby('data')['receita'].sum()

# Ordenando as vendas por data
receita_por_data = receita_por_data.sort_index()

# Plotando gráfico de linha para a evolução da receita ao longo do tempo
plt.figure(figsize=(12, 6))
plt.plot(receita_por_data.index, receita_por_data.values, marker='o', linestyle='-', color='b')

# Adicionando título e rótulos
plt.title('Evolução da Receita ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Receita Total')
plt.xticks(rotation=45)

# Mostrando o gráfico
plt.show()
