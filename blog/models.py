from django.db import models

# Create your models here.
class Blog(models.Model):
    # blog name, blog description, blog date, blog author
    blog_name = models.CharField(max_length=250)
    blog_author= models.CharField(max_length=40, blank=True)
    blog_date = models.DateField()
    blog_description = models.CharField(max_length=500)

    def __str__(self):
        return self.blog_name