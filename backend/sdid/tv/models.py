from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class DisplayType(models.Model):
    display_type = models.CharField(max_length=20)
    comment = models.CharField(max_length=50)    


class PublicRelations(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    content = RichTextUploadingField()
    displaytype = models.ForeignKey(DisplayType, null=True, on_delete=models.CASCADE)
    display = models.BooleanField()


    period_start = models.DateField()
    period_end = models.DateField()
    created_date = models.DateField(default=timezone.now)
    
    def __str__(self):
        PublicRelations.objects.order_by('created_date')
        return self.title