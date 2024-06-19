


from django.contrib import admin
from django.urls import path
from fitapp import views


admin.site.site_header ="LOGIN FITSERVE ADMIN"
admin.site.site_title = "WELCOME TO FITSERVE"
admin.site.index_title = "ADMIN PORTAL"
urlpatterns = [
    path('', views.index,name='home'),
    path('contact', views.contact,name='contact'),
    path('pricing', views.pricing,name='pricing'),
    path('members', views.members,name='members'),
    #path('admin', views.admin,name='admin'),
]