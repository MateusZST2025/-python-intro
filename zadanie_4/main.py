import numpy as np
from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm.helpers import rankdata

# --- Dane wejściowe ---
matrix = np.array([
    [250, 16, 12, 5],   # Alternatywa 1
    [200, 20, 8, 3],    # Alternatywa 2
    [300, 22, 16, 4]    # Alternatywa 3
])

# Wagi dla kryteriów (suma powinna wynosić 1)
weights = np.array([0.3, 0.2, 0.4, 0.1])

# Typy kryteriów: 1 = maksymalizować, -1 = minimalizować
types = np.array([1, 1, -1, -1])

# --- Metoda TOPSIS ---
topsis = TOPSIS()
topsis_result = topsis(matrix, weights, types)
topsis_ranking = rankdata(topsis_result, reverse=True)

# --- Wyświetlenie wyników TOPSIS ---
print("TOPSIS Scores:", np.round(topsis_result, 3))
print("TOPSIS Ranking:", topsis_ranking)

# --- Przygotowanie bounds dla SPOTIS (min, max dla każdego kryterium) ---
bounds = np.array([
    [np.min(matrix[:, i]), np.max(matrix[:, i])]
    for i in range(matrix.shape[1])
])

# --- Metoda SPOTIS ---
spotis = SPOTIS(bounds)
spotis_result = spotis(matrix, weights, types)
spotis_ranking = rankdata(spotis_result, reverse=False)

# --- Wyświetlenie wyników SPOTIS ---
print("SPOTIS Scores:", np.round(spotis_result, 3))
print("SPOTIS Ranking:", spotis_ranking)
