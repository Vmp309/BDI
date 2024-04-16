from psycopg2 import sql
from livro import Livro

class GerenciadorEstoque:
    def __init__(self, conexao):
        self.conexao = conexao

    def adicionar_livro(self, livro):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO estoque (titulo, autor, quantidade, preco, sinopse) VALUES (%s, %s, %s, %s, %s)",
                       (livro.titulo, livro.autor, livro.quantidade, livro.preco, livro.sinopse))
        self.conexao.commit()
        cursor.close()

    def buscar_livro(self, titulo):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM estoque WHERE titulo = %s", (titulo,))
        livro = cursor.fetchone()
        cursor.close()
        if livro:
            return Livro(livro[0], livro[1], livro[2], livro[3], livro[4])
        else:
            return None

    def listar_livros(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM estoque")
        livros = []
        for row in cursor.fetchall():
            livros.append(Livro(row[0], row[1], row[2], row[3], row[4]))
        cursor.close()
        return livros
    
    def excluir_livro(self, titulo):
        cursor = self.conexao.cursor()
        sql = "DELETE FROM estoque WHERE titulo = %s"
        values = (titulo,)
        cursor.execute(sql, values)
        self.conexao.commit()
        cursor.close()

    def editar_titulo(self, titulo, novo_titulo):
        cursor = self.conexao.cursor()
        sql = "UPDATE estoque SET titulo = %s WHERE titulo = %s"
        values = (novo_titulo, titulo)
        cursor.execute(sql, values)
        self.conexao.commit()
        cursor.close()

    def editar_autor(self, titulo, novo_autor):
        cursor = self.conexao.cursor()
        sql = "UPDATE estoque SET autor = %s WHERE titulo = %s"
        values = (novo_autor, titulo)
        cursor.execute(sql, values)
        self.conexao.commit()
        cursor.close()

    def editar_preco(self, titulo, novo_preco):
        cursor = self.conexao.cursor()
        sql = "UPDATE estoque SET preco = %s WHERE titulo = %s"
        values = (novo_preco, titulo)
        cursor.execute(sql, values)
        self.conexao.commit()
        cursor.close()

    def editar_quantidade(self, titulo, nova_quantidade):
        cursor = self.conexao.cursor()
        sql = "UPDATE estoque SET quantidade = %s WHERE titulo = %s"
        values = (nova_quantidade, titulo)
        cursor.execute(sql, values)
        self.conexao.commit()
        cursor.close()

    def editar_sinopse(self, titulo, nova_sinopse):
        cursor = self.conexao.cursor()
        sql = "UPDATE estoque SET sinopse = %s WHERE titulo = %s"
        values = (nova_sinopse, titulo)
        cursor.execute(sql, values)
        self.conexao.commit()
        cursor.close()