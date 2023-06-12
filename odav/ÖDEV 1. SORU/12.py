import pandas as pd

data = {'Bölünme': [1, 2, 3, 4, 5, 6, 7, 8],
        'Koşul Sol Tarafta': ['Maaş = Normal', 'Maaş = Yüksek', 'Maaş = Düşük', 'Deneyim = Yok', 'Deneyim = Orta', 'Deneyim = İyi', 'Görev = Uzman', 'Görev = Yönetici'],
        'Koşul Sağ Tarafta': ['Maaş = Düşük, Yüksek', 'Maaş = Düşük, Normal', 'Maaş = Normal, Yüksek', 'Deneyim = Orta, İyi', 'Deneyim = Yok, İyi', 'Deneyim = Yok, Orta', 'Görev = Yönetici', 'Görev = Uzman']}

df = pd.DataFrame(data)

print(df)