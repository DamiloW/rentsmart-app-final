# RentSmart - R.M Imóveis 🏠

Sistema desenvolvido em Python para automatizar o cálculo de orçamentos de locação de imóveis da **R.M Imóveis**, utilizando fundamentos de **Programação Orientada a Objetos (POO)**.

O sistema permite realizar orçamentos para **Casas, Apartamentos e Estúdios**, aplicando automaticamente as regras de negócio definidas para cada tipo de imóvel.

## Funcionalidades

* Interface interativa via terminal.
* Validação das entradas fornecidas pelo usuário.
* Cálculo automático do aluguel mensal.
* Aplicação das regras específicas de cada tipo de imóvel.
* Cálculo de adicionais de acordo com quantidade de quartos e garagem.
* Aplicação de desconto de 5% para apartamentos quando o cliente não possui crianças.
* Cálculo das vagas de garagem para estúdios.
* Separação entre valor do aluguel e taxa contratual.
* Possibilidade de parcelar a taxa contratual de 1 a 5 vezes.
* Apresentação detalhada do orçamento final.
* Geração automática de arquivo `.csv` com a projeção dos primeiros 12 meses de pagamento.

## Regras de negócio

### Casa

* 1 quarto: R$ 900,00.
* 2 quartos: adicional de R$ 250,00.
* Garagem: adicional de R$ 300,00.

### Apartamento

* 1 quarto: R$ 700,00.
* 2 quartos: adicional de R$ 200,00.
* Garagem: adicional de R$ 300,00.
* Clientes sem crianças recebem 5% de desconto sobre o valor do aluguel após os adicionais.

### Estúdio

* Valor base: R$ 1.200,00.
* Até 2 vagas de garagem: R$ 250,00.
* Cada vaga adicional acima de 2: R$ 60,00.

### Taxa contratual

* Valor da taxa: R$ 2.000,00.
* Pode ser paga em até 5 parcelas.
* O sistema permite escolher entre 1 e 5 parcelas.

## Estrutura do projeto

```text
RentSmart/
│
├── main.py
├── imoveis.py
├── README.md
└── projecao_12_meses_*.csv
```

### `main.py`

Responsável pela interação com o usuário, validação das entradas, criação dos objetos, apresentação do orçamento e geração da projeção financeira em `.csv`.

### `imoveis.py`

Contém as classes utilizadas pelo sistema:

* `Imovel` — classe base com atributos comuns.
* `Casa` — representa uma casa.
* `Apartamento` — representa um apartamento.
* `Estudio` — representa um estúdio.

As classes específicas herdam da classe `Imovel` e possuem seus próprios métodos para cálculo do aluguel.

## Como executar o projeto

### Pré-requisito

É necessário ter o **Python 3** instalado.

Para verificar a instalação:

```bash
python3 --version
```

### Execução

1. Clone este repositório ou baixe os arquivos do projeto.
2. Abra o terminal.
3. Navegue até a pasta do projeto.
4. Execute o arquivo principal:

```bash
python3 main.py
```

5. Siga as instruções apresentadas no terminal para informar os dados do imóvel.

Ao finalizar o orçamento, o sistema exibirá os valores calculados e criará automaticamente um arquivo `.csv` com a projeção dos primeiros 12 meses.

## Exemplo de funcionamento

Exemplo de um apartamento com:

* 2 quartos;
* sem garagem;
* cliente sem crianças;
* taxa contratual parcelada em 5 vezes.

O sistema calcula:

```text
Valor Base...............: R$ 700,00
Adicionais...............: R$ 200,00
Desconto Aplicado........: R$ 45,00
Valor do Aluguel.........: R$ 855,00 / mês

Taxa Contratual..........: R$ 2.000,00
Parcelamento.............: 5x de R$ 400,00

Valor nos primeiros 5 meses: R$ 1.255,00 / mês
Valor após o término da taxa: R$ 855,00 / mês
```

Também é gerado um arquivo `.csv` contendo a projeção dos pagamentos durante 12 meses.

## Programação Orientada a Objetos

O projeto utiliza conceitos de POO para representar os diferentes tipos de imóveis.

A classe `Imovel` funciona como classe base, concentrando atributos comuns, enquanto `Casa`, `Apartamento` e `Estudio` herdam suas características e implementam suas próprias regras de cálculo.

Essa estrutura permite organizar melhor as responsabilidades do sistema e representar cada tipo de imóvel de acordo com suas regras específicas.

## Tecnologias utilizadas

* **Python 3**
* **Programação Orientada a Objetos**
* **CSV**
* **Git**
* **GitHub**

## Objetivo acadêmico

O RentSmart foi desenvolvido como parte da disciplina **Algorithmic Thinking & Introduction to Object-Oriented Programming**, com o objetivo de aplicar conceitos de pensamento algorítmico e Programação Orientada a Objetos na resolução de um problema prático de negócio.
