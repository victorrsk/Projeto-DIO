
def cadastrar_usuario(*, lista_de_CPF, lista_de_usuarios, nome, data_nasc, CPF, endereço):
    # valida o nome
    if nome.isalpha() and len(nome) >= 3:
        # valida o cpf
        if CPF.isdigit() and len(CPF) == 11:
            # verifica se o cpf informado já existe na lista
            if CPF not in lista_de_CPF:

                lista_de_usuarios.append({'nome': nome, 'data_nasc': data_nasc, 'CPF': CPF, 'endereço': endereço})
                lista_de_CPF.append(CPF)
                return f'Usuário "{nome}" cadastrado'

            else:
                return 'CPF já cadastrado'
        else:
            return 'CPF inválido'
    else:
        return 'Nome inválido, 3 letras no mínimo'


def criar_conta(*, lista_de_contas, lista_de_usuarios, lista_de_CPF, vincular_CPF):
    
    if vincular_CPF not in lista_de_CPF:
        return 'O CPF informado não está cadastrado'
    else:
        for usuario in lista_de_usuarios:
            if usuario['CPF'] == vincular_CPF:
                # o desafio propõe que o numero da conta seja crescente, um a um
                # usei o len para buscar o comprimento da própria lista de contas somando + 1 para comecar com 1
                # visto que na criação da primeira conta ela começa com tam iguala 0
                lista_de_contas.append({'agência': '0001', 'numero_conta': '000'+str(len(lista_de_contas)+1), 'extrato': [], 'saldo': 0, 'limite': 500})
                return lista_de_contas

# mostrar os dados ca conta referente ao usuario
def listar_dados(*, lista_de_contas, lista_de_usuarios):
    # itera sobre os indices da lista
    for indice, usuario in enumerate(lista_de_usuarios):
        print('-------------------------------')
        print(f'{indice+1}° Usuário')
        print('-------------------------------')
        # mostra os pares de chave/valor do indice o qual está sendo iterado
        # no caso, é um dicionário dentro da lista maior
        for key, valor in usuario.items():
            print(f'{key} = {valor}')
        print('-------------------------------')
        
