# CloudFormation - Inne #


### 1. Wykorzystaj szablon BasicNetwork-2.yaml - aby powołać dwie sieci VPC. przy drugim wywołaniu, zmodyfikuj jednak szablon aby adresacja nie była z sieci 10.0.X.X a z 11.0.XX.

<details><summary>show</summary>
<p>

```bash
aws cloudformation deploy --template-file BasicNetwork-2.yaml --stack-name MyNetwork1
aws cloudformation deploy --template-file BasicNetwork-2.yaml --stack-name MyNetwork2
```

</p>
</details>

### 2. Utwórz połączenie pomiędzy sieciami wykorzystując szablon VPCPeering.yaml.

<details><summary>show</summary>
<p>

```bash
aws cloudformation deploy --template-file VPCPeering.yaml --stack-name VPCPeering --parameter-overrides Network1=MyNetwork1 Network2=MyNetwork2
```

</p>
</details>

### 3. Utwórz stack na podstawie SecretManager.yaml.

<details><summary>show</summary>
<p>

```bash
aws cloudformation deploy --template-file SecretManager.yaml --stack-name SecretManager
```

</p>
</details>


### 4. Utwórz stack na podstawie SecretManager.yaml.

<details><summary>show</summary>
<p>

```bash
aws cloudformation deploy --template-file SecretManager.yaml --stack-name SecretManager
```

</p>
</details>


### 5. Utwórz stack na podstawie secretuser.yaml.

<details><summary>show</summary>
<p>

```bash
aws cloudformation deploy --template-file secretuser.yaml --stack-name SecretUser --capabilities CAPABILITY_IAM
```

</p>
</details>


### 6. Zwaliduj jeden z wcześniej przygotowanych szablonów.

<details><summary>show</summary>
<p>

```bash
aws cloudformation validate-template --template-body  file://BasicNetwork.yaml
```

</p>
</details>

### 7. Utwórz stacki na podstawie poniższych szablonów, które wykreują stały adres IP a następnie podłaczą go do nowego serwera..

<details><summary>show</summary>
<p>

```bash
aws cloudformation deploy --template-file EIP.yaml --stack-name EIP
aws cloudformation deploy --template-file BasicNetwork-expot.yaml --stack-name Network
aws cloudformation deploy --template-file Server_with_EIP.yaml --stack-name ServerWithEIP

```

</p>
</details>


### 8. Utwórz poniższy stack i go przeanalizuj.

<details><summary>show</summary>
<p>

```bash
aws cloudformation deploy --template-file BasicArchitecture.json --stack-name BasicArchitecture.json

```

</p>
</details>
