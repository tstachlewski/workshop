# Zadanie - REST to SMS  #

## Cel zadania ##
Celem zadania jest zbudowanie prostej aplikacji RESTowej, która będzie przyjmowała parametr, który następnie zostanie wysłany w postaci SMSa do użytkownika

## Kroki ##

ETAP 1 - Konfiguracja SNS
1.	Przejdź do usługi "Simple Notification Service" a następnie wyszukaj opcję "Create Topic". 
2.	Nadaj topicowi własną nazwę a następnie utwórz go.
3.	Zanotuj sobie 'Topic ARN' topicu, który utworzyłeś (będzie postaci arn:...)
4.	Dodaj subskrypcje do swojego topicu:
		- Protocol: SMS
		- Endpoint: 0048 + twoj numer


ETAP 2 - Utworzenie kolejki SQS
1.	Przejdź do usługi "Simple Queue Service"
2.	Utwórz standardową kolejkę (nadaj jej własną nazwę)
3.	Pod przyciskiem "Queue Actions" wybierz opcję "Subscribe queue to SNS topic"
4.	W nowo utworzonym wizardzie wybierz swój topic (utworzony w etapie pierwszym) i zatwierdź powiązanie

ETAP 3 - Utworzenie funkcji Lambda
1.	Przejdź do usługi Lambda i utwórz nową pustą funkcję.
2.	Skonfiguruj funkcję następująco:
		- Nazwa dowolna
		- Runtime: Python 2.7
		- Kod funkcji: zawartość pliku 'lambda_rest_to_sms.py'
		- W ramach sekcji "Environment variables" dodaj zmienną "SNS_TOPIC" gdzie wartość to ARN skopiowany w etapie pierwszynm
		- Existing role: LambdaRole
		- W sekcji "Advanced settings" zwiększ czas do 5 minut.
3.	Przetestuj funkcję podając następujące wejście:

{
  "queryStringParameters": {
    "message": "To jest test z chmury"
  }
}

ETAP 4 - Dodanie endpointa RESTowego
1.	W ramach funkcji przejdź do zakładki "Triggers" i wybierz opcję "Add trigger"
2. 	Jako wyzwalacz funkcji wybierz funkcję "API Gateway"
3.	Ustaw parametr "Security" na "Open" po czym zatwierdź wizarda.
4.	Wejdź na ukazany link dodając na końcu parametr "?message=test"
5. 	Powinieneś otrzymać wiadomość SMS
