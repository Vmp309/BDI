import psycopg2
from  gerenciadorEstoque import GerenciadorEstoque
from livro import Livro
from gerenciadorRelatorio import GerenciadorRelatorio

if __name__ == "__main__":
    conexao = psycopg2.connect(
        database="bookProject",
        user="augusto",
        password="1234",
        host="localhost"
    )

    gerenciador = GerenciadorEstoque(conexao)
    gerador_relatorio = GerenciadorRelatorio()

    while True:
        print("\nOpções:")
        print("1 - Adicionar livro")
        print("2 - Buscar livro por título")
        print("3 - Listar todos os livros")
        print("4 - Excluir livro por titulo")
        print("5 - Editar livro")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            quantidade = int(input("Digite a quantidade de exemplares: "))
            preco = float(input("Digite o preço do exemplar:"))
            sinopse = input("Inclua a sinopse do livro: ")
            livro = Livro(titulo, autor, quantidade, preco, sinopse)
            gerenciador.adicionar_livro(livro)
            print("Livro adicionado com sucesso!")

        elif opcao == "2":
            titulo = input("Digite o título do livro a ser buscado: ")
            livro = gerenciador.buscar_livro(titulo)
            if livro:
                print(f"Encontrado: {livro.titulo} de {livro.autor}, Quantidade: {livro.quantidade}, Preço: {livro.preco},\n Sinopse: {livro.sinopse}")
            else:
                print("Livro não encontrado.")

        elif opcao == "3":
            livros = gerenciador.listar_livros()
            if livros:
                print("\nLista de Livros:")
                for livro in livros:
                    print(f"{livro.titulo} de {livro.autor}, Quantidade: {livro.quantidade}, Preço: {livro.preco},\n Sinopse: {livro.sinopse}")
            else:
                print("Nenhum livro cadastrado.")

        elif opcao == "4":
            titulo = input("Digite o título do livro a ser excluído: ")
            gerenciador.excluir_livro(titulo)

        elif opcao == "5":
           titulo_livro = input("Digite o titulo do livro a ser alterado: ")

           while True:
            print("\nO que você deseja alterar?")
            print("1 - Título do Livro")
            print("2 - Autor do Livro")
            print("3 - Quantidade em Estoque")
            print("4 - Preço do Livro")
            print("5 - Sinopse do Livro")
            print("6 - Editar tudo Livro")
            print("7 - Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                novo_titulo = input("Digite o novo titulo do livro: ")
                gerenciador.editar_titulo(titulo=titulo_livro, novo_titulo=novo_titulo)

            elif opcao == "2":
                novo_autor = input("Digite o novo autor do livro: ")
                gerenciador.editar_autor(titulo=titulo_livro, novo_autor=novo_autor)

            elif opcao == "3":
                nova_quantidade = input("Digite a nova quantidade: ")
                gerenciador.editar_quantidade(titulo=titulo_livro,nova_quantidade=nova_quantidade)

            elif opcao == "4":
                novo_preco = input("Digite o novo preço: ")
                gerenciador.editar_preco(titulo=titulo_livro, novo_preco=novo_preco)

            elif opcao == "5":
                nova_sinopse = input("Digite a nova sinopse: ")
                gerenciador.editar_sinopse(titulo=titulo_livro, nova_sinopse=nova_sinopse)

            elif opcao == "6":
                novo_titulo = input("Digite o novo titulo do livro: ")
                novo_autor = input("Digite o novo autor do livro: ")
                nova_quantidade = input("Digite a nova quantidade: ")
                novo_preco = input("Digite o novo preço: ")
                nova_sinopse = input("Digite a nova sinopse: ")
                gerenciador.editar_autor(titulo=titulo_livro, novo_autor=novo_autor)
                gerenciador.editar_quantidade(titulo=titulo_livro, nova_quantidade=nova_quantidade)
                gerenciador.editar_preco(titulo=titulo_livro, novo_preco=novo_preco)
                gerenciador.editar_sinopse(titulo=titulo_livro, nova_sinopse=nova_sinopse)
                gerenciador.editar_titulo(titulo=titulo_livro, novo_titulo=novo_titulo)

            elif opcao == "7":
                break

        elif opcao == "6":
            conexao.close()
            break

        else:
            print("Opção inválida. Tente novamente.")
