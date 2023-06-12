import numpy as np

# Veriler
X1 = np.array([5.1, 4.9, 7, 6.4, 6.3, 5.8])
X2 = np.array([3.5, 3, 3.2, 3.2, 3.3, 2.7])
X3 = np.array([1.4, 1.4, 4.7, 4.5, 6, 5.1])
X4 = np.array([0.2, 0.2, 1.4, 1.5, 2.5, 1.9])
Y = np.array(['A', 'A', 'B', 'B', 'C', 'C'])

Y1 = np.array([1, 1, 0, 0, 0, 0])
Y2 = np.array([0, 0, 1, 1, 0, 0])
Y3 = np.array([0, 0, 0, 0, 1, 1])

# Çoklu Doğrusal Regresyon modeli
X = np.column_stack((np.ones_like(X1), X1, X2, X3, X4))
Y1_coef = np.linalg.lstsq(X, Y1, rcond=None)[0]
Y2_coef = np.linalg.lstsq(X, Y2, rcond=None)[0]
Y3_coef = np.linalg.lstsq(X, Y3, rcond=None)[0]

# Yeni örneğin tahminini yapma
Yeni = np.array([5, 3.4, 1.5, 0.2])
Yeni_X = np.concatenate(([1], Yeni))
Y1_pred = np.dot(Yeni_X, Y1_coef)
Y2_pred = np.dot(Yeni_X, Y2_coef)
Y3_pred = np.dot(Yeni_X, Y3_coef)

# Katsayıları yuvarlama
Y1_coef_rounded = np.round(Y1_coef, decimals=2)
Y2_coef_rounded = np.round(Y2_coef, decimals=2)
Y3_coef_rounded = np.round(Y3_coef, decimals=2)

print("Y1 katsayıları:", Y1_coef_rounded)
print("Y2 katsayıları:", Y2_coef_rounded)
print("Y3 katsayıları:", Y3_coef_rounded)
print("Y1 tahmini:", Y1_pred)
print("Y2 tahmini:", Y2_pred)
print("Y3 tahmini:", Y3_pred)
