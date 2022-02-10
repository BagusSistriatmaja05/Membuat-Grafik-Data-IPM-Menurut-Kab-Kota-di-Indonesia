# Instalasi Matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Masukkan Data IPM Kab/Kota
y1 = np.array([64.61,65.12,65.6,65.93,66.38])
y2 = np.array([68.05,68.52,68.87,69.32,69.86])
y3 = np.array([67.66,68.19,69.17,69.89,70.86])
y4 = np.array([64.36,64.78,65.78,66.36,66.97])
y5 = np.array([67.1,67.88,68.05,69.04,69.4])
y6 = np.array([79.38,80.11,80.84,81.17,81.48])
y7 = np.array([71.1,71.43,72.4,72.96,73.43])

x = np.array([2015,2016,2017,2018,2019])

# Membuat Plot
plt.figure(1)

plt.plot(x,y1, label="Kab. Serang")
plt.plot(x,y2, label="Kab. Grobogan")
plt.plot(x,y3, label="Kab. Karawang")
plt.plot(x,y4, label="Kab. Indramayu")
plt.plot(x,y5, label="Kab. Lampung Timur")
plt.plot(x,y6, label="Kota. Tangsel")
plt.plot(x,y7, label="Kab. Sragen")

plt.legend(loc="lower right")

plt.title("IPM Menurut Kab/Kota di Indonesia")
plt.xlabel("Tahun")
plt.ylabel("IPM")

plt.yticks([60,70,80])
plt.xticks([2015,2016,2017,2018,2019])

#Tampilkan Plot
plt.show()