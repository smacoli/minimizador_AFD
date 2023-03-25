import csv

# Abre o arquivo
with open('E:/Users/User/Desktop/AFD_minimizador/arquivoEntrada.txt') as arquivo:
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

    # print("Estados: ", estados_do_automato)
    # print("Alfabeto: ", alfabeto)
    # print("Estado inicial: ", estado_inicial)
    print("Estados finais: ", estados_finais)
    # print("Trasicoes: ", transicoes)
    print("Estados nao finais: ", estados_nao_finais)
    
    # # Inicialização da tabela de transição
    # tabela_transicao = {}

    # # Processamento da entrada para montar a tabela
    # for linha in transicoes:
    #     origem, simbolo, destino = linha
    #     tabela_transicao[(origem, simbolo)] = destino

    # # Impressão da tabela de transição
    # print("AFD de entrada:")
    # print("---------------------")
    # print("| Estado | Simbolo | Destino |")
    # print("---------------------")
    # for (origem, simbolo), destino in tabela_transicao.items():
    #     print(f"| {origem:<6} | {simbolo:<7} | {destino:<7} |")
    # print("---------------------")

