from django.db import models

class Reuniao(models.Model):

    STATUS = (
        ('presente', 'Presente'),
        ('ausente', 'Ausente'),


    )


    id = models.CharField(primary_key=True, max_length=9)
    dig_RA = models.CharField(max_length=1)
    name = models.CharField(max_length=100)
    nascimento = models.DateField()
    serie = models.CharField(max_length=1)
    turma = models.CharField(max_length=1)
    photos = models.ImageField(upload_to='cadastro_photos', null=True, blank=True)
    ausente = models.CharField(
        max_length=8,
        choices=STATUS, null=True,
        default='ausente')

    tutor = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

