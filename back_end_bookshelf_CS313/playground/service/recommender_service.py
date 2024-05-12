from itertools import combinations
from playground.service.game_service import game_service
import json

class recommender_service:
    with open('playground/data/rules.json', "r") as f:
        data = json.load(f)

    def generate_combinations(game_id_list):
        numbers = game_id_list.split(', ')
        result = []

        for r in range(1, len(numbers) + 1):
            for comb in combinations(numbers, r):
                result.append(', '.join(comb))
        return result
    
    @classmethod
    def get_game_recommend(cls, game_id):
        unique_game_ids = set()

        for item in cls.data:
                if item["base_items"] == str(game_id):
                    game_ids = item['add_items'].split(', ')
                    unique_game_ids.update(map(int, game_ids))

        games_list = []
        for game_id in unique_game_ids:
            game = game_service.get_game_by_id_recommend(game_id)
            games_list.append(game)

        if games_list == None: return None

        return games_list
    

    @classmethod
    def get_game_recommend_cart(cls, game_id_list):
        game_id_list = cls.generate_combinations(game_id_list)
        unique_game_ids = set()

        for game_id in game_id_list:
            for item in cls.data:
                if item["base_items"] == game_id:
                    game_ids = item['add_items'].split(', ')
                    unique_game_ids.update(map(int, game_ids))

        games_list = []
        for game_id in unique_game_ids:
            game = game_service.get_game_by_id_recommend(game_id)
            games_list.append(game)
            
        if games_list == None: return None

        return games_list

