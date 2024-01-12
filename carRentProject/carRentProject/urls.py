from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from carRentApp.views import home
from carRentApp.views import home, search_results
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),
    path('search/', search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




