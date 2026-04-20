from time import sleep
def pode_aprovar(idade,renda,valor):
    if idade >= 18 and (renda * 20) >= valor:
        return "APROVADO"


def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05

    elif 7 <= parcelas <= 12:
        return 0.08

    elif 13 <= parcelas <= 24:
        return 0.10

def calcular_parcela(valor, taxa, parcelas):
    pmt = valor * (taxa * (1 + taxa)*parcelas) / ((1 + taxa)*parcelas - 1)
    return pmt

def calcular_total(parcela,parcelas):
    valorfinal = parcela * parcelas
    return valorfinal

nome = str(input('Nome do Cliente: ')).capitalize().strip()
sleep(0.5)
idade = int(input('Idade do Cliente: '))
sleep(0.5)
renda = float(input('Renda Mensal: '))
sleep(0.5)
valor = float(input('Valor do empréstimo: '))
sleep(0.5)
parcelas = int(input('Números de parcelas: '))
sleep(0.5)
while 24 < parcelas or parcelas <= 2:
    parcelas = int(input('Valor inválido!!! Tente novamente... [3X-24X] '))

taxa = definir_taxa(parcelas)
parcela = calcular_parcela(valor, taxa, parcelas)
total = calcular_total(parcela, parcelas)
aprovado = pode_aprovar(idade, renda, valor)
if aprovado:
    print(f'\nO nome do cliente é: {nome}')
    sleep(0.5)
    print(f'A taxa em questão é: {taxa*100:.0f}%')
    sleep(0.5)
    print(f'o valor da parcela é: R${parcela:.2f}')
    sleep(0.5)
    print(f'o valor total é: R${total:.2f}')
    sleep(0.5)
else:
    print(f'Cliente {nome} reprovado')