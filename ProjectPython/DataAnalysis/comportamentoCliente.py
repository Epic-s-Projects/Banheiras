import yaml
import pandas as pd
import matplotlib.pyplot as plt

with open('/home/alberto-linux/RepositoriosGitHub/Banheiras/ProjectPython/DataAnalysis/company.yaml', 'r') as file:
    data = yaml.safe_load(file)

    vendas_df = pd.DataFrame(data['vendas'])


# Convertendo 'preco_unitario' para numérico, se necessário
vendas_df['preco_unitario'] = pd.to_numeric(vendas_df['preco_unitario'], errors='coerce')
# Plotando o gráfico de caixa para 'preco_unitario'
plt.figure(figsize=(10, 6))
plt.boxplot(vendas_df['preco_unitario'].dropna())
plt.title('Distribuição dos Preços dos Produtos')
plt.ylabel('Preço Unitário')
plt.xticks([1], ['Produtos'])  # Adicionando um rótulo no eixo x para clareza

# Mostrando o gráfico
plt.show()
