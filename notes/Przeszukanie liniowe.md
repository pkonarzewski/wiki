---
title: Przeszukanie liniowe
created: '2020-05-16T15:58:45.137Z'
modified: '2020-05-16T15:58:50.381Z'
---

# Przeszukanie liniowe

Przeszukanie liniowe / sekwencyjne lub wyszukiwanie proste (*ang. linear search*) - Polega na porównywaniu żądanego klucza z kolejnymi kluczami w sekwencji. Liczba koniecznych porównań zależy do położenia elementu.

Algorytm ma złożoność $O(n)$.

Pseudokod:
```pseudocode
def przeszukanie_liniowe(szukany_klucz, tablica):
    for index := 0 to len(tablica) do
        if tablica[index] = szukany_klucz then
        return index  # zwraca pozycje znalezionego elementu
```
