import pandas as pd

data = {'Makanan': ['baso', 'mie goreng', 'mie rebus', 'basreng'],
        'Harga': [10000, 10000, 8000, 5000]}
index = ['1', '2', '3', '4']
index = ['1', '2', '3', '4']
df = pd.DataFrame(data, index=index)

df['Harga'] = df['Harga'] + 5000 # pertambahan
print(df)
print('\n')

df['Harga'] = df['Harga'] - 500 # pengurangan
print(df)
print('\n')

df['Harga'] = df['Harga'] * 2 # perkalian
print(df)
print('\n')

df['Harga'] = df['Harga'] / 2 # pembagian
print(df)
print('\n')
