from datetime import datetime
import os


class LogErro:
    """
    Classe para funções relacionadas ao gerar logs de erros no sistema
    @author - Fabio
    @version - 1.0
    @since - 22/06/2023
    """

    def __init__(self) -> None:
        self.caminhoArq = ""


    def geraLogErro(self, excecao, erro, listaErro, link) -> None:
        self.verificaArquivoRecente(self.caminhoPasta())
        with open (f"{self.caminhoArq}", "a+") as txt:
            txt.write(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}]\nErro: {excecao} {erro}")
            for erro in listaErro:
                txt.write(f"\nArquivo: {erro[0]} - Linha: {erro[1]} '{erro[3]}'")
            txt.write(f"\nURL: {link}\n\n\n\n")
            

    def caminhoPasta(self) -> str:
        caminho = os.path.dirname(os.path.realpath(__name__))
        caminho = f"{caminho}\\app\\log\\"
        return caminho
    
    
    def caminhoArquivo(self, numlog) -> None:
        self.caminhoArq = f"{self.caminhoPasta()}\\logErro_{numlog}.log"


    def verificaTamanhoArq(self, caminho: str, arquivo: str) -> None:
        try:
            tamanhoBytes = os.path.getsize(f"{caminho}\\{arquivo}")
            tamanhoMegaBytes = tamanhoBytes / (1024 * 1024)
            posicao1 = arquivo.find("_")
            posicao2 = arquivo.find(".")
            if tamanhoMegaBytes >= 5:
                numLog = int(arquivo[posicao1+1:posicao2])
                numLog += 1
                self.caminhoArquivo(numLog)
            else:
                self.caminhoArquivo(int(arquivo[posicao1+1:posicao2]))
            
        except FileNotFoundError:
            self.caminhoArquivo(0)


    def verificaArquivoRecente(self, caminho: str) -> None:
        arquivos = os.listdir(caminho)
        arquivoMaisRecente = ""
        dataModificacaoRecente = 0.0
        if len(arquivos) != 0:
            for arquivo in arquivos:
                caminho_completo = os.path.join(caminho, arquivo)
                if os.path.isfile(caminho_completo):  # Verifica se é um arquivo (ignora pastas)
                    dataModificacao = os.path.getmtime(caminho_completo)
                    if dataModificacao > dataModificacaoRecente:
                        dataModificacaoRecente = dataModificacao
                        arquivoMaisRecente = arquivo
        else:
            arquivoMaisRecente = "LogErro_0.log"

        self.verificaTamanhoArq(caminho, arquivoMaisRecente)