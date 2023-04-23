from django.contrib import admin
from django.urls import path, include
from home import views
from django.contrib.auth import views as auth_views


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
    path('profile/', views.profile, name='profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
    #Password Reset
    # path('reset_password/' , auth_views.PasswordResetView.as_view(), name="reset_password"),
    # path('reset_password_sent/' , auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('reset/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path('reset_password_complete/' , auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),



]
