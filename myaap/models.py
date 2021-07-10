from django.db import models

# Create your models here.
class Search(models.Model):
    Search = models.CharField(max_length=500)
    Category = models.CharField(max_length=20, null=True, default='none')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Search
     
    
    class Meta:
        verbose_name_plural = 'Searches'