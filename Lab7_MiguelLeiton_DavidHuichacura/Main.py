

import socket
import cliente


mi_socket = socket.socket()
mi_socket.connect(('localhost',3000))
mensaje = mi_socket.encode("Hola desde el cliente!")

mi_socket.send(mensaje)


mi_socket.close()

class rsa(object):
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None
        
    def generate_partial_key(self):
        partial_key = self.public_key1**self.private_key
        partial_key = partial_key%self.public_key2
        return partial_key
    
    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r**self.private_key
        full_key = full_key%self.public_key2
        self.full_key = full_key
        return full_key

    ############################################################################################################################ 
def Main():
    ############################################################## 

    c_public=33
    c_private=43
    Cliente = rsa(c_public, s_public, c_private)

    ############################################################

    s_public=73
    s_private=67
    Servidor = rsa(c_public, s_public, s_private)
    ###################################### (k)
    c_partial=Cliente.generate_partial_key()
    s_partial=Servidor.generate_partial_key()
    ################################################ (clave como tal)
    c_full=Cliente.generate_full_key(c_partial)
    s_full=Servidor.generate_full_key(s_partial)
    
    if c_full==s_full:
        archivo = open("mensajeentrada.txt","r")
        mensaje = str(archivo.readline().lower())
        codigo =  ds.encriptacion(mensaje)
        archivo.close()

    file = open("mensajerecibido.txt","w")
    desco = ds.desencriptacion(codigo)
    file.write(str(desco))
    file.close()
Main()