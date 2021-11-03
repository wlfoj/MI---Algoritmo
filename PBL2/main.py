"""
/*******************************************************************************
Autor: Washington Luis Ferreira de Oliveira Junior
Componente Curricular: MI - Algoritmos 
Concluido em: 25/04/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/
"""
import time
import keyboard
import os
from blessed import Terminal
from random import randint
term = Terminal()

##TRECHO DE FUNÇÕES PARA AUXILIAR O MENU
def clear():
    if(os.name == 'posix'):
        os.system('clear')
    else:
       os.system('cls')

def instrucao():
    clear()
    print('{:^90}'.format('INSTRUÇÕES PARA O JOGO\n'))
    print('- A nave será movimentada ao pressionar as teclas left ou right do teclado')
    print('- Ao pressionar a tecla espaço um tiro será lançado')
    print('- Não conseguir destruir 10 meteoros resulta em fim de jogo')
    print('- A partida pode ser encerrada ao pressionar esc')
    print('- Colidir com um asteroide resulta em anulação da partida')
    input("\nPressione Enter para continuar...")


def sobre():
    print('{:^90}'.format('SOBRE O JOGO\n'))
    print('Este jogo é uma versão do jogo Asteroids, onde o seu objetivo será destruir o máximo')
    print('de asteroides possiveis. Foi desenvolvido por Washington Luis, discente de Engenharia')
    print('de Computação na Universidade Estadual de Feira de Santana.')
    print('O game desenvolvido com o objetivo de solucionar o problema proposto no MI de Algoritmo,')
    print('de modo a ingressarna Rookie Software Inc.')
    input("\nPressione Enter para continuar...")

def recordes(historico):
    print('{:^90}'.format('15 MAIORES PONTUAÇÕES\n'))
    historico.sort(reverse=True)
    if (len(historico) == 0):
        print('{:^90}'.format('Não há registros'))
    else:
        for i in range(len(historico)):
            texto = '{:.<20}'.format(historico[i][1])+str(historico[i][0])
            print(texto.center(90))
            if (i == 14):#EXIBIR APENAS OS 15 MELHORES
                break
    input("\nPressione Enter para continuar...")

#TRECHO DE FUNÇÕES PARA A JOGATINA
def gameOver(colisao,historico,pontos):
    time.sleep(1.5)
    clear()
    print((int(term.height/2)-1)*'\n'+'{:^90}'.format('FIM DE JOGO')+(int(term.height/2)-2)*'\n')
    if(colisao == True):
        print("Colisão com Asteroide, Partida perdida!")
        input("Pressione Enter para retornar ao Menu...")
    else:
        input("Pressione Enter para continuar...")
        nome = input("Informe um nick, máximo 10 caracteres: ").strip()
        historico.insert(0,[pontos*3,nome[0:10]])

def sidebar(nAsteroid,ponto):#BARRA DE INFORMAÇÕES, TEMPO REAL
    print(term.home+term.move_xy(9*10, 10)+f'Pontos: {ponto*3}')
    print(term.home+term.move_xy(9*10, 11)+f'Asteroides não destruidos: {nAsteroid}')

def verificaAsteroids(posicaoNave,listaAsteroid,auxiliar,i):
    if(listaAsteroid[i][0]+4>=posicaoNave[0] and listaAsteroid[i][1] == posicaoNave[1]):#Vê se bateu na nave
        auxiliar[0] = 1    
    elif(listaAsteroid[i][0]>posicaoNave[0]+3):#Vê se atingiu parte de baixo da tela
        listaAsteroid.pop(i)
        auxiliar[1] = auxiliar[1] + 1
    try:
        listaAsteroid[i][0] = listaAsteroid[i][0] + 1
    except:
        pass
    
