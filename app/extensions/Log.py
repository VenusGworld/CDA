import os
from datetime import datetime

class LogErro:

    def __init__(self) -> None:
        self.caminhoArq = ""

    def geraLogErro(self, excecao, erro, arquivoErro, linhaErro, link) -> None:
        self.verificaArquivoRecente(self.caminhoPasta())
        with open (f"{self.caminhoArq}", "a+") as txt:
            txt.write(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] - Erro: {excecao} {erro} - Arquivo: {arquivoErro} - Linha: {linhaErro} - URL: {link}\n\n")


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