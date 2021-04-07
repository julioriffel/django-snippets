#  Copyright (c) 2021.
#  Julio Cezar Riffel <julioriffel@gmail.com>

from django.contrib import admin

from storagessnp.models import Document


class DocumentFileAdmin(admin.ModelAdmin):
    model = Document
    list_display = ['document']


admin.site.register(Document, DocumentFileAdmin)
