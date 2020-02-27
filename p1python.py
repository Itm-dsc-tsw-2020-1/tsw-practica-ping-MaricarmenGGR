"""Maricarmen Guadalupe Gonzalez Rodriguez"""
"""Analisis de Conexion"""
import os
hostname = "www.itmorelia.edu.mx"
respuesta = os.system("ping "+ hostname)

if respuesta ==0 : print(hostname + " Está funcionando")
else:
    print (hostname+ ":No funciona")

"""Detectar computadoras activas"""    

import os
red = "200.33.171.0/24"
os.system("nmap -sn "+red)

"""Ciclo para detectar cuantas computadoras hay encendidas 2.0"""

import os
contador = 0
red = "200.33.171."
for i in range(254):
    i+=1
    respuesta = os.system("ping "+red+str(i))
    if respuesta ==0: print("HOST PRENDIDO"); contador+=1; print ("Numero de host prendidos al momento: "+ str(contador))
    else:
        if respuesta == 1: print("HOST APAGADO")

"""Detectar puertos abiertos"""
import os
computadora = "192.168.2.4"
os.system("nmap -sT "+ computadora) 

"""Detectar sistema operativo"""

import os
computadora = "192.168.2.4"
os.system("nmap -O "+ computadora)








