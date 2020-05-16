---
tags: [wip]
title: Kimball's Four-Step Dimensional Design Process
created: '2020-05-12T19:06:45.515Z'
modified: '2020-05-13T20:19:08.238Z'
---

# Kimball's Four-Step Dimensional Design Process

Kroki:

## 1. Wybierz proces biznesowy

* [[Proces biznesowy|Proces biznesowy w hurtowniach danych]] jest podstawą do budowania hurtowni
* Należy odróżnić proces biznesowy od inicjatyw, w tym kontekście proces jest bardziej elementarny. Inicjatywa może składać się z wielu procesów.

## 2. Wybierz granulację

* Granulacja oznacza, szczrgółowość, czym dokładnie będzie indywidualny rekord w [[tabeli faktów|Tabela faktów]]
* Przykłady, jeden rekord to: jedena pozycja zeskanowana przy kasie, jedno konto bankowe na miesiąc
* Granulacja powinna być wyrażona w specyfikacji biznesowej, a nie jak w systemie źródłowym
* lowest atomic grain (atomic data) - najlepiej ustalić granulacje na najniższym poziomie na jaki pozwala system źródłowy, dzięku temu hurtownia będzie odporniejsza na zmiany wymagań i nowe wymagania raportowe

## 3. Zidentyfikuj wymiary

* Przy identyfikacji [[wymiarów|Tabela wymiarów]] powinno się zadać pytanie "Jak biznes opisuje dane wynikające z procesów biznesowych?"
* kto, co, gdzie, kiedy,dlaczego i jak?

## 4. Zidentyfikuj fakty

* Przy szukaniu [[faktów|Tabela faktów]] powinno się zdać pytanie: "Co mierzy dany proces?"
* Nie wolno mieszać granulacji w tabelach faktów
* Unikaj modelowania danych tylko na podstawie bazy źródłowej, potrzebne jest wsparcie biznesu
