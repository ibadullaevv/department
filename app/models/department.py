from django.db import models


class Department(models.Model):
    class Type(models.IntegerChoices):
        FACULTY = 1
        CENTER = 2
        CATHEDRA = 3
        SECTION = 4

    name = models.CharField(max_length=50, unique=True)
    about = models.TextField()
    type = models.IntegerField(choices=Type)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=200, unique=True)
