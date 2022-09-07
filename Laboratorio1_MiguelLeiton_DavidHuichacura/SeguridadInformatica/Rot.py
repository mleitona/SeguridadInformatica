alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_m = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def codifica(Mensaje,rotacion):
    cifrado = ""
    for c in Mensaje:
         if c.isupper() == True:
            if c in alfabeto:
                cifrado += alfabeto_m[(alfabeto_m.index(c)+rotacion)%(len(alfabeto_m))]
            else:
                cifrado+=c
         else:
             if c in alfabeto:
                cifrado += alfabeto[(alfabeto.index(c)+rotacion)%(len(alfabeto))]
             else:
                cifrado+=c

    return cifrado        
def decodifica(Mensaje,rotacion):
    cifrado = ""
    for c in Mensaje:
         if c.isupper() == True:
            if c in alfabeto:
                cifrado += alfabeto_m[(alfabeto_m.index(c)+rotacion)%(len(alfabeto_m))]
            else:
                cifrado+=c
         else:
             if c in alfabeto:
                cifrado += alfabeto[(alfabeto.index(c)+rotacion)%(len(alfabeto))]
             else:
                cifrado+=c

    return cifrado  