import Crypto
from Crypto.PublicKey import RSA
import ast

keyPair = RSA.generate(1024)

pubKey = keyPair.publickey()
d
encryptedMsg = pubKey.encrypt(b'This is my secret msg', 32)
decryptedMsg = keyPair.decrypt(ast.literal_eval(str(encryptedMsg)))

print('Decrypted message:', decryptedMsg)

    





    
    