from django.contrib import admin
from django.urls import path,include
from myweb import views
urlpatterns = [
    #path('polls/', include('polls.urls')),
    path('myweb/', include('myweb.urls')),
    path('', views.index),
    path('admin/', admin.site.urls),
]
