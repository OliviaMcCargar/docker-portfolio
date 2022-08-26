from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, second world. You're at the second portfolio index.")

