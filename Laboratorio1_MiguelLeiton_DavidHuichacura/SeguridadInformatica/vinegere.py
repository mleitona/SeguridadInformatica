alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_m = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cifrar(clave,cadena):
    texto = ""
    x = 0
    for letra in cadena:
        if letra.isupper() == True: #mayuscula
            suma = alfabeto_m.find(letra)+alfabeto_m.find(clave[x%len(clave)])
            modulo = int(suma)%len(alfabeto_m)
            texto += str(alfabeto_m[modulo])
        else:
            suma = alfabeto.find(letra)+alfabeto.find(clave[x%len(clave)])
            modulo = int(suma)%len(alfabeto)
            texto += str(alfabeto[modulo])
        
        x +=1
    return texto
def descifrar(clave,cadena):
    texto = ""
    x = 0
    for letra in cadena:
        if letra.isupper() == True: #mayuscula
            suma = alfabeto_m.find(letra)-alfabeto_m.find(clave[x%len(clave)])
            modulo = int(suma)%len(alfabeto_m)
            texto += str(alfabeto_m[modulo])
        else:
            suma = alfabeto.find(letra)-alfabeto.find(clave[x%len(clave)])
            modulo = int(suma)%len(alfabeto)
            texto += str(alfabeto[modulo])
        
        x +=1
    return texto
# def Traduce(Clave,mensaje,accion):
#     Mensaje_Traducido = []
#     in
