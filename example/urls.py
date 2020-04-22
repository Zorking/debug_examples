"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from qwerty import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("example3/", views.Example3.as_view()),
    path("example4/", views.Example4.as_view()),
    path("example4_2/", views.Example4_2.as_view()),
    path("example5/", views.Example5.as_view()),
    path("example6/", views.Example6.as_view()),
]

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

