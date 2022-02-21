# Robson API : o seu Banker Digital

<p align="center">
    <a href="#">
        <img src="https://user-images.githubusercontent.com/51249341/154862171-311f552d-61a0-4966-a345-c564d5a0baa6.png" alt="Project logo">
    </a>
</p>



<h3 align="center">Bem vindo ao Robson API!</h3>


---

Conteúdo

1. [Introdução](#introdução)
1. [O Problema](#o-problema)
1. [Oportunidade de Mercado](#oportunidade-de-mercado)
1. [Nossa Solução](#nossa-solução)
1. [Autores](#autores)

---

## Introdução

O Robson é um app desenvolvido para o Hackathon XP - Open Finance com o objetivo de fornecer consultorias de
investimento personalizadas a qualquer investidor, através do uso de inteligência artificial aplicada à carteira
consolidada do cliente via open finance.

O app oferece uma visualização consolidada da carteira do cliente, independentemente da instituição financeira onde
investe, e vai fazendo sugestões de rebalanceamento de carteira para otimizar a performance dos investimentos.

---

## O Problema

O Brasil ainda tem uma porcentagem pequena da população que investe no setor financeiro

E daqueles que investem, a grande maioria ainda não tem os conhecimentos adequados para fazer uma gestão apropriada de
seus investimentos.

Segundo o último Raio X do Investidor Brasileiro 2021, realizado pela ANBIMA, dos brasileiros que investem:

- 29% ainda investe na poupança
- 55% busca informações de investimento com amigos e parentes
- 61% não sabe o principal fator na escolha do investimento realizado.

## Oportunidade de Mercado

Acreditamos que o Open Finance permitirá uma redemocratização no acesso a serviços financeiros de qualidade, pelo qual decidimos criar o Robson.

Através da agregação de contas, nosso algoritmo conseguirá realizar sugestões de investimento mais aderentes ao perfil
do investidor, replicando o trabalho que um consultor de valores mobiliários faria com a carteira de pessoas de alta
renda.

Assim qualquer pessoa conseguirá ter uma melhor segurança na gestão dos seus investimentos.


## Nossa Solução

Usamos a inteligência artificial para segregar os usuários em grupos, para podermos oferecer investimentos objetivos e
comum entre eles e oferecer para novos usuários com o mesmo perfil do grupo.

### Arquitetura

![Arquitetura](./img/architecture.png)

### Endpoints

#### Usuario

> #### [GET] => <tt> /user/<string:user_id> </tt>
> *Pega usuarios no banco de dados*

> #### [GET] => <tt> /user/<string:user_id>/allocation </tt>
> *Pega alocação de investimentos do usuario.*
>
> Exemplo:
>```json
>{
>    "categories": {
>        "unknown": {
>            "percentage": 0.0,
>            "amount": 0
>        },
>        "variable_income": {
>            "percentage": 5.86,
>            "amount": 1651
>        },
>        "post_fixed": {
>            "percentage": 56.48,
>            "amount": 15914
>        },
>        "multi_market": {
>            "percentage": 1.17,
>            "amount": 331
>        },
>        "global": {
>            "percentage": 0.0,
>            "amount": 0
>        },
>        "inflation": {
>            "percentage": 36.49,
>            "amount": 10282
>        }
>    },
>    "total": 28178.0
>}
>```

> #### [GET] => <tt> /user/<string:user_id>/recommended_allocation </tt>
> *Pega alocação recomendado de investimentos seguindo o perfil do usuario.*

#### Objetivos

> #### [POST] => <tt> /objective/create </tt>
> *Cria um novo objetivo.*

#### Inteligencia artificial

> #### [GET] => <tt> /ai/cluster/ </tt>
> *Lista usuarios separados em clusters de acordo com suas transaçoes PIX.*
> > Confira [Clusterização](#clusterização) para mais detalhes.

### Clusterização

A clusterização é um método de classificação de dados que separa e categoriza em grupos. Usamos a clusterização para
segregar os usuários em grupos permitindo criar previsões de seus objetivos de vida, assim podendo oferecê-lo sugestões
de investimentos personalizados de acordo com o momento atual de sua vida.

Pegamos os CNPJ de cada transação feita pelo usuário, usando o histórico de pix provido pela api da xp. A api da XP nos
devolve apenas CPF, porém assumimos que com Open Finance esse dado estaria disponível com a devida permissão do usuário.

Com o CNPJ em mãos acessamos uma API pública para capturar as descrições dos CNAE e os CNAES secundários e usamos para
cruza e cria grupos com consumo parecido. Assim podendo propor um objetivo que seja comum ao grupo.

Fizemos um exemplo com um pequeno grupo de usuários inseridos manualmente no código, nesse caso foi possível separar os
usuários em dois grupos, um com consumo parecido e outro com consumo diferente. Com uma base de dados maior seria
possível a análise inteligente de todos os usuários, relacionando com os investimentos e objetivos.

- Entrada:

```python
UserTransactions(
    "JOAO",  # ID do Usuário
    0.1,  # Suitability (Perfil de investidor)
    [
        # Valor, Descrição do CNAE, Data da transação
        Transaction(100, "Educação infantil creche", "2022-01-01"),
        Transaction(50, "Fabricação outros brinquedos jogos recreativos especificados anteriormente",
                    "2022-01-02"),
        Transaction(200, "camisa flamenngo", "2022-01-03"),
        Transaction(20, "camisa flamego bebes", "2022-01-03"),
        Transaction(200, "gasolina", "2022-01-03"),
    ]
),
UserTransactions(
    "MARIA",
    0.1,
    [
        Transaction(12, "Educação infantil pré-escola", "2022-01-01"),
        Transaction(80, "Comércio varejista brinquedos artigos recreativos", "2022-01-02"),
        Transaction(30, "brinquedos bebes", "2022-01-05"),
        Transaction(30, "leite", "2022-01-08"),
        Transaction(50, "comida", "2022-01-010"),
    ]
),
UserTransactions(
    "ROBSON",
    0.1,
    [
        Transaction(60, "comida", "2022-01-01"),
        Transaction(300, "Aluguel aparelhos jogos eletrônicos", "2022-01-02"),
        Transaction(500, "skin fortnite", "2022-01-05"),
        Transaction(300, "controle xbola", "2022-01-08"),
        Transaction(50, "comida", "2022-01-010"),
    ]
),
UserTransactions(
    "RODRIGO",
    0.26,
    [
        Transaction(60, "comida", "2022-01-01"),
        Transaction(40, "Exploração jogos eletrônicos recreativos", "2022-01-02"),
        Transaction(500, "camisa botafogo", "2022-01-05"),
        Transaction(300, "controle xbola", "2022-01-08"),
        Transaction(50, "nerd", "2022-01-010"),
    ]
),
```

- Resposta da API:

```json
{
  "JOAO": 0,
  "MARIA": 0,
  "ROBSON": 1,
  "RODRIGO": 1
}
```

### Tecnologias Utilizadas

- Python
- Flask
- SQLite
- Open Banking XP API
- Scikit learn

---

## Autores

* [Lucas Martins](https://github.com/lucaomartins/)
* [Bruno Teixeira](https://github.com/brunotsantos1997)
* [Christian Rojas](https://www.linkedin.com/in/christianr1/)
* [Giovanni Postiglione](https://www.linkedin.com/in/giovannisaboya/)
* [Gisele SPrata](https://www.linkedin.com/in/gisprata/)
