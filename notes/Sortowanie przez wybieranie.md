---
title: Sortowanie przez wybieranie
created: '2020-05-16T15:58:58.998Z'
modified: '2020-05-16T15:59:05.343Z'
---

# Sortowanie przez wybieranie

Sortowanie przez wybieranie (*ang. Selection sort*) - prosta metoda sortowania polegająca na wyszukaniu elementu mającego się znaleźć na żądanej pozycji i zamianie miejscami z tym, który jest tam obecnie. Można sobie to wyobrazić jako sortowanie w ręce kart do gry.

Składa się z dwóch etapów:
1. Wyszukaj minimalną wartość z tablicy spośród elementów od i do końca talblicy 
2. Zamień wartość minimalną z elementem na pozycji i

Złożoność algorytmu $O(n^2)$

Przykład:

```pseudocode
function selection_sort(list)
    n := size of list

    for i = 1 to n-1:
        min := i
        for j = i+1 to n:
            if list[i] < list[min]:
                min := i

    if min != i then
        swap list[min] and list[i]
```
