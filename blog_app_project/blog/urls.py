from django.urls import path
from . import views


# Namespace urls to avoid conflict with urls named the same way in
# other app folders
app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug>", views.article_detail, name="article_detail"),
]
