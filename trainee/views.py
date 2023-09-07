from django.http import HttpResponse
from django.shortcuts import render



def insert(request):
    res = HttpResponse('Whatever');
    res.write("Inserting a trainee");
    return res;




def delete(request):
    res = HttpResponse("Whatever")
    res.write("Deleting a trainee");
    return res;


def update(request):
    res = HttpResponse("Whatever");
    res.write("Updating a trainee");
    return res;


def show(request):
    res = HttpResponse("Whatever");
    res.write("Showing a trainee")
    return res;