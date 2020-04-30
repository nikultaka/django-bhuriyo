from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from sorl.thumbnail import ImageField
from preferences.models import Preferences


class CMSPage(models.Model):

    def __str__(self):
        return self.title

    CMS_STATUS = ((1, 'Active'), (0, 'Inactive'))

    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    description = HTMLField()
    status = models.PositiveSmallIntegerField(choices=CMS_STATUS, default=1)


class Blog(models.Model):

    def __str__(self):
        return self.title

    BLOG_STATUS = ((1, 'Active'), (0, 'Inactive'))

    title = models.CharField(max_length=255)
    description = HTMLField()
    image = ImageField(upload_to='blog')
    status = models.PositiveSmallIntegerField(choices=BLOG_STATUS, default=1)
    published_date = models.DateTimeField(auto_now_add=True, blank=True)


class PortfolioCategory(models.Model):

    def __str__(self):
        return self.title

    PORTFOLIO_CATEGORY_STATUS = ((1, 'Active'), (0, 'Inactive'))
    title = models.CharField(max_length=255)
    status = models.PositiveSmallIntegerField(choices=PORTFOLIO_CATEGORY_STATUS, default=1)
    published_date = models.DateTimeField(auto_now_add=True, blank=True)


class Portfolio(models.Model):

    def __str__(self):
        return self.title

    PORTFOLIO_STATUS = ((1, 'Active'), (0, 'Inactive'))
    title = models.CharField(max_length=255)
    description = HTMLField()
    image = ImageField(upload_to='portfolio')
    url = models.CharField(max_length=255)
    category = models.ForeignKey(PortfolioCategory, default=1, on_delete=models.SET_DEFAULT)
    status = models.PositiveSmallIntegerField(choices=PORTFOLIO_STATUS, default=1)
    published_date = models.DateTimeField(auto_now_add=True, blank=True)


class Testimonial(models.Model):

    def __str__(self):
        return self.title

    TESTIMONIAL_STATUS = ((1, 'Active'), (0, 'Inactive'))
    title = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = HTMLField()
    image = models.ImageField(upload_to='testimonial')
    status = models.PositiveSmallIntegerField(choices=TESTIMONIAL_STATUS, default=1)
    published_date = models.DateTimeField(auto_now_add=True, blank=True)


class MyPreferences(Preferences):
    portal_contact_home_about = HTMLField()
    portal_contact_email = models.EmailField()
    portal_contact_phone = models.CharField(max_length=255)
    portal_contact_address = models.TextField()
    portal_contact_facebook = models.CharField(max_length=255)
    portal_contact_instagram = models.CharField(max_length=255)
    portal_contact_twitter = models.CharField(max_length=255)




