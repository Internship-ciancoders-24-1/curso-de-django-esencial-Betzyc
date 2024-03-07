# Description: This file is used to register the models with the admin site.
from django.contrib import admin

#Module
from users.models import Profile

# Register your models here.
#admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""
    list_display = ('pk','user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')
    """search_fields = (
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )
    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),)
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),)
        })
    )

    readonly_fields = ('created', 'modified')

    def get_readonly_fields(self, request, obj=None):
       
        if not request.user.is_superuser:
            return ('created', 'modified')
        return ('created', 'modified')"""


