from faker import Faker
from backend.backend.models import Publication, Category
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Adds fake users, categories and publications to django'
    def add_arguments(self, parser):
        parser.add_argument('count')

    def fake_publication(self):
        fake = Faker()
        text = fake.text()
        title=fake.word()
        tags = fake.word()
        p = Publication.create(title=title, text=text, tags=tags)
        p.save()

    def fake_category(self):
        fake = Faker()
        name = fake.text()
        c = Category.create(name=name)
        c.save()
    
    def fake_user(self):
        """Generates users. Pass is always 1111"""
        fake = Faker('cz_CZ')
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        User.objects.create_user(username=last_name, email=email, first_name=first_name, last_name=last_name, password='1111')

    
    def handle(self, *args, **options):
        for i in range(int(options['count'])):
            self.fake_publication()
            self.fake_category()
            self.fake_user()
        self.stdout.write("Successfully added users, categories and publications")
