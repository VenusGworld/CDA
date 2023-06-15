
#Classe de login do sistema
class Login:
    def __init__(self, user, pssd):
        self.user = user
        self.pssd = pssd
        
    def get_user(self):
        return self.user
    
    def get_pssd(self):
        return self.pssd
    
    def set_user(self, user):
        self.user = user
        
    def set_pssd(self, pssd):
        self.pssd = pssd