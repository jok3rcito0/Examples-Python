# ~*~ coding: utf-8

##
# 
##

def factorial(number):
	if number == 0:
		return 1
	else:
		return number * factorial(number - 1)

if __name__ == '__main__':
	number = int(raw_input('Escribe un número: '))

	result = factorial(number)

	#print ('{:.2e}').format(result)
	print ('%.3E'%result)