from django.db import models
from django.utils import timezone
from main.models import GrGameMasters

class GrGameCollections(models.Model):
    game = models.ForeignKey('main.GrGameMasters', models.DO_NOTHING)
    icon = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    layout_html = models.CharField(max_length=3000, blank=True, null=True)
    ref_name = models.CharField(max_length=10, blank=True, null=True)
    ref_icon = models.CharField(max_length=10, blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - (%s)' % (self.name, self.game.name)

    class Meta:
        managed = False
        db_table = 'gr_game_collections'
