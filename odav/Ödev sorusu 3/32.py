import pandas as pd
import math

# Verileri içeren DataFrame oluşturma
data = {
    'X': [1, 2, 2, 3, 4, 5, 6, 8, 10, 11],
    'Y': [3, 5, 3, 9, 7, 2, 8, 6, 6, 1],
    'Z': ['Negatif', 'Pozitif', 'Pozitif', 'Negatif', 'Negatif', 'Pozitif', 'Pozitif', 'Negatif', 'Negatif', 'Negatif']
}

df = pd.DataFrame(data)

# Yeni veri değerlerini belirleme
new_X = 7
new_Y = 3

# Öklid mesafesi hesaplama ve atama
df['Uzaklık'] = df.apply(lambda row: math.sqrt((row['X'] - new_X) ** 2 + (row['Y'] - new_Y) ** 2), axis=1)

# Yakınlık sırasını hesaplayarak atama
df['Rank'] = df['Uzaklık'].rank()

# En yakın 3 komşuyu belirleme
nearest_neighbors = df.nsmallest(3, 'Uzaklık')

# Sınıfın çoğunluğunu belirleme
class_label = nearest_neighbors['Z'].mode()[0]

print(f"Yeni örnek sınıfı: {class_label}")
