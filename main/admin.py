from django.contrib import admin

# Register your models here.

from main.models import Teams,Positions,Posts,AgeGroups,TeamTypes




# Register your models here.
admin.site.register(Teams)
admin.site.register(Positions)
admin.site.register(Posts)
admin.site.register(AgeGroups)
admin.site.register(TeamTypes)

