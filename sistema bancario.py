menu = '''
<---Menu bancario--->
|                   |
| 1-DEPOSITO        |
| 2-SAQUE           |
| 3-EXTRATO         |
| 4-SAIR            |
<------------------->
=>
'''

saldo = qnt_saque = qnt_deposito = escolha = saques_diarios = 0
LIMITE_CONTA = 500
extrato = ''


while True:
    
    try:
        escolha = int(input(menu))
        if escolha not in range(1,5):
            print('Digite um opção válida')
    except:
        print('Opção inválida')
    
    if escolha == 1:
        qnt_deposito = float(input('Valor do deposito: R$'))
        
        while qnt_deposito <= 0:
            print('Valores inválidos, tente novamente')
            qnt_deposito = float(input('Valor do deposito: R$'))
            
        saldo += qnt_deposito
        extrato += f'Foi realizado um deposito no valor de R${qnt_deposito:.2f}\n'
    
    elif escolha == 2:
        if saques_diarios == 3:
            print('Limite de saques excedido')
        else:
            qnt_saque = float(input('Valor do saque: R$'))
            
            if qnt_saque > saldo:
                print('Valor do saquece excede o saldo')
            elif qnt_saque > LIMITE_CONTA:
                print('Valor do saque excedo o limite da conta')
            else:
                saldo -= qnt_saque
                saques_diarios += 1
                extrato += f'Saque no valor de R${qnt_saque:.2f} foi realiazdo\n'
       
    elif escolha == 3:
        print(extrato)
        
    elif escolha == 4:
        print('Encerrando sistema')
        break

    print(saldo)
    