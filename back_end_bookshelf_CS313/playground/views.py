from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from playground.service.game_service import game_service
from playground.service.recommender_service import recommender_service


class api_handler:
    @api_view(['GET'])
    @staticmethod
    def get_game_genres_api(request):
        try:
            genres = game_service.get_genres()
        except Exception as e:
            return JsonResponse(str(e), status=500, safe=False)
        
        if genres == None:
            return JsonResponse("Not found any genre", status=404)

        genres_list = list(genres)

        return JsonResponse(genres_list, status=200, safe=False)
    
    @api_view(['GET'])
    @staticmethod
    def get_all_games_api(request):
        try:
            games = game_service.get_all_games()
        except Exception as e:
            return JsonResponse(str(e), status=500, safe=False)
        
        if games == None:
            return JsonResponse("Not found any game", status=404)
    

        return JsonResponse(games, status=200, safe=False)
    
    
    @api_view(['GET'])
    @staticmethod
    def get_game_detail_api(request, game_name):
        try:
            game = game_service.get_game_by_name(game_name)
        except Exception as e:
            return JsonResponse(str(e), status=500, safe=False)
        
        if game == None:
            return JsonResponse("Not found game", status=404)
        
        return JsonResponse(game, status=200, safe=False)
    

    @api_view(['GET'])
    @staticmethod
    def get_game_by_genres_api(request, genres):
        try:
            games = game_service.get_game_by_genres(genres)
        except Exception as e:
            return JsonResponse(str(e), status=500, safe=False)
        
        if games == None:
            return JsonResponse("Not found game", status=404)
        
        return JsonResponse(games, status=200, safe=False)
    

    @api_view(['GET'])
    @staticmethod
    def get_recommend_game_api(request, game_id):
        try:
            games = recommender_service.get_game_recommend(game_id)
        except Exception as e:
            return JsonResponse(str(e), status=500, safe=False)
        
        if games == None:
            return JsonResponse("Not found game", status=404)
        
        return JsonResponse(games, status=200, safe=False)


    @api_view(['GET'])
    @staticmethod
    def get_recommend_cart_api(request, game_id_list):
        try:
            games = recommender_service.get_game_recommend_cart(game_id_list)
        except Exception as e:
            return JsonResponse(str(e), status=500, safe=False)
        
        if games == None:
            return JsonResponse("Not found game", status=404)
        
        return JsonResponse(games, status=200, safe=False)
