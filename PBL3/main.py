"""
/*******************************************************************************
Autor: Washington Luis Ferreira de Oliveira Júnior
Componente Curricular: MI - ALGORITMOS
Concluido em: 03/06/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/
"""
import os
from datetime import date

#Função insertSort adaptada do algoritmo apresentado pela professora Claudia na disciplina Algortimo I
def insertSort(listaClientes,indice):
    #indice = 1 para lista de clientes. Organiza em ordem alfabetica
    #indice = 5 para lista de manutenções. Organiza pela menor data
    for i in range(1, len(listaClientes)):
        aux = listaClientes[i]
        j = i - 1
        while j >=0 and aux[indice] < listaClientes[j][indice]:
            listaClientes[j+1] = listaClientes[j]
            j -= 1
        listaClientes[j+1] = aux

def somaMeses(data, meses):#Modulo para somar os meses nas datas
    resto = meses - int(meses/12)*12
    if(int(meses/12) >= 1):
        data = date(data.year + (meses//12), data.month, data.day)
    if (data.month + resto >= 13):
        resto = data.month + resto - 13
        data = date(data.year + 1, 1, data.day)
    if (resto>=1): 
        data = date(data.year, data.month + resto, data.day)
    return data.isoformat()

def geraID(path):#OK
    with open(path, 'a+') as arquivo:
        arquivo.seek(0)
        linhas = arquivo.readlines()
    if len(linhas)>0:
        last = linhas[len(linhas)-1] #Id do ultimo item da lista
        last = last.split('|')
        return int(last[0]) + 1
    else:
        return 0

def clear():#Limpar tela
    if(os.name == 'posix'):
        os.system('clear')
    else:
       os.system('cls')

###########      CRUD
def altern(path,item):
    elementos = []
    encontrou = False
    posicao = 0
    with open(path, 'r') as arquivo:
        for linha in arquivo:
            posicao = posicao + 1
            auxiliar = linha.split('|')
            auxiliar[len(auxiliar)-1]= auxiliar[len(auxiliar)-1].replace('\n','')#retira o caracter '\n', presente no fim de cada linha, para evitar erros
            if (auxiliar[0] == str(item[0])):
                encontrou = True
                for i in range(1, len(item)):
                    if (bool(item[i]) == True):
                        auxiliar[i] = str(item[i])
            elementos.append(auxiliar)
    if encontrou:
        with open(path, 'w') as arquivo:
            for j in range(0,len(elementos)):
                linha = '\n'
                if j == 0:
                    linha = ''
                for i in range(0, len(elementos[j])-1):
                    linha = linha+elementos[j][i]+'|'
                linha = linha+elementos[j][len(elementos[j])-1]
                arquivo.write(linha)
    return encontrou

def create(path,item):
    with open(path, 'a+') as arquivo:
        arquivo.seek(0)
        teste = arquivo.readline()#ler, apenas, a primeira linha
        linha = '\n'
        if teste == '\n' or teste == '':
            linha = ''
        for i in range(0, len(item)-1):
            linha = linha+str(item[i])+'|'
        linha = linha+str(item[len(item)-1])
        arquivo.write(linha)

def read(path, posicao, identificador='None'):
    #posicao = 0 busca na primeira posicao
    #posicao = 1 busca na segunda posicao
    if (identificador == 'None'):#BUSCA AMPLA
        with open(path, 'a+') as arquivo:
            arquivo.seek(0)
            itens = arquivo.readlines()
        if len(itens) == 0:
            return False
        else:
            for i in range(len(itens)):
                itens[i] = itens[i].split('|')#Para retornar lista 2D
                itens[i][len(itens[i])-1] = itens[i][len(itens[i])-1].replace('\n','')#Para correção do ultimo elemento para exibição
            return itens
    else:#BUSCA RESTRITA
        encontrou = False
        with open(path, 'a+') as arquivo:
            arquivo.seek(0)
            for linha in arquivo:
                item = linha.split('|')
                if (item[posicao] == identificador):
                    encontrou = True
                    break
        if encontrou:
            return [item]#Para poder usar o foreach
        else:
            return False

def delete(path, identificador):
    item = []
    encontrou = False
    with open(path, 'a+') as arquivo:
        arquivo.seek(0)
        for linha in arquivo:
            auxiliar = linha.split('|')
            if (auxiliar[0] == identificador):
                encontrou = auxiliar
            else:
                item.append(linha)
    if encontrou:
        with open(path, 'w') as arquivo:
            for i in range(len(item)-1):
                arquivo.write(item[i])
            arquivo.write(item[len(item)-1].replace('\n',''))
    return encontrou
###########     FIM CRUD

###############   TELAS MENU ###
def menu_principal():
    opcao = 0
    while opcao!=4:
        opcao = 0
        clear()        
        print('{:^80}'.format('MENU'))
        print('[1] para Clientes')
        print('[2] para Manutenções')
        print('[3] para Balanço')
        print('[4] para Sair')
        try:
            opcao = int(input('Digite sua opção: '))
            verifica_menu_principal(opcao)
        except:
            pass
        
def menu_clientes():
    opcao = 0
    while opcao!=5:
        opcao = 0
        clear()        
        print('{:^80}'.format('MENU CLIENTES'))
        print('[1] para cadastrar Clientes')
        print('[2] para listar Clientes')
        print('[3] para excluir Clientes')
        print('[4] para alterar Clientes')
        print('[5] para retornar')
        try:
            opcao = int(input('Digite sua opção: '))
            verifica_menu_clientes(opcao)
        except:
            pass
               
def menu_manutencao():
    opcao = 0
    while opcao!=7:
        opcao = 0
        clear()
        print('{:^80}'.format('MENU MANUTENÇÃO'))
        print('[1] para agendar Manutenção')
        print('[2] para editar Manutenção')
        print('[3] para excluir Manutenção')
        print('[4] para realizar Manutenção')
        print('[5] para listar Manutenções')
        print('[6] para imprimir Manutenções')
        print('[7] para retornar')
        try:
            opcao = int(input('Digite sua opção: '))
            verifica_menu_manutencao(opcao)
        except:
            pass
        
###############  FIM TELAS MENU ###

###############   VERIFICAÇÃO MENUS ###
def verifica_menu_clientes(opcao):
    if opcao == 1:
        cadastrarCliente()
    elif opcao ==2:
        listarClientes()
    elif opcao == 3:
        excluirCliente()
    elif opcao == 4:
        editarCliente()
    
def verifica_menu_principal(opcao):
    if opcao == 1:
        menu_clientes()
    elif opcao == 2:
        menu_manutencao()
    elif opcao == 3:
        balanco()

def verifica_menu_manutencao(opcao):
    if opcao == 1:
        agendarManutencao()
    elif opcao == 2:
        editarManutencao()
    elif opcao == 3:
        excluirManutencao()
    elif opcao == 4:
        realizarManutencao()
    elif opcao == 5:
        listarManutencao()
    elif opcao == 6:
        imprimirManutencao()
###############  FIM MENUS ###

###############  CLIENTES ###
def cadastrarCliente():
    cliente = []
    
    while True:
        nome = input("Digite o nome do cliente: ").replace('|','/').title()#replace utilizado para evitar erros durante as leituras dos arquivos
        if len(nome) > 1:#Para não receber valores vazios
            break
        print('Insira um nome válido')
    
    while True:
        endereco = input("Digite o endereço do cliente: ").replace('|','/')#replace utilizado para evitar erros durante as leituras dos arquivos
        if len(endereco) > 5:#Para não receber valores vazios
            break
        print('Insira um endereço válido')
    
    while True:
        try:
            telefone = input('Digite o novo telefone. Ex. 75 95522 8877: ').replace('|','/').replace(' ','')
            if len(telefone) == 11 or len(telefone) == 10:#Para telefone celular ou telefone fixo
                int(telefone)
                break
            else:
                print('Insira um telefone valido')
        except:
            pass
    
    cliente.append(geraID('clientes/listaClientes.txt'))
    cliente.append(nome)
    cliente.append(endereco)
    cliente.append(telefone)
    create('clientes/listaClientes.txt',cliente)
    print('Cliente cadastrado com sucesso')
    input('Pressione Enter para retornar ao menu...')

def editarCliente():
    print('Caso não deseje alterar alguma informação, basta pressionar Enter.')
    print('Certifique-se que não digitou nada antes de pressionar Enter.')
    cliente = []
    while True:
        try:
            IDcliente = int(input("Digite o ID do cliente que deseja alterar os dados: "))
            if IDcliente >= 0:
                break
        except:
            print('O ID deve ser um numero inteiro e positivo')
            pass
    nome = input('Digite o nome que será salvo: ').replace('|','/').title()
    endereco = input('Digite o novo endereço: ').replace('|','/')
    while True:
        try:
            telefone = input('Digite o novo telefone. Ex. 75 95522 8877: ').replace('|','/').replace(' ','')
            if len(telefone) == 11 or len(telefone) == 10:
                telefone = int(telefone)
                break
            elif bool(telefone) == False:
                break
        except:
            pass
    cliente.append(IDcliente)
    cliente.append(nome)
    cliente.append(endereco)
    cliente.append(telefone)
    encontrou = altern('clientes/listaClientes.txt',cliente)
    if(encontrou == False):
        print('Não há cliente com esse ID no banco de dados')
    else:
        print('Alteração efetuada')
    input('Pressione Enter para retornar ao menu...')

def excluirCliente():
    clienteManuten = False
    while True:
        try:
            IDcliente = int(input("Digite o ID do cliente: "))
            break
        except:
            pass
    clienteManuten = read('manutencoes/agendada/ManutencoesAgendadas.txt',1,str(IDcliente))

    if clienteManuten:
        print('Não é possivel deletar este cliente')
    else:
        encontrou = delete('clientes/listaClientes.txt', str(IDcliente))
        if encontrou:
            print('Deletado com sucesso!')
        else:
            print('O cliente não foi encontrado')
    input('Pressione Enter para retornar ao menu...')

def listarClientes():
    identificador = 'None'
    resposta = 'N'
    while resposta!='A' and resposta!='R':
        clear()
        print("[A] para fazer uma busca ampla")
        print("[R] para uma busca restrita")
        resposta = input('Digite sua opção: ').upper()
    if resposta == 'R':
        while True:
            try:
                identificador = int(input("Digite o identificador do cliente: "))
                break
            except:
                pass
    clientes = read('clientes/listaClientes.txt',0,str(identificador))

    #TRECHO PARA EXIBIR NA TELA
    clear()
    if clientes== False:
        print('Sem clientes')
    else:
        insertSort(clientes,1)
        print('{:^110}'.format('LISTA DE CLIENTES'))
        print(110*'_'+'\n')
        for cliente in clientes:
            print('ID: '+cliente[0])
            print('Nome: '+cliente[1])
            print('Endereço:'+cliente[2])
            print('Telefone: '+cliente[3])
            print(110*'-')
    input('\nPressione Enter para continuar...')
############### FIM CLIENTES ###

###############  MANUTENÇÕES ###
def balanco():#
    while True:
        try:
            mes = input('Digite um mês: ')
            int(mes)#Acho que posso tirar isso
            ano = int(input('Digite um ano: '))
            data = f'{ano}-{mes}-{10}'
            date.fromisoformat(data)# Verifica se inseriu data válida
            break
        except:
            print('Insira os valores corretos')
    listaBalanco = []
    valor = 0
    #Lendo arquivo
    with open('manutencoes/realizada/ManutencoesRealizadas.txt', 'r') as arquivo:
        for linha in arquivo:
            item = linha.split('|')
            data = item[5].split('-')
            if (data[0] == str(ano)):
                listaBalanco.append(item)
                valor = valor + float(item[2])
    clear()
    #Exibindo na tela
    print('|{:<40}'.format('Peça'), end='')
    print('|{:<15}'.format('Validade'), end='')
    print('|{:<15}'.format('ID do cliente'), end='')
    print('|{:<15}'.format('Valor'))
    print(85*'_'+'\n')
    for elemento in listaBalanco:
        print('|{:<40}'.format(elemento[3][:40]), end='')
        print('|{:<15}'.format(elemento[4][:15]+' meses'), end='')
        print('|{:<15}'.format(elemento[1][:15]), end='')
        print('|{:<15}'.format(elemento[2][:15]))
        print(85*'-')
    print('{:>70}'.format('Valor total:'),'R$ ',valor)
    print('\nDeseja salvar em um arquivo de texto?')
    resposta = ''
    while resposta != 'S' and resposta != 'N':
        resposta = input('[S] para sim\n[N] para não\nDigite: ').upper()
    if resposta == 'S':
        #Salvando em um arquivo de texto
        nomeArquivo = ('Balanco' + mes + str(ano) + '.txt').replace('/','|')
        with open('balanco/'+nomeArquivo, 'w') as arquivo:
            titulo = 'Balanço de ' +mes +'/'+ str(ano)
            arquivo.write('{:^85}'.format(titulo)+2*'\n')
            arquivo.write('|{:<40}'.format('Peça'))
            arquivo.write('|{:<15}'.format('Validade'))
            arquivo.write('|{:<15}'.format('ID do cliente'))
            arquivo.write('|{:<15}'.format('Valor')+'\n')
            arquivo.write(85*'_'+2*'\n')
            for elemento in listaBalanco:
                arquivo.write('|{:<40}'.format(elemento[3][:40]))
                arquivo.write('|{:<15}'.format(elemento[4][:15]+' meses'))
                arquivo.write('|{:<15}'.format(elemento[1][:15]))
                arquivo.write('|R$ {:<15}'.format(elemento[2][:15])+'\n')
                arquivo.write(85*'-'+'\n')
            arquivo.write('{:>70}'.format('Valor total:')+' R$ '+str(valor))

def imprimirManutencao():
    nomeArquivo = input('Digite o nome para o arquivo: ').replace('/','|')
    manutencoes = read('manutencoes/agendada/ManutencoesAgendadas.txt',0)
    if manutencoes == False:
        print('Não há manutenções')
    else:
        insertSort(manutencoes,5)
        with open('impressao/'+nomeArquivo+'.txt', 'w') as arquivo:
            arquivo.write('MANUTENÇÕES AGENDADAS'.center(50)+'\n')
            arquivo.write(50*'_'+'\n')
            for elemento in manutencoes:
                arquivo.write(f'ID da manutenção: {elemento[0]}\n')
                arquivo.write(f'ID do cliente: {elemento[1]}\n')
                arquivo.write(f'Preço da manutenção: R$ {elemento[2]}\n')
                arquivo.write(f'Nome da peça: {elemento[3]}\n')
                arquivo.write(f'Validade da peça: {elemento[4]} meses\n')
                arquivo.write(f'Data da manutenção: {elemento[5]}\n')
                arquivo.write(50*'.'+'\n')
        print('Arquivo salvo com sucesso')
    input('Pressione Enter para continuar')

def agendarManutencao():
    manutencao = []
    cliente = False
    while True:
        try:
            IDcliente = int(input("Digite o identificador do cliente: "))
            cliente = read('clientes/listaClientes.txt', 0,str(IDcliente))
            if(cliente==False):
                print('ID não encontrado.')
            else:
                break
        except:
            print('O ID precisa ser um número inteiro e postivo.')   
    
    while True:
        try:
            valor = float(input('Digite o valor da manutenção: R$ '))
            if valor >=0:#Vai que ele teve que fazer uma manutenção gratuita para alguém
                break
        except:
            print('O valor deve ser numerico e positivo')
    
    while True:
        nomePeca = input("Informe o nome da peça: ").replace('|','/')
        if len(nomePeca) > 5:
            break
        print('Insira um nome válido')
    
    while True:
        try:
            prazoValidade = int(input('Informe de quantos meses é a validade da peça: '))
            if prazoValidade>0:
                break
        except:
            print('Insira um numero inteiro e positivo')
    
    while True:
        try:
            dataAgendada = input('Digite a data para a manutenção. A data deve ser do formato aaaa-mm-dd: ')
            date.fromisoformat(dataAgendada)#Verifica se a data é válida
            break
        except:
            print('Insira uma data valida')
    manutencao.append(geraID('manutencoes/agendada/ManutencoesAgendadas.txt'))
    manutencao.append(IDcliente)
    manutencao.append(valor)
    manutencao.append(nomePeca)
    manutencao.append(prazoValidade)
    manutencao.append(dataAgendada)
    create('manutencoes/agendada/ManutencoesAgendadas.txt',manutencao)
    print('Manutenção agendada com sucesso')
    input('Pressione Enter para retornar ao menu...')

def realizarManutencao():
    while True:
        try:
            IDmanutencao = int(input("Digite o ID da manutenção que deseja realizar: "))
            if IDmanutencao<0:
                raise Exception
            break
        except:
            print('O ID precisa ser um número inteiro e postivo.')
    item = read('manutencoes/agendada/ManutencoesAgendadas.txt', 0,str(IDmanutencao))
    if item:
        item[0][5] = item[0][5].replace('\n','')
        create('manutencoes/realizada/ManutencoesRealizadas.txt',item[0])
        print('Manutenção realizada com sucesso')
        item[0][5] = somaMeses(date.fromisoformat(item[0][5]), int(item[0][4]))
        altern('manutencoes/agendada/ManutencoesAgendadas.txt',item[0])
        print('Nova manutenção agendada automaticamente com sucesso.')
    else:
        print('Não econtramos manutenção com esse ID')
    input('Pressione Enter para retornar ao menu...')
    
def editarManutencao():
    print('Caso não deseje alterar alguma informação, basta pressionar Enter.')
    print('Certifique-se que não digitou nada antes de pressionar Enter.')
    manutencao = []
    while True:
        try:
            IDmanutencao = int(input("Digite o ID da manutenção que deseja alterar: "))
            if IDmanutencao<0:
                raise Exception
            break
        except:
            print('O ID precisa ser um número inteiro e postivo.')
    
    while True:
        try:
            IDcliente = input("Digite o identificador do cliente: ")
            if(bool(IDcliente) == False):
                break
            
            IDcliente=int(IDcliente)
            if(IDcliente<0):
                raise Exception
            cliente = read('clientes/listaClientes.txt', 0,str(IDcliente))
            if(cliente==False):
                print('ID não encontrado.')
            else:
                break
        except:
            print('O ID precisa ser um número inteiro e postivo.')
    
    while True:
        try:
            valor = input('Digite o valor da manutenção: R$ ')
            if(bool(valor) == False):
                break
            valor = float(valor)
            if (valor < 0):
                raise Exception
            break
        except:
            print('O valor deve ser numero e positivo')
    nomePeca = input("Informe o nome da peça: ").replace('|','/')
    
    while True:
        try:
            prazoValidade = input('Informe de quantos meses é a validade da peça: ')
            if(bool(prazoValidade) == False):
                break
            prazoValidade=int(prazoValidade)
            if (prazoValidade <= 0):
                raise Exception
            break
        except:
            print('Insira um numero inteiro e positivo')
    
    while True:
        try:
            dataAgendada = input('Digite a data para a manutenção. A data deve ser do formato aaaa-mm-dd: ')
            if bool(dataAgendada) == False:
                break
            date.fromisoformat(dataAgendada)
            break
        except:
            print('Insira uma data valida')

    manutencao.append(IDmanutencao)
    manutencao.append(IDcliente)
    manutencao.append(valor)
    manutencao.append(nomePeca)
    manutencao.append(prazoValidade)
    manutencao.append(dataAgendada)
    encontrou = altern('manutencoes/agendada/ManutencoesAgendadas.txt',manutencao)
    if(encontrou == False):
        print('Não há manutenção com esse ID no banco de dados')
    else:
        print('Alteração efetuada')
    input('Pressione Enter para retornar ao menu...')

def excluirManutencao():
    while True:
        try:
            IDmanutencao = int(input("Digite o ID da manutenção que deseja alterar: "))
            if IDmanutencao<0:
                raise Exception
            break
        except:
            print('O ID precisa ser um número inteiro e postivo.')
    encontrou = delete('manutencoes/agendada/ManutencoesAgendadas.txt', str(IDmanutencao))
    if encontrou:
        print('Manutenção deletada com sucesso!')
    else:
        print('Manutenção não encontrada')
    input('Pressione Enter para retornar ao menu...')

def listarManutencao():
    resposta = 'N'
    while resposta!='A' and resposta!='R' and resposta != 'AR':
        clear()
        print("[A] para ver as Manutenções agendadas")
        print("[R] para ver as Manutenções realizadas")
        print('[AR] para ver as Manutenções agendadas e realizadas')
        resposta = input('Digite sua opção: ').upper()
    clear()
    if(resposta=='A'):
        manutencao = read('manutencoes/agendada/ManutencoesAgendadas.txt',0)
        exibir_lista_manutencao(manutencao,'MANUTENÇÕES AGENDADAS')
    elif(resposta=='R'):
        manutencao = read('manutencoes/realizada/ManutencoesRealizadas.txt',0)
        exibir_lista_manutencao(manutencao,'MANUTENÇÕES REALIZADAS')
    else:
        manutencao = read('manutencoes/agendada/ManutencoesAgendadas.txt',0)
        exibir_lista_manutencao(manutencao,'MANUTENÇÕES AGENDADAS')
        manutencao = read('manutencoes/realizada/ManutencoesRealizadas.txt',0)
        print('\n\n')
        exibir_lista_manutencao(manutencao,'MANUTENÇÕES REALIZADAS')
    input('Pressione Enter para retornar ao menu...')
    
def exibir_lista_manutencao(manutencao,titulo):
    print(titulo.center(50)+'\n')
    print(50*'_'+'\n')
    for elemento in manutencao:
        print(f'ID da manutenção: {elemento[0]}')
        print(f'ID do cliente: {elemento[1]}')
        print(f'Preço da manutenção: R$ {elemento[2]}')
        print(f'Nome da peça: {elemento[3]}')
        print(f'Validade da peça: {elemento[4]} meses')
        print(f'Data da manutenção: {elemento[5]}')
        print(50*'.'+'\n')
###############  FIM MANUTENÇÕES ###
menu_principal()