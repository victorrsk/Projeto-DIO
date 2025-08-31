itens = []

for i in range(3):
    item = input(f'{i+1}° item: ')
    itens.append(item)

print("Lista de Equipamentos:")
for item in itens:
    print(f'- {item}')