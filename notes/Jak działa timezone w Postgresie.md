---
title: Jak działa timezone w Postgresie
created: '2020-05-10T12:25:35.878Z'
modified: '2020-05-10T12:32:17.133Z'
---

# Jak działa timezone w Postgresie

Na podstawie[^1] [^2].

* W postgresie mamy typ kolumny `timestamp without time zone` i `timestamp with time zone`, podstawowa różnica, że with timezone konwertuje czast do utc, gdzie without zostawia tak jak został podany (naive)
* Ustawiając po stronie klienta czas loklany `SET timezone TO 'Europe/Warsaw';` to daty w timestamptz będą przekształcone na czas podany.
* Jeżeli przy dodawaniu wpisów w kolumnie tz nie podamy offsetu to serwer zakłada, że jest to czas loklany ustawiony

[^1]: https://phili.pe/posts/timestamps-and-time-zones-in-postgresql/
[^2]: http://blog.untrod.com/2016/08/actually-understanding-timezones-in-postgresql.html
