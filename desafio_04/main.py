first_name = input("Digitel seu primeiro nome: ")
age = int(input('Digite sua idade: '))


print('Olá,', first_name,'! Você tem', age,'anos.')
print('Olá, {}! Você tem {} anos.'.format(first_name,age))
print(f'Olá, {first_name}! Você tem {age} anos.')