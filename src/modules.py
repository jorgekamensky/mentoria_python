import json
import random

def connectar_banco():
    try:
        with open('dados/musicas.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_musica(musicas):
    with open('dados/musicas.json', 'w') as arquivo:
        json.dump(musicas, arquivo, indent=2)

def cadastrar_musica():
    print("\nCadastrar uma música:")
    titulo = input("Título: ")
    artista = input("Artista: ")
    ano = input("Ano Lançamento: ")
    musicas = connectar_banco()
    musicas.append({"titulo": titulo, "artista": artista, "ano": ano})
    salvar_musica(musicas)
    print("Música cadastrada")

def buscar_por_titulo(titulo):
    musicas = connectar_banco()
    resultado = [musica for musica in musicas if musica['titulo'].lower() == titulo.lower()]
    return resultado

def buscar_por_ano(ano):
    musicas = connectar_banco()
    resultado = [musica for musica in musicas if musica['ano'] == ano]
    return resultado

def playlist_aleatoria():
    musicas = connectar_banco()
    
    try:
        quantidade_musicas = int(input("Digite a quantidade de músicas desejadas na playlist: "))
    except ValueError:
        print("Por favor, insira um valor numérico válido.")
        return
    
    if quantidade_musicas <= 0:
        print("A quantidade de músicas deve ser maior que zero.")
        return

    playlist = random.sample(musicas, min(quantidade_musicas, len(musicas)))

    print(f"\n=== Playlist ===")
    for i, musica in enumerate(playlist, 1):
        print(f"{i}. {musica['titulo']} - {musica['artista']} ({musica['ano']})")

    with open('dados/playlist.json', 'w') as arquivo_playlist:
        json.dump({"playlist": playlist}, arquivo_playlist, indent=2)

    print(f"\nPlaylist com {quantidade_musicas} música(s) salva em 'playlist.json'.")

# def gerar_playlist_aleatoria():
#     musicas = connectar_banco()
#     try:
#         quantidade_musicas = int(input("Digite a quantidade de músicas desejadas na playlist: "))
#     except ValueError:
#         print("Por favor, insira um valor numérico válido.")
#         return
    
#     if quantidade_musicas <= 0:
#         print("A quantidade de músicas deve ser maior que zero.")
#         return

#     playlist = random.sample(musicas, min(quantidade_musicas, len(musicas)))

#     print(f"\n=== Playlist ===")
#     for i, musica in enumerate(playlist, 1):
#         print(f"{i}. {musica['titulo']} - {musica['artista']} ({musica['ano']})")