from django.urls import path, include

from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'mysite'


urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name="contact"),
    path('about-us', views.about, name="about-us"),
    path('blog', views.blog, name="blog"),
    path('portfolio', views.portfolio, name="portfolio"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)