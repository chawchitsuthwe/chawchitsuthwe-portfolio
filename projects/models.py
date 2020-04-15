from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    project_year = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default=None)

    def __str__(self):
        return self.name
