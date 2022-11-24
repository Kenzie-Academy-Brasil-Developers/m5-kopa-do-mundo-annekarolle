from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=30, null=False)
    titles = models.IntegerField(null=True, blank=True, default=0)
    top_scorer = models.CharField(max_length=50, null=False)
    fifa_code = models.CharField(max_length=3, null=False, unique=True)
    founded_at = models.DateField(blank=True, null=True)

    def __repr__(self):
        return f'<[{self.id}] {self.name} - {self.fifa_code}>'