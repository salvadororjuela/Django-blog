from django.urls import path
from . import views


# Namespace urls to avoid conflict with urls named the same way in
# other app folders
app_name = "users"


urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
]
