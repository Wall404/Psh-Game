# your_app/management/commands/generate_stats.py
import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from Game.models import GameStatistic
import requests

class Command(BaseCommand):
    help = 'Generate random game statistics'

    def handle(self, *args, **kwargs):
        for _ in range(10):
            player_id = str(random.randint(1, 10))
            nickname = requests.get("https://randomuser.me/api/").json()["results"][0]["login"]["username"]
            profile_image = requests.get("https://randomuser.me/api/").json()["results"][0]["picture"]["thumbnail"]
            creation_date = timezone.now() - timezone.timedelta(minutes=random.randint(1, 1000))
            score = random.randint(1, 100)

            GameStatistic.objects.create(
                player_id=player_id,
                nickname=nickname,
                profile_image=profile_image,
                creation_date=creation_date,
                score=score
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated game statistics'))
