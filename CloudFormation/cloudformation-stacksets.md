# CloudFormation - StackSets #

CloudFormation StackSet to funkcjonalność, dzieki, której można w łatwy sposób zarządzać szablonami CloudFormation w ramach wielu kont i wielu regionów. W ramach tych zadań, wykorzystamy je aby uruchomić przykładowe szablony w innym koncie AWS.

### 1. Utwórz poniższy stack w swoim koncie. Stack ten utworzy rolę, która będzie wymagana do operowania na innych kontach AWS.

<details><summary>show</summary>
<p>

```bash
aws cloudformation create-stack --stack-name AWSCloudFormationStackSetAdministrationRole --template-url https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/AWSCloudFormationStackSetAdministrationRole.yml --capabilities CAPABILITY_NAMED_IAM

```

</p>
</details>


### 2. Utwórz poniższy stack w swoim drugim koncie, na którym później będziesz zdalnie uruchamiał inne stacki CloudFormation. Zauważ je znajduje się w nim parametr, który powinien być numerem konta z twojego konta głownego (poprzedni punkt).

<details><summary>show</summary>
<p>

```bash
aws cloudformation create-stack --stack-name AWSCloudFormationStackSetExecutionRole --template-url https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/AWSCloudFormationStackSetExecutionRole.yml --capabilities CAPABILITY_NAMED_IAM  --parameters ParameterKey=AdministratorAccountId,ParameterValue=154190748210
```

</p>
</details>


### 3. Wykorzystaj GUI CloudFormation aby utworzyc nowy StackSets i uruchomić na drugim koncie szablon BasicNetwork - który wcześniej wrzuciłeś do bucketu S3.

### 4. Powtórz poprzednią operację z wykorzystaniem CLI.

<details><summary>show</summary>
<p>

```bash
aws cloudformation create-stack-set --stack-set-name POWER-RING --template-body file://BasicNetwork.yaml
aws cloudformation create-stack-instances --stack-set-name POWER-RING --accounts 266195638045 --regions "eu-west-1"
```

</p>
</details>


### 5. Dokonaj jakiejś poprawki w szabonie BasicNetwork i dokonaj aktualizacji StackSet.

<details><summary>show</summary>
<p>

```bash
aws cloudformation update-stack-set --stack-set-name POWER-RING --template-body file://BasicNetwork.yaml
```

</p>
</details>

### 6. Skasuj zasoby.

<details><summary>show</summary>
<p>

```bash
aws cloudformation delete-stack-instances --stack-set-name POWER-RING --accounts 266195638045 --regions "eu-west-1" --no-retain-stacks
aws cloudformation delete-stack-set --stack-set-name POWER-RING
```

</p>
</details>
