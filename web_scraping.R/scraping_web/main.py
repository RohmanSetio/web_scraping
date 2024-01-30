import requests
import json
import os
from bs4 import BeautifulSoup

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def save_to_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# URL dari situs web yang ingin di-scrape
url = 'https://www.antaranews.com/berita/3940005/anies-temui-santri-hingga-pejuang-lingkungan-hidup-di-serang?utm_source=antaranews&utm_medium=desktop&utm_campaign=editor_picks'

# Melakukan permintaan GET ke URL
response = requests.get(url)

# Membuat objek BeautifulSoup dari konten HTML yang diperoleh
soup = BeautifulSoup(response.text, 'html.parser')

# Mencari elemen HTML tertentu dalam objek BeautifulSoup
# Misalnya, mencari semua elemen <div> (konten artikel) dengan class 'wrap__article-detail-content post-content'
article_content = soup.find("div", {"class": "wrap__article-detail-content post-content"})

# Mengambil teks dari konten artikel
content_text = article_content.get_text(separator='\n')

# Membuat dictionary untuk menyimpan data
data = {
    "url": url,
    "content": content_text
}

# Membuat folder untuk menyimpan file .json jika belum ada
folder_name = 'scraped_data'
create_folder(folder_name)

# Menyusun jalur file untuk menyimpan data dalam format .json
file_path = os.path.join(folder_name, 'article_data.json')

# Menyimpan data ke dalam file .json
save_to_json(file_path, data)

print(f'Data telah disimpan ke dalam file: {file_path}')
