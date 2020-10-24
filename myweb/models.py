from django.db import models

class herb(models.Model):
    herb_name = models.CharField(max_length=10000)
    img = models.CharField(max_length=255,blank=True)
    def __str__(self):
        return f'{self.herb_name}';