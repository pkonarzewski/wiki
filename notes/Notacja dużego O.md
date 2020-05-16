---
attachments: [big_o_notation.png]
title: Notacja dużego O
created: '2020-05-16T16:02:38.740Z'
modified: '2020-05-16T16:03:32.463Z'
---

# Notacja dużego O

Notacja duże-O (eng. *Big O notation*) - Asymptotyczne tempo wzrostu, miara określająca zachowanie wartości funkcji wraz ze wzrostem jej argumentów. Stosowana szczególnie w teori obliczeń, w celu opisu złożoności obliczeniowej w zależności od rozmiaru danych wejściowych algorytmu (najczęściej czasu wykonania lub wykorzystania pamięci). Opisuje jak szybko dana funkcja rośnie lub maleje, abstrahując od konkretnej postaci tych zmiennych. Notacja  informuje o najgorszym czasie wykonania algorytmu.
Notacja duże O ignoruje stałe.

## Rodzaje złożoności

|    Notacja     |                  nazwa pl.                   | nazwa ang. |
| -------------- | -------------------------------------------- | ---------- |
| $O(1)$         | złożoność stała                              | constant   |
| $O(log_2 n)$   | złożoność logarytmiczna                      |            |
| $O(n)$         | złożoność liniowa                            | linear     |
| $O(n log_2 n)$ | złożoność liniowo-logarytmiczna              |            |
| $O(n^2)$       | złożoność kwadratowa                         | quadratic  |
| $O(n^c)$       | gdzie c jest stałą – złożoność wielomianowa* |            |
| $O(c^n)$       | gdzie c jest stałą – złożoność wykładnicza   |            |
| $O(n!)$        | złożoność rzędu silnia                       |            |

* zakłada się, że jest to największa złożoność akceptowana dla algorytmu

![img](@attachment/big_o_notation.png)
