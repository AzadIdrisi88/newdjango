from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return HttpResponse("Hello")


def home(request):
    return HttpResponse("<input placeholder='Home'/>")


def add(request):
    return render(request, "test.html")
