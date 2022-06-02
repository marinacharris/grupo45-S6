import pandas as pd
import numpy as np
inventario = {
    'Impresoras': ['Canon', 'Hp', 'Epson'],
    'Cantidad': [10,8,15]
}
print(inventario, '\n')
df1 = pd.DataFrame(inventario, index=['P1','P2','P3'])
print(df1, '\n')
print(df1.iloc[1])
print(df1.loc['P1'])

# crear una matriz de 3*3 con numpy
arreglo = np.array([[4,5,8],[3,8,2],[3,25,8]])
print(arreglo, '\n')
df2 = pd.DataFrame(arreglo, columns=['Juan','Ana','Lía'], index=['Enero','Febrero','Marzo'])
print(df2, '\n')
print(df2.loc['Enero'])
print(df2.columns)
print(df2.iloc[1])



