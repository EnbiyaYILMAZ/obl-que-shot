import pandas as pd
B_sol = [1, 5, 5, 2, 5, 4, 6, 5]
B_sağ = [10, 6, 6, 9, 6, 7, 5, 6]
P_sol = [0.09, 0.45, 0.45, 0.18, 0.45, 0.36, 0.55, 0.45]
P_sağ = [0.91, 0.55, 0.55, 0.82, 0.55, 0.64, 0.45, 0.55]
T = 11
sinif_EVET = [0.6, 0.67, 0.67, 0.56, 0.67, 0.71, 1, 0.33]
sinif_HAYIR = [0.4, 0.33, 0.33, 0.44, 0.33, 0.29, 0, 0.67]

P_sol = [B / T for B in P_sol]
P_sağ = [B / T for B in P_sağ]
P_solP_sağ = [2 * P_sol[i] * P_sağ[i] for i in range(len(P_sol))]

P_EVET_tSol = [abs((sinif / B) - (sinif / sum(P_sağ))) for sinif, B in zip(sinif_EVET, P_sol)]
P_HAYIR_tSol = [abs((sinif / B) - (sinif / sum(P_sağ))) for sinif, B in zip(sinif_HAYIR, P_sol)]

uygunluk = [P_solP_sağ[i] * sum([abs((sinif / P_sol[i]) - (sinif / P_sağ[i])) for sinif in [sinif_EVET[j], sinif_HAYIR[j]]]) for i, j in enumerate(range(len(P_sol)))]

data = {
    'P_sol': P_sol,
    'P_sağ': P_sağ,
    '2P_solP_sağ': P_solP_sağ,
    'Φ(B|d)': uygunluk
}

df = pd.DataFrame(data)
print(df)
