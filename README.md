## Grupo:
- [Victor Hugo Freire](https://github.com/victorfreire7)
- [Lucas Melchior](https://github.com/itrolucas)
- [Gustavo Rocha](https://github.com/gustavo-rocha-batista)
- [Davi R. Silva](https://github.com/NyixTAA)

---

## Exercicío 1:

```
    Faça um programa que recebe:
    • o código do estado de origem da carga de um caminhão, supondo que é um
    número inteiro de 1 a 5
    • o peso da carga do caminhão em toneladas
    • o código da carga, supondo que é um número inteiro de 10 e 40
    Seu programa deve calcular:
    • o peso da carga do caminhão convertido em quilos
    • o preço da carga do caminhão
    • valor do imposto que é cobrado com base no preço da carga e do estado de
    origem
    • o valor total transportado pelo caminhão (carga + impostos)
```


## Exercicío 2:

```
    Faça um programa que leia 3 valores que representam os lados de um triângulo A,
    B e C e ordene-os em ordem decrescente, de modo que o lado A representa o
    maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados
    formam, com base nos seguintes casos:
    Se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO;
    Se A² = B² + C², apresente a mensagem: TRIANGULO RETANGULO;
    Se A² > B² + C², apresente a mensagem: TRIANGULO OBTUSANGULO;
    Se A² < B² + C², apresente a mensagem: TRIANGULO ACUTANGULO;
    Se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO;
    Se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO
    ISOSCELES;
```

## Exercicío 3:

```
    Uma instituição de ensino avalia seus alunos ao longo do semestre com base em diferentes atividades.
    Requisitos:

    1. O programa deve solicitar:
        o Nota do Checkpoint 1 (cp1)
        o Nota do Checkpoint 2 (cp2)
        o Nota do Checkpoint 3 (cp3)
        o Nota da Sprint 1 (sp1)
        o Nota da Sprint 2 (sp2)
        o Nota da Global Solution (gs)

    2. O programa deve solicitar:
        o Todas as notas variam de 0 a 10 e podem ser decimais
        o O sistema deve identificar a menor nota entre os três checkpoints
        o A menor nota deve ser desconsiderada no cálculo

    3. A composição da média segue os seguintes pesos:
        o 40% → média dos 2 maiores Checkpoints + 2 Sprints
        o 60% → nota da Global Solution
        o 40% → média do 1º semestre

    4. Cálculo da média:

        o A média do semestre deve ser calculada utilizando:
        ▪ As duas maiores notas dos checkpoints
        ▪ As duas notas das sprints
        ▪ A nota da Global Solution
        o Fórmula:
        o 𝑚𝑒𝑑𝑖𝑎 = ( 𝑐𝑝1+𝑐𝑝2+𝑐𝑝3−𝑚𝑒𝑛𝑜𝑟+𝑠𝑝1+𝑠𝑝2 / 4 ) ⋅ 0.4 + 𝑔𝑠 ⋅ 0.6
        o Média com peso: 𝑚𝑒𝑑𝑖𝑎𝑃𝑒𝑠𝑜 = 𝑚𝑒𝑑𝑖𝑎 ⋅ 0.4

    5. O sistema deve mostrar:
        ▪ Média do semestre (sem peso)
        ▪ Média do semestre com peso

    6. Regras de implementação:
        o Utilizar estruturas condicionais
        o Não utilizar funções prontas como min()
        o Trabalhar com valores decimais
        o Implementar manualmente a lógica para encontrar a menor nota

    7. Dica:
        o Primeiro encontre a menor nota entre os checkpoints
        o Depois aplique a fórmula removendo essa nota
        o Por fim, calcule as médias e exiba com 1 casa decimal
```

## Exercicío 4:

```
    Você foi contratado para criar um sistema de RH que calcula o salário final de um
    funcionário com base em diversos fatores: cargo, horas extras, faltas, bônus e
    descontos.
    Requisitos:

    1. O programa deve solicitar:
        o Nome do funcionário
        o Cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário)
        o Salário base (float)
        o Total de horas extras trabalhadas
        o Total de faltas no mês
        o Se recebeu bônus por desempenho (s ou n)

    2. Regras de cálculo:
        o Valor da hora extra:
        ▪ 1.5% do salário base por hora extra
        o Desconto por falta:
        ▪ 2% do salário base por falta
        o Bônus (se aplicável):
        ▪ Gerente: R$ 1000
        ▪ Analista: R$ 500
        ▪ Assistente: R$ 300
        ▪ Estagiário: R$ 100

    3. O sistema deve:
        o Calcular e mostrar:
        ▪ Salário bruto
        ▪ Total de acréscimos (horas extras + bônus)
        ▪ Total de descontos (faltas)
        ▪ Salário final

    Regras de Implementação:
        • Crie funções como:
        o def calcular_horas_extras(salario_base, horas):
        o def calcular_descontos_faltas(salario_base, faltas):
        o def calcular_bonus(cargo, recebeu_bonus):
```


## Exercicío 5:

```
    Você foi contratado para desenvolver um sistema simples de um banco que
    analisa e calcula um financiamento com parcelas fixas.
    Requisitos:

    1. O programa deve solicitar:
        o Nome do cliente
        o Idade
        o Renda mensal
        o Valor desejado do empréstimo
        o Número de parcelas (3 até 24)

    2. Regras para aprovação:
        o O cliente só será aprovado se:
        ▪ Ter mais de 18 anos
        ▪ O valor do financiamento for de no máximo 20 vezes a renda
        mensal

    3. Taxa de juros:
        o até 6 parcelas → 5% ao mês
        o de 7 até 12 parcelas → 8% ao mês
        o de 13 até 24 parcelas → 10% ao mês

    4. Cálculo do financiamento (parcelas fixas):
        o Para calcular o valor da parcela, utilize a fórmula:
        ▪ 𝑃𝑀𝑇 = 𝑃𝑉 ⋅
        𝑖(1+𝑖)
        𝑛
        (1+𝑖)𝑛−1
        ▪ PMT → valor da parcela (PMT significa Payment/Pagamento)
        ▪ PV → valor financiado (PV significa Present Value, valor inicial
        da dívida)
        ▪ i → taxa de juros (em decimal de 0 até 1)
        ▪ n → número de parcelas

    5. O sistema deve:
        o Informar se o empréstimo foi aprovado ou negado
        o Se aprovado:
        ▪ Nome do cliente
        ▪ Valor financiado
        ▪ Taxa de juros aplicada
        ▪ Valor da parcela
        ▪ Valor total pago
        ▪ Total de juros pagos

    6. Cálculos adicionais:
        o Total pago:
        ▪ 𝑡𝑜𝑡𝑎𝑙 = 𝑃𝑀𝑇 ⋅ 𝑛
        o Juros pagos:
        ▪ 𝑗𝑢𝑟𝑜𝑠 = 𝑡𝑜𝑡𝑎𝑙 − 𝑃𝑉

    Regras de Implementação:
        • Crie funções como:
            o def pode_aprovar(idade, renda, valor):
            o def definir_taxa(parcelas):
            o def calcular_parcela(valor, taxa, parcelas):
            o def calcular_total(parcela, parcelas):
            o def calcular_juros(total, valor):
```
