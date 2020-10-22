from django.db import models

class herbtype(models.Model):
    herb_type = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.herb_type}';
class herb(models.Model):
    herb_name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.herb_name}';