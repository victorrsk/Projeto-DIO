from datetime import datetime

def menu():
    
    print('---SISTEMA BANCÁRIO---')
    print()
    print('OPÇÕES:\n1-DEPÓSITO\n2-SAQUE\n3-VER EXTRATO\n4-CADASTRAR USUARIO\n5-CRIAR CONTA\n6-MOSTRAR SALDO\n7-MOSTRAR USUARIOS E CONTAS\n8-SAIR')
    print('----------------------')
    
def deposito(numero_conta, lista_de_contas, valor_deposito, lista_extrato, /):
    
    for conta in lista_de_contas:
        if conta['numero_conta'] == numero_conta:
            
            try:
                valor_deposito = float(valor_deposito)
            except:
                return ('Valor inválido')
                
            if valor_deposito < 50:
                return 'Deposite pelo menos R$50.00'
                
            else:
                conta['saldo'] += valor_deposito
                    
                ver_extrato(lista_extrato, f'Depósito de R${valor_deposito:.2f}')
                return 'Depósito realizado com sucesso'
            
    return 'Conta não encontrada'
        
def saque(*, numero_conta, lista_de_contas, valor_saque, lista_extrato):
    
    for conta in lista_de_contas:
        if conta['numero_conta'] == numero_conta:
    
            try:
                valor_saque = float(valor_saque)
            
            except:
                return 'Valor inválido'
            
            
            if valor_saque <= conta['limite'] and valor_saque <= conta['saldo']:
                
                conta['saldo'] -= valor_saque
                ver_extrato(lista_extrato, f'Saque de R${valor_saque:.2f}')
                return 'Saque realizado com sucesso'
            
            
            elif valor_saque > conta['limite']:
                return 'O valor do saque excede o limite da conta'
            
            elif valor_saque > conta['saldo']:
                return 'O valor do saque excede o saldo da conta'
    return 'Conta não encontrada'
       
def ver_extrato(lista_extrato, mensagem, /):

    hora_agora = datetime.now()
    hora_agora = hora_agora.strftime('%H:%M')
    lista_extrato.append(f'Horário:[{hora_agora}] {mensagem}')

def mostrar_saldo(numero_conta, lista_de_contas):
    for conta in lista_de_contas:
        if conta['numero_conta'] == numero_conta:
            return f'Saldo da conta: R${conta['saldo']:.2f}'
                
    return 'A conta não foi encontrada'


