import numpy as np
import pandas as pd


data = {
        'Nama': ['Kim', 'Vachirawit', 'Kasim', 'Xaviera', 'Putri', 'Vici', 'Kais', 'Kitty', 'Dul', 'Al'],
        'Tinggi Badan': [150, 161, 152, 163, 160, 169, 155, 154, 170, 171]
        }

nomor = ['1', '2', '3','4','5','6','7','8','9','10']
df = pd.DataFrame(data, index=nomor)

# Menampilkan semua data
print("Semua data:")
print(df)
print('\n')

# Menampilkan 5 data teratas
print("5 data teratas:")
print(df.head())
print('\n')

# Menampilkan 5 data terbawah
print("5 data terbawah:")
print(df.tail())
