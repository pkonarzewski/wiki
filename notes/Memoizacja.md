---
title: Memoizacja
created: '2020-05-16T16:02:23.194Z'
modified: '2020-05-16T16:02:29.060Z'
---

# Memoizacja

Memoizacja (eng. *Memoization*) - Technika opytmalizacyjna polegająca na przechowywaniu wyników funkcji dla najczęściej powtarzanych wektorów argumentów i zwracanie wyniku z cache'a zamiast wykonywania funkcji. Najprościej można stworzyć słownik, który będzie zapisywał w kluczu parametry funkcji i jako wartość wyniki operacji.

```python
from typing import Dict
memo = {0: 0, 1: 1}

def fib3(n):
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2) # memoization
    return memo[n]
```

W pythonie można użyć do tego deokratora `@lru_cache`.

