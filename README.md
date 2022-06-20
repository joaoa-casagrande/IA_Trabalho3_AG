# IA_Trabalho3_AG
Trabalho feito para a disciplina de Inteligência Artificial do semestre 2022/1

## Instalação de libs necessárias
O programa utiliza de algumas bibliotecas que não são nativas do Python 3, pra isso temos que instalá-las rodando o comando:

`
pip3 install -r requirements.txt
`

*É possível que você precise de permissões elevadas para instalar, fique atento a isso*




## Uso
Com as bibliotecas instaladas, rodamos o PSO.py

`
    python -m AG
`

O programa, primeiramente, apagar os resultados anteriores da pasta *"output"* caso haja.
Em seguida, irá gerar novos resultados utilizando como parâmetros:
- Individuos com 16 bits
- Populacao com 10 indivíduos
- Normalização dos resultados entre -20 e 20
- Número de execuções igual a 10
- Execuções de 10 e 20 gerações




Após um certo tempo, os resultados aparecerão na pasta *output*. 

## Resultados
Serão vários arquivos CSV no seguinte formato:

`
{Nº de execuções}p_{QTD de gerações}i_{Nº da execução}exec.csv
`

Exemplo: 10i_10g_5exec.csv, ou seja, é a *quinta* execução do programa para *10* execuções e *10* gerações.
Cada linha contendo os valores do melhor indivíduo daquela execução:

| <!-- -->    | <!-- -->    | <!-- -->    | <!-- -->    | <!-- -->    |
|---|---|---|---|---|
| 1  | Bits = 0010101110101010 | X = 11178 | X_normalizado = -13.177386129549095 | Fitness = -8.793146835227938  |
| 2  | Bits = 0010101110110100 | X = 11188 | X_normalizado = -13.171282520790417 | Fitness = -8.834067397463247  |
| 3  | Bits = 0010101110110100 | X = 11188 | X_normalizado = -13.171282520790417 | Fitness = -8.834067397463247  |
| 4  | Bits = 0010101110110100 | X = 11188 | X_normalizado = -13.171282520790417 | Fitness = -8.834067397463247  |
| 5  | Bits = 0000000111101011 | X = 491   | X_normalizado = -19.700312809948883 | Fitness = -10.990668404167238 |
| 6  | Bits = 0000000111101011 | X = 491   | X_normalizado = -19.700312809948883 | Fitness = -10.990668404167238 |
| 7  | Bits = 0000000111101011 | X = 491   | X_normalizado = -19.700312809948883 | Fitness = -10.990668404167238 |
| 8  | Bits = 0000000111101011 | X = 491   | X_normalizado = -19.700312809948883 | Fitness = -10.990668404167238 |
| 9  | Bits = 0000000111101011 | X = 491   | X_normalizado = -19.700312809948883 | Fitness = -10.990668404167238 |
| 10 | Bits = 0000000111101011 | X = 491   | X_normalizado = -19.700312809948883 | Fitness = -10.990668404167238 |


O programa também irá gerar gráficos para cada quantidade de geração:
![10g](https://user-images.githubusercontent.com/71766992/174679498-1810fe10-8132-4a6e-beac-30eaea65ae08.png)
![20g](https://user-images.githubusercontent.com/71766992/174679506-30f6de1a-c1e6-4f11-9c8b-4f5dbcc1004d.png)

Em azul, o melhor valor de X normalizado encontrado.
