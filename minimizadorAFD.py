# Itera por cada linha no arquivo e armazena em uma lista
linhas = []
for linha in automato:
    linhas.append(linha)

estados_do_automato = linhas[0]
alfabeto = linhas[1]
estado_inicial = linhas[len(linhas) - 2]
estado_final = linhas[len(linhas) - 1]
transicoes = linhas[2:len(linhas) - 2]

# Inicialização da tabela de transição
tabela_transicao = {}

# Processamento da entrada
for linha in transicoes:
    origem, simbolo, destino = linha
    tabela_transicao[(origem, simbolo)] = destino

# Impressão da tabela de transição
print("AFD de entrada:")
print("---------------------")
print("| Estado | Simbolo | Destino |")
print("---------------------")
for (origem, simbolo), destino in tabela_transicao.items():
    print(f"| {origem:<6} | {simbolo:<7} | {destino:<7} |")
print("---------------------")


grupos = [[estado] for estado in estados_do_automato]
particoes_anteriores = [] # Cria lista de particoes anteriores

while particoes_anteriores != grupos:
    particoes_anteriores = grupos.copy()
    grupos = []

    for grupo in particoes_anteriores:
        if len(grupo) == 1:
            grupos.append(grupo)
            continue
        grupos_filhos = [[] for i in range(len(grupo))]
        for i, estado in enumerate(grupo):
            for simbolo in alfabeto:
                destino = tabela_transicao[(estado, simbolo)]
                index_grupo_destino = -1
                for j, grupo_filho in enumerate(grupos_filhos):
                    if tabela_transicao[(grupo_filho[0], simbolo)] == destino:
                        index_grupo_destino = j
                        break
                grupos_filhos[index_grupo_destino].append(estado) if index_grupo_destino >=0 else None
        grupos += [grupo_filho for grupo_filho in grupos_filhos if grupo_filho]

estados_equivalentes = {}
for i, grupo in enumerate(grupos):
    for estado in grupo:
        estados_equivalentes[estado] = i

tabela_transicao_minimo = {}
for (origem, simbolo), destino in tabela_transicao.items():
    origem_minimo = estados_equivalentes[origem]
    destino_minimo = estados_equivalentes[destino]
    tabela_transicao_minimo[(origem_minimo, simbolo)] = destino_minimo
        
print("\n \n \nAFD minimizado: ")
print("___________________")
print("| Estado | Simbolo | Destino |")
print("___________________")
for(origem_minimo, simbolo), destino_minimo in tabela_transicao_minimo.items():
    print(f"| {origem_minimo:<6} | {simbolo:<7} | {destino_minimo:<7} |
