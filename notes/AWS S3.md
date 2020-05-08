---
title: AWS S3
created: '2020-05-04T10:50:04.946Z'
modified: '2020-05-07T07:06:54.920Z'
---

# AWS S3

Amazon S3 (Simple Storage Service)[^1] - usługa pozwalająca na przechowywanie plików w chmurze.

Zwykle Simple Storage Service wykorzystywany w ramach Amazon Web Services służy do: analizy Big Data, backupu i archiwizacji, Disaster Recovery, hostingu statycznych plików, przechowywania i dystrybucji contentu.

**Bucket** – to rodzaj folderu, w którym przechowuje się obiekty. Pełni on rolę m.in. w organizacji przestrzeni w ramach S3 oraz nadawaniu do niego dostępów.
**Obiekty** – tak nazywamy pliki, które przechowywane są w bucketach.
**Name** - nazwa identyfikacyjna bucketa, musi być unikatowa globalnie
**Prefix** - Bucket w s3 ma płaską strukturę, ale podobną funkcjonalność osiąga się przez nadawanie nazw z prefiksem np. 'logs/2020/data1.txt'. Jeżeli nazwa pliku kończy się na / to będzie on traktowany jako folder.
**Klucz** – unikalny identyfikator obiektu w ramach bucketu. Każdy obiekt w S3 można zidentyfikować po kombinacji nazwy bucketu, klucza oraz opcjonalnie id wersji danego obiektu.
**Region** – to geograficzna lokalizacja, w której Amazon przechowuje dane. W tym momencie jest ich 14. Wybór odpowiedniego regionu jest bardzo istotny, gdyż ma on wpływ m.in. na opóźnienia w przesyłaniu danych oraz koszty tej usługi.
**Availability Zone(AZ)** – To wyizolowana lokalizacja w ramach Data Center, w ramach jednego regionu.
**Klasy** - od tego zależy cena jednostkowa usługi i jaki jest poziom dostępności, gwarantowana trwałość i dostępność

[^1]: https://aws.amazon.com/s3/

