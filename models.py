from django.db import models

from django.forms.models import model_to_dict
from django.urls import reverse
from django.shortcuts import render
from kernel.models.base_metadata_model import BaseMetadataModel
from vocabulary.rules.stack import VOCABULARY_RULESTACK
from kernel.models.serialize import serializer__serialize__, serializer__init__


class VocabularyTranslation(BaseMetadataModel):
    """
    VocabularyTranslation class
    """
    language = models.CharField(
        'language',
        max_length=255,
        default='fr',
        choices=(
            ('fr', 'fr'),
        ),
    )

    word = models.CharField(
        max_length=255, 
        unique=True
    )

    definition = models.TextField()
    
    translateObject = models.ForeignKey(
        'vocabulary.Vocabulary',
        on_delete=models.CASCADE,
        related_name='translates',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.word
    
    def get_absolute_url(self):
        return reverse('vocabulary:vocabulary_detail', args=[str(self.id)])
    
    def serialize(self, request):
        serialized = model_to_dict(self)
        return serialized
    

class Vocabulary(BaseMetadataModel):
    """
    Vocabulary class
    """
    translation_model = VocabularyTranslation

    @serializer__init__
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    interface = models.CharField(
        choices=VOCABULARY_RULESTACK.models_choices(),
        max_length=255, 
        default='DEFAULT'
    )

    word = models.CharField(
        max_length=255, 
        unique=True
    )

    definition = models.TextField()

    def __str__(self):
        return self.word

    def get_absolute_url(self):
        return reverse('vocabulary:vocabulary_detail', args=[str(self.id)])
    
    def serialize(self, request):
        serialized = model_to_dict(self)
        return serialized