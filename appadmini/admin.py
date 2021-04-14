from django.contrib import admin

from appadmini.models import SuperHero


# admin.site.register(SuperHero)
class SuperHeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'added_on')
    search_fields = ["name"]
    ordering = ["name"]


admin.site.register(SuperHero, SuperHeroAdmin)


admin.site.site_header = "SuperBook Secret Area"