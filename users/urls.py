from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('employers/', user_views.employers_page, name="employers"),
    path('candidates/', user_views.candidates_page, name="candidates"),
    path('register/employer/', user_views.register_employer,
         name="register_employer"),
    path('register/candidate/', user_views.register_candidate,
         name="register_candidate"),
    path('login/', user_views.login_view, name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('profile-redirect/', user_views.logged_user_type, name="logged_user_type"),
    path('employer-profile/', user_views.employer_profile, name="employer_profile"),
    path('candidate-profile/', user_views.candidate_profile,
         name="candidate_profile"),
    path('delete-account/', user_views.delete_user_view, name="delete_user_view"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
         template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
         template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
         template_name='password_reset_complete.html'),
         name='password_reset_complete'),
]
