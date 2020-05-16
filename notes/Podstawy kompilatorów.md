---
attachments: [compiler_graph_representation.png, compiling_process.png]
title: Podstawy kompilatorów
created: '2020-05-16T15:43:07.288Z'
modified: '2020-05-16T15:49:02.819Z'
---

# Podstawy kompilatorów

## Pojęcia podstawowe

* Kompilator (ang. compilator) - to program, który czyta kod napisany w języku źródłowym (kod źródłowy) i tłumaczy go na równoważny kod w języku wynikowym (np. kod maszynowy), wykrywając przy tym ewentualne błędy.
* Kompilacja (ang. compilation) - to proces transalcji i składa się z dwóch części: analizy i syntezy. Analiza polega na rozłożeniu programu na części składowe i stworzenie jego reprezentacji pośredniej. Synteza polega na przekształceniu reprezentacji pośredniej w program wynikowy.
* Interpreter - nie generuje programu wynikowego, ale od razu wykonuje instrukcje zawarte w programie źródłowym.
* Lekser, Skaner (ang. lexem, scaner) - program dokonujący analizę leksykalną
* Parser (ang. parser) - program dokonujący analizy składniowej
* Generator (ang. generator) - 
* Leksem (ang. lexeme) - sekwencja znaków w kodzie źródłowym rozpoznawana przez lekser jako instancja tokena
* Token (ang. token) - jest abstrakcyjnym symbolem reprezentujący jednostkę leksykalną, np. słowo kluczowe, operator, identyfiaktor, nawias itd... . W Pythonie np. NEWLINE, INDENT, DEDENT
* Drzewo wyprowadzenia (ang. parse tree) - wynik przeprowadzonej analizy składniowej. Liśćmi w takim drzewie są symbolne terminalne gramatyki, a korzeniem symbol startowy.
* Tablica symboli - jest po pewna struktura danych, która przechowuje informacje o napotkanych w kodzie symbolach.

## Etapy

![img](@attachment/compiling_process.png)

Pierwsze trzy etapy generują kod pośredni, który potem jest brany przez optymalizator (opytmalizuje kod, nie zawsze wsytępuje) i generator (generuje z kodu pośredniego kod specyficzny dla dla konkretnej maszyny docelowej). Dzięki takiemu rozwiązaniu dla każdej architektury docelowej trzeba stworzyć tylko jeden generator, który korzysta z takiej samej formy kodu pośredniego.

### 1. Analiza leksykalna (liniowa)

Etap w którym strumień znaków (kod źródłowy) jest wczytywany i grupowany w symbole leksykalne (tokeny).

Za analizę odpowiada skaner(lekser).

Przykład

|     token     | leksem |   wzorzec   | atrybut |
| ------------ | ------ | ----------- | ------- |
| KWD_INT       | int    | int         |         |
| IDENTYFIKATOR | s      | [_zA-z0-9]* | "s"     |

**Przykład**: jeśli na wejściu pojawi się ciąg znaków "94873", to analizator leksykalny (skaner) wysyła parserowi jedynie symbol (token) "NUMBER".

### 2. Analiza składniowa (hierarchiczna, syntaktyczna)

Etap w którym znaki lub symbole leksykalne są grupowane hierarchicznie w zagnieżdżone struktury, mające wspólne znaczenie (drzewo składniowe). W tym etapie następuje sprawdzenie, czy ułożenie tokenów nie łamie reguł danego języka.

Za analizę odpowiada parser.

**Przykład**:

### 3. Analiza semantyczna

Etap w którym przeprowadzane są pewne testy mające zapewnić, że składniki programu pasują do siebie pod względem zaczenia.

**Przykład**:

## Reprezentacja kodu pośredniego

### Reprezentacja grafowa


![img](@attachment/compiler_graph_representation.png)
Różne reprezentacje grafowe dla `a:=b*c+b*c`

* drzewo wyprowadzenia - wiernie przedstawiają wyniki procesu analizy składniowej.
* drzewo składniowe (AST) - bardziej zwięzła reprezentacj pozbawiona niepotrzebnych wierzchołków, to na jego podstawie robi się analizę symantyczną.
* Skierowany graf acykliczyny, DAG (ang. direct acyclic graph) - wariant AST w którym podobne poddrzewa są łączone.
* graf przepływu - stosowany w kontekście bloków bazowych

### Reprezentacja liniowa


Dla wyrażenia `x - 2 * y`

* kod jednoadresowy: `push 2; push y;  mul; push x; sub;`
* kod dwuadresowy: `t1 := 2; mul t1, y; t2 := x; sub t2, t1;`
* kod trójadresowy: `t1 := 2; t2 := t1 * y; t3 := x - t2`


## Zasoby

* [Podstawy kompilatorów - wykład](http://wazniak.mimuw.edu.pl/index.php?title=Podstawy_kompilator%C3%B3w)
* [Metody realizacji języków programowania](http://wazniak.mimuw.edu.pl/index.php?title=Metody_realizacji_j%C4%99zyk%C3%B3w_programowania)
* [Introduction to Compilers - Udemy](https://classroom.udacity.com/courses/ud168)
