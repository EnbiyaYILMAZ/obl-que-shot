import pandas as pd

# Tablodaki verileri listeler şeklinde tanımlayalım
personel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
maaş = ['normal', 'yüksek', 'düşük','yüksek', 'düşük','yüksek', 'düşük','yüksek', 'düşük','yüksek', 'düşük']
deneyim = ['orta', 'yok', 'yok', 'orta', 'orta', 'iyi', 'iyi', 'orta', 'orta', 'iyi', 'iyi'] 
görev = ['uzman', 'uzman','yönetici', 'yönetici', 'yönetici', 'yönetici', 'yönetici', 'uzman', 'uzman', 'uzman', 'uzman']
memnun = ['evet', 'evet', 'evet', 'evet', 'evet', 'evet', 'evet', 'hayır', 'hayır', 'hayır', 'hayır']

# Verileri kullanarak bir sözlük oluşturalım
veriler = {
    'personel': personel,
    'maaş': maaş,
    'deneyim': deneyim,
    'görev': görev,
    'memnun': memnun
}

# Sözlüğü kullanarak bir veri çerçevesi oluşturalım
df = pd.DataFrame(veriler)

# Oluşturulan veri çerçevesini konsola yazdıralım
print(df)

