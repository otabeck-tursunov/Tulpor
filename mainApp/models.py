from django.db import models


class Joy(models.Model):
    raqam = models.PositiveSmallIntegerField()
    orin = models.PositiveSmallIntegerField(default=4)
    band = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Joy'
        verbose_name_plural = 'Joylar'

    def __str__(self):
        return f"{self.raqam} - joy"


class Taom(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    narx = models.IntegerField()

    class Meta:
        verbose_name = 'Taom'
        verbose_name_plural = 'Taomlar'

    def __str__(self):
        return self.nom


class Ichimlik(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    narx = models.IntegerField()

    class Meta:
        verbose_name = 'Ichimlik'
        verbose_name_plural = 'Ichimliklar'

    def __str__(self):
        return self.nom
