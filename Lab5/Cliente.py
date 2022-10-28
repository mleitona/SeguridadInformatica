import socket
import Cliente


mi_socket = socket.socket()
mi_socket.connect(('localhost',3000))
mensaje = mi_socket.encode("Hola desde el cliente!")

mi_socket.send(mensaje)




mi_socket.close()
