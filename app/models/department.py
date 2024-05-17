from django.db import models


class Department(models.Model):
    class Type(models.IntegerChoices):
        FACULTY = 1, 'Faculty'
        CENTER = 2, 'Center'
        CATHEDRA = 3, 'Cathedra'
        SECTION = 4, 'Section'

    name = models.CharField(max_length=50, unique=True)
    about = models.TextField()
    type = models.IntegerField(choices=Type.choices)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name
