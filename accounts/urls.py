from django.urls import path
from allauth.account.views import LoginView, SignupView
from . import views

urlpatterns = [
    #path('login/', LoginView.as_view(), name='account_login'),
    #path('signup/', SignupView.as_view(), name='account_signup'),
    # Custom views
    path('profile/', views.profile_view, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
