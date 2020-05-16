---
title: Tablica skrótów
created: '2020-05-16T15:56:46.015Z'
modified: '2020-05-16T15:56:51.912Z'
---

# Tablica skrótów

Tablice mieszające, tablice z hashowaniem (*ang. hash tables*) - nazywane też słownikiem lub mapą. Wykorzystywane jest funkcja hashująca (*ang. hash function*) i używanie jest to funkcja do obliczania skrótów. Funkcja musi spełniać następujące warunki: być stabilna (dla tego samego parametru zwraca zawsze taką samą wartość) i zwracane wartości powinny być równomiernie rozrzucone po wszystkich liczbach. Wykorzystywana np. jako pamięć podręczna (cache), rozpoznawania nazw DNS. Kolizje. Jeżeli dojdzie do zapełnienia, jeżeli współczynnik zapełnienia przekroczy wartość graniczną dochodzi do zmiany rozmiaru, wtedy tworzona jest nowa większa i z użyciem funkcji hash elementy są przenoszone.

|  operacja  | złożoność |
| ---------- | --------- |
| Odczyt     | **O(1)**  |
| Wstawianie | **O(1)**  |
| Usuwanie   | **O(1)**  |
