from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^game-categories/$', GameCategoryListView.as_view(), name=GameCategoryListView.name),
    url(r'^game-categories/(?P<pk>[0-9]+)/$', GameCategoryDetailView.as_view(), name=GameCategoryDetailView.name),
    url(r'^games/$', GameListView.as_view(), name=GameListView.name),
    url(r'^games/(?P<pk>[0-9]+)/$', GameDetailView.as_view(), name=GameDetailView.name),
    url(r'^players/$', PlayerListView.as_view(), name=PlayerListView.name),
    url(r'^players/(?P<pk>[0-9]+)/$', PlayerDetailView.as_view(), name=PlayerDetailView.name),
    url(r'^player-scores/$', PlayerScoreListView.as_view(), name=PlayerScoreListView.name),
    url(r'^player-scores/(?P<pk>[0-9]+)/$', PlayerScoreDetailView.as_view(), name=PlayerScoreDetailView.name),
    url(r'^$', ApiRootView.as_view(), name=ApiRootView.name),
]
