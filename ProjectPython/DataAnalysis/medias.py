import pandas as pd
import yaml
import matplotlib.pyplot as plt
import numpy as np

# Carregando dados do arquivo YAML
with open('/home/alberto-linux/RepositoriosGitHub/Banheiras/ProjectPython/DataAnalysis/company.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Criando DataFrame a partir da seção 'comportamento_do_cliente'
clientes_df = pd.DataFrame(data['comportamento_do_cliente'])

# Certifique-se de que 'idade' e 'valor_gasto_total' são numéricas
clientes_df['idade'] = pd.to_numeric(clientes_df['idade'], errors='coerce')
clientes_df['valor_gasto_total'] = pd.to_numeric(clientes_df['valor_gasto_total'], errors='coerce')

# Calculando estatísticas para a coluna 'idade'
estatisticas_idade = clientes_df['idade'].agg(['median', 'mean', 'min', 'max'])


# Preparando os dados para plotagem
estatisticas_plot = estatisticas_idade.reset_index()
estatisticas_plot.columns = ['Estatística', 'Valor']

# Plotando o gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(estatisticas_plot['Estatística'], estatisticas_plot['Valor'], color=['blue', 'orange', 'green', 'red'])

# Adicionando título e rótulos
plt.title('Estatísticas Descritivas da Idade')
plt.xlabel('Estatística')
plt.ylabel('Valor')
plt.xticks(rotation=45)  # Rotação dos rótulos para melhor visualização

# Mostrando o gráfico
plt.show()
# Calculando estatísticas para a coluna 'valor_gasto_total'
estatisticas_valor_gasto = clientes_df['valor_gasto_total'].agg(['median', 'mean', 'min', 'max'])
# Preparando os dados para plotagem
estatisticas_valor_gasto_plot = estatisticas_valor_gasto.reset_index()
estatisticas_valor_gasto_plot.columns = ['Estatística', 'Valor']

# Plotando o gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(estatisticas_valor_gasto_plot['Estatística'], estatisticas_valor_gasto_plot['Valor'], color=['blue', 'orange', 'green', 'red'])

# Adicionando título e rótulos
plt.title('Estatísticas Descritivas do Valor Gasto Total')
plt.xlabel('Estatística')
plt.ylabel('Valor')
plt.xticks(rotation=45)  # Rotação dos rótulos para melhor visualização

# Mostrando o gráfico
plt.show()
