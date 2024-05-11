import json
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from playground.models import Game
from django.db import transaction, connection

class Command(BaseCommand):
    help = 'Import data from JSON file to database'

    def handle(self, *args, **options):
        self.clear_data()
        #self.reset_primary_keys()
        self.import_transactions()

    # def handle(self, *args, **options):
    #     try:
    #         with open('playground/data/books_data.json', 'r') as file:
    #             data = json.load(file)
    #             for item in data:
    #                 models.Book.objects.create(**item)  
                    
    #         self.stdout.write(self.style.SUCCESS('Data imported successfully'))
    #     except FileNotFoundError:
    #         self.stdout.write(self.style.ERROR('File not found'))
    #     except Exception as e:
    #         self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))

    def clear_data(self):
        Game.objects.all().delete()
        #PurchaseOrder.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Data cleared successfully'))

    def reset_primary_keys(self):
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='PurchaseOrder'")
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='OrderDetail'")
        self.stdout.write(self.style.SUCCESS('Reset primary key sequence for PurchaseOrder and OrderDetail successfully'))

    def import_transactions(self):
        try:
            with open('playground/data/trailer_vid.json', 'r', encoding='utf-8') as file:
                transactions = json.load(file)

            for item in transactions:
                name = item.get('Name')
                about_game = item.get('about_game')
                gameplay = item.get('gameplay')
                price = item.get('price')
                video = item.get('Video')

                game_details = Game.objects.create(name=name, about_game=about_game, gameplay=gameplay, price=price, video=video)

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('Transactions file not found'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Error decoding JSON'))