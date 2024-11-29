from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'duration')
    search_fields = ('title',)
    list_filter = ('duration',)
