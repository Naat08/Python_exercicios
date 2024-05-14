print("Nossa empresa presta serviço á companhia de energia elétrica do estado, nós auxiliamos nos cálculos das principais grandezas da eletricidades que são Tensão, Resistência e Corrente.")
r1=str(input("Você deseja calcular a Tensão (digite U), a Resistência (digite R)ou a Corrente (digite i): "))
if (r1=="U") or (r1=="u"):
    res1=float(input("Digite o valor valor da Resistência: "))
    cor1=float(input("Digite o valor da Corrente: "))
    v1=res1*cor1
    print(f"O valor da tensão é {v1}")
elif (r1=="I") or (r1=="i"):
    ten2=float(input("Digete o valor o valor da Tensão: "))
    res2=float(input("Digite o valor da Resistência: "))
    v2=ten2/res2
    print(f"O valor da Corrente é {v2}")
elif (r1=="R") or (r1=="r"):
    ten3=float(input("Digete o valor o valor da Tensão: "))
    cor3=float(input("Digite o valor da Corrente: "))
    v3=ten3/cor3
    print(f"O valor da Corrente é {v3}")
else:
    print("Digite um valor válido!")


