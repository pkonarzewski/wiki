---
title: Wyszukiwanie binarne
created: '2020-05-16T15:57:50.809Z'
modified: '2020-05-16T15:58:33.796Z'
---

# Wyszukiwanie binarne

Wyszukanie binarne (*ang. binary search*) - Uporządkowana tablica jest dzielona na coraz mniejsze przedziały do momentu, w połowie zakresu i gdy szukany element jest porównywany z wartością tablicy(czyli musimy mieć posortowaną kolekcję do której możemy odwoływać się indeksem). W zależności od wyniku, szukanie jest kontynuowane w połówce, która może zawierać wynik i znowu wybierany jest środek przedziału. Algorytm opierający się na metodzie dziel i zwyciężaj. 

Złożoność obliczeniowa algorytmu wynosi $O(log_2 n)$.

Pseudokod:

```
def wyszukanie_binarne(tablica, szukana_wartosc):
    dol := 1
    gora := n

    while dol <= gora:
        srodek := dol+gora // 2
        if tablica[index] > szukana_wartosc:
            dol := srodek +1
        elif tablica[index] < szukana_wartosc:
            gora := srodek -1
        else
            return True
    return False
```

