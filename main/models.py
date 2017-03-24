from __future__ import unicode_literals
import quandl
from django.db import models
from data import Data

# Create your models here.
def getData(name):
    data = quandl.get(name)
    out =""
    for index, row  in data.iterrows():
        Data.objects.create_data(index,row['VALUE'])
#        out = out + row.to_string()+ index
    return out

