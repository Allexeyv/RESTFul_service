from django.db import models

class Resourse(models.Model):
    """Checks autorization"""
    pass

class Publication(models.Model):
    """ Describes publications"""
    title = models.CharField(max_length=30, blank=True, default='')
    text = models.CharField(max_length=600, blank=True, default='')
    created_at = models.DateField(("Created at"), auto_now=True, auto_now_add=False)
    tags = models.CharField(max_length=30, blank=True, default='')

    @classmethod
    def create(cls, title, text, tags):
        publication = cls(title=title, text=text, tags=tags)
        return publication

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ('title',)

class Category(models.Model):
    """ Describes categories"""
    name = models.CharField(max_length=30, blank=True, default='')
    created_at = models.DateField(("Created at"), auto_now=True, auto_now_add=False)

    @classmethod
    def create(cls, name):
        category = cls(name=name)
        return category

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)