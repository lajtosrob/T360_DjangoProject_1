from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
    context = {
       "books": [
           {"name": "", "author": "Author1", "read": True},
           {"name": "Book2", "author": "Author2", "read": False},
           {"name": "Book3", "author": "Author3", "read": False},
       ]
    }
    return render(request, "index.html", context)

"""
def project_name(request, project_name: str, project_owner: str):
    return HttpResponse(f"Project {project_name}!")

def number_endpoint(request, my_number: int):
    return HttpResponse(f"My number: {my_number + 13}")
"""
