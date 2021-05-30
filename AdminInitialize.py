import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matching_game.settings')

import django
django.setup()


from accounts.models import Account

def admin():
    admin = Account.objects.get_or_create(username='admin', password='admin', first_name='admin', last_name='admin', role='Administrator', institution='System',categories = {})[0]
    admin.save()