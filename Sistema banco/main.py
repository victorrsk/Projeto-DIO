from bancoutils import menu, deposito, saque, mostrar_saldo, ver_extrato
from conta import criar_conta, cadastrar_usuario, listar_dados

escolha = ''
lista_CPF = []
lista_usuarios = []
contas = []
lista_extrato = []

while True:
    
    menu()
    escolha = input('Informe a opção desejada: ') 
    try:
        escolha = int(escolha)
    except:
        print('Valor inválido')
  
    if escolha == 1:
        print(deposito(input('Informe o número da conta(ate 0009): '),
                       contas, input('Valor do depósito: '),
                       lista_extrato))
        
    elif escolha == 2:
        print(saque(numero_conta=input('Número da conta: '),
                    lista_de_contas=contas,
                    valor_saque=input('Valor do saque: '),
                    lista_extrato=lista_extrato))
    
    elif escolha == 3:
        for movimento in lista_extrato:
            print(movimento)
    
    elif escolha == 4:
        print(cadastrar_usuario(lista_de_CPF=lista_CPF,
                                lista_de_usuarios=lista_usuarios,
                                nome=input('Informe seu nome: ').strip(),
                                data_nasc=input('Sua data de nascimento(MM/DD/AAAA): '),
                                CPF=input('Informe seu CPF(sem pontos): '),
                                endereço=input('Seu endereço: ')))
        
    elif escolha == 5:
        print(criar_conta(lista_de_contas=contas,
                          lista_de_usuarios=lista_usuarios,
                          lista_de_CPF=lista_CPF,
                          vincular_CPF=input('Informe o CPF da conta que deseja vincular: ')))
         
    elif escolha == 6:
        print(mostrar_saldo(input('Número da conta(ate 0009): '),
                            contas))
        
    elif escolha == 7:
        listar_dados(lista_de_contas=contas,
                     lista_de_usuarios=lista_usuarios)
    
    elif escolha == 8:
        print('-----------------')
        print('|Fim do programa|')
        print('-----------------')
        break
    
    else:
        print('Opção inválida')
        
print(contas)
print(lista_usuarios)

