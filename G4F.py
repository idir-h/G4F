from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import requests
import fitz
import re
import gzip


def get_imgs_url(page_url):
  chrome_options = Options()
  chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

  driver = webdriver.Chrome(options=chrome_options)
  driver.get(page_url)

  # Attendre que les ressources soient bien chargées
  time.sleep(5)

  # Récupérer le nombre de pages (équivalent du span dans ton JS)
  try:
      span = driver.find_element("css selector", 'input[name="pageNumber"]').find_element("xpath", "following-sibling::*[1]")
      totalPages = int(span.text.replace("/", "").strip())
      print("Total des pages :", totalPages)
  except Exception as e:
      print("Impossible de trouver le total des pages :", e)

  # Récupérer les logs "performance" comme JS performance.getEntriesByType("resource")
  logs = driver.get_log("performance")

  resources = []
  for entry in logs:
      msg = entry["message"]
      if "Network.responseReceived" in msg and any(ext in msg for ext in [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".svgz"]):
          match = re.search(r'"url":"([^"]+)"', msg)
          if match:
              resources.append(match.group(1))
 # Filtrer comme en JS : /p\d+\.(jpg|png|...)
  pattern = re.compile(r'/p\d+\.(jpg|jpeg|png|gif|webp|svg|svgz)(\?.*)?$', re.IGNORECASE)
  imagesP = [res for res in resources if pattern.search(res)]
  url = imagesP[1] if len(imagesP) > 1 else None
  driver.quit()
  return url , totalPages


def download_and_save(page_num, BASE_URL):
    #Télécharge une page et la sauvegarde en .svg (gzip ou non)
    url = BASE_URL.format(page_num)
    print(f"\n---------------------------------\nTéléchargement page {page_num}...")
    res = requests.get(url)
    if res.status_code == 200:
        raw = res.content
        fname_svg = os.path.join(img_path, f"p{page_num}.svg")
        try:
            # Essayer de décompresser comme gzip (.svgz)
            svg_data = gzip.decompress(raw)
            with open(fname_svg, "wb") as f:
                f.write(svg_data)
            print(f"✅ Sauvegardé (décompressé) : {fname_svg}")
        except Exception:
            # Sinon c’est déjà un SVG
            with open(fname_svg, "wb") as f:
                f.write(raw)
            print(f"✅ Sauvegardé (brut) : {fname_svg}")

        return fname_svg
    else:
        print(f"⚠️ Page {page_num} introuvable (status {res.status_code})")
        return None



page_url = input("Donne-moi l'URL du livre : ")
url , totalPages = get_imgs_url(page_url)

if url:
    BASE_URL = re.sub(r"p\d+\.(?:jpg|jpeg|png|gif|webp|svgz|svg)", "p{}.svgz", url)
else : 
    print("BASE URL non trouver ! ")

OUTPUT_PDF = "output.pdf"
IMG_DIR = "testimgs"

# 📌 Créer dossier imgs avec chemin absolu
current_dir = os.getcwd()
img_path = os.path.join(current_dir, IMG_DIR)
os.makedirs(img_path, exist_ok=True)
print(f"📁 Dossier créé : {img_path}")

for i in range(1, totalPages + 1):
    download_and_save(i, BASE_URL) 
