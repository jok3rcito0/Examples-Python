# ~*~ coding: utf-8

###########################################################################################################################
# En matemáticas, un número primo es un número mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1. #
###########################################################################################################################

def is_prime(number):
	if number > 2:
		for x in xrange(2,number):
			if number % x != 0:
				if number % number == 0 and number % 1 == 0:
					response = True
			else:
				response = False
				break

	return response

def start():
	while True:
		try:
			digit = raw_input('Introduce un número: ')
			if digit.isdigit() == False and digit == 'exit':
				exit()
			elif is_prime(int(digit)) == True:
				print('El numero {}, es primo'.format(digit))
			else:
				print('{}, No es primo'.format(digit))
		except ValueError:
			print ('Si quieres salir escribe "exit" o escribe un entero y averigua si es primo')

if __name__ == '__main__':
	start()