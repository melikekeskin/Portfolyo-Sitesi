from django.db import models

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    projects = models.TextField()

    def __str__(self):
        return self.name
