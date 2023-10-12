from django.shortcuts import render


def home(request):
    context = {}
    template = 'comingsoon/home.html'
    return render(request, template, context)


def terms_of_use(request):
    return render(request, 'landingpage/terms_of_use.html')
