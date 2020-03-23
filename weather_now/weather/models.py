from django.db import models

# stores list of weather searches

class City(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "cities"