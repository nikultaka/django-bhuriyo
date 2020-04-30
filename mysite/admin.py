from django.contrib import admin

# Register your models here.
from preferences.admin import PreferencesAdmin
from django.contrib import admin
from .models import CMSPage, Blog, PortfolioCategory, Portfolio, Testimonial, MyPreferences


admin.site.register(CMSPage)
admin.site.register(Blog)
admin.site.register(PortfolioCategory)
admin.site.register(Portfolio)
admin.site.register(Testimonial)
admin.site.register(MyPreferences, PreferencesAdmin)