import json
from django.core.management.base import BaseCommand
from playground.models import GameDetail, GameInfo

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.import_game_detail()
        self.import_game_info()
        

    def import_game_detail(self):
        try:
            with open('playground/data/game_detail.json', 'r', encoding='utf-8') as file:
                game_details = json.load(file)

            for item in game_details:
                link = item.get("Link")
                image = item.get("Image")
                name = item.get("Name")
                developer = item.get("Developer")
                publisher = item.get("Publisher")
                genres = item.get("Genres")
                operating_systems = item.get("Operating systems")
                date_released = item.get("Date released")


                GameDetail.objects.create(
                    link=link,
                    image=image,
                    name=name,
                    developer=developer,
                    publisher=publisher,
                    genres=genres,
                    operating_systems=operating_systems,
                    date_released=date_released)
                
            self.stdout.write(self.style.SUCCESS('Import game detail successful'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('Game detail not found'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Error decoding JSON'))

    
    def import_game_info(self):
        try:
            with open('playground/data/game_info.json', 'r', encoding='utf-8') as file:
                game_info = json.load(file)

            for item in game_info:
                name = item.get("Name")
                about_game = item.get("about_game")
                gameplay = item.get("Gameplay")
                price = item.get("Price")
                video = item.get("Video")


                GameInfo.objects.create(
                    name=name, 
                    about_game=about_game, 
                    gameplay=gameplay, 
                    price=price, 
                    video=video)
                
            self.stdout.write(self.style.SUCCESS('Import game info successful'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('Game info not found'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Error decoding JSON'))

