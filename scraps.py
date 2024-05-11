import re
from bs4 import BeautifulSoup
import json
import requests

data = []

def scrape_wiki(url):
    # Tải nội dung của trang web
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the page")
        return None

    # Sử dụng BeautifulSoup để phân tích HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    all_tr = soup.find_all('tr')

    # Trích xuất thông tin từ HTML
    for tr in all_tr[1:len(all_tr)-1]:
        tds = tr.find_all('td')
        if len(tds) >= 6:
            if tds[5].text.strip() == "TBA": continue
            released_date = int(tds[5].text.strip()[-4:])
            if tds[0].find('a'): 
                if released_date >= 2018:
                    pattern_url = "/wiki"
                    link = tds[0].find('a').get('href')
                    if re.search(pattern_url, link) != None:
                        wiki_url = f'https://en.wikipedia.org{link}'
                        img_response = requests.get(wiki_url)
                        img_soup = BeautifulSoup(img_response.content, 'html.parser')
                        img = img_soup.find('a', attrs={'class': 'mw-file-description'})
                        game_info = {
                            "Link": tds[0].find('a').get('href'),
                            "Image": img.img.get("src"),
                            "Name": tds[0].text.strip(),
                            "Developer": tds[1].text.strip(),
                            "Publisher": tds[2].text.strip(),
                            "Genres": tds[3].text.strip(),
                            "Operating systems": tds[4].text.strip(),
                            "Date released": tds[5].text.strip()
                        }
                        data.append(game_info)

    # Chuyển đổi thành định dạng JSON
    return 

if __name__ == "__main__":
    alphabet = [chr(i).capitalize() for i in range(ord('a'), ord('z') + 1)]
    for char in alphabet:
        wiki_url = f'https://en.wikipedia.org/wiki/List_of_PC_games_({char})'
        scrape_wiki(wiki_url)
        json_data = json.dumps(data, ensure_ascii=False, indent=4)
        with open(f'game_data.json', 'w', encoding='utf-8') as f:
            f.write(json_data)
