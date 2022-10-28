import servidor
import Cliente


class DH_Endpoint(object):
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
    




    
message="This is a very secret message!!!"
s_public=197
s_private=199
m_public=151
Sadat = DH_Endpoint(s_public, m_public, s_private)
Michael = DH_Endpoint(s_public, m_public, m_private)
    
    

