from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from core.models import Hero

def index(request: HttpRequest) -> HttpResponse:
    heroes = Hero.objects.all()
    return render(request, "index.html", {
        "heroes": heroes
    })
