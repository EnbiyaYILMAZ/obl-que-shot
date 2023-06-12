import pandas as pd

data = {
    'age': ['genç', 'genç', 'orta yaşlı', 'yaşlı', 'yaşlı', 'yaşlı', 'orta yaşlı', 'genç', 'genç', 'yaşlı', 'genç', 'orta yaşlı', 'orta yaşlı', 'yaşlı'],
    'income': ['high', 'high', 'high', 'medium', 'low', 'low', 'low', 'medium', 'low', 'medium', 'medium', 'medium', 'high', 'medium'],
    'student': ['no', 'no', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'no', 'no'],
    'credit_rating': ['fair', 'excellent', 'fair', 'fair', 'fair', 'excellent', 'excellent', 'fair', 'fair', 'fair', 'excellent', 'excellent', 'fair', 'excellent'],
    'buying_computer': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']
}

df = pd.DataFrame(data)

# Sınıf olasılıklarını hesapla
P_C_yes = df['buying_computer'].value_counts()['yes'] / len(df)
P_C_no = df['buying_computer'].value_counts()['no'] / len(df)

# Koşullu olasılıkları hesapla
P_X_given_C_yes = (2/9) * (4/9) * (6/9) * (6/9)
P_X_given_C_no = (3/5) * (2/5) * (1/5) * (2/5)

# Bayes formülünü uygula
P_C_yes_given_X = P_X_given_C_yes * P_C_yes / (P_X_given_C_yes * P_C_yes + P_X_given_C_no * P_C_no)

print("Bilgisayar alabilme olasılığı:", P_C_yes_given_X)
