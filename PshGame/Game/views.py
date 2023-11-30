# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import GameStatistic
from django.utils import timezone
import csv
from django.http import HttpResponse
from io import StringIO

def top_scores(request):
    top_scores = GameStatistic.objects.order_by('-score')[:10]
    last_updated = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        'top_scores': [{'nickname': stat.nickname, 'score': stat.score} for stat in top_scores],
        'last_updated': last_updated
    }
    return JsonResponse(data)

def export_report(request):
    all_stats = GameStatistic.objects.all()

    # Generate CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=game_statistics.csv'
    csv_writer = csv.writer(response)
    csv_writer.writerow(['ID', 'Player ID', 'Nickname', 'Profile Image', 'Creation Date', 'Score'])

    for stat in all_stats:
        csv_writer.writerow([stat.id, stat.player_id, stat.nickname, stat.profile_image, stat.creation_date, stat.score])

    return response