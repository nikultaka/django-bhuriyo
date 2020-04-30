from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import CMSPage, Portfolio, Testimonial, Blog
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from preferences import preferences
from django.core.mail import EmailMessage


def index(request):

    about_us = CMSPage.objects.filter(slug='about_us')[:1]
    portfolio = Portfolio.objects.filter()[:5]
    testimonial = Testimonial.objects.filter()[:3]
    blogs = Blog.objects.filter()[:3]
    context = {'about_us': about_us, 'portfolio': portfolio, 'testimonial': testimonial, 'blogs':blogs}
    return render(request, 'mysite/index.html', context)

def contact(request):

    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    body = "Hi, we got new inquiry from, name : "+name+', Message : '+message

    email = EmailMessage('New Inquiry', body, to=['nikultaka@gmail.com'])
    email.send()

    data = {}
    data['status'] = 1
    return JsonResponse(data)