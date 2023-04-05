import csv

# Abre o arquivo
with open('arquivoEntradaAFD.txt') as arquivo:
    # Cria um objeto para ler o arquivo como um arquivo CSV
    automato = csv.reader(arquivo, delimiter=',')

    # Itera por cada linha no arquivo e armazena em uma lista
    linhas = []
    for linha in automato:
        linhas.append(linha)

    estados_do_automato = linhas[0]
    alfabeto = linhas[1]
    estado_inicial = linhas[len(linhas) - 2]
    estados_finais_ast = linhas[len(linhas) - 1]
    transicoes = linhas[2:len(linhas) - 2]

    # Remove * da lista de estados finais
    estados_finais = []
    for e in estados_finais_ast:
        novo_estado = e.replace('*', '')
        estados_finais.append(novo_estado)

    estados_nao_finais = []
    for estado in estados_do_automato:
        if estado not in estados_finais:
            estados_nao_finais.append(estado)

    print("Estados: ", estados_do_automato)
    print("Alfabeto: ", alfabeto)
    print("Estado inicial: ", estado_inicial)
    print("Estados finais: ", estados_finais)
    print("Trasicoes: ", transicoes)
    print("Estados nao finais: ", estados_nao_finais)

    # # Inicialização da tabela de transição
    tabela_transicao = {}

    # # Processamento da entrada para montar a tabela
    for linha in transicoes:
        origem, simbolo, destino = linha
        tabela_transicao[(origem, simbolo)] = destino

    # # Impressão da tabela de transição
    # print("AFD de entrada:")
    # print("---------------------")
    # print("| Estado | Simbolo | Destino |")
    # print("---------------------")
    # for (origem, simbolo), destino in tabela_transicao.items():
    #     print(f"| {origem:<6} | {simbolo:<7} | {destino:<7} |")
    # print("---------------------")

# Função que verifica se um autômato é um AFD
def verifica_afd(estados_do_automato, alfabeto, transicoes, estado_inicial, estados_finais):
    # Verifica se cada estado possui transição para cada símbolo do alfabeto
    for estado in estados_do_automato:
        for simbolo in alfabeto:
            if (estado, simbolo) not in transicoes:
                return False

    # Verifica se não existem transições vazias (sem símbolo do alfabeto)
    for origem, simbolo in transicoes.keys():
        if simbolo == "":
            return False

    # Verifica se há apenas um estado inicial
    if len(estado_inicial) != 1:
        return False

    # Verifica se todos os estados_do_automato finais são distintos
    if len(estados_finais) != len(set(estados_finais)):
        return False

    # Verifica se cada estado possui apenas uma transição para cada símbolo do alfabeto
    for estado in estados_do_automato:
        transicoes_estado = [simbolo for origem,
                            simbolo in transicoes.keys() if origem == estado]
        if len(transicoes_estado) != len(set(transicoes_estado)):
            return False

    # Se todas as verificações passaram, o autômato é um AFD
    return True


if verifica_afd(estados_do_automato, alfabeto, transicoes, estado_inicial, estados_finais):
    print("O automato não eh um AFD")
else:
    print("O automato eh um AFD")
    

