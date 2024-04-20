from .livro import Livro
from .gerenciadorEstoque import GerenciadorEstoque

from gerenciadorRelatorio import GerenciadorRelatorio

class GerenciadorLivros:

    def __init__(cls):
        estoque = GerenciadorEstoque()


    @classmethod
    def listar_livros(cls):
        return cls.estoque.listar_livros()

    @classmethod
    def criar_livro(cls, titulo, autor, quantidade_em_estoque):
        livro = Livro(titulo=titulo, autor=autor, quantidade_em_estoque=quantidade_em_estoque)
        cls.estoque.adicionar_livro(livro)
        return livro

    @classmethod
    def obter_livro(cls, titulo):
        return cls.estoque.achar_livro(titulo)

    @classmethod
    def atualizar_quantidade_livro(cls, titulo, quantidade):
        return cls.estoque.atualizar_quantidade(titulo, quantidade) 

    @classmethod
    def deletar_livro(cls, titulo):
        cls.estoque.excluir_livro(titulo)
    
    @classmethod
    def gerar_relatorio(cls):
        livros = cls.estoque.listar_livros()   
        GerenciadorRelatorio.gerar_relatorio_estoque(livros)
    
    @classmethod
    def encerrar_gerenciador(cls):
        cls.estoque.fechar_conexao()