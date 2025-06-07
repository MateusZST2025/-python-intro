import matplotlib.pyplot as plt

# Dane
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Wykres
plt.plot(x, y, marker='o')
plt.title("Prosty wykres liniowy")
plt.xlabel("Oś X")
plt.ylabel("Oś Y")
plt.grid(True)
plt.show()
