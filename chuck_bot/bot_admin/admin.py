from django.contrib import admin
from .models import Greeting, Helper


# Register your models here.
@admin.register(Greeting)
class GreetingAdmin(admin.ModelAdmin):
    list_display = ('hello_world',)


@admin.register(Helper)
class HelperAdmin(admin.ModelAdmin):
    list_display = ('help',)
