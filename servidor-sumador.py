#Laura Sanz Ruano G.ITT

#! /usr/bin/python
# -*- coding: utf-8 -*-

import socket

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Nos libera automaticamente el puerto para poder reutilizarlo
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

numero = None

try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        Puerto = address[1]
        peticion = recvSocket.recv(1024)
    try:
        numero = int(peticion.split(' ')[1][1:])
        if (numero == None):
            print "Necesito otro numero"
        else :
            numero2 = int(peticion.split(' ')[1][1:])
            suma = numero + numero2
            html += "<p> La suma de tus numeros es: " + str(suma) + "</p>"          
            html+= "</body></html>"
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                       html +
                       "\r\n")

        recvSocket.close()
    except ValueError:
        print "Introduzca un numero"
        recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" + "<html><body><h1>Introduzca un numero</h1></body></html>" + "\r\n")
except KeyboardInterrupt:
    print "Servidor interrumpido"
    mySocket.close()
