quant=int(input("Informe quantos números você deseja calcular a média: "))
soma = 0
iteracao = 1
while iteracao <= quant:
    # print(iteracao)
    n1=float(input(f"Digite o {iteracao}º número: "))
    soma += n1
    iteracao += 1
print(f'O resultado da sua média é: {soma/quant}')
