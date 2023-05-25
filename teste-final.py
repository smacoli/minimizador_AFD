import csv

with open('automato2.dat') as arquivo:
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
  # print("Estados finais: ", estados_finais)
  # print("Trasicoes: ", transicoes)
  # print("Estados nao finais: ", estados_nao_finais)

  # Verifica se cada estado possui transição para cada símbolo do alfabeto
  # Fase de preparação
  matriz = [[' ' for i in range(len(estados_do_automato))]
            for j in range(len(estados_do_automato))]
  for i in transicoes:
      comeca = int(i[0].split('q')[1])
      entrada = i[1]
      onde_vai = int(i[2].split('q')[1])
      if matriz[comeca][onde_vai] == ' ':
          matriz[comeca][onde_vai] = entrada
      else:
          matriz[comeca][onde_vai] = [matriz[comeca][onde_vai], entrada]

  # Análise para ver se tem mais de uma letra do alfabeto indo para uma transicao
  for i in range(len(matriz)):
      lista = False
      for j in range(len(matriz[0])):
          if type(matriz[i][j]) == list:
              lista = True
              for a in alfabeto:
                  cont1 = matriz[i].count(a)
                  cont2 = matriz[i][j].count(a)
                  cont3 = cont1 + cont2
                  if cont3 != 1:
                      print('Nao e AFD')
                      exit(0)
      if not lista:
          for a in alfabeto:
              cont1 = matriz[i].count(a)
              if cont1 != 1:
                  print('Nao e AFD!')
                  exit(0)
  print("AFD")
  # Definindo pares de estados equivalentes inicialmente
  equivalencia_finais = []
  for estado in estados_finais:
      for prox_estado in estados_finais:
          if estado != prox_estado:  # verificando se os estados são diferentes
              equivalencia_finais.append((estado, prox_estado))  # adicionando uma tupla na lista
  equivalencia = list(set(equivalencia_finais))          
  #print("finale: ", equivalencia) 
  equivalencia_nao_finais = []
  for estado in estados_nao_finais:
      for prox_estado in estados_nao_finais:
          if estado != prox_estado:
              equivalencia_nao_finais.append((estado, prox_estado))
  equivalencia_nao_final = list(set(equivalencia_nao_finais))

  # Imprimindo estados equivalentes em forma de lista
  # print("Equivalencia inicial entre estados: ")
  # for tupla in equivalencia_nao_final:
  #     print(tupla)
  # for tupla in equivalencia:
  #     print(tupla)

  # Pegando as transições na lista de transições para os estados equivalentes, e depois concatenando numa lista
  trans_equivalente_final = [t for t in transicoes if t[0] in [e[0] for e in equivalencia]]
  #print("TRANSICAO DE FINAIS: ", trans_equivalente_final) # ---------------------- OK
  trans_equivalente_nao_final = [t for t in transicoes if t[0] in [e[0] for e in equivalencia_nao_final]]
  #print("TRANSICAO DE NAO FINAIS: ", trans_equivalente_nao_final) # -------------- OK MAS PEGOU Q3 PORQUE ELE TEM QUE SAIR É NA COMPARAÇÃO
  transicoes_1_simbolo = trans_equivalente_final + trans_equivalente_nao_final
  #print("TRANSICOES DE 1 SIMBOLO: ", transicoes_1_simbolo) #-------------------------------------OK

  # Fazendo as comparações par a par pegando o estado destino de cada transição e compara com o estado destino das outras transições e com estados finais, 
  # quando uma transição leva ao estado final e a outra não leva, as tuplas são armazenadas na lista de estados não equivalentes
  equivalentes_finais_1 = []
  nao_equivalentes_finais = []
  for i in range(len(trans_equivalente_final)):
    for j in range(i+1, len(trans_equivalente_final)):
      if trans_equivalente_final[i][2] == trans_equivalente_final[j][2] and trans_equivalente_final[i][2] not in estados_finais: #ok
        equivalentes_finais_1.append(trans_equivalente_final[i])
        equivalentes_finais_1.append(trans_equivalente_final[j])
      elif trans_equivalente_final[i][2] == trans_equivalente_final[j][2] and trans_equivalente_final[i][2] in estados_finais: #ok
        equivalentes_finais_1.append(trans_equivalente_final[i])
        equivalentes_finais_1.append(trans_equivalente_final[j])
      elif trans_equivalente_final[i][2] != trans_equivalente_final[j][2] and trans_equivalente_final[i][2] not in estados_finais and trans_equivalente_final[j][2] not in estados_finais: #ok
        equivalentes_finais_1.append(trans_equivalente_final[i])
        equivalentes_finais_1.append(trans_equivalente_final[j])
      elif trans_equivalente_final[i][2] != trans_equivalente_final[j][2] and trans_equivalente_final[i][2] in estados_finais and trans_equivalente_final[j][2] in estados_finais: #ok
        equivalentes_finais_1.append(trans_equivalente_final[i])
        equivalentes_finais_1.append(trans_equivalente_final[j])
      elif trans_equivalente_final[i][2] != trans_equivalente_final[j][2] and trans_equivalente_final[i][2] in estados_finais and trans_equivalente_final[j][2] not in estados_finais: #ok
        nao_equivalentes_finais.append(trans_equivalente_final[i])
        nao_equivalentes_finais.append(trans_equivalente_final[j])
      elif trans_equivalente_final[i][2] != trans_equivalente_final[j][2] and trans_equivalente_final[i][2] not in estados_finais and trans_equivalente_final[j][2] in estados_finais: #ok
        nao_equivalentes_finais.append(trans_equivalente_final[i])
        nao_equivalentes_finais.append(trans_equivalente_final[j])

  # Removendo tuplas duplicadas
  equivalentes_1f = []
  for transicao in equivalentes_finais_1:
      if transicao not in equivalentes_1f:
          equivalentes_1f.append(transicao)
  #print("EQUIVALENTES FINAL: ", equivalentes_1f)

  equivalentes_nf1 = []
  nao_equivalentes_nf1 = []
  for i in range(len(trans_equivalente_nao_final)):
    for j in range(i+1, len(trans_equivalente_nao_final)):
      if trans_equivalente_nao_final[i][2] == trans_equivalente_nao_final[j][2] and trans_equivalente_nao_final[i][2] not in estados_finais: #ok
        equivalentes_nf1.append(trans_equivalente_nao_final[i])
        equivalentes_nf1.append(trans_equivalente_nao_final[j])
      elif trans_equivalente_nao_final[i][2] == trans_equivalente_nao_final[j][2] and trans_equivalente_nao_final[i][2] in estados_finais: #ok
        equivalentes_nf1.append(trans_equivalente_nao_final[i])
        equivalentes_nf1.append(trans_equivalente_nao_final[j])
      elif trans_equivalente_nao_final[i][2] != trans_equivalente_nao_final[j][2] and trans_equivalente_nao_final[i][2] not in estados_finais and trans_equivalente_nao_final[j][2] not in estados_finais: #ok
        equivalentes_nf1.append(trans_equivalente_nao_final[i])
        equivalentes_nf1.append(trans_equivalente_nao_final[j])
      elif trans_equivalente_nao_final[i][2] != trans_equivalente_nao_final[j][2] and trans_equivalente_nao_final[i][2] in estados_finais and trans_equivalente_nao_final[j][2] in estados_finais: #ok
        equivalentes_nf1.append(trans_equivalente_nao_final[i])
        equivalentes_nf1.append(trans_equivalente_nao_final[j])
      elif trans_equivalente_nao_final[i][2] != trans_equivalente_nao_final[j][2] and trans_equivalente_nao_final[i][2] in estados_finais and trans_equivalente_nao_final[j][2] not in estados_finais: #ok
        nao_equivalentes_nf1.append(trans_equivalente_nao_final[i])
        nao_equivalentes_nf1.append(trans_equivalente_nao_final[j])
      elif trans_equivalente_nao_final[i][2] != trans_equivalente_nao_final[j][2] and trans_equivalente_nao_final[i][2] not in estados_finais and trans_equivalente_nao_final[j][2] in estados_finais: #ok
        nao_equivalentes_nf1.append(trans_equivalente_nao_final[i])
        nao_equivalentes_nf1.append(trans_equivalente_nao_final[j])
  # Removendo tuplas duplicadas
  equivalentes_1nf = []
  for transicao in equivalentes_nf1:
    if transicao not in equivalentes_1nf:
      equivalentes_1nf.append(transicao)

  # Tratando do problema de ainda haver tuplas com transições que já deveriam ter sido excluidas nas comparações de 1 símbolo
  # Por exemplo, se a transição q3,0,q0 foi removida anteriormente por ser distinguivel, a transição q3,1,q1 era mantida
  # Logo, aqui analisaremos os primeiros simbolos de nossa lista de equivalencias resultante das primeiras comparações em busca de transições         
  primeiros = [x[0] for x in equivalentes_1f]
  frequencias = {x: primeiros.count(x) for x in set(primeiros)}
  equivalentes_1f = [x for x in equivalentes_1f if frequencias[x[0]] > 1]
  # print("EQUIVALENTES APOS COMPARACOES DE 1 SIMBOLO: ", equivalentes_1f)


  primeiros = [x[0] for x in equivalentes_1nf]
  frequencias = {x: primeiros.count(x) for x in set(primeiros)}
  equivalentes_1nf = [x for x in equivalentes_1nf if frequencias[x[0]] > 1]
  # print("EQUIVALENTES APOS COMPARACOES DE 1 SIMBOLO: ", equivalentes_1nf)

  ########################################################################################################################################################################

  # Criando a lista com 2 simbolos de entrada (00, 01, 10, 11 ou aa, ab, ba, ab)
  lista2 = equivalentes_1f
  lista_2 = []
  lista_2_simbolo = []
  for tupla in lista2:
      for simbolo in alfabeto:
        nova_tupla = [tupla[0], tupla[1] + simbolo, tupla[2]]
        lista_2.append(nova_tupla)
  for tupla in lista_2:
      lista_2_simbolo.append(tupla)

  # Corrigindo os estados destino da lista de dois simbolos
  lista_de_dois_simbolos = []
  for simbolo in lista_2_simbolo:
      for transicao in transicoes:
          if simbolo[2] == transicao[0]:
              ultimo_caractere = simbolo[1][-1]
              if len(transicao[1]) >= 2 and simbolo[1][-2] == transicao[1][-2]:
                lista_de_dois_simbolos.append([simbolo[0], simbolo[1], transicao[2]])
              elif simbolo[1][-1] == transicao[1][-1]:
                lista_de_dois_simbolos.append([simbolo[0], simbolo[1], transicao[2]])
  #print(lista_de_dois_simbolos)

  # Verificação de equivalencia para as entradas de dois símbolos, 
  estados_equivalentes = []
  estados_nao_equivalentes = []
  for i in range(len(lista_de_dois_simbolos)):
    for j in range(i+1, len(lista_de_dois_simbolos)):
      if lista_de_dois_simbolos[i][2] == lista_de_dois_simbolos[j][2] and lista_de_dois_simbolos[i][2] not in estados_finais: #ok
        estados_equivalentes.append(lista_de_dois_simbolos[i])
        estados_equivalentes.append(lista_de_dois_simbolos[j])
      elif lista_de_dois_simbolos[i][2] == lista_de_dois_simbolos[j][2] and lista_de_dois_simbolos[i][2] in estados_finais: #ok
        estados_equivalentes.append(lista_de_dois_simbolos[i])
        estados_equivalentes.append(lista_de_dois_simbolos[j])
      elif lista_de_dois_simbolos[i][2] != lista_de_dois_simbolos[j][2] and lista_de_dois_simbolos[i][2] not in estados_finais and lista_de_dois_simbolos[j][2] not in estados_finais: #ok
        estados_equivalentes.append(lista_de_dois_simbolos[i])
        estados_equivalentes.append(lista_de_dois_simbolos[j])
      elif lista_de_dois_simbolos[i][2] != lista_de_dois_simbolos[j][2] and lista_de_dois_simbolos[i][2] in estados_finais and lista_de_dois_simbolos[j][2] in estados_finais: #ok
        estados_equivalentes.append(lista_de_dois_simbolos[i])
        estados_equivalentes.append(lista_de_dois_simbolos[j])
      elif lista_de_dois_simbolos[i][2] != lista_de_dois_simbolos[j][2] and lista_de_dois_simbolos[i][2] in estados_finais and lista_de_dois_simbolos[j][2] not in estados_finais: #ok
        estados_nao_equivalentes.append(lista_de_dois_simbolos[i])
        estados_nao_equivalentes.append(lista_de_dois_simbolos[j])
      elif lista_de_dois_simbolos[i][2] != lista_de_dois_simbolos[j][2] and lista_de_dois_simbolos[i][2] not in estados_finais and lista_de_dois_simbolos[j][2] in estados_finais: #ok
        estados_nao_equivalentes.append(lista_de_dois_simbolos[i])
        estados_nao_equivalentes.append(lista_de_dois_simbolos[j])
  # print("EQUIVALENTES FINAIS: ", estados_equivalentes)
  # print("NAO EQUIVALENTES FINAIS: ", estados_nao_equivalentes)

  # # Criando a lista com 2 simbolos de entrada (00, 01, 10, 11)
  lista2 = equivalentes_1nf
  lista_2 = []
  lista_2_simbolo = []
  for tupla in lista2:
      for simbolo in alfabeto:
        nova_tupla = [tupla[0], tupla[1] + simbolo, tupla[2]]
        lista_2.append(nova_tupla)
  for tupla in lista_2:
      lista_2_simbolo.append(tupla)

  # Corrigindo os estados destino da lista de dois simbolos
  lista_de_dois_simbolos = []
  for simbolo in lista_2_simbolo:
      for transicao in transicoes:
          if simbolo[2] == transicao[0]:
              ultimo_caractere = simbolo[1][-1]
              if len(transicao[1]) >= 2 and simbolo[1][-2] == transicao[1][-2]:
                lista_de_dois_simbolos.append([simbolo[0], simbolo[1], transicao[2]])
              elif simbolo[1][-1] == transicao[1][-1]:
                lista_de_dois_simbolos.append([simbolo[0], simbolo[1], transicao[2]])
  # print(lista_de_dois_simbolos)

  # Verificação de equivalencia para as entradas de dois símbolos, 
  estados_equivalentes2 = []
  estados_nao_equivalentes = []
  for i in range(len(lista_de_dois_simbolos)):
    for j in range(i+1, len(lista_de_dois_simbolos)):
      if lista_de_dois_simbolos[i][2] == lista_de_dois_simbolos[j][2] and lista_de_dois_simbolos[i][2] not in estados_finais: #ok
        estados_equivalentes2.append(lista_de_dois_simbolos[i])
        estados_equivalentes2.append(lista_de_dois_simbolos[j])
      elif lista_de_dois_simbolos[i][2] == lista_de_dois_simbolos[j][2] and lista_de_dois_simbolos[i][2] in estados_finais: #ok
        estados_equivalentes2.append(lista_de_dois_simbolos[i])
        estados_equivalentes2.append(lista_de_dois_simbolos[j])
      elif lista_de_dois_simbolos[i][2] != lista_de_dois_simbolos[j][2] and lista_de_dois_simbolos[i][2] not in estados_finais and lista_de_dois_simbolos[j][2] not in estados_finais: #ok
        estados_equivalentes2.append(lista_de_dois_simbolos[i])
        estados_equivalentes2.append(lista_de_dois_simbolos[j])
      elif lista_de_dois_simbolos[i][2] != lista_de_dois_simbolos[j][2] and lista_de_dois_simbolos[i][2] in estados_finais and lista_de_dois_simbolos[j][2] in estados_finais: #ok
        estados_equivalentes2.append(lista_de_dois_simbolos[i])
        estados_equivalentes2.append(lista_de_dois_simbolos[j])
      elif lista_de_dois_simbolos[i][2] != lista_de_dois_simbolos[j][2] and lista_de_dois_simbolos[i][2] in estados_finais and lista_de_dois_simbolos[j][2] not in estados_finais: #ok
        estados_nao_equivalentes.append(lista_de_dois_simbolos[i])
        estados_nao_equivalentes.append(lista_de_dois_simbolos[j])
      elif lista_de_dois_simbolos[i][2] != lista_de_dois_simbolos[j][2] and lista_de_dois_simbolos[i][2] not in estados_finais and lista_de_dois_simbolos[j][2] in estados_finais: #ok
        estados_nao_equivalentes.append(lista_de_dois_simbolos[i])
        estados_nao_equivalentes.append(lista_de_dois_simbolos[j])
  # print("EQUIVALENTES NAO FINAIS: ", estados_equivalentes2)
  # print("NAO EQUIVALENTES NAO FINAIS: ", estados_nao_equivalentes)

  # Remove tuplas duplicadas
  unique_tuplas = set(tuple(i) for i in estados_equivalentes2)
  equivalentes = [list(i) for i in unique_tuplas]
  unique_tuplas = set(tuple(i) for i in estados_equivalentes)
  equivalentes2 = [list(i) for i in unique_tuplas]

  #estados_equivalentes = equivalentes + equivalentes2
  #print(estados_equivalentes)

  # for tupla in equivalentes:
  #   print(tupla)
  # for tupla in equivalentes2:
  #   print(tupla)

  # Tratando do problema de ainda haver tuplas com transições que já deveriam ter sido excluidas nas comparações de 2 símbolos
  # Por exemplo, se a transição q3,0,q0 foi removida anteriormente por ser distinguivel, a transição q3,1,q1 era mantida 
  primeiros_estados = {}
  for tupla in equivalentes2:
      estado = tupla[0]
      if estado not in primeiros_estados:
          primeiros_estados[estado] = 1
      else:
          primeiros_estados[estado] += 1

  # Cria uma lista com as tuplas que devem ser mantidas
  ESTADOS_FINAIS_EQUIVALENTES = []
  for tupla in equivalentes2:
      if primeiros_estados[tupla[0]] == 4:
          ESTADOS_FINAIS_EQUIVALENTES.append(tupla)

  print("Equivalentes finais: ", ESTADOS_FINAIS_EQUIVALENTES)


  ########################################################################################################################################################

  # Tratando do problema de ainda haver tuplas com transições que já deveriam ter sido excluidas nas comparações de 2 símbolos
  # Por exemplo, se a transição q3,0,q0 foi removida anteriormente por ser distinguivel, a transição q3,1,q1 era mantida 
  primeiros_estados = {}
  for tupla in equivalentes:
      estado = tupla[0]
      if estado not in primeiros_estados:
          primeiros_estados[estado] = 1
      else:
          primeiros_estados[estado] += 1

  # Cria uma lista com as tuplas que devem ser mantidas
  NAO_FINAIS_EQUIVALENTES = []
  for tupla in equivalentes:
      if primeiros_estados[tupla[0]] == 4:
          NAO_FINAIS_EQUIVALENTES.append(tupla)
  print("Equivalentes nao finais: ", NAO_FINAIS_EQUIVALENTES)


