import string
from bs4 import BeautifulSoup
import json
import requests
from pytube import Search

game_plot = []

if __name__ == "__main__":
    with open('game_plot_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    links = [item for item in data]
    for link in links:
        s = Search(link['Name']+" trailer")
        new_data = {}
        new_data["Name"] = link['Name']
        new_data['about_game'] = link['about_game']
        new_data['gameplay'] = link['gameplay']
        new_data['price'] = link['price']
        new_data["Video"] = "https://www.youtube.com/embed/"+s.results[0].video_id + "?html5=1&autoplay=1"
        game_plot.append(new_data)
        
        json_data = json.dumps(game_plot, ensure_ascii=False, indent=4)
        with open(f'trailer_vid.json', 'w', encoding='utf-8') as f:
            f.write(json_data)