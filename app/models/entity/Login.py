
"""
Classe Login
@author - Fabio
@version - 1.0
@since - 25/04/2023
"""

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