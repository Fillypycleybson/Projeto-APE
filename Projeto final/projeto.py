#Programadores: Fillypy Cleybson, Isaias Viana


import webbrowser

def lista_candidato(matriz, cod_municipio, cod_cargo, indice_procurado):
    resultados = []
    for item in matriz:
        # Atribuindo as colunas certas para cod_municipio e cod_cargo
        if int(item[11]) == cod_municipio and int(item[13]) == cod_cargo:
            # Retorna as informações com base nos índices procurados
             resultados.append([item[i] for i in indice_procurado])
    
    if resultados:
        for resultado in resultados:
            print("\n".join(f"{i+1}: {valor}" for i, valor in enumerate(resultado)))
            print("=-" * 20)  # Linha separadora entre os resultados
    else:
        print('Município não encontrado, Cargo Inválido ou Candidato não encontrado')
    

def candidato(matriz, cod_candidato, indice_procurado):
    resultados2 = []
    for dados_candidato in matriz:
        if int(dados_candidato[16]) == cod_candidato:
            resultados2.append([dados_candidato[i] for i in indice_procurado])

    if resultados2:
        for resultado2 in resultados2:
            print("\n".join(f"{i+1}: {valor}" for i, valor in enumerate(resultado2)))
            print("=-" * 20)  # Linha separadora entre os resultados
    else:
        print('Município não encontrado, Cargo Inválido ou Candidato não encontrado')





indice_procurado = [17, 18, 16, 25]  # Informações que deseja extrair
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
    opcao = int(input(''))
    print('=-'*39)
    print('')


    if opcao == 1: 
        cod_municipio = int(input('Código do município: '))
        cod_cargo = int(input('Código do cargo: '))
        lista_candidato(matriz, cod_municipio, cod_cargo, indice_procurado)

    if opcao == 2:
        cod_candidato = int(input('Código do candidato: '))
        candidato(matriz, cod_candidato, indice_procurado)

    if opcao == 3:
        caminho_arquivo = input("Digite o caminho completo do arquivo HTML: ")
        webbrowser.open(f"file:///{caminho_arquivo}")
        
    else:
        print('Município não encontrado, Cargo Inválido ou Candidato não encontrado')
        break


arq.close()






