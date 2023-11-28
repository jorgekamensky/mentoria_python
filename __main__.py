from module.modules import *

if __name__ == "__main__":

    while True:
        print("\n=== Gerenciador de Músicas ===")
        print("1. Cadastrar uma música")
        print("2. Buscar por título")
        print("3. Buscar por ano de publicação")
        print("4. Playlist aleatória")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_musica()
        elif opcao == '2':
            titulo = input("Digite o título da música: ")
            resultados = buscar_por_titulo(titulo)
            print(resultados if resultados else "Nenhuma música encontrada.")
        elif opcao == '3':
            ano = input("Digite o ano de publicação: ")
            resultados = buscar_por_ano(ano)
            print(resultados if resultados else "Nenhuma música encontrada.")
        elif opcao == '4':
            playlist = gerar_playlist_aleatoria()
        elif opcao == '5':
            print("Encerrando")
            break
        else:
            print("Digite uma opçao válida")
