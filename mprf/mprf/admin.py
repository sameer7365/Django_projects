from django.contrib import admin
from .models import Department,MprfRequest,Skills,MprfApply,EmployeeMaster

# Register your models here.
# To modify the list display and search functionality in the Django admin interface for the TODOO model
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)

class MprfRequestAdmin(admin.ModelAdmin):
    list_display = ('position', 'department', 'vacancies', 'location', 'status')
    # search_fields = ('position', 'department__name', 'location')
    list_filter = ('status', 'department')

class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)

class MprfApplyAdmin(admin.ModelAdmin):
    list_display = ('mprf_request','user_id', 'applicant_name', 'applicant_email', 'applied_on', 'status')
    search_fields = ('applicant_name', 'applicant_email', 'mprf_request__position')
    list_filter = ('mprf_request__department','status')
    # filter_horizontal = ('skills',)
class EmployeeMasterAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'applicant_name', 'applicant_email', 'applied_on', 'status')
    search_fields = ('applicant_name', 'applicant_email', 'mprf_request__position')
    list_filter = ('status',)



admin.site.register(Department,DepartmentAdmin)
admin.site.register(MprfRequest,MprfRequestAdmin)
admin.site.register(Skills,SkillsAdmin)
admin.site.register(MprfApply,MprfApplyAdmin)
admin.site.register(EmployeeMaster,EmployeeMasterAdmin)

