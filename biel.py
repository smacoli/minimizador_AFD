# realiza leitura do arquivo
with open('arquivoEntrada.txt', 'r') as arquivo:

    linhas = arquivo.readlines()

alfabeto = linhas[1].strip().split(',')
estados = linhas[0].strip().split(',')
estado_inicial = linhas[len(linhas) - 2].strip()
estado_finais_ast = linhas[len(linhas) - 1]

transicoes = {}
for estado in estados:
    transicoes[estado] = {}

for linha in linhas[2:len(linhas) - 2]:
    origem, simbolo, destino = linha.strip().split(',')
    if origem not in transicoes:
        transicoes[origem] = {}
    transicoes[origem][simbolo] = destino

estados_nao_finais = []
for estado in estados:
    if estado not in estado_finais_ast:
        estados_nao_finais.append(estado)


automato = {
    'estados': estados,
    'alfabeto': alfabeto,
    'transicoes': transicoes,
    'estado_incial': estado_inicial,
    'estados_finais': estado_finais_ast,
    'estados_nao_finais': estados_nao_finais
}
