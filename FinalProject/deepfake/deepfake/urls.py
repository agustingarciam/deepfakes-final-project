"""deepfake URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

#all of the import statements
from fake.views import home, login_view, logout_view, signup_view, delete, user_profile, splash, like_view, profiles


# added urls here
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', splash, name='splash'),
    path('home', home, name='home'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('like/<id_of_post>/', like_view, name="like_view"),
    path('signup', signup_view, name='signup'),
    path('delete', delete, name='delete'),
    path('user_profile', user_profile, name='user_profile'),
    path('profiles/<author>', profiles, name='profiles')
]
