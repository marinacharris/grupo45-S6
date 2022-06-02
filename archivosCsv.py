import pandas as pd
diccionario = {
    'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
    'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
    'age': [27, 31, 36, 53, 48, 36, 40, 34],
    'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
    'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]
}
df1 = pd.DataFrame(diccionario)
print(df1, '\n')
#Convertir dataframe a archivo .csv
df1.to_csv('C:/Users/robot/Documents/G45/S6/ejemploCsv.csv', sep='|', header= None)
#df1.to_csv('c:\\Users\\robot\\Documents\\G45\\S5\\ejemploCsv.csv')

#Leer un achivo csv
#pd.options.display.max_rows = 9999
df2 = pd.read_csv('casos_covid.csv')
print(df2)
df3 = pd.read_csv('C:/Users/robot/Documents/G45/S6/ejemploCsv.csv')
print(df3)
print(df2.head(10))
