from django.db import models

class Resourse(models.Model):
    """Checks autorization"""
    pass

class Publication(models.Model):
    """ Describes publications"""
    title = models.CharField(max_length=30, blank=True, default='')
    text = models.CharField(max_length=600, blank=True, default='')
    created_at = models.DateField(("Date"), auto_now=True, auto_now_add=False)
    tags = models.CharField(max_length=30, blank=True, default='')

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ('name',)

class Category(models.Model):
    """ Describes categories"""
    name = models.CharField(max_length=30, blank=True, default='')
    created_at = models.DateField(("Date"), auto_now=True, auto_now_add=False)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)