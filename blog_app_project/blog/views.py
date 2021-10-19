from django.http import HttpResponse
from django.shortcuts import render
from .models import Articles


# Create your views here.
def index(request):
    return render(request, "blog/index.html", {
        "Articles": Articles.objects.all().order_by("date")
    })


def article_detail(request, slug):
    article = Articles.objects.get(slug=slug)
    return render(request, "blog/articleContent.html", {
        'article': article
    })


def about(request):
    return render(request, "blog/about.html")
