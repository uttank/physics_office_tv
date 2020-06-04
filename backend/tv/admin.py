from django.contrib import admin
from .models import PublicRelations
# Register your models here.

class PublicRelationsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField:{'widget': TinyMCE()},
    }


admin.site.register(PublicRelations, PublicRelationsAdmin)