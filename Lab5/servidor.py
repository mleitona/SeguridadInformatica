import socket



Clave_Publica_S = 33


mi_socket = socket.socket()
mi_socket.bind(('localhost',3000))
mi_socket.listen(5)

while True:
    conexion, addr  = mi_socket.accept()
    print("Nueva coneccion establecida! :D")
    print(addr)
    mensaje = conexion.encode("Hola, te saludo desde el servidor")
    
    conexion.send(mensaje)
    conexion.close()