nome_funcionario = input("Nome do funcionário: ")
cargo = int(input("Cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): "))
salario_base = float(input("Salário base: "))
total_horas_extras = int(input("Total de horas extras: "))
total_faltas_mes = int(input("Total de faltas no mês: "))
bonus = input("Bônus? (s ou n) ")

def calcular_horas_extras(salario_base, horas):
    return (salario_base*.015) * horas
def calcular_descontos_faltas(salario_base, faltas):
    return (salario_base*.02) * faltas
def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus == 's':
        match cargo:
            case 1:
                return 1000.00
            case 2:
                return 500.00
            case 3:
                return 300.00
            case 4:
                return 100.00
    elif recebeu_bonus == 'n':
        return 0
    else:
        return 0

print(f"Salário bruto: {salario_base}")
acrescimos = calcular_horas_extras(salario_base, total_horas_extras) + calcular_bonus(cargo, bonus)
print(f"Total de acréscimos: {acrescimos}")
descontos  = calcular_descontos_faltas(salario_base, total_faltas_mes)
print(f"Total de descontos (faltas): {descontos}")
salario_final = salario_base + acrescimos - descontos
print(salario_final)