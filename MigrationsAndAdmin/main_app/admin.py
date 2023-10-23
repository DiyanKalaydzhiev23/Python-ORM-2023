from django.contrib import admin
from main_app.models import EventRegistration, Student, Supplier


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'participant_name', 'registration_date')

    list_filter = ('event_name', 'registration_date')

    search_fields = ('event_name', 'participant_name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'grade')

    list_filter = ('age', 'grade', 'date_of_birth')

    search_fields = ('first_name',)

    # readonly_fields = ('first_name',)  for the last task, the example is here

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'age', 'date_of_birth')
        }),
        ('Academic Information', {
            'fields': ('grade',),
            # 'classes': ['collapse'],
        }),
    )


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

    list_filter = ('name', 'phone')

    search_fields = ('email', 'contact_person', 'phone')

    list_per_page = 20

    fieldsets = (
        ('Information', {
            'fields': ('name', 'contact_person', 'email', 'address')
        }),
    )




