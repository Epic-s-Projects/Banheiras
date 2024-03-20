import Pandas  as pd;
import yaml;
import DataFrame as df;


with open('empresa.yaml') as file:
    dados_yaml = yaml.safe_load(file)

# Converter para DataFrame
df = pd.DataFrame(dados_yaml['funcionarios'])
