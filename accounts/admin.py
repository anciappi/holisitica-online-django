from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfieAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'location', 'celphone', 'user_groups')
    search_fields = ('location', 'country', 'user__username', 'user__email', 'user__last_name')
    list_filter = ('user__groups', 'country')

    def user_groups(self, obj):
        return " - ".join([group.name for group in obj.user.groups.all().order_by('name')])
    
    user_groups.short_description = 'Grupos'

admin.site.register(Profile, ProfieAdmin)