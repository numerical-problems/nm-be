## Instalação de bibliotecas:

-   Caso instale uma nova biblioteca, adicione ela no arquivo requirements.txt.

```shell
$ pip install -r requirements.txt
```

## Run server

> Powershell

```shell
$ set FLASK_APP=manage.py
```

-   Definir em um arquivo `.env` FLASK_APP="manage.py"
-   Executar o servidor

```
$ python -m flask run or flask run
```

## Run tests

> Powershell

```shell
$ pytest
```

### Requerimentos

-   Python 3.9

### Deploy

-   url: https://nm-be.herokuapp.com/
