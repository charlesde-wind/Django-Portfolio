from django.db import models

# Create your models here.
class Project(models.Model):

    # setting attributes
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="portfolio/images/")
    urls = models.URLField(blank=True)

    def __str__(self):
        return self.title