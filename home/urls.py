from django.contrib import admin
from django.urls import path, include
from home import views


# Changes in Database Admin Panel
admin.site.site_header = "Data Engineering"
admin.site.site_title = " Data Engineering Databse"
admin.site.index_title = "Welcome to Data Engineering Database"


# link files from main project folder to home app's views
urlpatterns = [
    path('', views.login, name='login'),
    path('admin/', admin.site.urls),
    path('forgot/', views.forgot, name='forgot'),
    path('signup/', views.Signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),

]
