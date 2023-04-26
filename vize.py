import random
import math
import matplotlib.pyplot as plt

# Hedef bilgileri
uzaklık_mesafesi = 20000 + 200 * random.randint(-10, 10)
genişlik_başlangıç = uzaklık_mesafesi
genişlik_bitiş = uzaklık_mesafesi + 1000 + 100 * random.randint(-2, 2)
hedef_konumu = [genişlik_başlangıç, genişlik_bitiş]

# Top bilgileri
top_konumu = [0, 16]
top_hızı = random.randint(330, 1800)  # Gereken hız
atış_sayısı = 0

# Fizik sabitleri
g = 10  # m/s^2
açı = 30  # Derece cinsinden

# Hedefi vurana kadar döngüyü çalıştır
while True:
    # Topun menzilini hesapla
    menzil = ((top_hızı ** 2) * math.sin(math.radians(2 * açı))) / g

    # Topun düştüğü noktanın koordinatlarını hesapla
    x_konumu = top_konumu[0] + menzil
    y_konumu = top_konumu[1] - ((top_hızı ** 2) * math.sin(math.radians(açı))) / (2 * g)  # Topun düştüğü nokta

    # Topun düştüğü noktanın hedefin neresinde olduğunu belirle
    if x_konumu < hedef_konumu[0]:
        print(f"Atış {atış_sayısı + 1}: Hedefin önünde düştü")
        top_hızı += 10  # Daha yüksek bir hıza ihtiyaç var, hızı arttır
    elif x_konumu > hedef_konumu[1]:
        print(f"Atış {atış_sayısı + 1}: Hedefin arkasına düştü")
        top_hızı -= 10  # Daha düşük bir hıza ihtiyaç var, hızı azalt
    else:
        print(f"Atış {atış_sayısı + 1}: Hedef vuruldu!")
        break

    # Atış sayısını arttır
    atış_sayısı += 1


print(f"{atış_sayısı+1}.seferde vuruş gerçekleşmiştir hedefi vurmak için gerekli hız: {top_hızı:.5f}")

# Grafik çizdirm
t = 0
dt = 0.01
x = [top_konumu[0]]
y = [top_konumu[1]]

while True:
    t += dt
    x_n = top_konumu[0] + top_hızı*math.cos(math.radians(açı))*t
    y_n = top_konumu[1] + top_hızı*math.sin(math.radians(açı))*t - (1/2)*g*(t**2)
    
    if y_n <= 0:
        break
        
    x.append(x_n)
    y.append(y_n)
    
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set(xlabel='X Koordinatı', ylabel='Y Koordinatı', title='Topun Yolu')
ax.grid()
plt.show()