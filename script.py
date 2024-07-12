import pyautogui as pa
import time
import pyperclip

pa.PAUSE = 1

pa.hotkey('win', 'r')
time.sleep(1)
# entra no navegador
pa.write("chrome")
pa.press('ENTER')
time.sleep(1)
pa.click(x=826, y=403)
time.sleep(1)

list_search = [
    "Unidas",
    "tim",
    "Mercado Pago",
    "Carrefour",
    "Coren",
    "Leonardo Rodrigues",
    "Uber",
    "Santander",
    "Spotify",
    "Porto Seguro",
    "Assessoria",
    "Zul Digital",
    "Riachuelo",
    "Dropbox",
    "Anatel"]


def execute():
    try:
        # Laço para verificar e clicar no botão de exclusão enquanto estiver presente
        while True:

            box = pa.locateCenterOnScreen('selecionar.png', confidence=0.7)

            pa.click(box)  # Selecionar
            time.sleep(0.3)

            button = pa.locateCenterOnScreen('button_excluir.png', confidence=0.7)

            if button is None:
                break

            pa.click(button)  # Lixeira
            time.sleep(0.7)

    except pa.ImageNotFoundException:
        print("Imagem 'button_excluir.png' não encontrada na tela.")
        time.sleep(0.5)


for serach in list_search:
    # seleciona barra de pesquisa e insere pesquisa
    pa.click(x=345, y=119)
    pa.hotkey('ctrl', 'a')
    pa.hotkey('ctrl', 'x')
    pyperclip.copy(f"{serach}")
    pa.hotkey('ctrl', 'v')
    pa.press('ENTER')
    time.sleep(1)

    execute()

# try:
#     # LIMPANDO LIXEIRA
#     while True:
#
#         pa.click(x=76, y=403)  # Mais
#         pa.click(x=88, y=597)  # Lixeira Icon
#         pa.click(x=301, y=226)  # Selecionar
#         pa.click(x=350, y=361)  # Tipo
#         time.sleep(0.3)
#
#         button = pa.locateCenterOnScreen('button_excluir.png', confidence=0.7)
#
#         if button is None:
#             break
#
#         pa.click(x=395, y=229)
#         time.sleep(0.7)
#
# except pa.ImageNotFoundException:
#     print("Imagem 'button_excluir.png' não encontrada na tela LIXEIRA.")
#     time.sleep(0.5)
