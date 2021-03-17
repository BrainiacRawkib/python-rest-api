from django.contrib import admin
from .models import GameCategory, Game, Player, PlayerScore


admin.site.register(Game)
admin.site.register(GameCategory)
admin.site.register(Player)
admin.site.register(PlayerScore)
