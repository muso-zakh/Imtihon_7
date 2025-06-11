from django.contrib import admin

# Register your models here.
from .models import Maqola

class MaqolaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',) 
    readonly_fields = ('view_count', 'created_at')


admin.site.register(Maqola, )