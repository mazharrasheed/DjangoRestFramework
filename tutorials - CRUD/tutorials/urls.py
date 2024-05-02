"""
URL configuration for tutorials project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# urls.py

from django.urls import path
from quickstart import views

urlpatterns = [
    path('', views.index, name='book_list'),
    path('books/', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/create/', views.book_create, name='book_create'),
    path('book/create/<int:pk>/', views.book_update, name='book_update'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
]
