"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path, include

from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
	path('', views.HomeView.as_view(), name='socialupdate-home'),
	path('login/', LoginView.as_view(template_name='socialupdate/loginPage.html'), name='socialupdate-login'),
	path('createPost/', views.CreatePostView, name='socialupdate-createPost'),
	path('userCreation/', views.UserCreationView.as_view(), name='socialupdate-userCreation'),
	path('profile/', views.ProfileView, name='socialupdate-profile'),
]
