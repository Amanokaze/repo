from django.db import models
from django.utils import timezone

# Create your models here.
class GrGameCategories(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s (%s)' % (self.name, self.code)

    class Meta:
        managed = False
        db_table = 'gr_game_categories'


class GrGameMasters(models.Model):
    category = models.ForeignKey('GrGameCategories', models.DO_NOTHING)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True, null=True)
    logo = models.ImageField(upload_to='collection/logos', blank=True)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s (%s)' % (self.name, self.code)

    class Meta:
        managed = False
        db_table = 'gr_game_masters'




