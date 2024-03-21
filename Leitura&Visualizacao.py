import Pandas  as pd;
import yaml;
import DataFrame as df;


with open('empresa.yaml') as file:
    dados_yaml = yaml.safe_load(file)

# Converter para DataFrame
df = pd.DataFrame(dados_yaml['funcionarios'])

# import tkinter as tk
# from tkinter import ttk

# # Criando um janela
# janela = tk.Tk()
# janela.title("Teste Abas")

# def selecionando_tabela(event):
#     selected_tab = controle_tab.index(controle_tab.select())
    
# # Notebook é utilizado como controle entre as abas
# controle_tab = ttk.Notebook(janela)
    
# # Criando abas (podendo ter o controle delas)
# tab1 = ttk.Frame(controle_tab)
# tab2 = ttk.Frame(controle_tab)
# tab3 = ttk.Frame(controle_tab)

# controle_tab.add(tab1, text='Tab 1')
# controle_tab.add(tab2, text='Tab 2')
# controle_tab.add(tab3, text='Tab 3')

# # Adiciona um evento para quando uma aba é selecionada
# controle_tab.bind(selecionando_tabela)

# # Adiciona widgets às abas
# label1 = tk.Label(tab1, text="Conteúdo da Tab 1")
# label1.pack(padx=10, pady=10)

# label2 = tk.Label(tab2, text="Conteúdo da Tab 2")
# label2.pack(padx=10, pady=10)

# label3 = tk.Label(tab3, text="Conteúdo da Tab 3")
# label3.pack(padx=10, pady=10)
         
# # Exibe o controle de abas
# controle_tab.pack(expand=1, fill="both")

# janela.mainloop()
