from django.contrib import admin
from testapp.models import Task

# Register your models here.
class ModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Task,ModelAdmin)
