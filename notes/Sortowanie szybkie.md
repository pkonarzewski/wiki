---
title: Sortowanie szybkie
created: '2020-05-16T16:01:11.970Z'
modified: '2020-05-16T16:01:18.981Z'
---

# Sortowanie szybkie

Sortowanie szybkie (*ang. quicksort*) - popularny algorytm sortujący działający na zasadzie "dziel i zwyciężaj". Działa następująco: z tablicy wybiera się element rozdzielający (osiowy, *ang. pivot*), po czym tablica jest dzielona na dwa fragmenty, potem następuje partycjonowanie (*ang. partitioning*), gdzie elementy mniejsze są przenoszone do początkowego fragmentu, a większe do do końcowego. Potem osobno sortuje się oba fragmenty. Rekurencja kończy się, gdy fragment zawiera jeden element lub jest pusty.

1. Wybieramy element osiowy
2. Podziel tablicę na dwie podtablice - z elementami mniejszymi i większymi od osiowego
3. Rekurencyjnie wywołuj funkcję sortującą na obu podtablicach

Złożoność obliczeniowa algorytmu wynosi $O(n log n)$, w wariancie pesymistyczny $O(n^2)$. Najgorszy przypadek jest zależny od umiejscowienia pivota. W algorytmie wysokość stosu wywołąń wynosi O(log n), a każdy poziom zajmuje O(n), czyli całkowita złożoność to $O(n)*O(logn)=O(nlogl)$, ale w najgorszym przypadku, gdzie tablic jest dzielona zawsze tak, że jeden z fragmentów jest pusty, to wysokość stosu wyniesie O(n).

```pseudocode
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        p = len(arr) // 2
        pivot := arr.pop(p)
        less := [x for arr if x < pivot]
        greater := [x for arr in x >= pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
```
