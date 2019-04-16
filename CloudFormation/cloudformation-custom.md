# CloudFormation - Custom Resources #

Custom Resources to metoda dzięki, której jesteś w stanie tworzyć kompletnie własne zasoby w ramach szablonu CloudFormation. W tym celu w pierwszej kolejnosci utworzymy Lambdę - która była by odpowiedzialna za tworzenie naszych zasobów. W celach warsztatowych, lambda ta nie będzie tworzyć faktycznych obiektów - ale wyśle nam SMS-a z informacją, że ktoś tworzy szablon.

### 1. W ramacach Cloud 9 utwórz nowy folder a następnie wykonaj następujące polecenie. Przygotują one Lambdę, którą będziemy dalej używać.

<details><summary>show</summary>
<p>

```bash
mkdir MyNotifier
cd MyNotifier
pip install crhelper -t .
```

</p>
</details>

Wrzuć do tego katalogu plik my_lambda.py - przeanalizuj go.

Spakuj tak utworzoną zawartość folderu a następnie utwórz nowy bucket S3, do którego załadujujesz tego zipa.

<details><summary>show</summary>
<p>

```bash
zip -r my_custom_cfn_resource.zip .
aws s3api create-bucket --region eu-west-1 --create-bucket-configuration LocationConstraint=eu-west-1 --bucket my-custom-cfn-resource-1431324
aws s3 cp my_custom_cfn_resource.zip s3://my-custom-cfn-resource-1431324/my_custom_cfn_resource.zip
```

</p>
</details>



### 2. Utwórz Lambdę wykorzystując (czy to nie oczywiste?) szablon CfnLambdaNotifier.yaml - znajdź parametr PHONE i go zaktualizuj - podobnie jak namiary na swój bucket S3 gdzie została umieszczona twoja funkcja.

<details><summary>show</summary>
<p>

```bash
aws cloudformation create-stack --stack-name CfnLambdaNotifier --template-body file://CfnLambdaNotifier.yaml --capabilities CAPABILITY_IAM
```

</p>
</details>


### 3. Utwórz nowy stack BasicNetwork-WithCustom.yaml - przeanalizuj go a następnie utwórz. Jeśli wszystko zadziała prawidłowo - powinieneś dostać SMS-a w momencie jego utworzenia - oraz jego skasowania.

<details><summary>show</summary>
<p>

```bash
aws cloudformation create-stack --stack-name BasicNetwork-NOTIFYME --template-body file://BasicNetwork-WithCustom.yaml
```

</p>
</details>
