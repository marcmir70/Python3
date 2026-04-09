#!/usr/bin/python3

# abre o browser, vai no Youtube, busca o vídeo da música e o reproduz
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AutomacaoYoutube:
    def __init__(self):
        # O "Construtor" (150) inicializa o navegador Chrome
        self.driver = webdriver.Chrome() 

    def buscar_e_tocar(self, nome_musica):
        # 1. Navega até o site
        self.driver.get("https://www.youtube.com")
        time.sleep(2) # Espera carregar

        # 2. Encontra a barra de busca pelo nome da tag HTML
        busca = self.driver.find_element(By.NAME, "search_query")
        
        # 3. Digita o nome da música e aperta ENTER
        busca.send_keys(nome_musica)
        busca.send_keys(Keys.ENTER)
        time.sleep(2)

        # 4. Clica no primeiro vídeo da lista de resultados
        primeiro_video = self.driver.find_element(By.ID, "video-title")
        primeiro_video.click()

        # # Mantém o browser aberto por um tempo para ouvir
        # print(f"Reproduzindo: {nome_musica}")
        # time.sleep(60) 

        # Mágica para esperar a música acabar:
        try:
            # Esperamos o player carregar
            time.sleep(5) 
            
            # Loop que verifica o status do vídeo a cada 5 segundos
            while True:
                # Script que pergunta ao player do YouTube o seu estado
                # 0 = acabou, 1 = tocando, 2 = pausado
                estado = self.driver.execute_script(
                    "return document.querySelector('#movie_player').getPlayerState()"
                )
                
                if estado == 0: # 0 significa 'Ended' (Terminou)
                    print(f"Fim de: {nome_musica}")
                    break
                
                time.sleep(5) # Espera 5 segundos antes de perguntar de novo
        except Exception as e:
            print("Ocorreu um erro ou o player foi fechado.")

# --- TESTANDO ---
if __name__ == '__main__':
    bot = AutomacaoYoutube()
    bot.buscar_e_tocar("Lynird Skynird Sweet Home Alabama")
    bot.buscar_e_tocar("Beat It Michael Jackson")
    bot.buscar_e_tocar("Take on Me A-ha")
    