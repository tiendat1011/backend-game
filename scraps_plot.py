import random
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

    # Sử dụng BeautifulSoup để phân tích HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.find('div', attrs={'class': 'mw-content-container'})

    temp = ""
    game_details = {}

    name = soup.find('h1', attrs={'id': 'firstHeading'})
    game_details["Name"] = name.get_text()

    for p in content.find_all(['p', 'h2']):
        if re.search('h2', p.name):
            break
        temp += p.text + '\n'

    game_details["about_game"] = temp
    temp = ""

    gameplay = content.find_all(['p', 'h2'])
    flags = 0

    for p in content.find_all(['p', 'h2']):
        if re.search('h2', p.name):
            if p.find('span', attrs={'id': 'Gameplay'}):
                flags += 1
                continue
            elif flags == 1:
                break

        if flags == 1:
            temp += p.text + '\n'

    game_details["gameplay"] = temp

    random_number = random.randint(1,100)
    game_details["price"] = random_number

    return game_details


if __name__ == "__main__":
    with open('game_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    links = [item['Link'] for item in data]
    pattern_url = "/wiki"
    game_details = []
    for link in links:
        if re.search(pattern_url, link) != None:
            wiki_url = f'https://en.wikipedia.org{link}'
        game_details.append(scrape_wiki(wiki_url))
        
        json_data = json.dumps(game_details, ensure_ascii=False, indent=4)
        with open(f'game_plot_data.json', 'w', encoding='utf-8') as f:
            f.write(json_data)
