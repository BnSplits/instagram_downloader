from selenium import webdriver
from selenium.webdriver.common.by import By
import clipboard
import pyautogui
from time import sleep
from pathlib import Path
import json

# Importation de la base de données des coordonnées
with open('db.json') as f:
    data = json.load(f)

# Sélection des coordonnées en fonction de la distribution Linux et de la résolution d'écran
db = data["mint"]["1920x1080"]

# Définition des coordonnées pour chaque point
image_link = db["image-link"]
exit_link = db["exit-link"]
close_adblock = db["close-adblock"]
image_link_entry = db["image-link-entry"]
launch_image_search = db["launch-image-search"]
download_button = db["download-button"]
download_more_button = db["download-more-button"]

# Demande du nombre d'images à télécharger et du compte à rebours
nb_images = int(input("Combien d'images à télécharger ? "))
secs = int(input("Un décompte de : "))

# Compte à rebours avant le lancement
for i in range(secs - 2 * secs, 0):
    print(-i)
    sleep(1)
print("START!")

# Fonction pour cliquer sur le lien de l'image trois fois
def click_link(x, y):
    pyautogui.click(x, y)
    pyautogui.click(x, y)
    pyautogui.click(x, y)
    sleep(1)

# Fonction pour passer à la page suivante
def next_page():
    pyautogui.press("right")
    sleep(0.5)
    pyautogui.press('down')
    sleep(1)

# Fonction pour coller le lien dans le fichier links.txt
def link_paste(link):
    with open('links.txt', 'a') as file:
        file.write(link + ',')

# Fonction pour lancer Firefox
def firefox_launch():
    driver = webdriver.Firefox()
    driver.install_addon('./adblock.xpi')
    driver.maximize_window()
    driver.get('https://snapinsta.app/')
    sleep(5)
    pyautogui.click(close_adblock["x"], close_adblock["y"])

# Fonction pour cliquer sur le bouton de téléchargement
def click_download_button():
    is_dw = False
    while not is_dw:
        if pyautogui.pixel(download_button["x"], download_button["y"]) == (0, 99, 249):
            dw_bts = driver.find_elements(By.CSS_SELECTOR, '.download-media')
            for dw_bt in dw_bts:
                dw_bt.click()
            is_dw = True
        else:
            pyautogui.scroll(-5)
            sleep(3)

# Fonction pour cliquer sur le bouton "Download more"
def click_download_more():
    pyautogui.click(download_more_button["x"], download_more_button["y"])
    sleep(2)

# Boucle pour récupérer chaque lien
for i in range(nb_images):
    click_link(image_link["x"], image_link["y"])
    pyautogui.hotkey('ctrl', 'c')
    sleep(1)
    pyautogui.click(exit_link["x"], exit_link["y"])
    sleep(1)
    next_page()
    link_paste(clipboard.paste())

# Lecture des liens depuis le fichier links.txt
links = Path("links.txt").read_text().split(',')

# Lancement de Firefox
driver = webdriver.Firefox()
driver.install_addon('./adblock.xpi')
driver.maximize_window()
driver.get('https://snapinsta.app/')
sleep(5)
pyautogui.click(close_adblock["x"], close_adblock["y"])

# Boucle pour traiter chaque lien
for link in links:
    clipboard.copy(str(link))
    sleep(1)
    pyautogui.click(image_link_entry["x"], image_link_entry["y"])
    sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(launch_image_search["x"], launch_image_search["y"])
    sleep(3)
    click_download_button()
    sleep(1)
    click_download_more()

# pour supprimer le contenu du fichier links.txt après utilisation
with open("links.txt", "w") as file:
    file.write("")

# Fermeture du navigateur
driver.close()
sleep(1)
print("FINI !")