---
title: Git dobre praktyki
created: '2020-04-27T09:27:59.410Z'
modified: '2020-04-27T09:28:05.068Z'
---

# Git dobre praktyki

!! Ogólne

* Twórz czyste, jedno celowe/funkcyjne commity
* Małe commity
* Commituj wcześnie i często
* Nie commituj generowanych plików
* Nie zmieniaj historii jeżeli opublikowałeś branch

!! Tytuły commitów

* w czasie terażniejszym, trybie rozkazującym (imperative, present tense)
* pierwsza linia nie powinna być dłuższa niż 50 znaków, kolejne 80
* Tytuł z dużej litery i kończy się kropką
* w opisie powinien być motyw commita, a nie kontrast z poprzednim zachowaniem
* jeżeli dotyczy jakiegoś taska to dajemy `Closes #234, #123`
* struktura commita

```
<type>: <subject>
<body>
```

* type:
** feat (new feature)
** fix (bug fix)
** docs (changes to documentation)
** style (formatting, missing semi colons, etc; no code change)
** refactor (refactoring production code)
** test (adding missing tests, refactoring tests; no production code change)
** chore (updating grunt tasks etc; no production code change)

!! Workflow

!! Zasoby

* [[Git project guidelines|https://git.kernel.org/pub/scm/git/git.git/tree/Documentation/SubmittingPatches?id=HEAD]]
* [[Commit Often, Perfect Later, Publish Once: Git Best Practices|https://sethrobertson.github.io/GitBestPractices/#commit]]
