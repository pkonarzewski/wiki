---
title: Kafka change data capture breaks database encapsulation
created: '2020-04-27T09:17:31.905Z'
modified: '2020-04-27T09:19:12.989Z'
---

# Kafka change data capture breaks database encapsulation

[[Artykuł|https://riccomini.name/kafka-change-data-capture-breaks-database-encapsulation]]

* Zmiany schematów bazy psują kafka streams, czyli psują enkaspulacje bazy, osoby nad nią pracujące muszą uważać na to co robią i zastosować odpowiednie procedury
* Twój "data model" jest API i trzeba tak traktować
* Zarządzanie schema migration (migracja schematów?), kiedy zmieniamy strukturę tabel, a na ich podstawie działają inne serwisy korzystające z Kafki. Potrzeba wtedy posiadać dwie wersje, nową i legacy dla systemów, które muszą się dostosować do zmiany
* Możliwe rozwiązania
    * Source db transformations - triggery i tworzenie dwóch wersji tabeli
    * Kafka source connector transformation - korzystanie z single message transform (?), dodanie nowego source connector, który przekształca dane na format legacy i jest to nowy topic
    * Kafka transformations - korzysta ze stream processora i emituje do nowego topicu
    * Kafka sink connector transormations - można wskazywać do nowej tabeli albo to tej samej po transformacji danych
    * Destination DB transformation - klasyczne ELT, po załadowainu danyc na bazie docelowej jest dokonywana transformacja


Technologie wymienione:

* [[Kafka]]
* [[Kafka Connect]]
* [[ Confluent]]
* [[Liquibase]], [[Flayway]], [[Alembic]]
* [[Flink]], [[Spark Streaming]], [[Kafka streams]], [[Samza]]
