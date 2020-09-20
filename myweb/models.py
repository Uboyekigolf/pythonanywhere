from django.db import models

class herbtype(models.Model):
    herbtype_text = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.herbtype_text}'

class herb(models.Model):
    herb_type = models.CharField(max_length=200)
    herb_name = models.CharField(max_length=200)
    herb_properties = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.herb_type} - {self.herb_name} - {self.herb_properties}'