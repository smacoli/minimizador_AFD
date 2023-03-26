with open('arquivoEntrada.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

alfabeto = linhas[1].strip().split(',')
estados = linhas[0].strip().split(',')
estado_inicial = linhas[len(linhas) - 2]
estado_finais_ast = linhas[len(linhas) - 1]

transicoes = {}
for estado in estados:
    transicoes[estado] = {}

for linha in linhas[2:len(linhas) - 2]:
    origem, simbolo, destino = linha.strip().split(',')
    if origem not in transicoes:
        transicoes[origem] = {}
    transicoes[origem][simbolo] = destino

automato = {
    'estados': estados,
    'alfabeto': alfabeto,
    'transicoes': transicoes,
    'estado_incial': estado_inicial,
    'estados_finais': estado_finais_ast
}

print(automato)
