from zenrows import ZenRowsClient
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Définir les options de Firefox pour utiliser le mode headless
firefox_options = Options()
firefox_options.add_argument("--headless")

# Ouvrir la page web avec l'URL spécifiée
driver = webdriver.Firefox(options=firefox_options)
driver.get("https://temporary-phone-number.com/France-Phone-Number/")

# Rechercher le bouton "End" et cliquer dessus
driver.find_element(By.XPATH, "//a[contains(text(), 'End')]").click()

# Obtenir la nouvelle URL
nouvelle_url = driver.current_url
driver.quit()

# Récupérer le nombre de pages
nombre_pages = int(nouvelle_url.split('page')[-1])

# Créer la liste de toutes les URLs correspondant aux différentes pages
toutes_urls = [f"{nouvelle_url[:nouvelle_url.index('page') + 4]}{numero}" for numero in range(1, nombre_pages + 1)]

# Parcourir toutes les pages et stocker les URLs des numéros français dans un fichier
with open('list_numeros.txt', 'w') as file:
    client = ZenRowsClient("a0ae95ca3fdce619f2eff0bde7f3fa877d03600b")
    for url in toutes_urls:
        response = client.get(url)
        html_file = BeautifulSoup(response.text, "html.parser")
        hrefs = [link.get('href') for link in html_file.find_all('a') if link.get('href', '').startswith('https://temporary-phone-number.com/France-Phone-Number/33')]
        file.write('\n'.join(hrefs) + "\n")
        file.flush()  # Pour vider le tampon d'écriture
