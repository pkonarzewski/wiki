---
attachments: [hanoi_towers.png]
title: Wieże Hanoi
created: '2020-05-16T16:03:52.079Z'
modified: '2020-05-16T16:04:47.417Z'
---

# Wieże Hanoi

Dany jest zestaw trzech kołków oraz nnn dysków, gdzie każdy z nich jest różnej wielkości. Kołki nazwijmy A, B i C, a dyski niech mają numery od 1 dla najmniejszego, do nnn dla największego. Na początku wszystkie nnn dyski są na kołku A, w kolejności malejącej od góry do dołu, tak że dysk nnn jest na dole a dysk 1 na górze. Celem jest przeniesienie wszystkich nnn dysków z kołka A na kołek B.

Ograniczenia:
1. Możesz przenieść tylko 1 dysk w jednym momencie.
1. Żaden dysk nie może zostać na szczycie mniejszego. Na przykład, jeśli dysk 3 jest na kołku, wtedy wszystkie dyski poniżej muszą mieć numery większe od 3.

![img](@attachment/hanoi_towers.png)

## Rozwiązanie

Zadanie jest łatwe do rozwiązania rekurencyjnie.

Przykład w pythonie:
```python
def hanoi(begin, end, temp, n):
    if n == 1:
        # jezeli na stosie jest tylko jeden krazek to przeloz na miejsce docelowe
        end.push(begin.pop())
    else:
        # jezeli wiecej
        hanoi(begin, temp, end, n - 1)  # przeloz wszystko poza niajnizszym na zapasowe
        hanoi(begin, end, temp, 1)  # przeloz najnizszy na docelowe
        hanoi(temp, end, begin, n - 1)  # przeloz pozostale na docelowe
```
