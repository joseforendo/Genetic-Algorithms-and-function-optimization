import random
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

def decimal_a_binario(decimal):
    if decimal <= 0:
        return int("0")
    binario = ""
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
    return int(binario)

def convertir_a_lista(numero):
    num = decimal_a_binario(numero)
    digit_num = str(num)
    digit_map = map(int,digit_num)
    digit_list = list(digit_map)
    while len(digit_list)<5:
        digit_list.insert(0,0)
    return digit_list

def valor_decimal(lst):
    valor = 0
    for i in range(len(lst)):
        if lst[i] !=0:
            valor = 2**(len(lst)-1-i) + valor
    return valor

def split(lst, cruce):
    first_half = lst[:cruce]
    second_half = lst[cruce:]
    return first_half, second_half

def Idoneidad(lst):
    x = valor_decimal(lst)
    return abs((x-5)/(2+math.sin(x)))

def f(x):
    return abs((x-5)/(2+math.sin(x)))

def Inicializacion(N):
    print("Inicializacion:")
    global Individuos
    global Mejor
    Individuos = {}
    
    for i in range(N):
        aleatorio = random.randint(0,30)
        aleatorio = convertir_a_lista(aleatorio)
        Individuos[i]=aleatorio
    
    for i in range(N):
        print(Individuos[i], ", f(x) = ", Idoneidad(Individuos[i]))

def Parejas(N):
    aleatorio = random.sample(range(int(N/2),N),int(N/2))
    Pareja = {}
    for i in range(int(N/2)):
        Pareja[i]=aleatorio[i]
        Pareja[aleatorio[i]]=i
    return Pareja

def Seleccion(N):
    print("Seleccion")
    Pareja = Parejas(N)
    print('Parejas', Pareja)
    for k, v in Pareja.items():
        if Idoneidad(Individuos[k]) >= Idoneidad(Individuos[v]):
            Individuos[v] = Individuos[k]
    for i in range(N):
        print(Individuos[i], ", f(x) = ", Idoneidad(Individuos[i]))

def Cruce(N):
    print("Cruce")
    Pareja = Parejas(N)
    print("Parejas", Pareja)
    item = 0
    for k, v in Pareja.items():
        if item%2==0:
            punto = random.randint(0,N-2)
            print("Punto de cruce: ", punto)
            gen1_f_half, gen1_s_half = split(Individuos[k], punto)
            gen2_f_half, gen2_s_half = split(Individuos[v], punto)
            mutacion1 = gen1_f_half + gen2_s_half
            mutacion2 = gen2_f_half + gen1_s_half
            Individuos[k]=mutacion1
            Individuos[v]=mutacion2
        item = item + 1
    for i in range(N):
        print(Individuos[i], ", f(x) = ", Idoneidad(Individuos[i]))

def Mutacion(N):
    print("Mutacion")
    for i in range(int(N/2)):
        ElegirI = random.randint(0,N-1)
        print(ElegirI, "Individuo")
        ElegirPos = random.randint(0,N-2)
        print(ElegirPos, "Cual de los elementos")
        ElegirGen = random.randint(1,N-1)
        print(ElegirGen, "Con qué elemento")
        Individuos[ElegirI][ElegirPos]=ElegirGen
        print("****")
    for i in range(N):
        print(Individuos[i], ", f(x) = ", Idoneidad(Individuos[i]))

def run():
    Inicializacion(N)
    Seleccion(N)
    Cruce(N)
    Mutacion(N)
    
run()
