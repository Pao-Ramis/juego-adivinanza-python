import random


número_secreto = random.randint(1,101)
adivinado = False
can_intentos = 0
cant_máxima_intentos = 5

print("Bienvenido al juego de adivinar el número secreto")

while not adivinado and can_intentos < cant_máxima_intentos:
    entrada = input("Introduce un número del 1 al 100 ")
    número = int(entrada)
   

    if número == número_secreto:
        print("¡Felicitaciones! Has adivinado el núero secreto")
        adivinado = True
    elif número < número_secreto:
        print("El número ingresado es menor al número secreto")
    else:
        print("El número ingresado es mayor al número secreto")

    can_intentos += 1

if not can_intentos < cant_máxima_intentos:
    print("Game over! No has podido adivinar dentro de los  intentos")



    


