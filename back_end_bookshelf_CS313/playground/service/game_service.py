from playground.models import GameDetail


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
    
    #api/all_games
    def get_all_games():
        games = GameDetail.objects.values('id', 'name', 'image')

        if games == None: return None

        return games
        