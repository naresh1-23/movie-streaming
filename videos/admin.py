from django.contrib.admin import register, ModelAdmin
from .models import Videos

@register(Videos)
class UserAdmin(ModelAdmin):
    list_display = ('name', 'rating', 'created_at', "updated_at")
