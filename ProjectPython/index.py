import tkinter as tk
from tkinter import ttk
#import


app = tk.Tk()
app.title('Análise de dados')
app.geometry('900x900') #largura - altura

nb = ttk.Notebook(app)

nb.place(x=0,y=0, width= 900, height=900)

tab1 = ttk.Frame(nb)
nb.add(tab1, text="Cursos")

tab2 = ttk.Frame(nb)
nb.add(tab2, text="Cursos 2")


lb1 = ttk.Label(tab1, text="a")
lb1.pack()
app.mainloop()