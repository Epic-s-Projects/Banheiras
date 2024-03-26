import seaborn as sns
import pandas as pd
import yaml
import matplotlib.pyplot as plt


with open('/home/alberto-linux/RepositoriosGitHub/Banheiras/ProjectPython/DataAnalysis/company.yaml', 'r') as file:
    data = yaml.safe_load(file)

    df = pd.DataFrame(data['vendas'])
# Cria um gráfico de dispersão com coloração baseada em 'categoria'
sns.scatterplot(data=df, x='produto', y='quantidade', hue='preco_unitario')

# Adicionando título e rótulos
plt.title('Gráfico de Dispersão com Categorias')
plt.xlabel('Variável X')
plt.ylabel('Variável Y')

# Mostrando o gráfico
plt.show()
# Calculando a matriz de correlação
correlacao = df.corr()

# Criando um mapa de calor para a matriz de correlação
plt.figure(figsize=(10, 8))
sns.heatmap(correlacao, annot=True, cmap='coolwarm', fmt=".2f")

# Adicionando título
plt.title('Mapa de Calor de Correlação')

# Mostrando o gráfico
plt.show()