def exibirAsteroid(listaAsteroid,cicloAsteroid,auxiliar,posicaoNave):
    asteroid=['{:^9}'.format('***'),'{:^9}'.format('*****'),'{:^9}'.format('*******'),'{:^9}'.format('*****'),'{:^9}'.format('***')]
    for i in range(len(listaAsteroid)):
        #Efeito surgindo
        if(listaAsteroid[i][0] < 0):
            for a in range(0, 5 + listaAsteroid[i][0]):
                print(term.home+term.move_xy(listaAsteroid[i][1]*9, 4+listaAsteroid[i][0]-a)+asteroid[4-a], end = '')
        #Efeito sumindo
        elif(listaAsteroid[i][0] > 33):
            for a in range(0,(38 - listaAsteroid[i][0])):
                print(term.home+term.move_xy(listaAsteroid[i][1]*9, listaAsteroid[i][0]+a)+asteroid[a], end = '')
        #Printa sem efeito
        else:
            for a in range(0,5):
                print(term.home+term.move_xy(listaAsteroid[i][1]*9, listaAsteroid[i][0]+a)+asteroid[a], end = '')
        #Chama as verificações
        if (cicloAsteroid == 3):
            verificaAsteroids(posicaoNave,listaAsteroid,auxiliar,i)

def verificaTiros(listaTiro,listaAsteroid,ponto,i):
    #Verifica se atingiu topo da tela
    if(listaTiro[i][0] < 0):
        listaTiro.pop(i)
    #Verificar se bateu no asteroid
    for a in range(len(listaAsteroid)):
        if (a < len(listaAsteroid) and i < len(listaTiro)):
            if((listaAsteroid[a][0] + 4 >= listaTiro[i][0]) and (listaAsteroid[a][1] == listaTiro[i][1])):
                listaAsteroid.pop(a)
                listaTiro.pop(i)
                ponto = ponto + 1
        else:
            break
    try:
        listaTiro[i][0] = listaTiro[i][0] - 1
    except:
        pass
    return ponto

def exibirTiro(listaTiro,listaAsteroid, ponto):
    for i in range(len(listaTiro)): 
        if (i < len(listaTiro)):
            print(term.home+term.move_xy(9*listaTiro[i][1], listaTiro[i][0])+'{:^9}'.format('o'))
            ponto = verificaTiros(listaTiro,listaAsteroid,ponto,i)
        else:
            break
    return ponto

def exibirNave(posicaoNave):
    print(term.home+term.move_xy(posicaoNave[1]*9, posicaoNave[0])+'{:^9}'.format('*'), end='')
    print(term.home+term.move_xy(posicaoNave[1]*9, posicaoNave[0]+1)+'{:^9}'.format('* *'), end='')
    print(term.home+term.move_xy(posicaoNave[1]*9, posicaoNave[0]+2)+'{:^9}'.format('* * *'), end='')

def Nave(posicaoNave,lado):
    if(not((lado=='E' and posicaoNave[1]==0) or (lado=='D' and posicaoNave[1]==8))):
        if (lado=='E'):
            posicaoNave[1] = posicaoNave[1] - 1
        elif (lado == 'D'):
            posicaoNave[1] = posicaoNave[1] + 1
    exibirNave(posicaoNave)

