from django.contrib import admin
from .models import AdminTool

@admin.register(AdminTool)
class AdminToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)
