---
title: Timezone w Airflow
created: '2020-04-27T09:25:19.347Z'
modified: '2020-04-27T09:26:05.817Z'
---

# Timezone w Airflow

Na podstawie [[How to use timezones in Apache Airflow|https://marclamberti.com/blog/how-to-use-timezones-in-apache-airflow/]] i [[oficjalnej dokumentacji|https://airflow.apache.org/docs/stable/timezone.html]].

## Skrót

* W artykule jest krótkie wyjaśnienie [[stref czasowych|Strefa czasowa]]
* ''aware / naive datetime ''objects - czyli czas z i bez strefy czasowej
* //"You should NEVER use naive datetime objects. Naive datetime objects should NOT be considered as UTC by default. Even if you are working in UTC you MUST specified the UTC timezone in your datetime objects."//
* Airflow używa paczki ''pendulum''
* Airflow każdy obiekt naive datetime przekształca na UTC aware i równa do UTC, jeżeli nie ma tz to uznaje, że czas jest UTC
* należy używać UTC w start_date, end_date i schedule_interval zgodnie z lokalnym tz
* jeżeli data jest aware tz to cron będzię uwzględniał to

## Kod

```
import pendulum

local_tz = pendulum.timezone("Europe/Warsaw")

(...)
"start_date" = datetime(... , tzinfo=local_tz)

schedule_interval="0 2 * * *" schedule 

```

Cały proces polega na podaniu czasu jaki oczekujemy w lokalnej strefie czasowej, airflow wtedy konwertując do utc+0, musi odjąć 1 lub 2 godziny i wywołać w tym przypadku o godzinie 01:00, która u nas jest godziną 02:00

## Templates

W templetach airflow przekazuje timezone w utc

## cron schedules vs time delta 

cron jeżeli jest tz aware respektuje zmiany czasu letniego, czyli odpali się np. o 4:00 UTC w trakcie DST i o 05:00 UTC.

Natomiast timedelta, będzie zawsze w tym samym czasie utc, np. 05:00
