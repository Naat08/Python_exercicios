def cadastro_aluno(alunos):
    nome = input("Digite o nome do aluno: ")
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    alunos[nome] = notas

def calcular_media(notas):
    media = sum(notas) / len(notas)

def resultado_notas(alunos):
    for nome, notas in alunos.items():
        media = calcular_media(notas)
        if media >= 5:
            return 'Aprovado'
        else:
            return 'Reprovado'
    r = resultado_notas(media)
    print(f"Aluno: {nome} Notas: {notas} Média: {media} Resultado: {r}")