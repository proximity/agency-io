from django.contrib import admin
from users.models import Agency, Department, Person, Employee, Status, Group
from users import views

class PersonAdmin(admin.ModelAdmin):
    model = Person
    exclude = ('is_guest',)
class EmployeeAdmin(PersonAdmin):

    model = Employee

    fieldsets = (
        ('Profile', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number', 'photo', 'address')
        }),
        ('Job', {
            'fields': ('job_title', 'department', 'group', 'active', 'bio')
        }),
        ('health and Safety', {
            'fields': ('emergency_contact_name', 'emergency_contact_phone', 'medical_alert')
        }),
    )

    search_fields = ['first_name', 'last_name', 'email']
    list_display = ('employee_name', 'group', 'department')

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context["show_send_welcome_email"] = True
        return super(EmployeeAdmin, self).change_view(request,object_id, form_url, extra_context)

    # Concatenate first_name last_name and give short description
    def employee_name(self, obj):
        return ("%s %s" % (obj.first_name, obj.last_name))
    employee_name.short_description = 'Name'

admin.site.register(Agency)
admin.site.register(Department)
admin.site.register(Group)
admin.site.register(Employee, EmployeeAdmin)
