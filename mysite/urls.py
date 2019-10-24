from django.contrib import admin
from django.urls import path
from myapp import views as appview

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',appview.index),
    path('index',appview.index),
    path('insert',appview.insert),
    path('',appview.insert),
    path('aboutme',appview.aboutme),
    path('',appview.aboutme),
    
]
