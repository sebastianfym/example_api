from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=100, verbose_name='name', null=True, blank=True)
    age = models.IntegerField(verbose_name='age', default=0)
    date_of_arrival = models.DateTimeField(auto_now=True, verbose_name='date_of_arrival')
    weight = models.IntegerField(verbose_name='weight', default=0, blank=True)
    height = models.IntegerField(verbose_name='height', default=0, blank=True)
    special_signs = models.CharField(max_length=1000, verbose_name='special_signs', null=True, blank=True)

    def __str__(self):
        return f'{self.name},{self.age},{self.date_of_arrival}'

    class Meta:
        verbose_name = 'pet'
        verbose_name_plural = 'pets'
