from __future__ import unicode_literals
import quandl
from django.db import models

# Create your models here.
def getData(name):
    return quandl.get(name)

