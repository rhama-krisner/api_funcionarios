# API de Cadastro de Funcionários

Para que seja usado a api, são necessários alguns downloads e configurações.


|O que é necessário|Download                                  |
|:-----------------|:-----------------------------------------|
|Python 3.x            |https://www.python.org/downloads/     |
|Django | https://www.djangoproject.com/start/                |
|Django RestFramework | https://www.django-rest-framework.org/|
|Insomnia|https://insomnia.rest/download|

### Endereços configurados para usar com Insomnia
|Endereços| |
|:-----------------:|:----------------------------------------|
|GET | http://127.0.0.1:8000/user/funcionarios/|
|POST | http://127.0.0.1:8000/user/add/|
|PUT | http://127.0.0.1:8000/user/*id*|
|DELETE | http://127.0.0.1:8000/user/*id*|




### Para Realizar o GET, são necessários três informações.

* nome
* cpf 
* cargo            

~~~
{
   "nome":"John Smith",
   "cpf":"123456789000",
   "cargo":"Dev Python Backend"
}
~~~


<div style="text-align: right"> <i>v1.0 </div>
