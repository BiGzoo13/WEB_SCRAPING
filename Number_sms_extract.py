from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Configurer les options du pilote Firefox
firefox_options = Options()
firefox_options.add_argument("--headless")  # Activer le mode headless

# Ouvrir le fichier contenant les URLs
with open('list_numeros.txt', 'r') as file:
    # Lire chaque ligne du fichier
    for line in file:
        url = line.strip()  # Supprimer les espaces et les sauts de ligne
        numero = int(url.split('/')[-1])
    # Ouvrir la page web avec l'URL spécifiée en mode headless
        driver = webdriver.Firefox(options=firefox_options)
        driver.get(url)

        # Utilisation de BeautifulSoup pour analyser le contenu HTML
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Trouver l'élément contenant le chiffre des SMS envoyés
        nombre = soup.find('div', class_='col-sm-4 col-xs-12').find('span', class_='badge bg-light-blue').text

        print("Il y a :", nombre, "SMS envoyés avec le numéro suivant : ",numero)

        driver.quit()
