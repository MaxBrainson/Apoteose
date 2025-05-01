from django.shortcuts import render


def home(request):
    def openApp():
        return render(request, 'home.html')

    if request.method == 'POST' and 'run_script' in request.POST:
        return openApp()
    return render(request, 'home.html')


def loading(request):
    return render(request, 'initial_loading.html')


