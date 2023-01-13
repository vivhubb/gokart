from django.shortcuts import render


def home(request):
    return render(request, 'race/home.html')


def feedback(request):
    return render(request, 'race/feedback.html')


def booking(request):
    return render(request, 'race/booking.html')
