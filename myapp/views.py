from django.shortcuts import render


def progress_view(request):
    return render(request, 'progress_bar.html', context={})
    
