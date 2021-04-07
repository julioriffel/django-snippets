#  Copyright (c) 2021.
#  Julio Cezar Riffel <julioriffel@gmail.com>

from django import forms

from storagessnp.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document',)
