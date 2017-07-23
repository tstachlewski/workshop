# Zadanie - CLI on Windows  #

## Cel zadania ##
Celem zadania jest instalacja i przetestowanie działania CLI na platformie Windows

## Kroki ##

ETAP 1 - Instalacja CLI
1.	Zainstaluj CLI zgodnie z instrukcjami zawartymi na stronie http://docs.aws.amazon.com/cli/latest/userguide/awscli-install-windows.html#install-msi-on-windows 
2.	Zweryfikuj działanie instalacji poprzez wywołanie polecenia "aws --version" w lini komend.

ETAP 2 - Konfiguracja CLI
1.	Wowyłaj polecenie 'aws configure'
2.	Podaj następujące parametry konfiguracji:
	- AWS Access Key ID: Wklej wartość dla swojego użytkownika
	- AWS Secret Access Key: Wklej wartość dla swojego użytkownika
	- Default region name:  eu-west-1
	- Default output format: json
3.	Zweryfikuj działanie CLI poprzez wywołanie polcenia: "aws ec2 describe-regions"

ETAP 3 - Utworzenie serwera EC2
1.	Utwórz nowy serwer wywołująć następujące polecenie: aws ec2 run-instances --image-id ami-d7b9a2b1 --instance-type t2.micro --tag-specifications ResourceType=instance,Tags=[{Key=Name,Value=TWOJE_IMIE}]
2.	Po kilku sekundach serwer powinien pojawić się na liście serwerów EC2 w konsoli AWS
(Dokumentacja do CLI znajduje się pod adresem: http://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html)
	
	 