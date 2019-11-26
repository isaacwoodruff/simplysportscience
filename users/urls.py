from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('employers/', user_views.employers_page, name="employers"),
    path('candidates/', user_views.candidates_page, name="candidates"),
    path('register/employer/', user_views.register_employer, name="register_employer"),
    path('register/candidate/', user_views.register_candidate, name="register_candidate"),
    path('login/', user_views.login_view, name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('profile-redirect/', user_views.logged_user_type, name="logged_user_type"),
    path('employer-profile/', user_views.employer_profile, name="employer_profile"),
    path('candidate-profile/', user_views.candidate_profile, name="candidate_profile"),
]
