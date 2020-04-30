from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import CMSPage, Portfolio, Testimonial, Blog
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from preferences import preferences


def index(request):

    about_us = CMSPage.objects.filter(slug='about_us')[:1]
    portfolio = Portfolio.objects.filter()[:5]
    testimonial = Testimonial.objects.filter()[:3]
    blogs = Blog.objects.filter()[:3]
    context = {'about_us': about_us, 'portfolio': portfolio, 'testimonial': testimonial, 'blogs':blogs}
    return render(request, 'mysite/index.html', context)

def contact(request):

    pass;