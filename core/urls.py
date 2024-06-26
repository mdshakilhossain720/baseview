"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

# create objest
router=DefaultRouter()
# regestry 
router.register('studentapi',views.Studentviewset,basename='studentapi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    # path('student/',views.Studentlist.as_view()),
    # path('student/',views.StudentCreate.as_view()),
    #path('studentlist/',views.StudentApiView.as_view(),)
    # path('studentinfo/',views.student),
    # path('studentinfo/<int:pk>',views.student),
    #  path('student/',views.StudentApi.as_view()),
    # path('student/<int:pk>',views.StudentApi.as_view()),
]
