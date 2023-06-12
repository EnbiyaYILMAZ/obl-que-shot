import pandas as pd

# Başlangıç bilgilerini tanımlama
T = 11
B_sol = [1, 5, 5, 2, 5, 4, 6, 5]
sinif_EVET = [1, 3, 3, 2, 3, 2, 2, 5]
sinif_HAYIR = [0, 2, 2, 0, 2, 2, 4, 0]

# Formüllere dayalı hesaplamaları yapma
P_Sol = [b / T for b in B_sol]
P_EVET_tSol = [s_ev / b for s_ev, b in zip(sinif_EVET, B_sol)]
P_HAYIR_tSol = [s_ha / b for s_ha, b in zip(sinif_HAYIR, B_sol)]

# Tabloyu içeren verileri oluşturma
data = {
    'Bölünme': range(1, 9),
    'B_sol': B_sol,
    'P_Sol': P_Sol,
    'sinif_EVET': sinif_EVET,
    'sinif_HAYIR': sinif_HAYIR,
    'P(EVET|t_Sol)': P_EVET_tSol,
    'P(HAYIR|tSol)': P_HAYIR_tSol
}

# Verileri DataFrame'e dönüştürme
df = pd.DataFrame(data)

# DataFrame'i ekrana yazdırma
print(df)






