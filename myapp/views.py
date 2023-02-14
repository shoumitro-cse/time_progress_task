from django.shortcuts import render

from myapp.tasks import progress_scheduled_create


def progress_view(request):
    # progress_scheduled_create('progress_group', 6)
    # progress_scheduled_create.apply_async(('progress_group', 'json_data'))
    return render(request, 'progress_bar.html', context={})
    
