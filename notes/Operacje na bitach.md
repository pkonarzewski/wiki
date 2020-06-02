---
title: Operacje na bitach
created: '2020-05-16T15:59:55.005Z'
modified: '2020-05-16T16:00:11.566Z'
---

# Operacje na bitach

## AND &

Operacja bitowa "i" (*ang. bitwise and*) AND '&' - zwrca 1 tylko jeżeli oba bity są 1.

|  a  |  b  |  &  |
| --- | --- | --- |
| 0   | 0   | 0   |
| 0   | 1   | 0   |
| 1   | 0   | 0   |
| 1   | 1   | 1   |

Przyklad:
```
5 & 7 -> 5
0b101 & 0b111 -> 0b101
```

## OR |

Operacja bitowa "lub" (*ang. bitwise or*) OR '|' - zwraca 1 jeżeli, którykolwiek z bitów jest 1.

|  a  |  b  |  &  |
| --- | --- | --- |
| 0   | 0   | 0   |
| 0   | 1   | 1   |
| 1   | 0   | 1   |
| 1   | 1   | 1   |

Przykład:
```
6 | 1 -> 7
0b110 | 0b1 -> 0b111
```

## XOR ^

Operacja bitowa "albo" (*ang. bitwise xor*) XOR ^ - zwraca 1 jeżeli jeden bit jest 0, a drugi 1.

|  a  |  b  |  &  |
| --- | --- | --- |
| 0   | 0   | 0   |
| 0   | 1   | 1   |
| 1   | 0   | 1   |
| 1   | 1   | 0   |

Przykład:
```
6 ^ 3 -> 5
0b110 ^ 0b11 -> 0b101
```
## NOT ~

Zaprzeczenie bitowe, dopełnienie bitowe (*ang. bitwise not/complement*) 1's complement NOT ~ - operacja jednoargumentowa, zwraca 1 tylko jeżeli bit argumentu jest ustawiony na 0.

| a | ~a  |
| --- | --- |
| 0 | 1 |
| 1 | 0 |

Przykład:
```
~0b0101 -> 0b1010
```

Przykład  w języku Python:
Dla Python, który korzysta z kodu uzupełnień do dwóch, odwrócenie polega na dodaniu 1 i inwersji bitów (*-(x+1)*). Tradycyjnie zakłada się, że najstarszy bit jest jest bitem znaku, ale liczby w Pythonie nie mają najstarszego bitu (mają nieskończoną ilość bitów).

Przykład:
```
~60 -> -61
~0b111100 -> 0b111101

~7 -> -8
~0b111 -> 0b1000
```

Natomiast, żeby uzyska takie odwrócenie trzeba zastosować następującą operację:
```
x + ~x = -1
~x = -1-x

# czyli
~0b1101 -> -0b1101
```


## Left-Shift <<

Przesunięcie bitowe w lewo (*ang. shift left*)Left-Shift << - polega na przesunięciu o n bitów w lewo. Bity pojawiające się z prawej stroyny (uzupełniające przesunięcie) są ustawione na 0. Przesunięcie o 1 bit jest równoznaczne z pomnożeniem przez 2, przesunięcie o 2 bity to dwukrotne pomnożenie przez 2.

Przykład:
```
2<<2 -> 8  # 2*2^2
0b10<<2 -> 0b1000

2<<4 -> 32  # 2*2^4
0b10<<4 -> 0b100000
```

## Right-Shift >>

1. Przesunięcie bitowe w prawo (*ang. shift right*) Right-Shift >> - przesunięcie w prawo polega na przesunięcie x bitów w prawo. Operacja jest równoważna dzieleniu całkowitemu przez 2.

Przykład:
```
2>>2 -> 0  # 2/2^2
0b10>>2 -> 0b0
256>>2 -> 64  # 256/2^2
0b100000000>>2 -> 0b1000000
```

Źródła:
* [algorytmy.org](http://www.algorytm.org/kurs-algorytmiki/operacje-bitowe.html)
* [Python Bitwise Operators with Syntax and Example](https://data-flair.training/blogs/python-bitwise-operators/)
