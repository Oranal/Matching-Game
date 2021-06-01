from django.shortcuts import render, redirect

def play(request):
    return render(request, 'game/play.html')