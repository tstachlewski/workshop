# CloudFormation - Nested Stacks #


### 0. Utwórz nowy bucket S3 i wrzuć do niego szablon BasicNetwork

<details><summary>show</summary>
<p>

```bash
aws s3api create-bucket --region eu-west-1 --create-bucket-configuration LocationConstraint=eu-west-1 --bucket testbucket123123123123123
aws s3 cp BasicNetwork.yaml s3://testbucket123123123123123/BasicNetwork.yaml

```

</p>
</details>

### 1. Utwórz nowy stack na podstawie szablonu RootTemplate1.yaml - niech będzie on nadrzędny dla szablonu BasicNetwork.

<details><summary>show</summary>
<p>

```bash
aws cloudformation create-stack --stack-name RootTemplate --template-body file://RootTemplate1.yaml
```

</p>
</details>

### 2. Utwórz nowy stack na podstawie szablonu RootTemplate2.yaml - niech będzie on nadrzędny dla szablonu BasicNetwork.

<details><summary>show</summary>
<p>

```bash
aws cloudformation update-stack --stack-name RootTemplate --template-body file://RootTemplate2.yaml
```

</p>
</details>


### 3. Utwórz nowy stack na podstawie szablonu RootTemplate3.yaml - tym razem niech korzysta z dwóch szablonów Nested - sieci i serwera.

<details><summary>show</summary>
<p>

```bash
aws s3 cp LinuxServer.yaml s3://testbucket123123123123123/LinuxServer.yaml
aws cloudformation update-stack --stack-name RootTemplate --template-body file://RootTemplate3.yaml
```

</p>
</details>

### 4. Skasuj poprzednie stacki. Utwórz ponownie stack BasicNework i opisz go CLI zwracając uwagę na jego sekcję outputs.

<details><summary>show</summary>
<p>

```bash
aws cloudformation create-stack --stack-name BasicNetwork --template-body file://BasicNetwork.yaml
aws cloudformation describe-stacks --stack-name BasicNetwork
```

</p>
</details>

### 4. Zmodyfikuj poprzedni stack i dodaj w Outputach parametr Export - dzięki, któremu zwracane wartości będą mogły być łatwo reużywalne w innych stackach.(hint: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html). Zweryfikuj czy parametry są widoczne w sekcji Exports w CloudFormation.

<details><summary>show</summary>
<p>

```bash
aws cloudformation update-stack --stack-name BasicNetwork --template-body file://BasicNetwork-export.yaml
```

</p>
</details>

### 4. Wylistuj exporty CloudFormation w CLI.

<details><summary>show</summary>
<p>

```bash
aws cloudformation list-exports
```

</p>
</details>

### 5. Wylistuj exporty CloudFormation w CLI.

<details><summary>show</summary>
<p>

```bash
aws cloudformation list-exports
```

</p>
</details>

### 6. Przeanalizuj i utwórz stack LinuxServer-imported.yaml - gdzie wykorzystywana jest zmienna z poprzedniego stacka.

<details><summary>show</summary>
<p>

```bash
aws cloudformation create-stack --stack-name LinuxServer --template-body file://LinuxServer-imported.yaml
```

</p>
</details>


### 7. Wylisuj stacki, które używają zmiennej eksportowej PublicSubnet1

<details><summary>show</summary>
<p>

```bash
aws cloudformation list-imports --export-name PublicSubnet1
```

</p>
</details>
