from django.contrib import admin
from todo_user.models import TODOO



# To modify the list display and search functionality in the Django admin interface for the TODOO model
class TODOOAdmin(admin.ModelAdmin):
    list_display = ('srno', 'title', 'date', 'user')
    search_fields = ('title',)
    list_filter = ('date',)
    
admin.site.register(TODOO, TODOOAdmin)