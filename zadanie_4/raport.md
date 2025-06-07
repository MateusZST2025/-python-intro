# Raport – Laboratorium 4 – MCDM z użyciem pymcdm

## Dane wejściowe

**Macierz decyzyjna:**

| Alternatywa | Kryterium 1 | Kryterium 2 | Kryterium 3 | Kryterium 4 |
|-------------|-------------|-------------|-------------|-------------|
| A1          | 250         | 16          | 12          | 5           |
| A2          | 200         | 20          | 8           | 3           |
| A3          | 300         | 22          | 16          | 4           |

- Kryteria 1 i 2 – **maksymalizowane**
- Kryteria 3 i 4 – **minimalizowane**

**Wagi:** `[0.3, 0.2, 0.4, 0.1]`

## Zastosowane metody

- TOPSIS
- SPOTIS (z określonymi bounds dla każdego kryterium)

## Wyniki

**TOPSIS:**

- Scores: `[0.427, 0.585, 0.475]`
- Ranking: `[3, 1, 2]`

**SPOTIS:**

- Scores: `[0.650, 0.367, 0.450]`
- Ranking: `[3, 1, 2]`

## Wnioski

W obu metodach najlepszą alternatywą okazała się **A2**.

Dlaczego?
- A2 ma **najniższy koszt i czas**, co ma wysoką wagę (szczególnie koszt: 0.4).
- Choć A2 nie ma największego zysku, **sumarycznie wypada najlepiej** po normalizacji i przeliczeniu wag.

Wyniki metod są spójne, co potwierdza ich wiarygodność w tej analizie.

## Autor

Imię i nazwisko: *Mateusz Gruszczyński*  
Nr. Albumu: *154201*

