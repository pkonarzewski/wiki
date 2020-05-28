---
title: Lista wiązana
created: '2020-05-16T15:51:01.524Z'
modified: '2020-05-23T19:04:16.711Z'
---

# Lista wiązana

Lista powiązana (*ang. linked list*) - elementy listy mogą być porozrzucane po całej pamięci. Każdy element zawiera adres do następnego elementu na liście. Jeżeli chcemy odczytać ostatni element z listy, musimy przejść przez wszystkie elementy [^1].

rodzaje: jednokierunkowe, dwukierunkowe, cykliczne

node : węzeł
head / front - wskazanie pierwszego elementu w liście, jeżeli jest null to znaczy, że jest pusta

Operacje:
- wstawianie
- usuwanie

wstawianie w środek trzeba uważać, żeby nie stracic ogonu

|  operacja    | złożoność |
| ----------   | --------- |
| Odczyt       | **O(n)**  |
| Wyszukiwanie | **O(n)**  |
| Wstawianie*   | **O(1)**  |
| Usuwanie*     | **O(1)**  |

/* - chodzi tylko o operacje, bez wyszukiwania elementu

https://eduinf.waw.pl/inf/alg/001_search/0083.php
https://pl.wikibooks.org/wiki/Struktury_danych/Listy
https://pl.wikipedia.org/wiki/Lista

[^1]: https://www.samouczekprogramisty.pl/struktury-danych-lista-wiazana
