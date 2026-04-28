def notaCheckpoint(cp1, cp2, cp3):
    if cp1 <= cp2 and cp1 <= cp3:
        menor = cp1
    elif cp2 <= cp1 and cp2 <= cp3:
        menor = cp2
    else:
        menor = cp3

    return (cp1 + cp2 + cp3) - menor

def notaSprint(sp1, sp2): # retorno a soma das duas sprint
    return sp1 + sp2;

def validator(args): # todas as validações do que foi enviado aqui
    for i in range(len(args)):
        if args[i] > 10 or args[i] < 0:
            print("----------------------------------------");
            print("Por favor, insira uma nota entre 0 e 10.");
            print("----------------------------------------");
            exit();
            break;


def notaSemestre(arr): # arr[0] = cp1    arr[1] = cp2      arr[2] = cp3     arr[3] = sp1     arr[4] = sp2     arr[5] = gs
    validator(arr); # validando se as notas estão entre 0 e 10

    arit = (notaCheckpoint(arr[0], arr[1], arr[2]) + notaSprint(arr[3], arr[4])) / 4;
    media = (arit * 0.4) + (arr[5] * 0.6);
    mediaPeso = media * 0.4;

    print("---------------------------------");
    print(f"Média do semestre: {media}");
    print(f"Média do semestre com peso: {mediaPeso:.1f}");


cp1 = float(input('Qual foi a nota do seu Checkpoint 1? '));
cp2 = float(input('Qual foi a nota do seu Checkpoint 2? '));
cp3 = float(input('Qual foi a nota do seu Checkpoint 3? '));

sp1 = float(input('Qual foi a nota da sua 1º Sprint? '));
sp2 = float(input('Qual foi a nota da sua 2º Sprint? '));

gs = float(input('Qual foi a nota da sua Global Solution? '));

notaSemestre([cp1, cp2, cp3, sp1, sp2, gs]); # envio como array, pra realizar um tratamento mais simplificado dos dados