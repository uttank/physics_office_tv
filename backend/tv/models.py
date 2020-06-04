from django.db import models
from django.utils import timezone

# Create your models here.

class PublicRelations(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    post = models.TextField()
    period_start = models.DateTimeField()
    period_end = models.DateTimeField()
    display = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        PublicRelations.objects.order_by('created_date')
        return self.title