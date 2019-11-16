from django.urls import path
from .views import register_employer, register_candidate, employer_profile, candidate_profile, logged_user_type
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/employer', register_employer, name="register_employer"),
    path('register/candidate', register_candidate, name="register_candidate"),
    path('login', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('profile-redirect', logged_user_type, name="logged_user_type"),
    path('employer-profile', employer_profile, name="employer_profile"),
    path('candidate-profile', candidate_profile, name="candidate_profile"),
]
