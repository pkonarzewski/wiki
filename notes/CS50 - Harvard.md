---
tags: [Kurs]
title: CS50 - Harvard
created: '2020-04-27T09:12:07.306Z'
modified: '2020-04-27T09:19:46.413Z'
---

# CS50 - Harvard

* [[Kurs na Edx|https://courses.edx.org/courses/course-v1:HarvardX+CS50+X)]]
* [[Materiały Dodatkowe|https://cs50.harvard.edu/x/2020/)]]
* [[Moje materiały|https://github.com/pkonarzewski/what-i-learned/tree/master/moocs/cs50_introduction_to_computer_science)]]

## Week 0

* Pobieżnie o wszystkim co będzie mówione na wykładach
* Szybkie wprowadzenie do systemu binarnego
* Pokazówka ich własnego programu do tworzeania kodu z bloków Scratch


## Week 1

* Nauka języka C
* printf - f oznacza formated, czyli zformatowany tekst\
* stdio.h - standard input and output, a h to header
* clang, gcc
* ls to skrót od list
* arguments / parameters
* %s placeholder w stringach
* increment: a = a +1; a += 2; a++
* funkcje: void func_name(void) {}
* c czyta kod zrodlowy od gory do dolu, kolejnosc jest wazna, ale mozna zainicjowac pusta na gorze void cough(void); a ponizej prawdziwa implementacje
* ang. implementation detail
* formatowanie float %1.f
* unitsd.h
* floating point inperfection
* integer overflow


### Shorts

#### Data Types

* int - 4 bytes (32 bits), negatywny i pozytywny
* unsigned int tylko dodatni wartości (0, 2^32-1)
* short, long int
* chars 1 byte (-218, 127)
* float - floating points 4 bytes, nie da sie jednoznacznie powiedziec o maksymalnej i minimalnej wartosci
* double (double precision) 8 bytes (64bits)
* void - type nie data type, taki None
* cs50 bool - wartości logiczne true and false
* cs50 string - list of chars
* structs, typedefs
* int var1, var2;
* variable:
    * declaration
    * assignment
    * initialization (declaration + assignment at once)

#### Operators

* `+ - / *`
* `%` modulus - reszta z dzielenia
* `= *= x-- x++`
* boolean expression kazda wartość #= 0 jest True
* `&& AND  OR || NOT # (wymawia sie: bang ,exclamation, not)`
* `< <= > >= == (equals equals) #=`

#### Conditional Statements

* if (boolean expression) {}
* if, else if, else
* switch(var) {case val: case val: default: break
    * break moze byc opuszczany, wtedy przeleci przez caly satement
* `int x = (expr) ? 5 : 6` nazywa się `?:` albo tenary operator

#### Loops

* `while (expr) {}`
*  `do {} while (expr)`
* `for (start; expr; increment){}`

#### Command line

* Linux
* cd, pwd
* . ..
* ls
* mkdir
* cp
* rm
* mv
* cmod
* touch
* rmdir
* man
* diff
* sudo
* clear
* telnet
