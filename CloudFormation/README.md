# Warsztaty AWS #

## Wstęp ##
Uruchom środowisko Cloud9 w regionie Irlandia. Po uruchomieniu się środowiska, skopiuj do niego plik 'BasicNetwork.yaml' - plik ten będziemy wykorzystywać przez większość część warsztatów.

### Utwórz stack CloudFormation z wykorzystaniem CLI

<details><summary>show</summary>
<p>

```bash
aws cloudformation create-stack --stack-name BasicNetwork --template-body file://BasicNetwork.yaml
```

</p>
</details>
