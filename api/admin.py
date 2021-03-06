from django.contrib import admin
from . import models

# register Parent User Model
@admin.register(models.ParentUser)
class ParentUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'city', 'state']
    list_per_page = 10


# Register Child User Model
@admin.register(models.ChildUser)
class ChildUserAdmin(admin.ModelAdmin):
    list_display = ['child_first_name', 'child_last_name']
    list_per_page = 10