def jogatina(historico):
    listaAsteroid = [] #Registro de Asteroides
    listaTiro = []     #Registro de Tiros
    cicloAsteroid = 0  #Para controlar o momento de mover asteroide
    cicloCriarAster = 0 #Para controlar o momento de criar asteroide
    posicaoNave = [term.height-3,4] #35
    ponto = 0
    travaSpace = False
    lado = 'C'
    auxiliar =[0,0,1]   # auxiliar[0] -> Informa se houve colisão da nave com asteroid
                        # auxiliar[1] -> Informa a quantidade de asteroids não destruidos
                        # auxiliar[2] -> Informa se pressionou esc
    while(auxiliar[0] == 0 and auxiliar[1] < 10 and auxiliar[2] == 1):
        clear()
        #TRECHO SOBRE OS ASTEROID
        exibirAsteroid(listaAsteroid,cicloAsteroid,auxiliar,posicaoNave)
        if (cicloAsteroid == 3):
            cicloAsteroid = 0
            if(cicloCriarAster == 5):# Conta 5 ciclos dentro do ciclo asteroide e cria outro asteroide
                listaAsteroid.insert(0,[-4,randint(0,8)])
                cicloCriarAster = 0
            cicloCriarAster = cicloCriarAster + 1

        #TRECHO SOBRE OS TIROS
        ponto = exibirTiro(listaTiro,listaAsteroid, ponto)
        #Trecho baseado na explicação do tutor, criando tiros
        if(keyboard.is_pressed('space') == True and travaSpace == False):
            travaSpace = True
        elif(keyboard.is_pressed('space') == False and travaSpace == True):
            travaSpace = False
            listaTiro.append([34,posicaoNave[1]])
        
        #TRECHO SOBRE A NAVE
        #Trecho baseado na explicação do tutor, movimento da nave
        if(keyboard.is_pressed('left') == True and lado == 'C'):
            lado = 'E'
        elif(keyboard.is_pressed('left') == False and lado == 'E'):
            Nave(posicaoNave,lado)
            lado = 'C'
        if(keyboard.is_pressed('right') == True and lado == 'C'):
            lado = 'D'
        elif(keyboard.is_pressed('right')== False and lado == 'D'):
            Nave(posicaoNave,lado)
            lado = 'C'
        else:
            Nave(posicaoNave,'C')
        
        #DESISTÊNCIA
        if(keyboard.is_pressed('esc')):
            auxiliar[2] = 0

        sidebar(auxiliar[1],ponto)
        cicloAsteroid = cicloAsteroid + 1
        time.sleep(0.0333)#30FPS
    gameOver(auxiliar[0], historico, ponto)

#TRECHO DE FUNÇÕES PARA O MENU
def printMenu(posicao):#Printa o menu
    clear()
    print('{:^90}\n\n'.format('ASTEROIDS'))
    print(('Pressione SHIFT para selecionar:\n').center(90))
    if (posicao == 0):
        print(('{:<10}'.format('Jogar')+'<-').center(90))
    else:
        print(('{:<10}'.format('Jogar')).center(90))
    if (posicao == 1):
        print(('{:<10}'.format('Recordes')+'<-').center(90))
    else:
        print(('{:<10}'.format('Recordes')).center(90))
    if (posicao == 2):
        print(('{:<10}'.format('Sobre')+'<-').center(90))
    else:
        print(('{:<10}'.format('Sobre')).center(90))
    if (posicao == 3):
        print(('{:<10}'.format('Sair')+'<-').center(90))
    else:
        print(('{:<10}'.format('Sair')).center(90))

def operacao(posicao,historico,sair):#Seleciona a opção do menu
    if (keyboard.is_pressed('shift')):
        clear()
        if(posicao == 0):
            instrucao()
            jogatina(historico)
        elif(posicao == 1):
            recordes(historico)
        elif(posicao == 2):
            sobre()
        else:
            sair = True
        printMenu(posicao)
    return sair

def menu():#Função princiapl, onde todo o menu funciona
    posicao = 0
    fechar = False
    historico = []
    printMenu(posicao)
    while (fechar == False):
        if (keyboard.is_pressed('up')):
            while (keyboard.is_pressed('up')):
                pass
            if (posicao == 0):
                posicao = 3
            else:
                posicao = posicao - 1
            printMenu(posicao)#Chamar a função somente se pressionar as teclas, evita ficar piscando
        elif (keyboard.is_pressed('down')):
            while (keyboard.is_pressed('down')):
                pass
            if (posicao == 3):
                posicao = 0
            else:
                posicao = posicao + 1
            printMenu(posicao)
        fechar = operacao(posicao,historico,fechar)
    
menu()#RODA O GAME   