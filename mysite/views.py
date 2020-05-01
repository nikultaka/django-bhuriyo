from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import CMSPage, PortfolioCategory, Portfolio, Testimonial, Blog
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
    context = {'about_us': about_us, 'portfolio': portfolio, 'testimonial': testimonial, 'blogs': blogs}
    return render(request, 'mysite/index.html', context)


def about(request):

    about_us = CMSPage.objects.filter(slug='about_us')[:1]
    context = {"about_us": about_us}
    return render(request, 'mysite/about.html', context)


def blog(request):

    blogs = Blog.objects.filter()
    context = {'blogs': blogs}
    return render(request, 'mysite/blog.html', context)


def blog_detail(request, id):
    blog_id = id
    blogs = Blog.objects.filter(id=blog_id)
    all_blogs = Blog.objects.filter().exclude(id=blog_id)
    context = {"blogs": blogs, "all_blogs": all_blogs}
    return render(request, "mysite/blog_detail.html",context)


def portfolio(request):

    portfolio = Portfolio.objects.filter()
    portfolio_category = PortfolioCategory.objects.filter()
    context = {"portfolio": portfolio, "portfolioCategory": portfolio_category}
    return render(request, "mysite/portfolio.html", context)



def contact(request):

    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    portal_contact_email = preferences.MyPreferences.portal_contact_email

    body = "Hi, we got new inquiry from, name : "+name+', Message : '+message

    email = EmailMessage('New Inquiry', body, to=[portal_contact_email])
    email.send()

    data = {}
    data['status'] = 1
    return JsonResponse(data)