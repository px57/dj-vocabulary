from django.contrib import admin
from vocabulary import models


class VocabularyTranslateInline(admin.TabularInline):
    model = models.VocabularyTranslation
    extra = 0

    fields = [
        'language',
        'word', 
        'definition', 
    ]

    readonly_fields = ['link']
    formfield_overrides = {}     

    def link(self, obj):
        if obj.pk is None:
            return ''
        return 'test'


@admin.register(models.Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    inlines = [VocabularyTranslateInline]
