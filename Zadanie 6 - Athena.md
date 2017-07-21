# Zadanie - Athena - analityka bezserwerowa  #

## Cel zadania ##
Celem zadania jest przetestowanie funcjonalności analityki bezserwerowej

## Kroki ##

ETAP 1 - Utworzenie bucketu S3
1.	Przejdź do usługi S3 i utwórz nowy bucket w regionie Irlandia
2.	Do utworzonego bucketu wrzuć plik 'simpleCSVFile.csv' - możesz go zmodyfikować dodając swoje dane

ETAP 2 - Athena
1.	Przejdź do usługi Athena
2.	Wywołaj skrypt athena-CreateSimpleTable.txt tworzący widok na dane umieszczone w buckecie S3. Pamiętaj aby zmodyfikować go, poprzez podanie nazwy bucketu utworzonego w etapie pierwszym.
3.	Przetestuj działanie całości poprzez wywołanie wywołanie zapytań SQL na utworzonym widoku (np. "SELECT * FROM people_list")
