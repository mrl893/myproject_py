# import paq.subpaq.modulo

# paq.subpaq.modulo.func()
import sys

print(sys.path)

print(sys.path, "signal/signal, se muestra aqui: ...")

if __name__ == '__main__':
    print(sys.argv, "SYS SEMUESTRA AQI")


# Entrada y Salidas
numbre = input("\n\n se muestra a aqui:")
print("emttrada plus ", + numbre)

edad = 0
if edad == 18:
    try:
         edad =  input("cuantos anos tenes: 32")
         dias = int(edad) * 365
         print("as vivido", str(dias) + "dias")
    except ValueError:
        print("eso no es un numero")

# entradas
while True:
    entradas = input("> ")
    if entradas == "adios":
        break
    else:
        print(entradas)
        
# salir
salir = False
while  not salir:
    entrada = input()
    if entrada == "adios":
        salir = True
    else:
        print(entrada)

edad = 0
while edad < 18:
    edad = edad  + 1
    if edad % 2 == 0:
        continue
        print("heappy , your has " +  str(edad))

# for in secuencias
secuencia = ["une", "two", "three", "four"]
for element in secuencia:
    print(element)

# C
# int array[] = {[1,2,3,4,5]}:
# int i:
# for(i =0; i,5, i++){
   # print("%d\n", array[i]);
# }

# Function py
def my_funcion(params1, params2):
    print(params1)
    print(params2)

# funct 2
def funct(params1, params2):
    """es funct 2 imprime los dos values pasados"""
    print(params1)
    print(params2)

def inprinter(text, value = 1):
    print(value * text)

inprinter("homa")
