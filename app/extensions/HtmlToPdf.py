import pdfkit
import os

class PdfKit:

    def __init__(self) -> None:
        pastaProjeto = os.getcwd()
        self.pastaWkthmltopdf = f"{pastaProjeto}/app/extensions/wkhtmltopdf/bin/wkhtmltopdf.exe"
        self.config = pdfkit.configuration(wkhtmltopdf = self.pastaWkthmltopdf)
        self.listaCss = []
        self.options = {
            'page-size': 'A4',
            'orientation': 'Landscape',  # Altere para 'Portrait' se desejar retrato
        }


    def fromString(self, string: str, css: list) -> pdfkit:
        print(self.pastaWkthmltopdf)
        self.adicionaPastaCss(css)
        return pdfkit.from_string(string, css=self.listaCss, configuration=self.config, verbose=True, options=self.options)
    

    def adicionaPastaCss(self, listaCss: list) -> None:
        for css in listaCss:
            self.listaCss.append(f"{os.getcwd()}/app{css}")