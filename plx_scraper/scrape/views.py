from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Files, Path
from django.urls import reverse
from .forms import PathModelForm
from django.contrib import messages
from django.db.models import Q
import os
import operator


# Create your views here.
def scrape(request):
    
    # Path value
    path = Path.objects.filter().first()
    # First 15 files values
    files = Files.objects.all()[:15]
    # All files values 
    all_files = Files.objects.all()
    # Count all files
    count_files = Files.objects.all().count()

    # Search data from files table
    query = request.GET.get("q")

    if query:
        files = all_files.filter(file_name__iregex=query)
    else:
        files = all_files.all()[:50]

    context = {
        'files': files[:50],
        'path': path,
        'query': query,
        'count_files': count_files
    }

    return render(request, "scrape/list.html", context)

# Add new name files from directory(path)
def add_files(request):
    path = Path.objects.filter().first()
    choice = str(request.POST['choice']).upper()
    if os.path.exists(str(path)):
        path_list = os.listdir(str(path))
        for file in path_list:
            if choice in file.upper():
                file = os.path.splitext(file)[0]
                del_file = Files.objects.filter(file_name__contains=file)
                if del_file:
                    del_file.delete()
                files = Files(file_name=file, path=path)
                files.save()
        if not any(choice in file.upper() for file in path_list):
            messages.info(request, 'None match of the files')
            return redirect("/scrape")
        messages.success(request, 'The database has been updated')
        return redirect('/scrape')
    else:
        messages.info(request, 'The directory doesnt exists. Change the direcotry path!')
        return redirect('/scrape')


# Change the path
def change_path(request, path_id=None):
    path = Path.objects.get(id=path_id)
    form = PathModelForm(request.POST or None, instance=path)

    if form.is_valid():
        form.save()
        messages.success(request, 'The path has been updated')
        return redirect('/scrape')
    
    context = {
        "form": form
    }

    return render(request, "scrape/change_path.html", context)
