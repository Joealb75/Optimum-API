import json
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Generate tokens for users and save them as fixtures'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        tokens = []

        for user in users:
            token, created = Token.objects.get_or_create(user=user)
            tokens.append({
                "model": "authtoken.token",
                "pk": token.pk,
                "fields": {
                    "key": token.key,
                    "user": token.user_id,
                    "created": token.created.isoformat(),
                }
            })

        with open('tokens.json', 'w') as f:
            json.dump(tokens, f, indent=4)

        self.stdout.write(self.style.SUCCESS('Successfully generated tokens.json'))
