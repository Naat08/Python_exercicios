nome=str(input("Digite seu nome: "))
s = 123456
iteracao = 3
while iteracao > 0:
    test=int(input("Digite sua senha: "))
    if test == s:
        print(f"Olá {nome}. Seja bem-vindo ao nosso banco!")
        break
    else:
        iteracao-=1
        if iteracao == 0:
            print("Tentativas de senhas esgotadas. Programa encerrado!")
            break
        print(f"Você agora só tem mais {iteracao} tentativas!")        