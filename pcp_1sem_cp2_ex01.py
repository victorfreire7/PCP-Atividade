cod_origem = int(input('Insira o código de estado de origem do caminhão (1-5): '))
peso = float(input('Insira o peso do caminhão em toneladas: '))
cod_carga = int(input('Insira o código da carga (10-40): '))

if 10 <= cod_carga <= 20:
    preco = 100.0

elif 21 <= cod_carga <= 30:
    preco = 250.0

elif 31 <= cod_carga <= 40:
    preco = 340.0

if cod_origem == 1:
    imposto = preco * 0.35

elif cod_origem == 2:
    imposto = preco * 0.25

elif cod_origem == 3:
    imposto = preco * 0.15

elif cod_origem == 4:
    imposto = preco * 0.05

elif cod_origem == 5:
    imposto = 0

valor_total = preco + imposto
print(f'O peso do caminhão em quilogramas é de: {peso * 1000} KG\n O preço da carga é de: R$ {preco}\n O valor do imposto é de: R$ {imposto}\n E o valor total é de: R$ {valor_total}')