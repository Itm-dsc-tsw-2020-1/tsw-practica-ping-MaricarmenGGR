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


"""
RESULTADOS: 
    Prueba 1
    Haciendo ping a denebvirtual.itmorelia.edu.mx [200.33.171.77] con 32 bytes de datos:
Respuesta desde 200.33.171.77: bytes=32 tiempo=23ms TTL=63
Respuesta desde 200.33.171.77: bytes=32 tiempo=9ms TTL=63
Respuesta desde 200.33.171.77: bytes=32 tiempo=43ms TTL=63
Respuesta desde 200.33.171.77: bytes=32 tiempo=15ms TTL=63

Estadísticas de ping para 200.33.171.77:
    Paquetes: enviados = 4, recibidos = 4, perdidos = 0
    (0% perdidos),
Tiempos aproximados de ida y vuelta en milisegundos:
    Mínimo = 9ms, Máximo = 43ms, Media = 22ms
www.itmorelia.edu.mx Está funcionando

Prueba 2
Starting Nmap 7.80 ( https://nmap.org ) at 2020-02-27 12:22 Hora estßndar central (MÚxico)
Nmap scan report for delfin2.itmorelia.edu.mx (200.33.171.11)
Host is up (0.019s latency).
Nmap scan report for 200.33.171.13
Host is up (0.041s latency).
Nmap scan report for dsc.itmorelia.edu.mx (200.33.171.20)  
Host is up (0.031s latency).
Nmap scan report for libra.itmorelia.edu.mx (200.33.171.54)
Host is up (0.062s latency).
Nmap scan report for 200.33.171.60
Host is up (0.032s latency).
Nmap scan report for 200.33.171.66
Host is up (0.0020s latency).
Nmap scan report for denebvirtual.itmorelia.edu.mx (200.33.171.77)
Host is up (0.0030s latency).
Nmap scan report for sappp.itmorelia.edu.mx (200.33.171.80)       
Host is up (0.024s latency).
Nmap scan report for vinculacion.itmorelia.edu.mx (200.33.171.124)
Host is up (0.031s latency).
Nmap scan report for 200.33.171.125
Host is up (0.071s latency).
Nmap scan report for 200.33.171.127
Host is up (0.070s latency).
Nmap done: 256 IP addresses (11 hosts up) scanned in 18.87 seconds

Prueba 3

Starting Nmap 7.80 ( https://nmap.org ) at 2020-02-27 12:24 Hora estßndar central (MÚxico)
Nmap scan report for denebvirtual.itmorelia.edu.mx (200.33.171.77)
Host is up (0.0076s latency).
Not shown: 989 filtered ports
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
25/tcp   open  smtp
80/tcp   open  http
110/tcp  open  pop3
119/tcp  open  nntp
143/tcp  open  imap
443/tcp  open  https
2000/tcp open  cisco-sccp
5060/tcp open  sip
8008/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 50.57 seconds

Prueba 4
Starting Nmap 7.80 ( https://nmap.org ) at 2020-02-27 12:27 Hora estßndar central (MÚxico)
Nmap scan report for 200.33.171.77
Host is up (0.0099s latency).
Not shown: 989 closed ports
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
25/tcp   open  smtp
80/tcp   open  http
110/tcp  open  pop3
119/tcp  open  nntp
143/tcp  open  imap
443/tcp  open  https
2000/tcp open  cisco-sccp
5060/tcp open  sip
8008/tcp open  http
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.80%E=4%D=2/27%OT=21%CT=1%CU=36892%PV=N%DS=2%DC=I%G=Y%TM=5E580A6
OS:0%P=i686-pc-windows-windows)SEQ(SP=100%GCD=1%ISR=10A%TI=BI%II=I%SS=O%TS=
OS:7)SEQ(SP=100%GCD=1%ISR=10A%TI=RD%II=I%TS=9)SEQ(II=I)OPS(O1=M5B4ST11NWD%O
OS:2=M5B4ST11NWD%O3=M5B4NNT11NWD%O4=M5B4ST11NWD%O5=M5B4ST11NWD%O6=M5B4ST11)
OS:WIN(W1=A9B0%W2=A9B0%W3=A9B0%W4=A9B0%W5=A9B0%W6=3890)ECN(R=Y%DF=Y%T=40%W=
OS:A564%O=M5B4NNSNWD%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)
OS:T3(R=N)T4(R=N)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=N)T7(R=
OS:N)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y
OS:%DFI=N%T=40%CD=S)IE(R=N)

Network Distance: 2 hops

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 57.58 seconds

Probando el CICLO

Haciendo ping a 10.27.146.1 con 32 bytes de datos:
Respuesta desde 10.27.146.1: bytes=32 tiempo=4ms TTL=255
Respuesta desde 10.27.146.1: bytes=32 tiempo=2ms TTL=255
Respuesta desde 10.27.146.1: bytes=32 tiempo=7ms TTL=255
Respuesta desde 10.27.146.1: bytes=32 tiempo=9ms TTL=255

Estadísticas de ping para 10.27.146.1:
    Paquetes: enviados = 4, recibidos = 4, perdidos = 0
    (0% perdidos),
Tiempos aproximados de ida y vuelta en milisegundos:
    Mínimo = 2ms, Máximo = 9ms, Media = 5ms
HOST PRENDIDO
Numero de host prendidos al momento: 1

Haciendo ping a 10.27.146.2 con 32 bytes de datos:
Respuesta desde 10.27.146.2: bytes=32 tiempo=353ms TTL=128
Respuesta desde 10.27.146.2: bytes=32 tiempo=7ms TTL=128
Respuesta desde 10.27.146.2: bytes=32 tiempo=4ms TTL=128
Respuesta desde 10.27.146.2: bytes=32 tiempo=2ms TTL=128

Estadísticas de ping para 10.27.146.2:
    Paquetes: enviados = 4, recibidos = 4, perdidos = 0
    (0% perdidos),
Tiempos aproximados de ida y vuelta en milisegundos:
    Mínimo = 2ms, Máximo = 353ms, Media = 91ms
HOST PRENDIDO
Numero de host prendidos al momento: 2

Haciendo ping a 10.27.146.3 con 32 bytes de datos:
Respuesta desde 10.27.146.29: Host de destino inaccesible.
Respuesta desde 10.27.146.29: Host de destino inaccesible.
Respuesta desde 10.27.146.29: Host de destino inaccesible.
Respuesta desde 10.27.146.29: Host de destino inaccesible.

Estadísticas de ping para 10.27.146.3:
    Paquetes: enviados = 4, recibidos = 4, perdidos = 0
    (0% perdidos),
HOST PRENDIDO
Numero de host prendidos al momento: 3

Haciendo ping a 10.27.146.4 con 32 bytes de datos:
Respuesta desde 10.27.146.4: bytes=32 tiempo=68ms TTL=64
Respuesta desde 10.27.146.4: bytes=32 tiempo=4ms TTL=64
Respuesta desde 10.27.146.4: bytes=32 tiempo=6ms TTL=64
Respuesta desde 10.27.146.4: bytes=32 tiempo=5ms TTL=64

Estadísticas de ping para 10.27.146.4:
    Paquetes: enviados = 4, recibidos = 4, perdidos = 0
    (0% perdidos),
Tiempos aproximados de ida y vuelta en milisegundos:
    Mínimo = 4ms, Máximo = 68ms, Media = 20ms
HOST PRENDIDO
Numero de host prendidos al momento: 4

Haciendo ping a 10.27.146.5 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 10.27.146.5:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
HOST APAGADO

Haciendo ping a 10.27.146.6 con 32 bytes de datos:
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.
Tiempo de espera agotado para esta solicitud.

Estadísticas de ping para 10.27.146.6:
    Paquetes: enviados = 4, recibidos = 0, perdidos = 4
    (100% perdidos),
HOST APAGADO

Haciendo ping a 10.27.146.7 con 32 bytes de datos:
Respuesta desde 10.27.146.7: bytes=32 tiempo=164ms TTL=64
Respuesta desde 10.27.146.7: bytes=32 tiempo=5ms TTL=64
Respuesta desde 10.27.146.7: bytes=32 tiempo=2ms TTL=64
Respuesta desde 10.27.146.7: bytes=32 tiempo=7ms TTL=64

Estadísticas de ping para 10.27.146.7:
    Paquetes: enviados = 4, recibidos = 4, perdidos = 0
    (0% perdidos),
Tiempos aproximados de ida y vuelta en milisegundos:
    Mínimo = 2ms, Máximo = 164ms, Media = 44ms
HOST PRENDIDO
Numero de host prendidos al momento: 5

Haciendo ping a 10.27.146.8 con 32 bytes de datos:
Respuesta desde 10.27.146.29: Host de destino inaccesible.
Respuesta desde 10.27.146.29: Host de destino inaccesible.
Respuesta desde 10.27.146.29: Host de destino inaccesible.
Respuesta desde 10.27.146.29: Host de destino inaccesible.

Estadísticas de ping para 10.27.146.8:
    Paquetes: enviados = 4, recibidos = 4, perdidos = 0
    (0% perdidos),
HOST PRENDIDO
Numero de host prendidos al momento: 6

"""








