from bs4 import BeautifulSoup
import json
import requests
import re


def scrape_wiki(url):
    # Tải nội dung của trang web
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the page")
        return None
    print(url)

    # Sử dụng BeautifulSoup để phân tích HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    khoego = soup.find('a', attrs={'id': "thumbnail"})
    
    print(khoego)
    data = {}
    #data["Youtube"]="https://www.youtube.com"+link.get("href")
    return 


if __name__ == "__main__":
    with open('game_plot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    links = [item['Name'] for item in data]
    print(links)
    game_details = []
    for link in links:
        link=link.replace(' ', '+')
        wiki_url = f'https://www.youtube.com/results?search_query={link}+trailer'
        game_details.append(scrape_wiki(wiki_url))
        
        json_data = json.dumps(game_details, ensure_ascii=False, indent=4)
        with open(f'trailer.json', 'w', encoding='utf-8') as f:
            f.write(json_data)
