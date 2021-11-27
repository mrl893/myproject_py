# tipos BS
c = "hola\ a todos"
e = 23
print(type(c)) # str
print(type(e)) # init

# number
entero1 = 23
print(type(entero1)) # int

# enter
entero2 = 0x17
print(entero2) # int 23

real0 = 0.2703
print(real0+1)


real1 = 0.1e-3
print(real1)

complejos0 = 2.1 + 7.8j
print(complejos0)

# arimetrix r

r = 3.0 /2
print(r)

r1 = float(2) /3
print(r1)


# cadenas

unicode = u"aoe" # aoe
raw = r"\n" # \n

triple = """first lines
            the result is other lines"""
print(triple)

a = "une"
b = "two"

c1 = a + b
c2  = a * 3
print(c1, c2)

# list

l = [22, True, "one list", [1,2]]
#print(l)

l = [11,False]
#mi_var2 = l[0]
#print(mi_var2) # 11


# mi_var2 = l[1][0]
#print(mi_var2)


mi_var2 = l[0:2] [:2] [:] [::2]
mi_var2 = l[0:4:2]

# tuples

t = (1,2,  True, "javascript")
# t = 1,2,3
type(t)
print(t)

mi_var3 = t[0]
mi_var3 = t[0:2]
print(mi_var3)

c = "morel"
print(c[0])
print(c[5:])
print(c[::3])

c = a
print(a)


# Dictionarys

dict = {"Love Actually ": "My wifer",
        "Katerine ": "Morel"}
print(dict["Love Actually "])
dict["Katerine"] = "morel"
print(dict["Katerine"])

# Controll de flujos
# if
fv = "mkwmkm.net"
if fv == "tyshows.net":
    print("tienes buen gustos")
print(f"gracias")

# if else:
if fv == "tyshows":
    print("colorbas")
    print("Gracias")
else:
    print("yallas : tu")


# if elif else:
# if numbers < 0:
    #print ("negative number")
# elif numbers > 0:
    #print("Positive")
#else:
    #print("Cero")



# A if C else B

# var = "par" if (num % 2 == 0) else "impar"


# Bucles heres

edad = 0
while  edad < 18:
    edad = edad + 1
    print("""happy, have:  """, format(edad) + str(edad)) # you can added format(edad

while True: # false
    enter = input("Enter number:")
    if enter == "yes": # add salir
        salir = strue
        # break
    else:
        print(enter)

