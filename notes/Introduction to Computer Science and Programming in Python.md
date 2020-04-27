---
title: Introduction to Computer Science and Programming in Python
created: '2020-04-27T09:10:26.876Z'
modified: '2020-04-27T09:19:24.148Z'
---

# Introduction to Computer Science and Programming in Python

[[strona kursu|https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/index.htm]]

[[slajdy|https://onedrive.live.com/?id=1D982CBFAB0D3F19%2125071&cid=1D982CBFAB0D3F19]]

## Wykłady

### 1. What is Computation?

* declarative
* imperative
* algorytm
* fixed program computer - wykonuje jedno zadanie, np. prymitywny kalkulator
* stored program computer - maszyna przechowuje i wykonuje instrukcje
* built-in
* steps, flow of control, when to stop -> algorithm

* Podstawowa architektura komputera

* Memory
* ALU
* Control Unit
* Input Output

* primitve constructors - numbers, strings, etc
* syntax - blad skladni
* static semantics - blad np. dodawanie tekstu do numerow

* operator
* operand

* program manipulates objects
* commands
* data objects
* objects has types
* scalar object (cant be subdivided)?
* non-scalar (have internal structure that can be accessed)
* type conversion (implicite, explicite)

* scalars
* int
* float
* bool
* NoneType

* float -> int - truncate after decimal

* expressions - combine objects and operators
* expresion has a value with type
* syntex for simple expression - object operator object
* assignment

* operatory: + - * / %(reszta z dzielenia remainder)     * (potegowanie power)
* operator precedence

* re-bind variable - previous value may still be stored in memory but lost the handle for it

### 2. Branching and Iteration

* string - sequenc of characters
* concatonation of strings
* input("Type anything")
* operatory porównawcze
* operatory logiczne
* control flow (branching), condition
* control flow loops

### 3. String Manipulation, Guess and Check, Approximations, Bisection

* strings - sequence of characters
* string indexing
* slice [start:stop:step=1]
* strings are immutable
* for char in word:
* exhaustive enumeration
* approximate solutions
* bisection search

### 4. Decomposition, Abstractions, Functions

* decomposition: modules, function, clases
* abstraction - supressing details
* call /invoke function
* variable scope
* formal actual parameter
* scope mozna uznac jako new environment
* w Pythonie funkcja nie ma w ciele return, to interperete doda "return None"
* In python function can access variable from outer scope, but can change them
* ale mozna to zrobic global variable

### 5. Tuples, Lists, Aliasing, Mutability, and Cloning

* tuple są immutable, listy są mutable
* compund data types: data consists of other type data
* swap variable (x, y) = (y, x)
* `//` integer division
* % division remainder modulo
* del(some_list[1])
* split, join
* list sorted is inplace, sorte() returns copy
* cloning a list bla[:]

### 6. Recursion, Dictionaries

* recursion - function calls itself (divide-and-conquer or decrease-and-conquer)
* recursion
    * recursion step - reduce problem to simpler / smaller version of same problem
    * base case - case that can be solved directly after reduction
    * each recursion call to a function crates its own scope/environment
    * inductive reasoning
    * examples
        * towers of hanoi
        * fibonacci
        * factorial
        * palindrom
* dictionaries (mutable, unordered), key, value, look ups
* del (dict_name[key_name])
* memoization

### 7. Testing, Debugging, Exceptions, and Assertions

* classes of tests
    * unit testing - testing each function
    * regression testing - add test for bugs as you found and rerun tests
    * integration testing - check overall program works
* testing approach
    * intuition - based on problem create tests
    * black box testing - explore test paths through specification
    * glass box testing - explore paths through code

### Lecture 8: Object Oriented Programming

* object has: type, data representation, interactions
* object is an instance of class
* atributes and methods
* special methods

### Lecture 9: Python Classes and Inheritance

* class definition of an object type vs instance of class
* getters and setters
* inheretance
* class variables

### 10. Understanding Program Efficiency, Part 1

* problem mierzenia wydajności algorytmów
    * można mierzyć czas, użycie pamięci/procesora
    * mierzenie liczby operacji
    * [[Notacja dużego O]]
* orders of grow
* koncepcja: best case, average case i worst case
* orders of growth
* focus on dominant terms
* combine
    * law of addition for O() - used with sequential statements, bierzemy najwyższą klasę złożoności
    * in nested we multiplay
* complexity classes
    * O(1) - constant
    * O(log n) - logarithmic
    * O(n) - linear
    * O(n log n) - log-linear
    * O(n^c) - polynomial (c is constant)
    * O(c^n) - exponential (c is constant)

### 11. Understanding Program Efficiency, Part 2

* Omówienie klas złożoności algorytmicznej na przkładach
    * O(1) - not depends on size of problem
    * O(log n) - redue problem in half each step
    * O(n) - simple iterative or recursive programs
    * O(n log n) -
    * O(n^c)  - nested loops or revursive calls
    * O(c^n) - multiple recursive calls
* [[binary search|Wyszukiwanie binarne]]
* Towers of Hanoi complexity is exponential
* power set - rozwiazanie rekurencyjne
* complexity of python common operations on lists and dicts


### 12. Searching and Sorting

* listy mogą być posortowane i nie posortowane
* [[Linear Search|Przeszukiwanie liniowe]] - brute force search
* [[Bisection search|Wyszukiwanie binarne]]
* Amortized cost , sort a list once then do many searches
* [[Bogosort]]
* [[Bubble sort|Sortowanie bąbelkowe]]
* [[Selection sort|Sortowanie przez wybieranie]]
* [[Merge sort|Sortowanie prez scalanie]]
* Three A's of computational thinking: abstraction, automation and algorithms
