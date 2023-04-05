import csv

# Abre o arquivo
with open('arquivoEntradaAFD.txt') as arquivo:
    # Cria um objeto para ler o arquivo como um arquivo CSV
    automato = csv.reader(arquivo, delimiter=',')

    def minimizar_automato(automato):
    # Itera por cada linha no automato e armazena em uma lista
        linhas = []
        for linha in automato:
            linhas.append(linha)

        estados_do_automato = linhas[0].split(",")
        alfabeto = linhas[1].split(",")
        estado_inicial = linhas[len(linhas) - 2]
        estados_finais_ast = linhas[len(linhas) - 1].split(",")
        transicoes = linhas[2:len(linhas) - 2]

        # Remove * da lista de estados finais
        estados_finais = [e.replace('*', '') for e in estados_finais_ast]

        estados_nao_finais = [estado for estado in estados_do_automato if estado not in estados_finais]

        print("Estados: ", estados_do_automato)
        print("Alfabeto: ", alfabeto)
        print("Estado inicial: ", estado_inicial)
        print("Estados finais: ", estados_finais)
        print("Transições: ", transicoes)
        print("Estados não finais: ", estados_nao_finais)

        # Minimização do autômato
        estados_equivalentes = [estados_finais, estados_nao_finais]
        novos_estados_equivalentes = []
        while estados_equivalentes != novos_estados_equivalentes:
            estados_equivalentes = novos_estados_equivalentes
            novos_estados_equivalentes = []
            for estados in estados_equivalentes:
                for simbolo in alfabeto:
                    proximos_estados = []
                    for estado in estados:
                        for transicao in transicoes:
                            origem, entrada, destino = transicao.split(",")
                            if origem == estado and entrada == simbolo:
                                proximos_estados.append(destino)
                    if proximos_estados:
                        estados_equivalentes = [estados for estados in estados_equivalentes if estados not in novos_estados_equivalentes]
                        novos_estados_equivalentes.append(proximos_estados)
                        for estado in estados:
                            if estado not in proximos_estados:
                                novos_estados_equivalentes[-1].append(estado)

        # Cria lista de estados minimizados
        estados_minimizados = []
        for estados_equivalentes in novos_estados_equivalentes:
            estados_minimizados.append(",".join(sorted(estados_equivalentes)))
        
            return estados_minimizados

# # Exemplo de uso da função
# automato = "q0,q1,q2,q3,q4,q5\n0,1\nq0,0,q0\nq0,1,q1\nq1,0,q2\nq1,1,q3\nq2,0,q4\nq2,1,q5\nq3,0,q0\nq3,1,q1\nq4,0,q2\nq4,1,q3\nq5,0,q4\nq5,1,q5\n>q0\n*q0"
estados_minimizados = minimizar_automato(automato)
print("Estados minimizados: ", estados_minimizados)


