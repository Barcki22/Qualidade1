def ler_nota(mensagem):
    while True:
        nota = int(input(mensagem))
        if 0 <= nota <= 3:
            return nota
        print("Informe um valor entre 0 e 3.")


def calcular_nivel(processo):
    if processo["execucao"] < 2:
        return 0
    if processo["gerenciamento"] < 2:
        return 1
    if processo["definicao"] < 2:
        return 2
    if processo["medicao"] < 2:
        return 3
    if processo["melhoria"] < 2:
        return 4
    return 5


def gerar_diagnostico(processo):
    nivel = calcular_nivel(processo)
    print("=" * 40)
    print("AVALIAÇÃO DE PROCESSO")
    print("=" * 40)
    print("Processo:", processo["nome"])
    print("Nível:", nivel)

    if processo["execucao"] < 2:
        print("- Melhorar execução do processo")
    if processo["gerenciamento"] < 2:
        print("- Melhorar planejamento e acompanhamento")
    if processo["definicao"] < 2:
        print("- Criar e padronizar o processo")
    if processo["medicao"] < 2:
        print("- Criar indicadores")
    if processo["melhoria"] < 2:
        print("- Implantar melhoria contínua")

    if "evidencias" in processo:
        print("Evidências encontradas:")
        for evidencia in processo["evidencias"]:
            print("-", evidencia)


processo = {
    "nome": "Processo de Testes",
    "execucao": 3,
    "gerenciamento": 2,
    "definicao": 1,
    "medicao": 0,
    "melhoria": 0
}

print("Processo:", processo["nome"])
print("Execução:", processo["execucao"])
print("Gerenciamento:", processo["gerenciamento"])
print("Definição:", processo["definicao"])
print("Medição:", processo["medicao"])
print("Melhoria:", processo["melhoria"])

media = (
    processo["execucao"]
    + processo["gerenciamento"]
    + processo["definicao"]
    + processo["medicao"]
    + processo["melhoria"]
) / 5
print(f"Média: {media:.2f}\n")

nivel = calcular_nivel(processo)
print("Nível de capacidade:", nivel)

gerar_diagnostico(processo)

processos = [
    {
        "nome": "Requisitos",
        "execucao": 3,
        "gerenciamento": 2,
        "definicao": 2,
        "medicao": 1,
        "melhoria": 0
    },
    {
        "nome": "Desenvolvimento",
        "execucao": 3,
        "gerenciamento": 3,
        "definicao": 3,
        "medicao": 2,
        "melhoria": 1
    },
    {
        "nome": "Testes",
        "execucao": 3,
        "gerenciamento": 1,
        "definicao": 1,
        "medicao": 0,
        "melhoria": 0
    }
]

print("\n--- AVALIANDO VÁRIOS PROCESSOS ---")
for p in processos:
    nivel = calcular_nivel(p)
    print(p["nome"], "- Nível:", nivel)

menor_nivel = 5
processo_critico = ""
for p in processos:
    nivel = calcular_nivel(p)
    if nivel < menor_nivel:
        menor_nivel = nivel
        processo_critico = p["nome"]

print("Processo prioritário para melhoria:", processo_critico)

print("\n--- ENTRADA DO USUÁRIO ---")
print("AVALIAÇÃO DO PROCESSO DE TESTES")
execucao = ler_nota("Execução (0 a 3): ")
gerenciamento = ler_nota("Gerenciamento (0 a 3): ")
definicao = ler_nota("Definição (0 a 3): ")
medicao = ler_nota("Medição (0 a 3): ")
melhoria = ler_nota("Melhoria (0 a 3): ")

processo_usuario = {
    "nome": "Testes",
    "execucao": execucao,
    "gerenciamento": gerenciamento,
    "definicao": definicao,
    "medicao": medicao,
    "melhoria": melhoria,
    "evidencias": [
        "Plano de testes",
        "Casos de teste",
        "Relatório de defeitos"
    ]
}

gerar_diagnostico(processo_usuario)