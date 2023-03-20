from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import BookForm
from . models import Book


# Create your views here.
def index(request):
    book = Book.objects.all()
    list = {'booklist': book}
    return render(request, 'index.html', list)


def detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request,"detail.html",{'book':book})


def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        author = request.POST['author']
        desc = request.POST['desc']
        img = request.FILES['img']
        store = Book(name=name,author=author,desc=desc,img=img)
        store.save();
    return render(request,'add.html')


def update(request,id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None,request.FILES, instance=book)
    if form.is_valid():
        form.save();
        return redirect('/')
    return render(request,'update.html',{'form':form,'book':book})


def delete(request,id):
    if request.method == 'POST':
        book = Book.objects.get(id=id)
        book.delete();
        return redirect('/')
    return render(request,'delete.html')
