# CloudFormation - Makro #


### 1. W ramacach Cloud 9 utwórz nowy folder a następnie wykonaj następujące polecenie. Przygotują one Lambdę, którą będziemy dalej używać.

<details><summary>show</summary>
<p>

```bash
mkdir MyMakro
cd MyMakro
```

</p>
</details>


Wrzuć do tego katalogu plik my_makro.py - przeanalizuj go.

Spakuj tak utworzoną zawartość folderu a następnie utwórz nowy bucket S3, do którego załadujujesz tego zipa.

<details><summary>show</summary>
<p>

```bash
zip -r my_makro.zip .
aws s3api create-bucket --region eu-west-1 --create-bucket-configuration LocationConstraint=eu-west-1 --bucket my-custom-cfn-resource-1431324
aws s3 cp my_makro.zip s3://my-custom-cfn-resource-1431324/my_makro.zip
```

</p>
</details>



### 2. Utwórz Lambdę wykorzystując (czy to nie oczywiste?) szablon CfnMyMakro.yaml - znajdź namiary na swój bucket S3 gdzie została umieszczona twoja funkcja.

<details><summary>show</summary>
<p>

```bash
aws cloudformation update-stack --stack-name MyNamer --template-body file://CfnMyMakro.yaml --capabilities CAPABILITY_IAM
```

</p>
</details>


### 3. Utwórz nowy stack BasicNetwork-WithTransform.yaml - przeanalizuj go a następnie utwórz.

<details><summary>show</summary>
<p>

```bash
aws cloudformation deploy --template-file BasicNetwork-WithTransform.yaml --stack-name BasicNetwork-WithTransform --parameter-overrides Identifier=DEV
```

</p>
</details>


### 4. W ramacach Cloud 9 utwórz nowy folder a następnie wykonaj następujące polecenie. Przygotują one Lambdę, którą będziemy dalej używać.

<details><summary>show</summary>
<p>

```bash
mkdir MyMakroTagger
cd MyMakroTagger
```

</p>
</details>


Wrzuć do tego katalogu plik my_makro_tagger.py - przeanalizuj go.

Spakuj tak utworzoną zawartość folderu a następnie utwórz nowy bucket S3, do którego załadujujesz tego zipa.

<details><summary>show</summary>
<p>

```bash
zip -r my_makro_tagger.zip .
aws s3api create-bucket --region eu-west-1 --create-bucket-configuration LocationConstraint=eu-west-1 --bucket my-custom-cfn-resource-1431324
aws s3 cp my_makro_tagger.zip s3://my-custom-cfn-resource-1431324/my_makro_tagger.zip
```

</p>
</details>


### 5. Utwórz Lambdę wykorzystując szablon CfnTaggerMakro.yaml - znajdź namiary na swój bucket S3 gdzie została umieszczona twoja funkcja.

<details><summary>show</summary>
<p>

```bash
aws cloudformation create-stack --stack-name TaggerMakro --template-body file://CfnTaggerMakro.yaml --capabilities CAPABILITY_IAM
```

</p>
</details>

### 3. Utwórz nowy stack BasicNetwork-WithTaggerTransform.yaml - przeanalizuj go a następnie utwórz.

<details><summary>show</summary>
<p>

```bash
aws cloudformation deploy --template-file BasicNetwork-WithTaggerTransform.yaml --stack-name BasicNetwork-WithTaggs
```

</p>
</details>
