from django.shortcuts import render

# Create your views here.
import textwrap

from django.http import HttpResponse
from django.views.generic.base import View
import models

class HomePageView(View):

    def dispatch(request, *args, **kwargs):
        data = models.getData("FRED/GDP")
        #response_text = textwrap.dedent(data.to_string)

        return HttpResponse(data)
