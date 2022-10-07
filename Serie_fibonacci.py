## La serie figonashi es una secuencia numerica, en la cual cada elemento es igual a la suma de los dos anteriores. Tomando como variales iniciales los dos primeros elementos, a = 0 b=1 hacer el diagrama y el programa el python, que calcule y imprima apartir del tercero, todos los elementos de la serie de figonashii que sean menores de 1000

print("---------------------------")
print("------SERIE-FIGONACCI------")
print("---------------------------")

sec = 0
n = 3

while sec < 1000:
    sec = int((1.618033989**n - (-0.6180339887**n))/5**0.5)
    
    print("El absu",n,"es:",sec)
    n = n + 1
print("Programa terminado.")
    
