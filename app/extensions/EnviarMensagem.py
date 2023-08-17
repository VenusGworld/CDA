import os


class Mensagem:
    
    def enviarMensagem(self, mensagem: str, destino: str) -> bool:
        os.system(f"msg /server:{destino} * {mensagem}")

        return True