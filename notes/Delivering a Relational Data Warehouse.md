---
tags: [Kurs]
title: Delivering a Relational Data Warehouse
created: '2020-04-27T09:15:38.181Z'
modified: '2020-04-27T09:19:56.347Z'
---

# Delivering a Relational Data Warehouse

[[Kurs|https://courses.edx.org/login?next=/courses/course-v1%3AMicrosoft%2BDAT216x%2B1T2018a/courseware/653b57900c3744a79cefcd7a13a66531/cedd37d54d8449a983c53dc0d873a4ec/%3Fchild%3Dfirst]]

DWH

* Dimension Table Design Concepts
The implementation then within the dimension table itself can
be achieved in three different ways.

enormalized approach,
we call that a star schema dimension.
There's the normalized snow flake dimension.
And then there's the self referencing relationship.

dim should be wide and short

aviod snoflake dim tables, use only if you need granulation of fact tables
primary key: business key and surrogate key
SCD typ-2
AdventureWorksDW


fact tables - collection of measurements associated with a specific business process. Allow to store transactionc and events and the measurements associated with them
define a consistant granuality, most attomic level which te facts can be defined

prefix - fact_

grain / granularity fact table
dimensonality 
additive measurements


Order line number - https://stackoverflow.com/questions/10367206/what-is-a-order-line

role playing - reference a dimension table more than once
if you have sale date, due date, and ship date, you implement date key for each of those roles


Fact table types:
- transaction grain (single instant) used in sales
- periodic snapshot grain (eg for every day we load stock on hand ) used in financial, stock or weateher
- accumulating snapshot grain (measurements accumulated across period or workflow) events are recorded by progression in the workflow or by a status update

measure columns are typically numeric and commonyl additive (can sum them)
non-additive measures (rates and ratios)
semi-additive - stock balance

fact tables dosent need primary key

warto jednak materializować jakieś typowe operacje, dal potrzeb wydajnościowych np. amount*price

w adwenture works tabelą faktów jest plany realizacji dla sprzedawców (łączą się ze sprzedawcą)

slowniczek 
general ledger - księga główna
erd - entity relation diagram
quota

jezeli granulacje czegos jest np. kwartalna to najlepiej jest znormalizowac do pierwszego dnia danego okresu i reszte bierzemy z dim_date

dla dim_date glowny klucz moze byc w formie 20191025


## date dimension

datekey should be humanredable (exception)


dim_time - other dimension separated from date column

## slow changing dimensions

type1 - overwrite change
type2 - insert new version (current_flag, start_date, end_date)
type3 - tracked limited history (previous_value, change_date)

use scd when really it is occasional and sporadic change
use only on critical things vs historical

if changes are frequent:
- type2 for small tables
- fact table for changing numeric values

## parent-child hierarchies

regular "fixed" hierarchies - levels (sibliings) are same type (year, quarter, etc., 
 - facts are attached at lower level and aggregated (rolled up) to higher levels

ragged hierarchies - eg. organizations charts, bill of materials nad general ledger structures

when parent-child - avoid if you can implementing scd type 2 
- the root members should be either null or their key

* UnaryOperator - + - ~

ssas

convert to tabular fixed  (Level1, Level2, etc.)

## additional schema design

### degemerated dimensions
it dosen make sense to design a dimension that consists of single attribute, you add it fact table
eg invoice, tracking numbers


### Junk dimension
several falg or tex columns with low cardinality can be grouped into one. you create carthesian product of all flags and create surogate key

### Factless fact table
when you count events, it store a combination of dimension key values

