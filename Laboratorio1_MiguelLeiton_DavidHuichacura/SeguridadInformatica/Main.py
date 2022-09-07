#Miguel Leiton
#David Huichacura
import Rot
import vinegere
import requests

def cifrado(clave,mensaje):
    print("va")
    defi=Rot.codifica(mensaje,8)
    defini=vinegere.cifrar(clave,defi)
    definite=Rot.codifica(defini,12)
    print('Mensaje cifrado: ',definite)
    return(definite)
def descifrado(clave,mensaje):
    defi=Rot.decodifica(mensaje,-12)
    defini=vinegere.descifrar(clave,defi)
    definite=Rot.decodifica(defini,-8)
    print('Mensaje descifrado: ',definite)
    return(definite)

Mensaje = input("Introdusca un mensaje: ")
Mensaje = Mensaje  #Transforma mensaje a minuscula 
clave1 = "heropassword"
print("Desafio 1")
v = cifrado(clave1,Mensaje)
descifrado(clave1,v)
headers = {
    'Content-Type': 'text/plain',
}
mensajeprueba = cifrado(clave1,Mensaje)

data = '{"msg":"mensajeprueba"}'

response1 = requests.post('https://finis.mmae.cl/SendMsg', headers=headers, data=data)




##########################################################################33333
print("desafio 2")
clave2 = "finispasswd"
headers = {
    'Content-Type': 'text/plain',
}

response = requests.get('https://finis.mmae.cl/GetMsg', headers=headers)
response = response.json()
mensaje_decifrar = response["msg"]

mensaje_desifrado = descifrado(clave2,mensaje_decifrar)
print(mensaje_desifrado)




