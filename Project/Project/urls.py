"""Project URL Configuration

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
from django.urls import path
import mainApp.views
import profileApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainApp.views.mainPage, name="main"),
    path('post/<int:blog_id>', mainApp.views.detail, name="detail"),
    path('write/', mainApp.views.newPost, name="newPost"),
    path('create/', mainApp.views.saveNewPost, name='writeNewPost'),
    path('delete/<int:blog_id>', mainApp.views.deletePost, name="delete"),
    path('edit/<int:blog_id>', mainApp.views.editPost, name="edit"),
    path('profile/', profileApp.views.profile, name="profile"),
    path('editSave/<int:blog_id>', mainApp.views.saveEditedPost, name="saveEditedPost")
]
