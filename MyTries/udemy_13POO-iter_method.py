#!/usr/bin/python3

# (tópico 155) Método __iter__ : Permite que seu objeto seja "iterável", 
# ou seja, que você possa usar um for nele.
# Exemplo: classe Playlist que, ao ser colocada num for, 
#          percorre as músicas nela contidas.

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self._musicas = [] # Lista interna que guarda os dados

    def adicionar_musica(self, musica):
        self._musicas.append(musica)

    # O CORAÇÃO DO TÓPICO 155:
    def __iter__(self):
        # Nós "pedimos emprestado" o iterador da nossa lista interna.
        # Isso diz ao Python: "Quando alguém me usar num for, percorra self._musicas"
        return iter(self._musicas)

# --- TESTANDO ---
if __name__ == '__main__':
    minha_playlist = Playlist("Rock Anos 80")
    minha_playlist.adicionar_musica("Beat It - Michael Jackson")
    minha_playlist.adicionar_musica("Take on Me - A-ha")
    minha_playlist.adicionar_musica("Under Pressure - Queen")

    print(f"Tocando a playlist: {minha_playlist.nome}\n")

    # A MÁGICA: Percorremos o OBJETO diretamente, não a lista interna!
    for musica in minha_playlist:
        print(f"-> {musica}")