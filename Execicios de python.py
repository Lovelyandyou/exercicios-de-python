a  = input(' Digite algo na tela:')
print( ' O tipo primitivo desse valor é ', type(a))
print(' Só tem espaços? ' , a.isspace())
print(' É um número? ', a.isnumeric())
print( 'É alfabético? ', a.isalpha())
print('É alfanúmerico? ', a.isalnum())
print('Está em minúsculo? ', a.islower())
print(' Está capitalizada? ', a.istitle())