---
title: Future of Data Engineering
created: '2020-04-27T09:16:35.940Z'
modified: '2020-04-27T09:19:30.515Z'
---

# Future of Data Engineering

[[link do prezentacji|https://www.infoq.com/presentations/data-engineering-pipelines-warehouses/]]

## Rozwój infrastuktury danowej, etapy:

* Etap 0. None
    * baza produkcyjne (lub kopia) do której wszysci się łączą i pracują na niej
* 1. Batch
    * dane ładowane są codziennie do bazy raportowej (dwh)
    * problemy z create_time, modify_time, brak propagacji dla hard deletów, problemy wydajnościowe
* 2. Realtime
    * korzystanie z platformy streamingowej np. Kafka, Debezium
    * CDC
* 3. Integration
* 4. Automation
* 5. Decentralization


## Technologia:

* [[Debezium]]
* [[Kafka]]
* [[Amundsen]]
