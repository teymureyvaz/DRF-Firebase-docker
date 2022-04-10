from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        User.objects.all().delete() 
        User.objects.create(email="test@admin.com", 
                            username="demo_admin", 
                            password="demo")