# Zadanie - Text to Speech  #

## Cel zadania ##
Celem zadania jest zbudowanie prostej aplikacji, która będzie wykrywała nowe pliki tekstowe (.txt) w S3 i na tej podstawie tworzyła plik audio.


## Kroki ##

ETAP 1 - Utworzenie bucketu S3
1.	Przejdź do usługi S3 i utwórz nowy bucket w regionie Irlandia
2.	W ramach bucketu utwórz następnie folder 'text' a w nim dwa foldery: 'Maja' oraz 'Joanna' (wielkość liter ma znaczenie). To właśnie do tych folderów będziesz wrzucał pliki tekstowe - do folderu 'Maja' pliki w języku polskim a do folderu 'Joanna' pliki w języku angielskim.

ETAP 2 - Utworzenie bazy nierelacyjnej
1.	Przejdź do usługi DynamoDB i utwórz nową tabelę
2.	Jako ID tabeli utwórz parametr 'name' o typie String. 

ETAP 3 - Utworzenie funkcji Lambda
1.	Przejdź do usługi Lambda i utwórz nową funkcję.
2.	Jako wyzwalacz funkcji wybierz S3, skonfiguruj go aby monitorował bucket utworzony w punkcie '1' jako prefix dodaj wartość 'text' a jako sufix dodaj '.txt'. Powinieneś wykrywać eventy o typie PUT. Uaktywnij trigger.
3.	Skonfiguruj funkcję następująco:
		- Nazwa dowolna
		- Runtime: Python 2.7
		- Kod funkcji: zawartość pliku 'lambda_text_to_audio.py'
		- W ramach sekcji "Environment variables" dodaj zmienną 'DB_NAME' o wartości tabeli z punktu drugiego.
		- Existing role: LambdaRole
		- W sekcji "Advanced settings" zwiększ czas do 5 minut.
4.	Po utworzeniu funkcji wszystko jest gotowe. Przetestuj aplikację wrzucając do katalogu 'maja' pliki 'polly_test.txt'. Jeśli wszystko przebiegnie poprawnie, powinieneś otrzymać w buckecie nowy folder 'audio' gdzie zostanie umieszczony plik .mp3
