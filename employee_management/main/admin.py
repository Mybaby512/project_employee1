from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'position',
        'department',
        'employment_type',
        'salary',
        'start_date',
    )

    list_display_links = (
        'id',
        'name',
    )

    search_fields = (
        'name',
        'position',
        'department',
        'phone',
        'email',
        'id_card',
    )

    list_filter = (
        'position',
        'department',
        'employment_type',
        'pay_period',
    )

    ordering = (
        '-id',
    )