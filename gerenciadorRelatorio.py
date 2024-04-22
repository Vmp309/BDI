from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import *
from io import BytesIO

class GerenciadorRelatorio:
    @classmethod
    def gerar_relatorio_estoque(cls, data):
        
        caminho_arquivo = 'Relatório de Estoque de Livros.pdf'

        # Configure o buffer para armazenar o PDF
        buffer = BytesIO()

        # Crie o objeto PDF com o buffer
        pdf = canvas.Canvas(buffer,pagesize=letter)

        # Adicione o conteúdo ao PDF
        pdf.drawString(100, 800, "Relatório de Estoque de Livros")

        # Adicione as informações dos livros
        y = 750
        for livro in data:
            pdf.drawString(100, y, f"Título: {livro.titulo}")
            pdf.drawString(100, y - 20, f"Autor: {livro.autor}")
            pdf.drawString(100, y - 40, f"Quantidade em Estoque: {livro.quantidade}")
            pdf.drawString(100, y - 60, f"Preço do exemplar: {livro.preco}")
            pdf.drawString(100, y - 80, f"Sinopse: {livro.sinopse}")
            y -= 100

        # Salvando o PDF
        pdf.showPage()
        pdf.save()

                # Gravando o PDF no arquivo
        with open(caminho_arquivo, 'wb') as arquivo:
            arquivo.write(buffer.getvalue())


        # Coloque o buffer na posição 0 e retorne o PDF como uma resposta
        buffer.seek(0)
        return "Operação realizada!"