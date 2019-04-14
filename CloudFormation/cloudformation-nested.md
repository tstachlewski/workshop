# CloudFormation - Podstawy CLI #

## Wstęp ##
Uruchom środowisko Cloud9 w regionie Irlandia. Po uruchomieniu się środowiska, skopiuj do niego plik 'BasicNetwork.yaml' - plik ten będziemy wykorzystywać przez większość część warsztatów.

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
