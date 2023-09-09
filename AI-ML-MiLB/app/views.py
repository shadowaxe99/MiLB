
from django.shortcuts import render
from django.http import JsonResponse

from .models import Player

def player_list(request):
    players = Player.objects.all()
    data = {
        'players': list(players.values())
    }
    return JsonResponse(data)

def player_detail(request, player_id):
    try:
        player = Player.objects.get(id=player_id)
        data = {
            'player': {
                'id': player.id,
                'name': player.name,
                'team': player.team,
                'position': player.position,
                'age': player.age,
                'stats': player.stats,
            }
        }
        return JsonResponse(data)
    except Player.DoesNotExist:
        return JsonResponse({'error': 'Player not found'}, status=404)

