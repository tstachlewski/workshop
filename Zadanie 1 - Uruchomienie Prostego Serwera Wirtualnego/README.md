# Zadanie - Uruchomienie prostego serwera wirtualnego  #

## Cel zadania ##
Celem zadania jest uruchomienie prostego serwera wirtualnego, na którym zostanie uruchomiony prosta usługa webowa i strona WWW

## Kroki ##
1. W konsoli AWS przejdź do usługi EC2 gdzie wyszukaj opcję "Launch Instance".
2. W ramach utworzonego wizarda pozostań przy wybranym obrazie AMI "Amazon Linux".
3. W ramach trzeciego kroku pozostań przy domyślnej wielkości serwera "t2.micro"
4. W ramach piątego kroku wizarda zmodyfikuj usutawienia zaawanowane "Advanced Details" - w tym celu wklej skrypt umieszczony w pliku "user_data.txt"
5. Na kroku czwartym wizarda dodaj drugi dysk do serwera. Dysk powinien mieć pojemność 10 MB. Zaznacz opcję "Delete on Termination"
6. Na piątym kroku wizarda otaguj swój serwer, w tym celu dodaj następujące tagi:
	Name : TwojeInicjaly
	Env: Test
	System: E-Commerce
7. W ramach 6 kroku wizarda skonfiguruj reguły FW dla serwera. W tym celu:
	- Utwórz Security Groupę o nazwie "FireWall_TwojeInicjaly".
	- Utwórz nową regułę przepuszczającą ruch HTTP z całego świata (0.0.0.0/0)
	- Utwórz regułę przepuszczającą ruch SSH z 'twojego adresu IP'
8. Przejdź do ostatniego kroku wizarda i wybierz opcję 'Launch'. Pojawi się popup w którym wybierz opcję  "Create a new key pair" - po czym wpisz swoje inicjały i pobierz klucze.
9. Wciśnij przycisk "Launch Instance" - po czym odczekaj 2 minuty i przetestuj działanie serwera.
 