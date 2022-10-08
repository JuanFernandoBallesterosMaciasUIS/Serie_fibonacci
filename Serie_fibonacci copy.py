## La serie figonashi es una secuencia numerica, en la cual cada elemento es igual a la suma de los dos anteriores. Tomando como variales iniciales los dos primeros elementos, a = 0 b=1 hacer el diagrama y el programa el python, que calcule y imprima apartir del tercero, todos los elementos de la serie de figonashii que sean menores de 1000

print("---------------------------")
print("------SERIE-FIBONACCI------")
print("---------------------------")

n = 3
a = 0 
b = 1
c = a + b

while c < 1000:
    a = b
    b = c
    c = a + b
    print("El absu",n,"es:",c)
    n = n + 1

