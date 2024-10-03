#Programadores: Fillypy Cleybson, Isaias Viana

import webbrowser

# Função para exibir os dados com o codigo do município e código do cargo 
def lista_candidato(matriz, cod_municipio, cod_cargo, indice_procurado):
    resultados = []
    for item in matriz:
        if int(item[11]) == cod_municipio and int(item[13]) == cod_cargo:
             resultados.append([item[i] for i in indice_procurado])
    if resultados:
       informs = ['Nome', 'Nome na Urna', 'Numero', 'Partido']
       for resultado in resultados:
           i = 0
           for r in resultado:
               if i < len(informs):
                   print(f"{informs[i]}: {r}")
               else:
                   print(f"Item {i + 1}: {r}")
               i += 1
           print("=-" * 20)

    else:
        print('Município não encontrado, Cargo Inválido ou Candidato não encontrado')


# Função para exibir os dados com o codigo do candidato
def candidato(matriz, cod_candidato, indice_procurado):
    resultados2 = []
    for dados_candidato in matriz:
        if int(dados_candidato[15]) == cod_candidato:
            resultados2.append([dados_candidato[i] for i in indice_procurado])
    if resultados2:
        informs = ['Nome', 'Nome na Urna', 'Numero', 'Partido']
        for resultado2 in resultados2:
            i = 0 
        for r in resultado2:
            if i < len(informs):
                print(f"{informs[i]}: {r}")
            else:
                print(f"Item {i + 1}: {r}") 
            i += 1 
        print("=-" * 20)
    else:
        print('Município não encontrado, Cargo Inválido ou Candidato não encontrado')


# Informações que deseja extrair
indice_procurado = [17, 18, 16, 26]
arq = open("consulta_cand_2024_PB.csv", "r")
conteudo = arq.read()

linhas = conteudo.strip().split('\n')
matriz = [linha.replace('"', '').split(';') for linha in linhas]

# Menu interativo
while True:

    print('=-'*39)
    print(' ')
    print('Escolha uma opção: ')
    print(' ')
    print('=-'*39)
    print(' ')
    print('1- Pesquisar com o código do município e o código do cargo. ')
    print('2- Pesquisar com o código do candidato. ')
    print('3- Abrir Página HTML ')
    print(' ')
    print('=-'*39)
    opcao = int(input('Digite: '))
    print('=-'*39)
    print('')


    if opcao == 1: 
        cod_municipio = int(input('Código do município: '))
        cod_cargo = int(input('Código do cargo: '))
        print()
        lista_candidato(matriz, cod_municipio, cod_cargo, indice_procurado)

    elif opcao == 2:
        cod_candidato = int(input('Código do candidato: '))
        print()
        candidato(matriz, cod_candidato, indice_procurado)

    elif opcao == 3:
        webbrowser.open('http://127.0.0.1:5500/pagina_info.html')
        print('Pagina HTML foi aberta')
        
    else:
        print('Município não encontrado, Cargo Inválido ou Candidato não encontrado')
    break

arq.close()






