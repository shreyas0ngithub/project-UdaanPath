from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse("<h1>Welcome to Project-UdaanPath: Home page</h1>")

def about(request):
  return HttpResponse("<h1>Welcome to Project-UdaanPath: About page</h1>")

def contact(request):
  return HttpResponse("<h1>Welcome to Project-UdaanPath: Contact page</h1>")