from django.contrib import admin
from django.urls import path,include
from myweb import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index),
    path('Signup/', views.Signup),
    path('Login/', views.Login),
    path('myweb/', include('myweb.urls')),
    path('admin/', admin.site.urls),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
