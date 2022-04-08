
# Register your models here.
from django.contrib import admin
from .models import Registeration
# Register your models here.
@admin.register(Registeration)
class SudoRegistration(admin.ModelAdmin):
    list_display = ['id','Name','Address','Email','Mobile','Password','Gender']