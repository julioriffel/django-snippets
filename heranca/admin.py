#  Copyright (c) 2021.
#  Julio Cezar Riffel <julioriffel@gmail.com>

from django.contrib import admin

from heranca.models import Carro, Post, ProfileH

admin.site.register(Carro)


# admin.site.register(Post)
# admin.site.register(ProfileH)

@admin.register(Post)
class ProstHAdmin(admin.ModelAdmin):
    list_display = ('message', 'public', 'modified')


@admin.register(ProfileH)
class ProfileHAdmin(admin.ModelAdmin):
    list_display = ('origin', 'age', 'user')
    # readonly_fields = ['age']
    pass
