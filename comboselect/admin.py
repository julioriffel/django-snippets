#  Copyright (c) 2021.
#  Julio Cezar Riffel <julioriffel@gmail.com>

from django.contrib import admin

from comboselect.models import Country, City, Person

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Person)
