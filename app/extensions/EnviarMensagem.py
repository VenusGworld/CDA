import os


class Mensagem:
    """
    Classe para funções relacionadas ao enviar Mensagem
    @author - Fabio
    @version - 1.0
    @since - 15/08/2023
    """
    
    def enviarMensagem(self, mensagem: str, destino: str) -> bool:
        """
        Esta função envia mensagen para uma máquina espesifica na rede ineterna através serviço de mensageria do windows

        :param mensagem: A mesnagem que será enviada ao destinário.
        :param destino: O nome da máquina que será o destinário da mensagem (Ex: MOR-TI-01).

        :return: True se o envio de mensagem for bem-sucedido, False caso contrário.
        """

        os.system(f"msg /server:{destino} * {mensagem}")

        return True