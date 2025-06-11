from django.contrib import admin

# Register your models here.
from .models import Register

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name')
    search_fields = ('first_name',) 


admin.site.register(Register, RegisterAdmin)