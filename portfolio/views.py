from django.shortcuts import render,get_list_or_404, get_object_or_404
from .models import Project

# Create your views here.

def portfolio(request):
    #vamos a traer los projects para listarlos
    title= 'portfolio Cipriano Escorche'
    active='portfolio'
    projects = get_list_or_404(Project)   
    return render(request,'projects/projects.html',{'projects':projects,'title':title, 'active':active})