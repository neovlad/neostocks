from django.db import models 

class DataManager(models.Manager):

    def create_data(self, date, price):
        data = self.create(date=date,price=price)
        return data

class Data(models.Model):
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=8,decimal_places=2)
    objects = DataManager()


