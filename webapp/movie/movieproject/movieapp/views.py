from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from .forms import MovieForm


# Create your views here.
def index(request):
    Movie = movie.objects.all()
    context = {
        'movie_list': Movie
    }
    return render(request, 'index.html', context)


def detail(request, movie_id):
    Movie = movie.objects.get(id=movie_id)
    return render(request, "details.html", {'movie': Movie})


def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('name',)
        year = request.POST.get('year',)
        description = request.POST.get('desc',)
        image = request.FILES['img']
        Movie = movie(name=name, year=year, desc=description, img=image)
        Movie.save()
        print("added")
        return redirect('/')
    return render(request, "add.html")

def update(request, id):
    Movie = movie.objects.get(id=id)
    form = MovieForm(request.POST or None,request.FILES,instance=Movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'movie':Movie})

def delete(request, id):
    if request.method == "POST":
        Movie=movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request,"delete.html")