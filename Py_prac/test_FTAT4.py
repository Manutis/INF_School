import matplotlib.pyplot as plt
import numpy as np

# Beispiel-Daten generieren
stunden = np.arange(1, 161)  # 160 Stunden
temperaturen = 15 + 5 * np.sin(stunden / 20) + np.random.normal(0, 1, 160)  # Zufällige Werte

plt.figure(figsize=(12, 6))
plt.plot(stunden, temperaturen, marker='o', linestyle='-', color='b')
plt.title("Temperaturverlauf der letzten 160 Stunden")
plt.xlabel("Stunde")
plt.ylabel("Temperatur [°C]")
plt.grid(True)
plt.tight_layout()
plt.savefig("temperaturverlauf.png")  # Grafik als PNG speichern
# plt.show()  # Diese Zeile kannst du entfernen oder auskommentieren