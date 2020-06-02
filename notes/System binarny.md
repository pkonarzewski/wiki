---
title: System binarny
created: '2020-05-16T15:23:13.561Z'
modified: '2020-05-17T12:35:33.302Z'
---

# System binarny

System binarny / Dwójkowy system liczbowy

## Podstawy

Dwójkowy system liczbowy (*ang. Base-2 numeral system*) - System liczbowy, w którym podstawą jest liczba 2, a do zapisu liczby potrzebne są tylko dwie cyfry: 0 i 1. Ojcem nowoczesnego systemu binarnego jest Gottfried Wilhelm Leibniz, 1703 rok. Liczenie (wyliczanie) w binarny jest podobne do innych systemów, czyli zaczynamy z jedną cyfrą i zwiększamy  o jeden, jako, że mamy tylko 0 i 1, to po osiągnięciu 1 następuje "przesunięcie" do kolejnej pozycji i zrestartowanie pozycji ostatniej (w dziesiętnym [9 -> 10], w binarnym [0b11 -> -b100]).

|     | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |
| --- | ----- | ----- | ----- | ----- | ----- |
|     | 16    | 8     | 4     | 2     | 1     |
| 0   |       |       |       |       | 0     |
| 1   |       |       |       |       | 1     |
| 2   |       |       |       | 1     | 0     |
| 3   |       |       |       | 1     | 1     |
| 4   |       |       | 1     | 0     | 0     |
| 9   |       | 1     | 0     | 0     | 1     |
| 12  |       | 1     | 1     | 0     | 0     |
| 15  |       | 1     | 1     | 1     | 1     |
| 16  | 1     | 0     | 0     | 0     | 0     |

Przykład:
**9** binarnie to: $1*2^3 + 0*2^2 + 0*2^1 + 1*2^0$

## Słowniczek

* bit, cyfra dwójkowa (*ang. bit, binary digit*) - 
* Kod uzupełnień do dwóch U2 ZU2, (*ang. Two's complement*) - System reprezentacji liczb.
* Najbardziej znaczący bit (*ang. most significant bit, MSB*), zwany też najstarszym bitem – bit o największej wadze, znajdujący się w słowie maszynowym na miejscu najbardziej wysuniętym w lewo, przedstawiający największą wartość liczbową. 
* Najmniej znaczący bit (*ang. least significant bit, LSB*), zwany też najmłodszym bitem – bit o najmniejszej wadze, znajdujący się w słowie maszynowym na miejscu najbardziej wysuniętym w prawo, przedstawiający najmniejszą wartość liczbową.
* Bit znaku (*Sign bit*) – bit występujący w dwójkowym zapisie liczb, świadczący o jej znaku. Zwykle wartość 1 oznacza liczbę ujemną lub niedodatnią, a 0 – nieujemną. Występuje w większości powszechnie stosowanych sposobów zapisu liczb na bitach, dopuszczających zarówno liczby dodatnie jak i ujemne. Najczęściej występuje na najbardziej znaczącej pozycji.

[wiki kod uzupelnien do dwoch](https://pl.wikipedia.org/wiki/Kod_uzupełnień_do_dwóch)

## Operatory bitowe
