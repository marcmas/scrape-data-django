from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Files, Path
from django.urls import reverse
from .forms import PathModelForm
from django.contrib import messages
from django.template.loader import render_to_string

import os

# Create your views here.
# def test_view(request):
    
    # # Path value
    # path = Path.objects.filter().first()
    # # First 15 files values
    # files = Files.objects.all()[:15]
    # # All files values 
    # all_files = Files.objects.all()
    # # Count all files
    # count_files = Files.objects.all().count()

    # # Search data from files table
    # query = request.GET.get("q")
    
    # # Check query True
    # if query:
        # if "%" in query:
            # # Change a query "%" to ".*" regex
            # query = query.replace("%", ".*")
            # files = all_files.filter(file_name__iregex=query)
            # query = query.replace(".*", "%")
        # elif "%" not in query:
            # files = all_files.filter(file_name__icontains=query)
        # else:
            # files = all_files.all()[:50]
        
    # context = {
        # 'files': files[:100],
        # 'path': path,
        # 'query': query,
        # 'count_files': count_files
    # }

    # return render(request, "scrape/list.html", context)


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
        if "%" in query:
            # Change a query "%" to ".*" regex
            query = query.replace("%", ".*")
            files = all_files.filter(file_name__iregex=query)[:80]
            query = query.replace(".*", "%")
        elif "%" not in query:
            files = all_files.filter(file_name__icontains=query)[:80]
        else:
            files = all_files.all()[:70]
            

    context = {
        'files': files,
        'path': path,
        'query': query,
        'count_files': count_files
    }
    
    if request.is_ajax():

        html = render_to_string(
            template_name="scrape/results-partial.html", context={"files": files}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

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
                del_file = Files.objects.filter(file_name=file)
                if del_file:
                    continue
                files = Files(file_name=file, path=path)
                files.save()
        if not any(choice in file.upper() for file in path_list):
            messages.info(request, 'None match of this phrase')
            return redirect("/scrape")
        messages.success(request, 'The database has been updated')
        return redirect('/scrape')
    else:
        messages.info(request, 'The directory doesnt exists. Change the direcotry path!')
        return redirect('/scrape')


# Add all files from directory(path)
def add_all_files(request):
    path = Path.objects.filter().first()
    if os.path.exists(str(path)):
        path_list = os.listdir(str(path))
        for file in path_list:
            file = os.path.splitext(file)[0]
            del_file = Files.objects.filter(file_name=file)
            if del_file:
                continue
            files = Files(file_name=file, path=path)
            files.save()
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


