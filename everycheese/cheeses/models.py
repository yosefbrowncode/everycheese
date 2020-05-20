from django.db import models

from autoslug import AutoSlugField
from model_utils.models  import  TimeStampedModel



class Cheese(TimeStampedModel):

        class Firmness(models.TextChoices):
            UNSPECIFIED = "unspecified", "unspecified"
            SOFT  = "soft","soft"
            SEMI_SOFT = 'semi_soft','semi_soft'
            SEMI_HARD = 'semi_hard','semi_hard'
            HARD = 'hard','hard'

        name = models.CharField("Name of Cheese", max_length=255)
        slug   = AutoSlugField("Cheese Address",
            unique = True, always_update = False, populate_from="name")
        description = models.TextField("Descripton",blank=True)

        firmness = models.CharField("Firmness",max_length=20,
        choices = Firmness.choices, default = Firmness.UNSPECIFIED)


        def __str__(self):
            return self.name

   