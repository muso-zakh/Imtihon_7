from django.contrib import admin

# Register your models here.

from .models import Jurnal

class JurnalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',) 
    readonly_fields = ('view_count', 'created_at')


admin.site.register(Jurnal, )