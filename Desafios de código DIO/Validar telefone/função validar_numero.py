import re

def validar_numero(numero):
    # o modelo aceita (XX) XXXXX-XXXX, o espaco entre o DDD e os 5 primeiros digitos
    # e o traço dividindo os 5 digitos dos ultimos 4 são opcionais 
    padrao = r'^\(\d{2}\)\s?\d{5}-?\d{4}'

    if re.match(padrao, numero):
        return 'Número válido'
    else:
        return 'Número inválido'
    
numero = input('Informe o número: ')
resultado = validar_numero(numero)

print(resultado)
