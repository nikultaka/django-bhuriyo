from django.urls import path, include

from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'mysite'


urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name="contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)