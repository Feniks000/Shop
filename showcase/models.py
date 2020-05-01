
from django.db import models


# Create your models here.


class Star(models.Model):
    star_name = models.CharField(max_length=200)
    star_description = models.TextField()
    star_image = models.ImageField()
    star_cost = models.BigIntegerField()
    star_type = models.CharField(max_length=200)
    star_position = models.CharField(max_length=200)

    def name(self):
        return str(self.star_name)

    def description(self):
        return str(self.star_description)

    def img(self):
        return self.star_image

    def cost(self):
        return self.star_cost

    def stype(self):
        return self.star_type

    def spos(self):
        return self.star_position


