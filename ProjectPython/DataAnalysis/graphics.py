import pandas as pd
import matplotlib.pyplot as plt


#creating a data frame
data = {
    'Amount': [1, 2],
    'Sales per Month': ['Janeiro', 'Fevereiro'],
}

df = pd.DataFrame(data)

#plotting the graph

df.plot(x='Sales per Month', y='Amount', kind='bar')
plt.title('Sales throughout the month')
plt.xlabel('Amount')
plt.ylabel('Sales per Month')
plt.grid(True)
plt.show()