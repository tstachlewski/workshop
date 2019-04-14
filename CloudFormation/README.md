# Warsztaty AWS #

## Wstęp ##
Uruchom środowisko Cloud9 w regionie Irlandia. Po uruchomieniu się środowiska, skopiuj do niego plik 'BasicNetwork.yaml' - plik ten będziemy wykorzystywać przez większość część warsztatów.

### 1. Utwórz stack 'BasicNetwork' CloudFormation z wykorzystaniem CLI

<details><summary>show</summary>
<p>

```bash
aws cloudformation create-stack --stack-name BasicNetwork --template-body file://BasicNetwork.yaml
```

</p>
</details>

### 2. Wylistuj zasoby utworzone w poprzednim stacku.

<details><summary>show</summary>
<p>

```bash
aws cloudformation list-stack-resources --stack-name  BasicNetwork
```

</p>
</details>

### 3. Skopiuj zawartość szablonu 'BasicArchitecture' do środowiska Cloud9 i spróbuj utworzyć stack na jego podstawie.

<details><summary>show</summary>
<p>

```bash
aws cloudformation create-stack --stack-name MyApp --template-body file://BasicArchitecture.json
```

</p>
</details>


### 4. Upewnij się, że na swoim koncie masz utworzone klucze EC2 a następnie spróbuj utworzyć ponownie poprzedni stack dodajac w parametrach nazwę klucza.

<details><summary>show</summary>
<p>

```bash
aws cloudformation create-stack --stack-name MyApp --template-body file://BasicArchitecture.json --parameters ParameterKey=KeyName,ParameterValue=key-Ireland
```

</p>
</details>

### 5. Zaktualizuj szablon 'BasicNetwork.yaml' - np. poprzez modyfikację tag-a Name i zaktualizuj utworzony wcześniej stack.

<details><summary>show</summary>
<p>

```bash
aws cloudformation update-stack --stack-name BasicNetwork --template-body file://BasicNetwork.yaml
```

</p>
</details>

### 6. Zaktualizuj szablon 'BasicNetwork.yaml' - np. poprzez modyfikację adresacji jednej z podsieci i zaaktualizuj utworzony wcześniej stack.

<details><summary>show</summary>
<p>

```bash
aws cloudformation update-stack --stack-name BasicNetwork --template-body file://BasicNetwork.yaml
```

</p>
</details>

### 7. Utwórz ChangeSet dla szablonu i zweryfikuj czy wprowadza jakieś zmiany.

<details><summary>show</summary>
<p>

```bash
aws cloudformation create-change-set --stack-name BasicNetwork --template-body file://BasicNetwork.yaml --change-set-name MyChange
aws cloudformation describe-change-set --stack-name BasicNetwork  --change-set-name MyChange
```

</p>
</details>
