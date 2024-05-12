from playground.models import GameDetail, GameInfo


class game_service:
    # api/games/genres
    @staticmethod
    def get_genres():
        game_genres = GameDetail.objects.values_list('genres', flat=True)

        unique_genres = set()

        for genres_str in game_genres:
            if genres_str:
                # Tách chuỗi thành các thể loại riêng biệt dựa trên dấu phẩy
                genres_list = genres_str.split(', ')
                # Bổ sung các thể loại vào set
                unique_genres.update(genres_list)

        return unique_genres
    
    #api/games/get_all_games
    def get_all_games():
        games = GameDetail.objects.values('id', 'name', 'image')

        if games == None: return None

        return games
        
    #api/games/{game_id}
    def get_game_by_id(game_id):
        game_id = str(game_id)

        game_detail = GameDetail.objects.get(id=game_id)
        game_info = GameInfo.objects.get(id=game_id)

        if game_detail == None or game_info == None: return None

        games = {
            'image': game_detail.image,
            'name': game_detail.name,
            'developer': game_detail.developer,
            'publisher': game_detail.publisher,
            'genres': game_detail.genres,
            'operating_systems': game_detail.operating_systems,
            'date_released': game_detail.date_released,
            'about_game': game_info.about_game,
            'gameplay': game_info.gameplay,
            'price': game_info.price,
            'video': game_info.video
        }

        return games