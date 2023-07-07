import time
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

# Ouvrir la page web avec l'URL spécifiée
driver = uc.Chrome()
driver.get("https://temporary-phone-number.com/France-Phone-Number/")

# Rechercher le bouton "End" et cliquer dessus
end_button = driver.find_element(By.XPATH, "//a[contains(text(), 'End')]")
end_button.click()

# Imprimer la nouvelle URL
nouvelle_url = driver.current_url
driver.quit()

# Récupérer le nombre de pages
nombre_pages = int(nouvelle_url.split('page')[-1])

# Créer la liste de toutes les URLs correspondant aux différentes pages
toute_urls = [f"{nouvelle_url[:nouvelle_url.index('page') + 4]}{numero}" for numero in range(1, nombre_pages + 1)]
driver = uc.Chrome()

# Ouvrir le fichier en mode écriture
with open('list_numeros.txt', 'w') as file:
    # boucle qui parcours toutes les pages et stocke tous les URL de tous les numéros français
    for url in toute_urls:
        driver = uc.Chrome()
        driver.get(url)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        hrefs = [link.get('href') for link in soup.find_all('a') if
                 link.get('href', '').startswith('https://temporary-phone-number.com/France-Phone-Number/33')]

        # Écrire chaque URL dans le fichier en temps réel
        for item in hrefs:
            file.write(item + "\n")
            file.flush()  # Pour vider le tampon d'écriture

        driver.quit()
