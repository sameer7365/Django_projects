from django.contrib import admin
from .models import TodoItem, Task


# This is used to view the fields in the admin panel
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description','project', 'completed', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('completed', 'created_at', 'updated_at')
    ordering = ('-created_at',)


admin.site.register(TodoItem,TodoItemAdmin)
admin.site.register(Task)
