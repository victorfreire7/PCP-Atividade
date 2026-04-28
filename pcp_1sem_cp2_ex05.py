def pode_aprovar(idade, renda, valor):
    if idade <= 18:
        return False
    if (renda * 20) < valor:
        return False
    return True


def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10


def calcular_parcela(valor, taxa, parcelas):
    pmt = valor * (taxa * (1 + taxa) ** parcelas) / ((1 + taxa) ** parcelas - 1)
    return pmt


def calcular_total(parcela, parcelas):
    return parcela * parcelas


def calcular_juros(total, valor):
    return total - valor


nome = str(input('Nome do Cliente: ')).capitalize().strip()
idade = int(input('Idade do Cliente: '))
renda = float(input('Renda Mensal: R$ '))
valor = float(input('Valor do empréstimo: R$ '))

parcelas = int(input('Número de parcelas (3 a 24): '))
while parcelas < 3 or parcelas > 24:
    parcelas = int(input('Valor inválido! Insira entre 3 e 24 parcelas: '))

if not pode_aprovar(idade, renda, valor):
    print(f'\nEmpréstimo NEGADO para {nome}.')
    if idade <= 18:
        print('Motivo: cliente deve ter mais de 18 anos.')
    if (renda * 20) < valor:
        print(f'Motivo: valor solicitado excede 20x a renda mensal (limite: R$ {renda * 20:.2f}).')
else:
    taxa = definir_taxa(parcelas)
    parcela = calcular_parcela(valor, taxa, parcelas)
    total = calcular_total(parcela, parcelas)
    juros = calcular_juros(total, valor)

    print(f'\nEmpréstimo APROVADO!')
    print(f'-----------------------------------')
    print(f'Cliente:           {nome}')
    print(f'Valor financiado:  R$ {valor:.2f}')
    print(f'Taxa de juros:     {taxa * 100:.0f}% ao mês')
    print(f'Valor da parcela:  R$ {parcela:.2f}')
    print(f'Total pago:        R$ {total:.2f}')
    print(f'Total de juros:    R$ {juros:.2f}')
    print(f'-----------------------------------')