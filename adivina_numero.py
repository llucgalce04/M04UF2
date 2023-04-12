import random

numero_adivinar = random.randrange(100)
#print(numero_adivinar)



teclado = input("Introduce tu numero: ")

while numero_adivinar != teclado:

	if int(teclado) > numero_adivinar:
		print("El numero que quieres adivinar es mas pequeño ")
		
		teclado = input("Introduce tu numero: ")
	
	elif int(teclado) < numero_adivinar:
		print("El numero que quieres adivinar es mas grande ")
		
		teclado = input("Introduce tu numero: ")
	
	else:	
		print("Lo adivinaste papurri!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		break
	
