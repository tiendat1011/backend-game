from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.http import require_http_methods
from playground.views import api_handler

# URLConf
# api/
urlpatterns = [
    path('games/genres/', require_http_methods(["GET"])(api_handler.get_game_genres_api)),
    path('games/get_all_games/', require_http_methods(["GET"])(api_handler.get_all_games_api)),
    path('games/<str:game_id>/', require_http_methods(["GET"])(api_handler.get_game_detail_api))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)