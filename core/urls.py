"""makeup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from core.views import service_list, home, pricing, service, add_record

urlpatterns = [
    path('', home, name='home'),
    path('pricing/', pricing, name='pricing'),
    path('add_record/', add_record, name='add_record'),
    path('services/<str:category_slug>/', service_list, name='services_list'),
    path('services/<str:category_slug>/<int:id>/<str:slug>/', service, name='service_detail'),
]
