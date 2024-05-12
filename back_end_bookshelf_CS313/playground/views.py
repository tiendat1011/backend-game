from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from playground.service.game_service import game_service


class api_handler:
    # api/games/genres
    @api_view(['GET'])
    @staticmethod
    def get_game_genres_api(request):
        try:
            genres = game_service.get_genres()
        except Exception as e:
            return JsonResponse({'success': False,
                                 'ErrorMsg': str(e),
                                 'data': None}, status=500)
        
        if genres == None:
            return JsonResponse({'success': False,
                                 'ErrorMsg': "Not found any genre",
                                 'data': None}, status=404)

        genres_list = list(genres)

        return JsonResponse({'success': True,
                            'ErrorMsg': None,
                            'data': genres_list}, status=200)
    
    @api_view(['GET'])
    @staticmethod
    def get_all_games_api(request):
        try:
            games = game_service.get_all_games()
        except Exception as e:
            return JsonResponse({'success': False,
                                 'ErrorMsg': str(e),
                                 'data': None}, status=500)
        
        if games == None:
            return JsonResponse({'success': False,
                                 'ErrorMsg': "Not found any game",
                                 'data': None}, status=404)
        
        games_list = list(games)

        return JsonResponse({'success': True,
                            'ErrorMsg': None,
                            'data': games_list}, status=200)
    
    
    @api_view(['GET'])
    @staticmethod
    def get_game_detail_api(request, game_id):
        try:
            game = game_service.get_game_by_id(game_id)
        except Exception as e:
            return JsonResponse({'success': False,
                                 'ErrorMsg': str(e),
                                 'data': None}, status=500)
        
        if game == None:
            return JsonResponse({'success': False,
                                 'ErrorMsg': "Not found any game",
                                 'data': None}, status=404)
        

        return JsonResponse({'success': True,
                            'ErrorMsg': None,
                            'data': game}, status=200)
