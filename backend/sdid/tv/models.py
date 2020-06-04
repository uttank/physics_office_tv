from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models

# Create your models here.

class PublicRelations(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    content = tinymce_models.HTMLField('HTML content')
    display = models.BooleanField()

    period_start = models.DateField()
    period_end = models.DateField()
    created_date = models.DateField(default=timezone.now)
    
    def __str__(self):
        PublicRelations.objects.order_by('created_date')
        return self.title