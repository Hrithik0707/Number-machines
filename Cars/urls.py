from django.contrib import admin
from django.urls import path,include
from Cars.views import signin,signup,logout,main,save

urlpatterns = [
    path('',signup,name="signup"),
    path('signin/',signin,name="signin"),
    path('logout/',logout,name="logout"),
    path('analysis/',main,name="main"),
    path('analysis/save',save,name="save"),
]
