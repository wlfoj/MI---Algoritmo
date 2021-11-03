"""
/*******************************************************************************
Autor: Washington Luis Ferreira de Oliveira Júnior
Componente Curricular: MI - ALGORITMOS
Concluido em: 20/03/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/
"""
continuar = True
totalVacinados = 0
totalMasculino = 0    
totalManha = 0     
dose2 = 0           
dose1 = 0             
coronavac = 0       
idoso = 0

while(continuar == True):
    print("\n{:^60}\n".format("MENU"))
    resposta = input("Digite:\n1 - Cadastrar dose\n2 - Consultar relatório\nQualquer tecla - Sair: ").strip()

##   INSERINDO DADOS   ##
    if (resposta == '1'):
        print("\n{:^60}\n".format("CADASTRO DA DOSE"))
        nome = input("Informe o nome do vacinado: ")
        cpf = input("Informe o CPF do vacinado, apenas numeros: ")
        ##   VALIDAR DATA   #
        data = ''
        while(data == ''):
            data = input("Digite a data no formato: DD/MM/AAAA\n")
            data = data.split('/')
            if(len(data)!= 3):
                data = ''
                print("Insira uma data valida no formato indicado")
            else:
                if(not((int(data[2])==2021) and (int(data[1])>=1 and int(data[1])<=12) and ((int(data[0])>=1 and int(data[0])<=31)))):
                    print("Data invalida")
                    data = ''

        ##   VALIDANDO O HORÁRIO   #
        hora = ''
        while(hora == ''):
            hora = input("Informe o horário da vacinação como no exemplo: HH:MM\n")
            hora = hora.split(':')
            if(len(hora)!= 2):
                hora = ''
                print("Insira um horario valido no formato indicado")
            else:
                if(not(int(hora[1])>=0 and int(hora[1])<60)):
                    print("Horario invalido")
                    hora = ''
                else:
                    if(int(hora[0])>=8 and int(hora[0])<12):
                        totalManha = totalManha + 1
                    elif(not(int(hora[0])>=12 and int(hora[0])<18)):
                        print("Horario invalido")
                        hora = ''
  
        dose = input("\nDigite\n1 - para a 1° dose\nQualquer tecla - para a 2° dose: ").strip()
        if(dose == '1'):
           #  VALIDANDO O SEXO  #
            sexo = ''
            while(sexo == ''):
                sexo = input("\nDigite o sexo\nM - para masculino\nF - para feminino: ").strip()
                if(sexo == 'M'):
                    totalMasculino = totalMasculino + 1 
                elif(sexo != 'F'):
                    sexo = ''
                    print("Insira um valor valido")

            ##  VALIDANDO AO GRUPO PRIORITÁRIO  #
            grupo_prioritario = ''
            while(grupo_prioritario == ''):
                grupo_prioritario = input("\nDigite o grupo\n1 - Idosos com 80 anos ou mais\n2 - Idosos que vivem em lares permanentes\n3 - Trabalha na saúde\n4 - Indígena/Aldeados\n5 - Outros: ").strip()
                if(int(grupo_prioritario) == 1 or int(grupo_prioritario) == 2):
                    idoso = idoso + 1
                elif(int(grupo_prioritario) > 5 or int(grupo_prioritario) < 1):
                    grupo_prioritario = ''
                    print('Insira um valor valido')

            ##  VALIDANDO O LOCAL  #
            local_vacina = ''
            while(local_vacina == ''):
                local_vacina = input("\nInforme o local\n1 - UBS\n2 - USF\n3 - Drive Thru\n4 - Hospital\n5 - Outros: ").strip()
                if(int(local_vacina) > 5 or int(local_vacina) < 1 ):
                    local_vacina = ''
                    print("Insira um valor valido")

            #  VALIDANDO O FABRICANTE  #
            fabricante_vacina = ''
            while(fabricante_vacina == ''):
                fabricante_vacina = input("\nDigite \n1 - para Coronavac\n2 - para Astrazeneca: ").strip()
                if(fabricante_vacina == '1'):
                    coronavac = coronavac + 1
                elif(fabricante_vacina != '2'):
                    fabricante_vacina = ''
                    print("Insira um valor valido")

            lote_vacina = input("\nInsira o lote da vacina: ")
            totalVacinados = totalVacinados + 1
            dose1 = dose1 + 1
            print("Cadastro realizado com sucesso!")
        else:
            if(dose1 > dose2):
                dose2 = dose2 + 1
                print("Cadastro realizado com sucesso!")
            else:
                print("Para acrescentar a segunda dose, é preciso que o paciente tenha tomado a primeira")
        input("Pressione Enter para retornar ao Menu...")
        totalDose = dose2 + dose1

##   BUSCANDO DADOS   ##
    elif(resposta == '2'):
        if(totalVacinados == 0):
           print("\nNão há vacinados") 
        else:
            print("\n{:^60}\n".format("RELATÓRIO"))
            porcentMasc = (totalMasculino/totalVacinados)*100 
            porcentFemi = 100 - porcentMasc
            porcentManha = (totalManha/totalDose)*100
            porcentTarde = 100 - porcentManha
            porcentCoronavac = (coronavac/totalVacinados)*100
            porcentAstrazeneca = 100 - porcentCoronavac
            porcentIdoso = (idoso/totalVacinados)*100

            print(f'Sexo Masculino: {round(porcentMasc,2)}%\nSexo Feminino: {round(porcentFemi,2)}%')
            print(f'Doses aplicadas pela manhã: {round(porcentManha,2)}%\nDoses aplicadas pela tarde: {round(porcentTarde,2)}%')
            print(f'Quantidade de 1° dose aplicadas: {dose1}\nQuantidade de 2° dose aplicadas: {dose2}')
            print(f'Vacinas da Coronavac: {round(porcentCoronavac,2)}%\nVacinas da Astrazeneca: {round(porcentAstrazeneca,2)}%')
            print(f'Grupo dos idosos: {round(porcentIdoso,2)}%')
            print(f'Total de doses aplicadas: ', totalDose)
            print(f'Total de pessoas vacinadas: ', totalVacinados)
        input("Pressione Enter para retornar ao Menu...")

##   SAINDO DO LOOP   ##
    else:
        continuar = False

print("Tenha um bom dia!")
