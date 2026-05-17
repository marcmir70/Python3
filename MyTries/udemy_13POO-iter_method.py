#!/usr/bin/python3

# abre o browser, vai no Youtube, busca o vídeo da música e o reproduz
# chamada via Terminal : source venv/bin/activate
#             e então  : python MyTries/udemy_13POO-iter_method.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AutomacaoYoutube:
    def __init__(self):
        # O "Construtor" (150) inicializa o navegador Chrome
        # self.driver = webdriver.Chrome() 

        options = webdriver.ChromeOptions()
        
        # 1. Remove a mensagem "Chrome is being controlled..."
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        # 2. Desativa a flag de WebDriver para o site não saber que é um bot
        options.add_argument("--disable-blink-features=AutomationControlled")

        # 3. define tamanho da janela
        # options.add_argument("--start-maximized")
        options.add_argument("--window-size=1650,850")
        
        self.driver = webdriver.Chrome(options=options)

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
        time.sleep(3) # Espera o player carregar um pouco

        # Extraindo a duração total (em segundos) via JavaScript
        duracao_total = self.driver.execute_script(
            "return document.querySelector('#movie_player').getDuration()"
        )

        print(f"A música '{nome_musica}' tem {duracao_total} segundos.")

        # # Agora, em vez de um loop de 5 em 5 segundos, 
        # # podemos simplesmente esperar o tempo da música!
        # time.sleep(duracao_total)

        # um 'DISFARCE' aqui, se o YouTube se 'irritar' com pulos de vídeo
        print(f"Simulando interação humana para: {nome_musica} {duracao_total} seg")
        self.driver.execute_script("window.scrollTo(0, 10);")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 0);")        

        # # Mantém o browser aberto por um tempo para ouvir
        # print(f"Reproduzindo: {nome_musica}")
        # time.sleep(60) 

# Antes de entrar no loop, pegamos a URL do vídeo que clicamos
        url_original = self.driver.current_url

        # para esperar a música acabar:
        try:
            # Espera o player carregar
            time.sleep(5) 

            # Loop que verifica o status do vídeo a cada 5 segundos
            while True:
                # 1. verifica estado do player do YouTube
                # 0=acabou, 1=tocando, 2=pausado
                estado = self.driver.execute_script(
                    "return document.querySelector('#movie_player').getPlayerState()"
                )
                
                # 2. vê se URL mudou (Autoplay pulou pra outro vídeo)
                url_atual = self.driver.current_url
                
                # Se o estado for 'Fim' OU a URL mudou, encerramos esta música
                if estado == 0 or url_atual != url_original:
                    print(f"Fim detectado para: {nome_musica}")
                    break
                
                time.sleep(5) # Espera 5 segundos antes de perguntar de novo
        except Exception as e:
            print("Ocorreu um erro '{e}' ou o player foi fechado.")

# --- TESTANDO ---
if __name__ == '__main__':
    bot = AutomacaoYoutube()
    bot.buscar_e_tocar("Lynird Skynird Sweet Home Alabama")
    bot.buscar_e_tocar("Beat It Michael Jackson")
    bot.buscar_e_tocar("Take on Me A-ha")
    