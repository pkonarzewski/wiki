---
title: Idempotentność w DBT
created: '2020-06-01T09:35:07.002Z'
modified: '2020-06-01T09:46:53.830Z'
---

# Idempotentność w DBT

* dbt promuje [[idempotentność|Idempotentność]] w  transformacjch danych
* rozumiemy przez to, że wielokrotne wywołanie daje zawsze te same wyniki
* Jeżeli chodzi o obszar transformacji danych to:
  * jeżeli źródło przestanie być aktualizowane to tabele wynikowe będą takie same
  * jeżeli operacja zostanie przerwana ponowne wywołanie nie pozostawi śladu
  * jeżeli wywołamy ręcznie pomiędzy planowanymi wywołaniami to efekt planowanego będzie takim sam jakby nie było ręcznego
  * jeżeli zostanie wykonany drop modelu to można go odbudować od podstaw
* nie używamy autoincrementa w kolumnach, bo to psuje idempotetność
